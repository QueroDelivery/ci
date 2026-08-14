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
  "Compare the declaration with the deployed command" \
  "$COMPARE" \
  '${{ github.event_name }}=>$EVENT_NAME'

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
DECLARED='["consumers"]' EVENT_NAME=push \
  assert "declaracao e defs de acordo passam" ok "$COMPARE" "de acordo"

scenario
DECLARED='["consumers"]' EVENT_NAME=push \
  assert "declarado sem pasta nos defs bloqueia no push" erro "$COMPARE" '::error::worker "consumers" declarado sem pasta'

# defs/main e alvo movel: o PR de um dev nao pode ficar vermelho por mudanca
# pendente de outra pessoa.
scenario
DECLARED='["consumers"]' EVENT_NAME=pull_request \
  assert "declarado sem pasta apenas avisa em PR" ok "$COMPARE" '::warning::worker "consumers" declarado sem pasta'

scenario
mkdir -p defs/qd-products-service-worker-consumers/staging
mkdir -p defs/qd-products-service-worker-fantasma/staging
DECLARED='["consumers"]' EVENT_NAME=push \
  assert "pasta orfa nos defs bloqueia no push" erro "$COMPARE" "fantasma"

scenario
mkdir -p defs/qd-products-service-worker-fantasma/staging
DECLARED='[]' EVENT_NAME=pull_request \
  assert "pasta orfa apenas avisa em PR" ok "$COMPARE" "::warning::"

# A app do proprio servico nao pode ser lida como se fosse um worker.
scenario
mkdir -p defs/qd-products-service/staging
DECLARED='[]' EVENT_NAME=push \
  assert "pasta do servico nao e lida como worker" ok "$COMPARE" "de acordo"

scenario
mkdir -p defs/qd-products-service-worker-consumers/staging
DECLARED='["consumers","reports"]' EVENT_NAME=push \
  assert "worker faltando entre dois bloqueia" erro "$COMPARE" "reports"

summary "workers-defs"
