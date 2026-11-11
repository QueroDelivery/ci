"""Tests for block_direct_merge.py, run the way Claude Code runs it: JSON payload on stdin.

Run with: python3 -B -m unittest discover -s .claude/hooks -v
"""

import json
import os
import shlex
import subprocess
import sys
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "block_direct_merge.py")


def make_repo(root: str, name: str, branch: str, default_branch: str = "") -> str:
    """Create an empty repo with `branch` checked out (no commits needed)."""
    path = os.path.join(root, name)
    quiet = {"check": True, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    subprocess.run(["git", "init", "--quiet", path], **quiet)
    subprocess.run(["git", "-C", path, "symbolic-ref", "HEAD", f"refs/heads/{branch}"], **quiet)
    if default_branch:
        subprocess.run(
            ["git", "-C", path, "symbolic-ref", "refs/remotes/origin/HEAD", f"refs/remotes/origin/{default_branch}"],
            **quiet,
        )
    return path


class BlockDirectMergeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.on_main = make_repo(cls._tmp.name, "on-main", "main")
        cls.on_feature = make_repo(cls._tmp.name, "on-feature", "feature")
        cls.develop_default = make_repo(cls._tmp.name, "develop-default", "feature", default_branch="develop")

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def run_hook(self, command: str, cwd: str, tool_name: str = "Bash") -> subprocess.CompletedProcess:
        payload = {"tool_name": tool_name, "tool_input": {"command": command}, "cwd": cwd}
        return subprocess.run(
            [sys.executable, "-B", HOOK], input=json.dumps(payload), capture_output=True, text=True, check=False
        )

    def assert_cases(self, cases, expected_code: int) -> None:
        for command, cwd in cases:
            with self.subTest(command=command, cwd=os.path.basename(cwd)):
                result = self.run_hook(command, cwd)
                self.assertEqual(result.returncode, expected_code, f"stderr: {result.stderr}")
                if expected_code == 2:
                    self.assertIn("pull request", result.stderr)

    def test_blocks_merge_into_protected_branch(self) -> None:
        self.assert_cases(
            [
                ("git merge feature", self.on_main),
                ("git merge --no-ff --squash feature", self.on_main),
                (f"git -C {shlex.quote(self.on_main)} merge feature", self.on_feature),
                (f"cd {shlex.quote(self.on_main)} && git merge feature", self.on_feature),
            ],
            2,
        )

    def test_blocks_push_to_protected_branch(self) -> None:
        self.assert_cases(
            [
                ("git push origin main", self.on_feature),
                ("git push origin master", self.on_feature),
                ("git push origin HEAD:main", self.on_feature),
                ("git push -f origin +feature:refs/heads/main", self.on_feature),
                ("git push origin --delete main", self.on_feature),
                ("git push origin :main", self.on_feature),
                ("git push --all origin", self.on_feature),
                ("git push", self.on_main),
                ("git push -u origin HEAD", self.on_main),
                ("git push origin develop", self.develop_default),
            ],
            2,
        )

    def test_blocks_merging_pull_requests_from_cli(self) -> None:
        self.assert_cases(
            [
                ("gh pr merge 123 --squash", self.on_feature),
                ("gh pr merge --auto --merge", self.on_feature),
                ("gh -R QueroDelivery/ci pr merge 1", self.on_feature),
                ("gh api -X PUT repos/QueroDelivery/ci/pulls/1/merge", self.on_feature),
                ("gh api graphql -f query='mutation { mergePullRequest(input: {}) { clientMutationId } }'", self.on_feature),
            ],
            2,
        )

    def test_sees_through_chains_and_nested_shells(self) -> None:
        self.assert_cases(
            [
                ("npm test && git push origin main", self.on_feature),
                ("git status; git push origin main", self.on_feature),
                ("git status # inline comment\ngit push origin main", self.on_feature),
                ("GIT_TRACE=1 git push origin main 2>&1 | tail -5", self.on_feature),
                ('bash -c "git push origin main"', self.on_feature),
                ("eval git push origin main", self.on_feature),
            ],
            2,
        )

    def test_allows_pr_based_workflow(self) -> None:
        self.assert_cases(
            [
                ("git push -u origin feature", self.on_feature),
                ("git push", self.on_feature),
                ("git push origin feature/main-fix", self.on_feature),
                ("git merge main", self.on_feature),
                ("git merge --abort", self.on_main),
                ("git pull", self.on_main),
                ("git push --tags", self.on_main),
                ("gh pr create --base main --title x --body y", self.on_feature),
                ("gh pr view 12 --json mergeable", self.on_feature),
                ("gh api repos/QueroDelivery/ci/pulls/1/merge", self.on_feature),
                ('git commit -m "docs: never git push origin main"', self.on_feature),
                ("cat > notes.md <<'EOF'\nDon't run: git push origin main\nEOF\ngit status", self.on_feature),
                ("echo main 2>&1", self.on_main),
            ],
            0,
        )

    def test_ignores_other_tools(self) -> None:
        result = self.run_hook("git push origin main", self.on_feature, tool_name="Write")
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
