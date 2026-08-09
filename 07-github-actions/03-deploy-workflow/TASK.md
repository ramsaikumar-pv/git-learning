# Task: Build a Deploy Workflow

You'll build a complete CI/CD pipeline: test on every PR, deploy on merge to main.

## Setup

1. Create a GitHub Environment called `staging`:
   - Settings → Environments → New environment → name it `staging`
   - Optionally add yourself as a required reviewer

## Steps

2. Create the deploy workflow:

```bash
vi .github/workflows/deploy.yml
```

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  # Job 1: Run tests (on both PR and push)
  test:
    name: Test
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - run: pip install pytest && pytest tests/ -v

  # Job 2: Deploy (only on push to main, after tests pass)
  deploy:
    name: Deploy to Staging
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    environment: staging

    steps:
      - uses: actions/checkout@v4

      - name: Build release artifact
        run: |
          mkdir -p dist
          cp app.py dist/
          cp config.yaml dist/ 2>/dev/null || true
          echo "BUILD_SHA=${{ github.sha }}" > dist/build.info
          echo "BUILD_TIME=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> dist/build.info
          cat dist/build.info

      - name: Upload release artifact
        uses: actions/upload-artifact@v4
        with:
          name: release-${{ github.sha }}
          path: dist/
          retention-days: 7

      - name: Deployment summary
        run: |
          echo "### Deployment Complete 🚀" >> $GITHUB_STEP_SUMMARY
          echo "- **SHA**: \`${{ github.sha }}\`" >> $GITHUB_STEP_SUMMARY
          echo "- **Branch**: \`${{ github.ref_name }}\`" >> $GITHUB_STEP_SUMMARY
          echo "- **Time**: $(date -u)" >> $GITHUB_STEP_SUMMARY
```

3. Commit and push:

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: add CI/CD pipeline with staging deploy"
git push origin main
```

4. Watch the Actions tab:
   - Does the `test` job run?
   - Does the `deploy` job run (after test passes)?

5. Now open a PR (don't merge it):
   ```bash
   git switch -c test/pr-flow
   echo "# PR test" >> README.md
   git add README.md
   git commit -m "docs: test PR flow"
   git push origin test/pr-flow
   ```
   Open a PR on GitHub. Which jobs run on the PR? Does `deploy` run?

---

## What do you see? What does it mean?

- Why does the `deploy` job have `needs: test`?
- What does `if: github.ref == 'refs/heads/main'` do?
- What shows up in `$GITHUB_STEP_SUMMARY`?
