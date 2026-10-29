// Extrai o `run:` de um step nomeado de um workflow, para o script real ser
// exercitado fora do GitHub Actions. O workflow continua sendo a fonte unica:
// os testes leem dele, nao de uma copia.
//
// Uso: node tests/extract-step.js <workflow> <nome do step> <destino> [expr=>valor ...]
const fs = require('fs');
const yaml = require('js-yaml');

const [file, stepName, outFile, ...substitutions] = process.argv.slice(2);
const doc = yaml.load(fs.readFileSync(file, 'utf8'));

let found;
for (const job of Object.values(doc.jobs || {})) {
  for (const step of job.steps || []) {
    if (step.name === stepName) {
      found = step.run;
    }
  }
}

if (!found) {
  console.error(`step nao encontrado: ${stepName}`);
  process.exit(1);
}

let script = found;
for (const pair of substitutions) {
  const [from, to] = pair.split('=>');
  script = script.split(from).join(to);
}

// Uma expressao ${{ }} nao substituida quebraria o bash de forma confusa:
// melhor falhar aqui, dizendo qual e.
if (/\$\{\{/.test(script)) {
  console.error(`expressao nao substituida em "${stepName}":`);
  console.error(script.match(/\$\{\{[^}]*\}\}/g).join('\n'));
  process.exit(1);
}

fs.writeFileSync(outFile, `#!/usr/bin/env bash\n${script}`);
