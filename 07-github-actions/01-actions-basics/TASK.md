# Task: Create Your First GitHub Actions Workflow

You need your repo pushed to GitHub (module 03-01).

## Steps

1. Create the workflows directory:

```bash
mkdir -p .github/workflows
```

2. Create a simple workflow that runs on every push:

```bash
vi .github/workflows/hello.yml
```

Paste:

```yaml
name: Hello World

on:
  push:
    branches: ['**']    # any branch
  pull_request:

jobs:
  greet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Say hello
        run: echo "Hello from GitHub Actions! Branch is ${{ github.ref_name }}"

      - name: Show repo info
        run: |
          echo "Repo: ${{ github.repository }}"
          echo "SHA: ${{ github.sha }}"
          echo "Actor: ${{ github.actor }}"

      - name: List files
        run: ls -la
```

3. Commit and push:

```bash
git add .github/workflows/hello.yml
git commit -m "ci: add hello world workflow"
git push origin main
```

4. Go to GitHub → your repo → Actions tab.

5. Find the workflow run. Click on it. Click on the `greet` job. Expand each step.

6. Create a second workflow that runs on a schedule:

```bash
vi .github/workflows/scheduled.yml
```

```yaml
name: Scheduled Check

on:
  schedule:
    - cron: '*/5 * * * *'   # every 5 minutes (for testing)
  workflow_dispatch:          # manual trigger too

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check file count
        run: |
          echo "Files in repo:"
          find . -not -path './.git/*' | wc -l
```

7. Commit and push. Then manually trigger it via the GitHub UI (Actions tab → "Scheduled Check" → "Run workflow").

---

## What do you see? What does it mean?

- What's in the step output for "Show repo info"?
- How long did the workflow take to run?
- What's the difference between `run: echo "..."` and `run: | echo "..."` (the `|` syntax)?
