#!/usr/bin/env bash
# Checagem barata da declaracao em .quero/workers/, do job setup do
# base_node_build.yml. Roda antes do `yarn release` e existe para falhar rapido.
set -uo pipefail

# shellcheck source=tests/lib.sh
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

VALIDATE="$WORK/validate.sh"
RUNNER="$WORK/runner.sh"

extract "$WORKFLOWS/base_node_build.yml" "Validating workers declaration" "$VALIDATE"

# O script comunica pelo $GITHUB_OUTPUT: o runner junta stdout e outputs para as
# asserções poderem olhar os dois.
cat > "$RUNNER" <<EOF
#!/usr/bin/env bash
export GITHUB_OUTPUT="\$PWD/.github_output"
: > "\$GITHUB_OUTPUT"
bash "$VALIDATE"
status=\$?
cat "\$GITHUB_OUTPUT"
exit \$status
EOF
chmod +x "$RUNNER"

fixture() {
  local dir
  dir="$(mktemp -d "$WORK/repo.XXXXXX")"
  mkdir -p "$dir/.quero/workers" "$dir/src/workers"
  cd "$dir" || exit 1
}

declaration() {
  cat <<EOF
name: $1
description: Consome os topicos do catalogo
owner: team-merchant
entrypoint: ${2:-dist/src/worker.js}
EOF
}

echo "workers-declaration"

# Servico sem worker nao paga nada: e o que permite a convencao valer para os 38
# repos sem editar workflow nenhum.
cd "$(mktemp -d "$WORK/repo.XXXXXX")" || exit 1
assert "servico sem .quero/workers/ passa e emite has_workers=false" ok "$RUNNER" "has_workers=false"

fixture
declaration consumers > .quero/workers/consumers.yaml
touch src/workers/consumers.worker.ts
assert "declaracao valida emite has_workers=true" ok "$RUNNER" "has_workers=true"
assert "declaracao valida emite o nome do worker" ok "$RUNNER" 'workers=\["consumers"\]'

fixture
declaration reports > .quero/workers/reports.yaml
declaration consumers > .quero/workers/consumers.yaml
touch src/workers/reports.worker.ts src/workers/consumers.worker.ts
assert "dois workers saem ordenados" ok "$RUNNER" 'workers=\["consumers","reports"\]'

fixture
declaration outro > .quero/workers/consumers.yaml
touch src/workers/consumers.worker.ts
assert "name divergente do nome do arquivo falha" erro "$RUNNER" "igual ao nome do arquivo"

# O caso que gera CrashLoopBackOff: declarado e nao implementado.
fixture
declaration consumers > .quero/workers/consumers.yaml
assert "worker declarado sem implementacao falha" erro "$RUNNER" "sem implementacao"

fixture
printf 'name: consumers\nentrypoint: dist/src/worker.js\n' > .quero/workers/consumers.yaml
touch src/workers/consumers.worker.ts
assert "campo obrigatorio ausente falha" erro "$RUNNER" "campo obrigatorio ausente"

# Um servico, uma imagem, um entrypoint.
fixture
declaration consumers > .quero/workers/consumers.yaml
declaration reports dist/src/outro.js > .quero/workers/reports.yaml
touch src/workers/consumers.worker.ts src/workers/reports.worker.ts
assert "entrypoints diferentes entre workers falham" erro "$RUNNER" "entrypoints diferentes"

fixture
assert "pasta .quero/workers/ vazia falha" erro "$RUNNER" "nao declara nenhum worker"

# Em producao o worker roda compilado.
fixture
declaration consumers > .quero/workers/consumers.yaml
touch src/workers/consumers.worker.js
assert "implementacao .js e aceita" ok "$RUNNER" "has_workers=true"

summary "workers-declaration"
