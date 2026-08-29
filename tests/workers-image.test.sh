#!/usr/bin/env bash
# Comparacao entre os workers que a IMAGEM aceita e a declaracao, do job
# validate-workers. Um docker falso no PATH simula a saida do `--list`.
set -uo pipefail

# shellcheck source=tests/lib.sh
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

COMPARE="$WORK/compare.sh"
STUB="$WORK/bin"
mkdir -p "$STUB"

extract "$WORKFLOWS/base_node_build.yml" \
  "Compare the image registry with the declaration" \
  "$COMPARE"

stub_docker() {
  cat > "$STUB/docker" <<EOF
#!/usr/bin/env bash
cat <<'LIST_OUTPUT'
$1
LIST_OUTPUT
EOF
  chmod +x "$STUB/docker"
}

export IMAGE=qd-products-service:ci-build
export ENTRYPOINT=dist/src/worker.js
export PATH="$STUB:$PATH"

echo "workers-image"

stub_docker '["consumers"]'
DECLARED='["consumers"]' assert "imagem e declaracao iguais passam" ok "$COMPARE"

stub_docker '["consumers","reports"]'
DECLARED='["reports","consumers"]' assert "ordem diferente com mesmo conjunto passa" ok "$COMPARE"

stub_docker '["consumers"]'
DECLARED='["consumers","reports"]' assert "declarado que a imagem nao aceita falha" erro "$COMPARE" "divergem"

stub_docker '["consumers","reports"]'
DECLARED='["consumers"]' assert "worker na imagem sem declaracao falha" erro "$COMPARE" "divergem"

# Agente de instrumentacao escrevendo em stdout antes do entrypoint nao pode
# invalidar a leitura.
stub_docker 'OpenTelemetry agent loaded
noise from a preload hook
["consumers"]'
DECLARED='["consumers"]' assert "ruido antes do JSON nao invalida a leitura" ok "$COMPARE"

stub_docker 'Error: cannot find module'
DECLARED='["consumers"]' assert "saida nao-JSON falha mostrando a saida completa" erro "$COMPARE" "cannot find module"

stub_docker '{"consumers":true}'
DECLARED='["consumers"]' assert "JSON que nao e array falha" erro "$COMPARE" "array JSON"

summary "workers-image"
