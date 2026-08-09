# CI Pipeline 🌱

## 📖 In plain words

CI (Continuous Integration) simply means: every time someone changes code, a robot automatically builds it and runs the tests — without anyone having to remember to do it manually. The goal is to catch broken code the moment it appears, before it ever reaches `main`.

A CI pipeline for a Python service typically:
1. Checks out code
2. Installs dependencies
3. Lints (checks code style)
4. Runs tests
5. Reports results

For a platform team: CI is the automated admission check that runs before a PR can merge. It's your `pre-receive` hook at scale.

---

## A real CI workflow

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Cache pip dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Lint with flake8
        run: |
          pip install flake8
          flake8 . --max-line-length=100 --exclude=.git,__pycache__

      - name: Run tests
        run: python -m pytest tests/ -v

      - name: Upload test results
        if: always()    # run even if tests fail
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: test-results.xml
```

---

## Dependency caching

Without caching, every workflow run installs packages from scratch. With `actions/cache`, the `~/.cache/pip` directory is saved and restored between runs. The cache key includes the hash of `requirements.txt` — if the file changes, the cache is invalidated.

This cuts install time from 60s → 5s for warm runs.

---

## Failing fast

By default, all steps in a job run sequentially. If one fails, subsequent steps are skipped. Use `if: always()` on a cleanup step if it must run regardless of previous failures.

```yaml
- name: Cleanup
  if: always()
  run: rm -rf /tmp/test-artifacts
```

---

## Status badges

After CI is running, add a badge to your README:

```markdown
![CI](https://github.com/ramsaikumar-pv/my-repo/actions/workflows/ci.yml/badge.svg)
```

Shows green/red in your README based on the last CI run on `main`.

---

## Branch rules + CI

In module 06-03, you set up branch protection. Now add:
- "Require status checks to pass before merging"
- Select your CI workflow as a required check

This makes CI mandatory. No broken code can merge to `main`.

---

## ✅ Quick recap

- CI pipeline = checkout → install deps → lint → test → report, all automatic.
- `actions/cache` speeds up repeat runs by reusing downloaded dependencies.
- `if: always()` lets a step (like cleanup or uploading results) run even after a failure.
- Pair CI with branch protection's "required status checks" to make it truly mandatory.
