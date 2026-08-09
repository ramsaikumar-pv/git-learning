# Task: Build a CI Pipeline for Your Python App

## Setup

Make sure you have `app.py` in your repo and a GitHub remote.

Create the required files:

```bash
# requirements.txt (if you don't have one)
cat > requirements.txt << 'EOF'
pytest==7.4.0
flake8==6.1.0
EOF

# tests/test_app.py
mkdir tests
cat > tests/test_app.py << 'EOF'
from app import health_check, start_server

def test_health_check():
    result = health_check()
    assert result["status"] == "ok"

def test_start_server():
    result = start_server()
    assert result is True
EOF

# make tests importable
touch tests/__init__.py
```

## Steps

1. Create the CI workflow:

```bash
vi .github/workflows/ci.yml
```

Paste this (adjust Python version if needed):

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Lint
        run: flake8 . --max-line-length=100 --exclude=.git,__pycache__,tests

      - name: Run tests
        run: pytest tests/ -v
```

2. Commit and push everything:

```bash
git add .github/workflows/ci.yml requirements.txt tests/
git commit -m "ci: add CI pipeline with lint and test"
git push origin main
```

3. Go to GitHub Actions tab. Watch the pipeline run.

4. Introduce a failing test to see CI fail:

```bash
echo "def test_fail(): assert False" >> tests/test_app.py
git add tests/test_app.py
git commit -m "test: add intentionally failing test"
git push origin main
```

Does the CI turn red?

5. Fix it:

```bash
vi tests/test_app.py    # remove the failing test
git add tests/test_app.py
git commit -m "test: remove intentionally failing test"
git push origin main
```

---

## What do you see? What does it mean?

- How long does the pipeline take with a cold vs warm pip cache?
- What does the lint step catch that tests don't?
- After CI goes red, what's the impact on PR mergeability (if branch protection is set)?
