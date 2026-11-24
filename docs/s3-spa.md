# SPA CI/CD

Reusable GitHub Actions workflows that build a single-page application, provision its S3 and CloudFront infrastructure with Terraform, upload the build, and invalidate the cache.

The Terraform module lives in [`QueroDelivery/terraform`](https://github.com/QueroDelivery/terraform) at `infra/spa-static-frontend`. Application repositories do not keep a copy of that module. The deploy workflow checks it out at tag `v1.3.0` and applies it.

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

After `yarn install --frozen-lockfile`, the checks depend on the environment:

- **Preview.** Commit message lint, `yarn tsc --build`, and `yarn lint`. On a pull request, Vitest runs the test files that import a changed file (`yarn test:ci --changed <base> --passWithNoTests`). The full `yarn test:ci` runs when the diff touches `package.json`, a lockfile, Vite or Vitest config, a `tsconfig`, or a test setup file (`setupTests`, `setup-tests`, `vitest.setup`, `test/setup`, `tests/setup`), and whenever preview starts outside a pull request. The coverage comment is posted only after that full run.
- **Stage.** Commit message lint, `yarn tsc --build`, `yarn lint`, and the full `yarn test:ci`.
- **Production.** Those checks are skipped. The job installs dependencies, releases, builds, and uploads the commit that already passed on stage.

`yarn lint` runs only when `package.json` declares a `lint` script. Without one, the step is skipped.

When the `lint` script is a single ESLint command, such as `eslint ./src/**/*.{ts,tsx}`, the workflow adds `--cache --cache-strategy content` and keeps the cache file in the GitHub Actions cache. ESLint then re-lints only the files whose content changed since the cached run. The cache key includes `yarn.lock`, the ESLint config, `.eslintignore`, and the `tsconfig` files, so a change to any of them starts from an empty cache. A pull request reads the cache saved by its own earlier runs or by its base branch, which stage keeps warm. A script that chains other commands (`&&`, `||`, `;`, `|`) or does not start with `eslint` runs without the cache.

Rules that read other files, such as `import/named`, are not re-checked on a file that did not change. The `yarn tsc --build` step, which runs before lint, reports the same broken imports.

`test:ci` must be Vitest and must forward the extra arguments. `yarn test:ci --changed <base> --passWithNoTests` has to reach Vitest unchanged. A pull request that only changes files no test imports succeeds because of `--passWithNoTests`.

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

After the cache invalidation, the workflow comments that URL on the pull request, with the commit, the branch, and a link to the run. The comment starts with `<!-- preview-url -->`, and every later push edits that same comment instead of adding a new one. It is posted with `WF_GITHUB_TOKEN`, or with the caller's `GITHUB_TOKEN` when that secret is absent, which then needs `pull-requests: write`.

On a pull request, preview runs the tests related to the diff. Vitest compares the branch with the pull request base and runs each test file that imports a changed file. Dependencies, Vite, Vitest, TypeScript, and test setup still run the full suite. The coverage comment is posted only after a full suite.

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

The publish job sets that URL on its GitHub environment (`preview`, `stage`, or `prod`). The deployment then shows a **View deployment** button on the pull request and in the repository's **Deployments** page.

Production does not repeat commit lint, the typecheck, ESLint, or tests. Preview and stage already ran those checks on the same commit.

`custom_aliases` is an optional input and `SPA_CUSTOM_CERT_ARN` is an optional secret. Leave either one out and the workflow does not pass that variable. The module then keeps its default: no extra aliases, and the certificate from `certificate_arn`. To serve a domain outside the hosted zone, follow [Custom domains](#custom-domains-custom_aliases).

## Custom domains (`custom_aliases`)

Use this when a stage or production application must also answer on a domain outside the hosted zone, for example `manager.querodelivery.com` next to `qd-manager.app.quero.io` in prod, or `stage-manager.querodelivery.com` next to `qd-manager.stg.app.quero.io` in stage.

How it works:

- `custom_aliases` is a Terraform list added next to the generated domain of the environment: `<app>.<hosted-zone>` in prod, `<app>.stg.<hosted-zone>` in stage.
- `SPA_CUSTOM_CERT_ARN` replaces `certificate_arn` when it is set. The certificate must be in `us-east-1` and cover **every** alias, the generated one included.
- Stage and prod each use their own values, passed by their own caller. Preview ignores both, because it uses one distribution shared by every application.
- The workflow checks out Terraform `v1.3.0`, which applies both variables in stage and prod. Every deploy applies them again, so the aliases and the certificate in the caller are the source of truth.

Steps:

The steps below use prod as the example. For stage, use the stage generated domain (`<app>.stg.<hosted-zone>`), the `stage` environment and the stage caller, and request a separate certificate.

1. **List the names.** The generated domain `<app>.<hosted-zone>` and each custom domain. Example for `qd-manager`: `qd-manager.app.quero.io` and `manager.querodelivery.com`.

2. **Request one ACM certificate** in `us-east-1`, with the generated domain as the main name and the custom domains as alternative names:

   ```bash
   aws acm request-certificate --region us-east-1 --validation-method DNS \
     --domain-name qd-manager.app.quero.io \
     --subject-alternative-names manager.querodelivery.com
   ```

   Use one certificate per application. The command prints the certificate ARN.

3. **Create the DNS validation records.** Get them with:

   ```bash
   aws acm describe-certificate --region us-east-1 --certificate-arn <arn> \
     --query 'Certificate.DomainValidationOptions[].[DomainName,ResourceRecord.Name,ResourceRecord.Value]' --output text
   ```

   Create each CNAME in the DNS zone that owns that name: the generated domain in the hosted zone (Route 53), each custom domain wherever it is hosted (for example Cloudflare). In Cloudflare, leave the record as **DNS only** (no proxy). Wait until the certificate status is `ISSUED`.

4. **Save the ARN as a secret.** In the application repository, add `SPA_CUSTOM_CERT_ARN` to the `prod` environment secrets (or `stage`, for stage). The certificate belongs to one application and one environment, so do not use an organization secret.

5. **Update the production caller** (`deploy-prod.yml`, or `deploy-stage.yml` with `environment_type: stage`):

   ```yaml
       with:
         environment_type: prod
         custom_aliases: '["manager.querodelivery.com"]'
       secrets:
         SPA_CUSTOM_CERT_ARN: ${{ secrets.SPA_CUSTOM_CERT_ARN }}
   ```

   Keep both lines in the caller from now on. Because every deploy of that environment applies these values again, removing `custom_aliases` removes the alias from the distribution, and removing the secret puts `certificate_arn` back.

6. **Deploy.** Push to `main` (or `stage`), or re-run the deploy workflow. The apply adds the alias and the certificate to the distribution, which works on a distribution that already exists. Wait until the distribution status is `Deployed`.

7. **Test before changing DNS.** Call the custom host against the CloudFront name:

   ```bash
   curl -sI --connect-to manager.querodelivery.com:443:<distribution>.cloudfront.net:443 \
     https://manager.querodelivery.com/
   ```

   Expect `200` and no certificate error.

8. **Point the DNS to the application.** Lower the record TTL a few hours before. Then change the custom domain record to a CNAME to the generated domain (`qd-manager.app.quero.io`). In Cloudflare, keep it **DNS only**. Keep the previous target written down: restoring it is the rollback.

9. **Verify** the custom URL in a browser, including a refresh on a deep route.

Common failures:

| Error | Cause |
|---|---|
| `InvalidViewerCertificate` on apply | The certificate does not cover every alias, or is not `ISSUED`, or is not in `us-east-1`. |
| `CNAMEAlreadyExists` on apply | Another CloudFront distribution already has that alias. Remove it there first. |
| Alias disappears after a deploy | The caller no longer passes `custom_aliases` or `SPA_CUSTOM_CERT_ARN`. |

`qd-plan` is the reference: its production distribution serves `qd-plan.app.quero.io` and `qdplan.querodelivery.com` with one certificate that names both.

## Inputs

| Input | Type | Required | Default | Description |
|---|---|---|---|---|
| `environment_type` | `string` | Yes | — | `preview`, `stage`, or `prod`. |
| `node_version` | `number` | No | `22` | Node.js version used to install, test, and build. |
| `has_semantic_release` | `boolean` | No | `true` | Runs `yarn release` before the build. Skipped for `preview`. |
| `create_pr_in_main` | `boolean` | No | `false` | On `stage`, opens a pull request from `stage` to `main` when one is not already open. |
| `build_node_options` | `string` | No | empty | `NODE_OPTIONS` for the build step only, for example `--max-old-space-size=2048` when the build runs out of memory. Install, tests and release keep the Node.js defaults. |
| `custom_aliases` | `string` | No | empty | Optional Terraform list of extra CloudFront aliases, for example `["qdplan.querodelivery.com"]`. Empty omits the variable and the module keeps its default `[]`. |

## Secrets

Pass these secrets from the caller. `WF_GITHUB_TOKEN` is optional in the workflow contract and required in practice: the job uses it to check out the Terraform repository, lint commits, comment coverage and the preview URL, run semantic-release, and open the production pull request.

- `NEW_AWS_ACCESS_KEY_ID` and `NEW_AWS_SECRET_ACCESS_KEY`: credentials that can apply the Terraform module, sync S3, and invalidate CloudFront. These are the secrets callers must use. Pass them into the workflow inputs `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Do not use the older `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` repository secrets.
- `AWS_REGION`: AWS region for those credentials.
- `SPA_TF_STATE_BUCKET`: S3 bucket that stores the Terraform state.
- `SPA_PROD_CERT_ARN`, `SPA_STAGE_CERT_ARN`, `SPA_PREVIEW_CERT_ARN`: ACM certificate ARNs in `us-east-1`, one per environment.
- `SPA_CUSTOM_CERT_ARN`: optional ACM certificate ARN in `us-east-1`. In stage and prod it replaces `certificate_arn` when set. Ignored in preview. Empty omits the variable. Pass it as a secret so the ARN stays masked in the logs.
- `WF_GITHUB_TOKEN`: classic token with `repo` scope.
- `PACKAGE_REGISTRY_ENV`: optional variables for private package registries, one `KEY=value` per line. A step before `Setup Node.js` exports each line to the rest of the build job, so the application's `.npmrc` can read it in every Yarn command, `yarn run` included. A new registry needs no change in this repository. Pass it from the caller:

  ```yaml
  secrets:
    PACKAGE_REGISTRY_ENV: |
      FONT_AWESOME_TOKEN=${{ secrets.FONT_AWESOME_TOKEN }}
  ```

  And reference the variable in the `.npmrc`:

  ```ini
  @fortawesome:registry=https://npm.fontawesome.com/
  //npm.fontawesome.com/:_authToken=${FONT_AWESOME_TOKEN}
  ```

  The step masks every value in the logs. It fails the job when a non-blank line is not in the `KEY=value` format, or when a name starts with `VITE_`, `REACT_APP_`, or `NEXT_PUBLIC_`, so no secret ends up in the public bundle. Build variables still come from the Parameter Store.

  Nothing is exported when the caller does not pass the secret. An application whose `.npmrc` references `${FONT_AWESOME_TOKEN}` must pass that line, or Yarn fails with `Failed to replace env in config`.

`ci_s3_clear_preview.yml` only needs `NEW_AWS_ACCESS_KEY_ID`, `NEW_AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`. It reads the preview bucket and the CloudFront distribution from organization variables.

## Organization variables

- `SPA_HOSTED_ZONE_NAME`: Route 53 hosted zone, for example `app.quero.io`.
- `SPA_PREVIEW_DOMAIN`: wildcard domain of the shared preview distribution, for example `*.preview.app.quero.io`.
- `SPA_PREVIEW_BUCKET_NAME`: shared S3 bucket for preview builds.
