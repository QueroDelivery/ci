#!/usr/bin/env bash
# Comparacao entre a declaracao e o kube-apps-definitions, do job
# validate-workers-defs. E este par que gera CrashLoopBackOff, e ele mora em
# outro repositorio.
set -uo pipefail

# shellcheck source=tests/lib.sh
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

COMPARE="$WORK/compare.sh"

extract "$WORKFLOWS/base_node_build.yml" \
  "Compare the declaration with the deployed folders" \
  "$COMPARE"

scenario() {
  local dir
  dir="$(mktemp -d "$WORK/run.XXXXXX")"
  mkdir -p "$dir/defs"
  cd "$dir" || exit 1
  export SERVICE=qd-products-service
}

echo "workers-defs"

scenario
mkdir -p defs/qd-products-service-worker-consumers/staging
DECLARED='["consumers"]' LEVEL=error \
  assert "declaracao e defs de acordo passam" ok "$COMPARE" "de acordo"

scenario
DECLARED='["consumers"]' LEVEL=error \
  assert "declarado sem a pasta nos defs bloqueia no push" erro "$COMPARE" '::error::worker "consumers" declarado sem a pasta'

# defs/main e alvo movel: o PR de um dev nao pode ficar vermelho por mudanca
# pendente de outra pessoa.
scenario
DECLARED='["consumers"]' LEVEL=warning \
  assert "declarado sem a pasta apenas avisa em PR" ok "$COMPARE" '::warning::worker "consumers" declarado sem a pasta'

scenario
mkdir -p defs/qd-products-service-worker-consumers/staging
mkdir -p defs/qd-products-service-worker-fantasma/staging
DECLARED='["consumers"]' LEVEL=error \
  assert "pasta orfa nos defs bloqueia no push" erro "$COMPARE" "fantasma"

scenario
mkdir -p defs/qd-products-service-worker-fantasma/staging
DECLARED='[]' LEVEL=warning \
  assert "pasta orfa apenas avisa em PR" ok "$COMPARE" "::warning::"

# A app do proprio servico nao pode ser lida como se fosse um worker.
scenario
mkdir -p defs/qd-products-service/staging
DECLARED='[]' LEVEL=error \
  assert "pasta do servico nao e lida como worker" ok "$COMPARE" "de acordo"

scenario
mkdir -p defs/qd-products-service-worker-consumers/staging
DECLARED='["consumers","reports"]' LEVEL=error \
  assert "worker faltando entre dois bloqueia" erro "$COMPARE" "reports"

# LEVEL saiu do bash e virou expressao no env do step: sem esta asercao, a
# regra "bloqueia no push, avisa em PR" ficaria sem cobertura.
cat > "$WORK/level.sh" <<'SH'
grep -q "LEVEL:.*github.event_name == .push.* 'error' || 'warning'" \
  "$WORKFLOWS/base_node_build.yml"
SH
assert "o nivel vem de github.event_name no env do step" ok "$WORK/level.sh"

summary "workers-defs"
