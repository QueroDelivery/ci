# ci

This repository contains example GitHub Actions workflows that build, publish and deploy Node.js services. Each workflow is designed to be re-used via `workflow_call` in other projects.

## Workflows

### CI-BASE (`.github/workflows/base_node_build.yml`)
This workflow prepares the Node.js project, runs tests and builds a Docker image.
- Sets up the Node environment and caches dependencies
- Runs lint and tests (optionally publishing coverage)
- Publishes a release using semantic-release
- Builds a Docker image and uploads it as an artifact
- Outputs the service name so other workflows can use it
- Validates the workers declared in `.quero/workers/`, when the service has any (see below)

### CI-ECR-BASE (`.github/workflows/base_build_push_ecr.yml`)
Loads the Docker image artifact produced by `CI-BASE` and pushes it to Amazon ECR.
- Configures AWS credentials and logs in to ECR
- Tags the image with the commit SHA and environment
- Optionally tags the pull request number
- Outputs the service name and image digest

### CI-K8-BASE (`.github/workflows/ci_k8_base.yml`)
Deploys the previously built image to Kubernetes.
- Checks out the `kube` manifests repository
- Loads environment variables from AWS SSM
- Renders manifests with `envsubst` and applies them with `kubectl`
- Manages deployment metadata in `.deploys/service.json`
- Optionally comments on the pull request with the deployed image

### CI-K8-BASE-UNDEPLOY (`.github/workflows/ci_k8_undeploy_base.yml`)
Removes preview environments created for pull requests by deleting the Kubernetes namespace.

### promote.yml
Promotes an image from one environment to another.
- Reads deployment metadata from `.deploys/service.json` or a dev artifact
- Updates the target environment entry and retags the image in ECR
- Pushes the updated metadata back to the `deploy-state` branch

### CI-WORKERS-DEPLOY (`.github/workflows/ci_workers_deploy.yml`)
Deploys the workers a service declares in `.quero/workers/`, one job per worker, derived from the declaration — adding a worker adds no workflow line to any service.

It does **not** call `CI-PUSH_GITOPS`: a worker runs the same image, in the same namespace and with the same ConfigMap as its service, so it only needs its image tag bumped in `kube-apps-definitions`. Worker sizing (cpu, memory, probes, replicas) stays in `kube-apps-definitions`, owned by DevOps.

The matrix is serial on purpose: the jobs commit to the same definitions repo, and concurrent pushes turn into rebase conflicts.

### CI-LOCAL (`.github/workflows/ci_local.yml`)
Runs semantic-release on the `main` branch. It is mainly used locally to generate releases.

## Workers convention (`.quero/workers/`)

A service declares each worker in one file, `.quero/workers/<name>.yaml`:

```yaml
name: consumers
description: Consumes the catalog Kafka topics
owner: team-merchant
entrypoint: dist/src/worker.js
```

The deployed command is derived from it as `node <entrypoint> <name>`, and the app in `kube-apps-definitions` is `<service>-worker-<name>`.

**Adopting the convention is creating the file.** No service workflow changes: `CI-BASE` detects the directory and skips every worker job when it is absent, so a service with no worker pays nothing.

Three things are checked, in this order:

1. **The declaration, before `yarn release`.** Schema, `name` matching the filename, a single entrypoint across the service, and an existing `src/workers/<name>.worker.ts`. Cheap and fails fast — it runs before the release precisely because the authoritative check cannot.
2. **The declaration against the built image** (`validate-workers`). Runs `<entrypoint> --list` inside the image that is about to ship and compares the set of workers it accepts with the declared one. This is the authoritative check, and it can only run after `docker build` — which happens after `yarn release`. Hence the split.
3. **The declaration against `kube-apps-definitions`** (`validate-workers-defs`). Read-only: DevOps keeps the pen. A declared worker with no folder never deploys; a folder with no declaration means a pod running a name the entrypoint does not know, which is `CrashLoopBackOff` forever. Blocking on push, warning on pull request, because `defs/main` is a moving target and a developer's PR should not go red over someone else's pending change.

The `--list` contract lives in `@querodelivery/qd-packages` (`WorkerBootstrap`): it prints the registry as JSON and exits before touching Mongo, Redis or the broker, so it answers with no environment configured.

## Tests

The bash inside the workflows is tested. The tests extract the scripts from the workflow files themselves, so there is no copy to fall out of sync:

```bash
yarn install
yarn test
```

## Sequence overview

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant CI_BASE as CI-BASE
    participant CI_ECR as CI-ECR-BASE
    participant Deploy as CI-K8-BASE
    Dev->>CI_BASE: workflow_call
    CI_BASE->>CI_ECR: upload image artifact
    CI_ECR->>Deploy: push image & output digest
    Deploy->>Kubernetes: apply manifests
```

## Promote flow

```mermaid
flowchart TD
    A[Deploy metadata] --> B[promote.yml]
    B --> C{FROM_ENV}
    C -->|dev| D[Download artifact]
    C -->|stg/prod| E[Read .deploys/service.json]
    D --> F[Update metadata for TO_ENV]
    E --> F
    F --> G[Retag image in ECR]
    G --> H[Push deploy-state]
```
The `ci_local.yml` workflow is used only for running semantic-release locally
