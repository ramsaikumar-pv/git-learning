# GitHub Actions Basics 🌱

## 📖 In plain words

GitHub Actions lets GitHub automatically *do things* for you whenever something happens in your repo — most commonly, whenever code is pushed. You describe what should happen in a YAML file; GitHub spins up a temporary computer (called a runner) and follows your instructions step by step, then throws the computer away when done.

For a platform engineer: think of it like a Kubernetes Job that runs on a trigger. The runner is the pod, the steps are the container commands, the workflow file is the Job spec.

---

## Workflow file location

```
.github/
└── workflows/
    └── ci.yml          # your workflow definition
```

Any `.yml` file in `.github/workflows/` is a workflow.

---

## Anatomy of a workflow

```yaml
name: CI

on:                         # what triggers this workflow
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:                     # job name (any identifier)
    runs-on: ubuntu-latest  # runner OS

    steps:
      - name: Checkout code
        uses: actions/checkout@v4    # official action

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m pytest tests/
```

---

## Key concepts

| Concept | Explanation |
|---------|-------------|
| `on` | Trigger events (push, pull_request, schedule, workflow_dispatch) |
| `jobs` | Parallel units of work. Each job runs on its own runner |
| `steps` | Sequential commands within a job |
| `uses` | A pre-built action from GitHub Marketplace |
| `run` | A raw shell command |
| `with` | Parameters passed to an action |
| `env` | Environment variables for a step or job |

---

## Trigger types

```yaml
on:
  push:
    branches: [main, develop]
    tags: ['v*']              # only on version tags
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'      # every Monday at 6am UTC
  workflow_dispatch:          # manual trigger via GitHub UI
```

---

## The runner

`runs-on: ubuntu-latest` gives you a fresh Ubuntu VM for every job. Nothing persists between jobs (use artifacts or caching to share state).

Available: `ubuntu-latest`, `ubuntu-22.04`, `windows-latest`, `macos-latest`

---

## actions/checkout

Almost every workflow starts with this. It clones your repo into the runner:

```yaml
- uses: actions/checkout@v4
```

Without this, the runner has no code to work with.

---

## ✅ Quick recap

- A workflow = a YAML file in `.github/workflows/`, triggered automatically by events like `push`.
- `jobs` run in parallel, each on its own runner. `steps` inside a job run in order.
- `uses` runs a pre-built action; `run` runs a raw shell command.
- Almost every workflow starts with `actions/checkout@v4` to get your code onto the runner.
