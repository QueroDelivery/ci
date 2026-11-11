# SPA CI/CD

Reusable GitHub Actions workflows that build a single-page application, provision its S3 and CloudFront infrastructure with Terraform, upload the build, and invalidate the cache.

The Terraform module lives in [`QueroDelivery/terraform`](https://github.com/QueroDelivery/terraform) at `infra/spa-static-frontend`. Application repositories do not keep a copy of that module. The deploy workflow checks it out at tag `v1.2.0` and applies it.

## Architecture

- **Stage and prod.** Terraform state is isolated per application and environment: `<app_name>/<environment>/terraform.tfstate`.
- **Preview.** State is shared at `global/preview/terraform.tfstate`. Previews reuse one S3 bucket and one wildcard CloudFront distribution.
- **Locking.** The state bucket uses S3 lock files (`use_lockfile`, Terraform 1.10+).
- **Name.** The application name, the Route 53 record, and the preview prefix come from the `name` field in `package.json`. The workflow removes the npm scope, lowercases the name, and replaces any character outside `a-z0-9-` with `-`. `@querodelivery/qd-plan` becomes `qd-plan`.

## Application prerequisites

```json
{
  "name": "@querodelivery/checkout-app",
  "scripts": {
    "build": "vite build",
    "test:ci": "vitest run --coverage"
  }
}
```

The deploy workflow always runs, after `yarn install --frozen-lockfile`:

- commit message lint
- `yarn tsc --build`
- `yarn test:ci`
- on a pull request, a Vitest coverage comment

The coverage comment reads `coverage/coverage-summary.json` and `coverage/coverage-final.json`. Configure Vitest with those reporters:

```ts
coverage: {
  reporter: ['text', 'json-summary', 'json'],
}
```

`yarn release` runs before the build when `has_semantic_release` is `true` and the environment is not `preview`.

## Pin a release

Every `uses` below must point at a full release tag of this repository. The examples pin `v5.11.0`, the release that contains this guide. Do not use `@main`, a branch name, or a floating major such as `v5`. `main` moves on every merge and would change the pipeline of every application that calls it.

Use the same tag in every caller workflow of one application. A newer CI release is adopted only by changing that tag in the application repository.

## Caller workflows

Add these files under `.github/workflows/` in the application repository.

The calling job uses a GitHub environment named `preview`, `stage`, or `prod`. Put the secrets on that environment.

### Preview (`.github/workflows/preview.yml`)

```yaml
name: Deploy Preview

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  deploy_preview:
    uses: QueroDelivery/ci/.github/workflows/ci_s3_deploy_multi_environment.yml@v5.11.0
    with:
      environment_type: preview
      node_version: 22
      has_semantic_release: false
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.NEW_AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.NEW_AWS_SECRET_ACCESS_KEY }}
      AWS_REGION: ${{ secrets.AWS_REGION }}
      SPA_PROD_CERT_ARN: ${{ secrets.SPA_PROD_CERT_ARN }}
      SPA_STAGE_CERT_ARN: ${{ secrets.SPA_STAGE_CERT_ARN }}
      SPA_PREVIEW_CERT_ARN: ${{ secrets.SPA_PREVIEW_CERT_ARN }}
      SPA_TF_STATE_BUCKET: ${{ secrets.SPA_TF_STATE_BUCKET }}
      WF_GITHUB_TOKEN: ${{ secrets.WF_GITHUB_TOKEN }}
```

The preview URL is `https://<app>-pr-<N>.<preview-domain>`, with the `*.` prefix removed from `SPA_PREVIEW_DOMAIN`.

### Clear preview (`.github/workflows/clear-preview.yml`)

Runs when the pull request is closed. It removes the preview prefix from S3 and invalidates CloudFront. It does not run Terraform.

```yaml
name: Clear Preview

on:
  pull_request:
    types: [closed]

permissions:
  contents: read

jobs:
  clear_preview:
    uses: QueroDelivery/ci/.github/workflows/ci_s3_clear_preview.yml@v5.11.0
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.NEW_AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.NEW_AWS_SECRET_ACCESS_KEY }}
      AWS_REGION: ${{ secrets.AWS_REGION }}
```

### Stage (`.github/workflows/deploy-stage.yml`)

`create_pr_in_main` compares the branches named `stage` and `main`. Keep the stage branch name as `stage`.

```yaml
name: Deploy Stage

on:
  push:
    branches:
      - stage

permissions:
  contents: write
  pull-requests: write

jobs:
  deploy_stage:
    uses: QueroDelivery/ci/.github/workflows/ci_s3_deploy_multi_environment.yml@v5.11.0
    with:
      environment_type: stage
      node_version: 22
      has_semantic_release: false
      create_pr_in_main: true
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.NEW_AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.NEW_AWS_SECRET_ACCESS_KEY }}
      AWS_REGION: ${{ secrets.AWS_REGION }}
      SPA_PROD_CERT_ARN: ${{ secrets.SPA_PROD_CERT_ARN }}
      SPA_STAGE_CERT_ARN: ${{ secrets.SPA_STAGE_CERT_ARN }}
      SPA_PREVIEW_CERT_ARN: ${{ secrets.SPA_PREVIEW_CERT_ARN }}
      SPA_TF_STATE_BUCKET: ${{ secrets.SPA_TF_STATE_BUCKET }}
      WF_GITHUB_TOKEN: ${{ secrets.WF_GITHUB_TOKEN }}
```

### Production (`.github/workflows/deploy-prod.yml`)

```yaml
name: Deploy Production

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy_prod:
    uses: QueroDelivery/ci/.github/workflows/ci_s3_deploy_multi_environment.yml@v5.11.0
    with:
      environment_type: prod
      node_version: 22
      has_semantic_release: true
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.NEW_AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.NEW_AWS_SECRET_ACCESS_KEY }}
      AWS_REGION: ${{ secrets.AWS_REGION }}
      SPA_PROD_CERT_ARN: ${{ secrets.SPA_PROD_CERT_ARN }}
      SPA_STAGE_CERT_ARN: ${{ secrets.SPA_STAGE_CERT_ARN }}
      SPA_PREVIEW_CERT_ARN: ${{ secrets.SPA_PREVIEW_CERT_ARN }}
      SPA_TF_STATE_BUCKET: ${{ secrets.SPA_TF_STATE_BUCKET }}
      WF_GITHUB_TOKEN: ${{ secrets.WF_GITHUB_TOKEN }}
```

Stage is published at `https://<app>.stg.<hosted-zone>`. Production is published at `https://<app>.<hosted-zone>`.

`custom_aliases` and `custom_certificate_arn` are optional. Leave either one out and the workflow does not pass that variable. The module then keeps its default: no extra aliases, and the certificate from `certificate_arn`.

In prod, `custom_aliases` is a Terraform list added next to `<app>.<hosted-zone>`. `custom_certificate_arn` replaces `certificate_arn` when it is set, so the extra domains can use their own ACM certificate in `us-east-1`. Stage and preview ignore both values. The certificate in use must cover every alias.

```yaml
      custom_aliases: '["qdplan.querodelivery.com"]'
      custom_certificate_arn: ${{ secrets.SPA_CUSTOM_CERT_ARN }}
```

`custom_aliases` is a Terraform list. `custom_certificate_arn` is the certificate ARN. The workflow checks out Terraform `v1.2.0`, which declares both variables.

## Inputs

| Input | Type | Required | Default | Description |
|---|---|---|---|---|
| `environment_type` | `string` | Yes | — | `preview`, `stage`, or `prod`. |
| `node_version` | `number` | No | `22` | Node.js version used to install, test, and build. |
| `has_semantic_release` | `boolean` | No | `true` | Runs `yarn release` before the build. Skipped for `preview`. |
| `create_pr_in_main` | `boolean` | No | `false` | On `stage`, opens a pull request from `stage` to `main` when one is not already open. |
| `custom_aliases` | `string` | No | empty | Optional Terraform list of extra CloudFront aliases, for example `["qdplan.querodelivery.com"]`. Empty omits the variable and the module keeps its default `[]`. |
| `custom_certificate_arn` | `string` | No | empty | Optional ACM certificate ARN in `us-east-1`. In prod it replaces `certificate_arn` when set. Empty omits the variable. |

## Secrets

Pass these secrets from the caller. `WF_GITHUB_TOKEN` is optional in the workflow contract and required in practice: the job uses it to check out the Terraform repository, lint commits, comment coverage, run semantic-release, and open the production pull request.

- `NEW_AWS_ACCESS_KEY_ID` and `NEW_AWS_SECRET_ACCESS_KEY`: credentials that can apply the Terraform module, sync S3, and invalidate CloudFront. These are the secrets callers must use. Pass them into the workflow inputs `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Do not use the older `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` repository secrets.
- `AWS_REGION`: AWS region for those credentials.
- `SPA_TF_STATE_BUCKET`: S3 bucket that stores the Terraform state.
- `SPA_PROD_CERT_ARN`, `SPA_STAGE_CERT_ARN`, `SPA_PREVIEW_CERT_ARN`: ACM certificate ARNs in `us-east-1`, one per environment.
- `WF_GITHUB_TOKEN`: classic token with `repo` scope.

`ci_s3_clear_preview.yml` only needs `NEW_AWS_ACCESS_KEY_ID`, `NEW_AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`. It reads the preview bucket and the CloudFront distribution from organization variables.

## Organization variables

- `SPA_HOSTED_ZONE_NAME`: Route 53 hosted zone, for example `app.quero.io`.
- `SPA_PREVIEW_DOMAIN`: wildcard domain of the shared preview distribution, for example `*.preview.app.quero.io`.
- `SPA_PREVIEW_BUCKET_NAME`: shared S3 bucket for preview builds.
