#!/usr/bin/env python3
"""Claude Code PreToolUse hook: changes reach a protected branch only through a pull request.

Reads the hook payload on stdin and blocks (exit code 2, reason on stderr, which
Claude Code hands back to the model) any Bash command that would land changes on a
protected branch without a reviewed PR:

- ``git merge`` while a protected branch is checked out (``--abort``/``--quit`` pass);
- ``git push`` whose destination is a protected branch: an explicit refspec
  (``main``, ``HEAD:main``, ``+feat:refs/heads/main``, ``:main``), a push with no
  refspec while a protected branch is checked out, and ``--all``/``--mirror``/``--branches``;
- ``gh pr merge`` (``--auto`` included) and ``gh api`` calls that merge a PR.

Protected branches are ``main``, ``master`` and the remote's default branch
(``origin/HEAD``). Every other command exits 0.

The command is tokenized like a shell would (quotes, comments, heredocs), so chained
commands (``&&``, ``;``, ``|``, newlines), a ``cd`` before git, ``git -C``,
``bash -c "..."`` and ``eval`` are covered. Variables and command substitutions are
not expanded: this is a guardrail against mistakes, not a sandbox. Branch protection
on GitHub remains the real enforcement.
"""

import json
import os
import re
import subprocess
import sys
from typing import List, Optional, Set, Tuple

STATIC_PROTECTED_BRANCHES = {"main", "master"}
OPERATOR_CHARS = ";&|()<>"
SHELLS = {"bash", "sh", "zsh"}
COMMAND_WRAPPERS = {"command", "builtin", "exec", "nohup", "time", "sudo", "env"}
ENV_ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
SHELL_COMMAND_FLAG = re.compile(r"^-[A-Za-z]*c[A-Za-z]*$")
GIT_GLOBAL_OPTIONS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace"}
PUSH_OPTIONS_WITH_VALUE = {"-o", "--push-option", "--repo", "--receive-pack", "--exec"}
PUSH_ALL_BRANCHES_FLAGS = {"--all", "--mirror", "--branches"}
MERGE_SAFE_FLAGS = {"--abort", "--quit"}
GH_REPO_FLAGS = {"-R", "--repo"}
GH_API_MERGE_PATH = re.compile(r"(^|/)pulls/\d+/merge/?$")
GH_GRAPHQL_MERGE_MUTATIONS = ("mergePullRequest", "enablePullRequestAutoMerge")
MAX_NESTING = 3
GUIDANCE = (
    "Changes reach a protected branch only through a pull request: push a feature "
    "branch and open a PR; merging it is up to a human reviewer. "
    "(Guardrail: .claude/hooks/block_direct_merge.py)"
)

Token = Tuple[str, bool]  # (text, is_operator)
Heredoc = Tuple[str, bool]  # (delimiter, strip_leading_tabs)


def skip_heredoc_bodies(command: str, start: int, pending: List[Heredoc]) -> int:
    """Return the index just past the bodies of the pending heredocs, starting at `start`."""
    position = start
    for delimiter, strip_tabs in pending:
        while position < len(command):
            end = command.find("\n", position)
            line = command[position:] if end == -1 else command[position:end]
            position = len(command) if end == -1 else end + 1
            if (line.lstrip("\t") if strip_tabs else line) == delimiter:
                break
    pending.clear()
    return position


def tokenize(command: str) -> List[Token]:
    """Split a shell string into words and operators, dropping comments and heredoc bodies."""
    tokens: List[Token] = []
    pending_heredocs: List[Heredoc] = []
    word: List[str] = []
    has_word = False  # tells an empty quoted word ("") apart from no word at all
    index, length = 0, len(command)

    def flush() -> None:
        nonlocal word, has_word
        if not has_word:
            return
        text = "".join(word)
        if tokens and tokens[-1] == ("<<", True):
            strip_tabs = text.startswith("-")  # `<<-EOF` lexes as `<<` + `-EOF`
            pending_heredocs.append((text[1:] if strip_tabs else text, strip_tabs))
        tokens.append((text, False))
        word, has_word = [], False

    while index < length:
        char = command[index]
        if char == "\\":
            if index + 1 < length and command[index + 1] != "\n":
                word.append(command[index + 1])
                has_word = True
            index += 2
        elif char == "'":
            end = command.find("'", index + 1)
            end = length if end == -1 else end
            word.append(command[index + 1:end])
            has_word = True
            index = end + 1
        elif char == '"':
            index += 1
            while index < length and command[index] != '"':
                if command[index] == "\\" and index + 1 < length and command[index + 1] in '"\\$`\n':
                    if command[index + 1] != "\n":
                        word.append(command[index + 1])
                    index += 2
                else:
                    word.append(command[index])
                    index += 1
            has_word = True
            index += 1
        elif char in " \t\r":
            flush()
            index += 1
        elif char == "#" and not has_word:
            end = command.find("\n", index)
            index = length if end == -1 else end
        elif char == "\n":
            flush()
            tokens.append(("\n", True))
            index = skip_heredoc_bodies(command, index + 1, pending_heredocs)
        elif char in OPERATOR_CHARS:
            if char in "<>" and has_word and "".join(word).isdigit():
                word, has_word = [], False  # file descriptor, as in `2>&1`
            flush()
            end = index
            while end < length and command[end] in OPERATOR_CHARS:
                end += 1
            tokens.append((command[index:end], True))
            index = end
        else:
            word.append(char)
            has_word = True
            index += 1
    flush()
    return tokens


def split_simple_commands(tokens: List[Token]) -> List[List[str]]:
    """Group tokens into simple commands, dropping redirections and their targets."""
    commands: List[List[str]] = []
    current: List[str] = []
    skip_redirect_target = False
    for text, is_operator in tokens:
        if is_operator:
            if "<" in text or ">" in text:
                skip_redirect_target = True
                continue
            if current:
                commands.append(current)
                current = []
            skip_redirect_target = False
        elif skip_redirect_target:
            skip_redirect_target = False
        else:
            current.append(text)
    if current:
        commands.append(current)
    return commands


def strip_wrappers(words: List[str]) -> List[str]:
    index = 0
    while index < len(words) and (ENV_ASSIGNMENT.match(words[index]) or words[index] in COMMAND_WRAPPERS):
        index += 1
    return words[index:]


def resolve_dir(base: str, target: str) -> str:
    if target == "-":
        return base
    return os.path.normpath(os.path.join(base, os.path.expanduser(target)))


def run_git(repo_dir: str, *args: str) -> Optional[str]:
    """Run a read-only git query; None means the answer is unknown (not a repo, no branch, ...)."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_dir, *args], capture_output=True, text=True, timeout=5, check=False
        )
    except (OSError, subprocess.SubprocessError) as error:
        print(f"block_direct_merge: could not run git in {repo_dir}: {error}", file=sys.stderr)
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def current_branch(repo_dir: str) -> Optional[str]:
    return run_git(repo_dir, "symbolic-ref", "--quiet", "--short", "HEAD")


def protected_branches(repo_dir: str) -> Set[str]:
    branches = set(STATIC_PROTECTED_BRANCHES)
    default = run_git(repo_dir, "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD")
    if default:
        branches.add(default.split("/", 1)[-1])
    return branches


def push_destination(refspec: str, current: Optional[str]) -> str:
    refspec = refspec.lstrip("+")
    target = refspec.split(":", 1)[1] if ":" in refspec else refspec
    if target in ("HEAD", "@"):
        target = current or ""
    if target.startswith("refs/heads/"):
        target = target[len("refs/heads/"):]
    return target


def check_merge(args: List[str], repo_dir: str) -> Optional[str]:
    if MERGE_SAFE_FLAGS.intersection(args):
        return None
    branch = current_branch(repo_dir)
    if branch and branch in protected_branches(repo_dir):
        return f"`git merge` with the protected branch '{branch}' checked out."
    return None


def check_push(args: List[str], repo_dir: str) -> Optional[str]:
    positional: List[str] = []
    flags: Set[str] = set()
    index = 0
    while index < len(args):
        arg = args[index]
        if arg == "--":
            positional.extend(args[index + 1:])
            break
        if arg.startswith("-"):
            flags.add(arg)
            index += 2 if arg in PUSH_OPTIONS_WITH_VALUE else 1
            continue
        positional.append(arg)
        index += 1

    if flags & PUSH_ALL_BRANCHES_FLAGS:
        return "`git push --all/--mirror/--branches` also pushes the protected branches."

    protected = protected_branches(repo_dir)
    current = current_branch(repo_dir)
    refspecs = positional[1:]  # positional[0] is the remote
    if not refspecs:
        # `--tags` alone pushes only tags; otherwise the current branch goes to its upstream.
        if "--tags" not in flags and current in protected:
            return f"`git push` with the protected branch '{current}' checked out pushes straight to it."
        return None
    for refspec in refspecs:
        destination = push_destination(refspec, current)
        if destination in protected:
            return f"`git push` to the protected branch '{destination}' (refspec '{refspec}')."
    return None


def check_git(args: List[str], cwd: str) -> Optional[str]:
    repo_dir = cwd
    index = 0
    while index < len(args) and args[index].startswith("-"):
        option = args[index]
        if option in GIT_GLOBAL_OPTIONS_WITH_VALUE:
            if option == "-C" and index + 1 < len(args):
                repo_dir = resolve_dir(repo_dir, args[index + 1])
            index += 2
        else:
            index += 1
    if index >= len(args):
        return None
    subcommand, rest = args[index], args[index + 1:]
    if subcommand == "merge":
        return check_merge(rest, repo_dir)
    if subcommand == "push":
        return check_push(rest, repo_dir)
    return None


def check_gh(args: List[str]) -> Optional[str]:
    positional: List[str] = []
    method = ""
    index = 0
    while index < len(args):
        arg = args[index]
        if arg in GH_REPO_FLAGS:
            index += 2
            continue
        if arg in ("-X", "--method"):
            method = args[index + 1] if index + 1 < len(args) else ""
            index += 2
            continue
        if arg.startswith("--method="):
            method = arg.split("=", 1)[1]
        elif arg.startswith("-X"):
            method = arg[2:]
        elif not arg.startswith("-"):
            positional.append(arg)
        index += 1

    if positional[:2] == ["pr", "merge"]:
        return "`gh pr merge` merges the PR without a human; leave the merge to a reviewer."
    if positional[:1] == ["api"]:
        endpoints = [path.split("?", 1)[0] for path in positional[1:]]
        if method.upper() == "PUT" and any(GH_API_MERGE_PATH.search(path) for path in endpoints):
            return "`gh api` call to the pull request merge endpoint."
        if "graphql" in endpoints and any(m in arg for arg in args for m in GH_GRAPHQL_MERGE_MUTATIONS):
            return "`gh api graphql` mutation that merges a pull request."
    return None


def find_violation(command: str, cwd: str, depth: int = 0) -> Optional[str]:
    if depth > MAX_NESTING:
        return None
    for words in split_simple_commands(tokenize(command)):
        words = strip_wrappers(words)
        if not words:
            continue
        program, args = os.path.basename(words[0]), words[1:]
        reason: Optional[str] = None
        if program == "cd":
            cwd = resolve_dir(cwd, args[0] if args else "~")
        elif program == "eval":
            reason = find_violation(" ".join(args), cwd, depth + 1)
        elif program in SHELLS:
            flag_index = next((i for i, arg in enumerate(args) if SHELL_COMMAND_FLAG.match(arg)), None)
            if flag_index is not None and flag_index + 1 < len(args):
                reason = find_violation(args[flag_index + 1], cwd, depth + 1)
        elif program == "git":
            reason = check_git(args, cwd)
        elif program == "gh":
            reason = check_gh(args)
        if reason:
            return reason
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as error:
        print(f"block_direct_merge: invalid hook payload, check skipped: {error}", file=sys.stderr)
        return 1
    if payload.get("tool_name") != "Bash":
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not re.search(r"\b(git|gh)\b", command):
        return 0
    reason = find_violation(command, payload.get("cwd") or os.getcwd())
    if reason is None:
        return 0
    print(f"Blocked: {reason}\n{GUIDANCE}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
