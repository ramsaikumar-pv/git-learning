# Challenge

## Challenge 1: Matrix strategy

Run your workflow on multiple Python versions simultaneously:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python --version
```

This creates 4 parallel jobs. View them in the Actions tab — are they running in parallel? What's the total time vs running them sequentially?

---

## Challenge 2: Workflow dispatch with inputs

Add a manual trigger with user input:

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options: [staging, production]
      dry_run:
        description: 'Dry run only?'
        required: false
        type: boolean
        default: true
```

Trigger it manually from the Actions tab. Select different options and see how `${{ inputs.environment }}` and `${{ inputs.dry_run }}` change.

---

## Challenge 3: Environment variables and secrets

Add a step that uses an environment variable:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      APP_VERSION: '1.0.0'
      LOG_LEVEL: debug
    steps:
      - run: echo "Version $APP_VERSION, logging at $LOG_LEVEL"
```

Then add a secret: Settings → Secrets and variables → Actions → New repository secret. Name it `MY_SECRET`. Reference it in your workflow:

```yaml
      - run: echo "Secret length is ${#MY_SECRET}"
        env:
          MY_SECRET: ${{ secrets.MY_SECRET }}
```

Notice: GitHub masks secret values in logs (replaces with `***`). Does the length still work?

---

## Bonus: Understand the GitHub Actions marketplace

Go to github.com/marketplace?type=actions. Browse:
- `actions/checkout` — what's new in v4 vs v3?
- `actions/cache` — why would you cache `~/.cache/pip`?
- `docker/build-push-action` — builds and pushes Docker images
- `azure/k8s-deploy` — deploys to Kubernetes

As a platform engineer, which of these would be most immediately useful to your work?
