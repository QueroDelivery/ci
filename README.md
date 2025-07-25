# CI

Este repositório contém workflows do **GitHub Actions** usados para construir aplicações Node, publicar imagens no Amazon ECR e realizar implantações em clusters Kubernetes. Também há um fluxo destinado à remoção de aplicações em ambientes de revisão.

## Visão geral dos fluxos

- **CI-BASE** (`base_node_build.yml`): fluxo de construção de projetos Node. Executa instalação de dependências, lint, testes e publica uma versão através do [semantic-release](https://github.com/semantic-release/semantic-release).
- **CI-ECR-BASE** (`base_build_push_ecr.yml`): prepara o repositório ECR, gera o arquivo `.env` opcionalmente, constrói a imagem Docker e faz push para o ECR.
- **CI-K8-BASE** (`ci_k8_base.yml`): realiza o deploy de imagens no Kubernetes utilizando arquivos padronizados presentes neste repositório.
- **CI-K8-BASE-UNDEPLOY** (`ci_k8_undeploy_base.yml`): remove um deploy previamente criado para ambientes de revisão.
- **CI-LOCAL** (`ci_local.yml`): fluxo simplificado utilizado apenas para executar o `semantic-release` localmente.

Os arquivos ficam em `.github/workflows/` e são reutilizáveis via `workflow_call` em outros repositórios.

## Diagramas de sequência

### CI-BASE
```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Runner as Runner
    GH->>Runner: checkout do repositório
    Runner->>Runner: setup Node e cache
    Runner->>Runner: instalar dependências
    Runner->>Runner: lint
    Runner->>Runner: testes
    Runner->>Runner: semantic-release
    Runner->>GH: retorna nome do serviço
```

### CI-ECR-BASE
```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Runner as Runner
    GH->>Runner: checkout do repositório
    Runner->>Runner: configurar AWS e login no ECR
    alt commit inicial
        Runner->>Runner: criar repositórios ECR
    end
    Runner->>Runner: (opcional) gerar .env do Parameter Store
    Runner->>Runner: build e push da imagem
    Runner->>GH: exporta nome do serviço e imagem
```

### CI-K8-BASE
```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Runner as Runner
    GH->>Runner: checkout código e repositório kube
    Runner->>Runner: configurar AWS e login no ECR
    Runner->>Runner: gerar configmap a partir do Parameter Store
    Runner->>Runner: sobrescrever manifestos quando necessário
    Runner->>Runner: configurar kubectl
    Runner->>Runner: aplicar manifestos (namespace, configmap, deployment, hpa, service, ingress)
    Runner->>Runner: opcionalmente definir visibilidade e comentar na PR
    opt criar PR para main
        Runner->>GH: abrir PR
    end
```

### CI-K8-BASE-UNDEPLOY
```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Runner as Runner
    GH->>Runner: checkout código e repositório kube
    Runner->>Runner: configurar AWS e login no ECR
    Runner->>Runner: configurar kubectl
    Runner->>Runner: deletar namespace
```

## Política do ECR

Apolítica `ecr_policy.json` define uma regra de lifecycle para manter apenas as duas últimas imagens em cada repositório do ECR:

```json
{
    "rules": [
      {
        "rulePriority": 1,
        "description": "Expire count images more then 2 ",
        "selection": {
          "tagStatus": "any",
          "countType": "imageCountMoreThan",
          "countNumber": 2
        },
        "action": {
          "type": "expire"
        }
      }
    ]
}
```

## Execução local

O workflow `ci_local.yml` é utilizado apenas para disparar o `semantic-release` quando um push é realizado na branch `main`.

