#!/usr/bin/env bash
# Roda todos os testes de scripts de workflow.
#
#   yarn install && bash tests/run.sh
#
# Os testes extraem os scripts dos proprios arquivos de workflow, entao nao
# existe copia para sair de sincronia.
set -uo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

if [ ! -d node_modules/js-yaml ]; then
  echo "js-yaml ausente: rode 'yarn install' antes." >&2
  exit 1
fi

failed=0

for suite in tests/*.test.sh; do
  bash "$suite" || failed=1
done

if [ "$failed" != "0" ]; then
  echo ""
  echo "Ha suites com falha."
  exit 1
fi

echo ""
echo "Todas as suites passaram."
