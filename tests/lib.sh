#!/usr/bin/env bash
# Helpers comuns aos testes de scripts de workflow.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export REPO_ROOT

WORKFLOWS="$REPO_ROOT/.github/workflows"
export WORKFLOWS

pass=0
fail=0

# extract <workflow> <nome do step> <destino> [expr=>valor ...]
extract() {
  node "$REPO_ROOT/tests/extract-step.js" "$@" || exit 1
  chmod +x "$3"
}

# assert <descricao> <ok|erro> <script> [padrao esperado na saida]
assert() {
  local description="$1" expectation="$2" script="$3" pattern="${4:-}"
  local out status

  out="$(bash "$script" 2>&1)"
  status=$?

  local ok=1
  if [ "$expectation" = "ok" ] && [ "$status" != "0" ]; then ok=0; fi
  if [ "$expectation" = "erro" ] && [ "$status" = "0" ]; then ok=0; fi
  if [ -n "$pattern" ] && ! printf '%s' "$out" | grep -q "$pattern"; then ok=0; fi

  if [ "$ok" = "1" ]; then
    pass=$((pass + 1))
    printf '  PASS  %s\n' "$description"
  else
    fail=$((fail + 1))
    printf '  FAIL  %s (status=%s)\n' "$description" "$status"
    printf '        saida: %s\n' "$out"
  fi
}

summary() {
  printf '\n%s: %s passaram, %s falharam\n' "$1" "$pass" "$fail"
  [ "$fail" = "0" ]
}
