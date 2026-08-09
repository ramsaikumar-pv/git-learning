# Challenge

## Challenge 1: Add coverage reporting

```yaml
      - name: Run tests with coverage
        run: |
          pip install pytest-cov
          pytest tests/ -v --cov=. --cov-report=xml --cov-report=term

      - name: Upload coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage.xml
```

What percentage coverage do your tests achieve? Add a test to cover the `get_config()` function (if it exists in `app.py`).

---

## Challenge 2: Parallel jobs

Split lint and tests into parallel jobs:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install flake8 && flake8 . --max-line-length=100

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt && pytest tests/ -v
```

Does the total pipeline time decrease? When does parallelism help vs when is it overkill?

---

## Challenge 3: CI badge in README

1. Go to your repo → Actions tab → select the CI workflow → click the `...` menu → "Create status badge"
2. Copy the markdown
3. Add it to your README.md:

```markdown
![CI](https://github.com/ramsaikumar-pv/your-repo/actions/workflows/ci.yml/badge.svg)
```

Commit and push. Does the badge update automatically on the next CI run?

---

## Bonus: `act` — run GitHub Actions locally

Install `act` (a tool that runs GitHub Actions workflows locally using Docker):

```bash
# Install on Ubuntu/WSL
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
act push    # simulates a push event
act -l      # list available workflows and jobs
```

This lets you debug workflow files without pushing to GitHub. Huge time-saver for complex pipelines.
