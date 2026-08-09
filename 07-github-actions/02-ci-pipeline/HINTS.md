# Hints

<details>
<summary>Hint 1 — flake8 is failing on my app.py — what's wrong?</summary>

Run flake8 locally first to see the errors:

```bash
pip install flake8
flake8 app.py --max-line-length=100
```

Common issues:
- `E302` — expected 2 blank lines between functions
- `E501` — line too long
- `W291` — trailing whitespace
- `F401` — imported but unused

Fix the issues in your code, or if they're in practice files, exclude them from linting:

```yaml
- name: Lint
  run: flake8 app.py --max-line-length=100   # lint only app.py, not all files
```

Or add a `setup.cfg` to configure flake8:

```ini
[flake8]
max-line-length = 100
exclude = tests/,__pycache__/,.git/
```

</details>

<details>
<summary>Hint 2 — pytest can't import app.py — ModuleNotFoundError</summary>

Python needs to find `app.py` when running tests. Ensure the test file uses a relative import or that `app.py` is in the same directory level:

```python
# tests/test_app.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import health_check
```

Or better: add a `conftest.py` at the repo root:

```python
# conftest.py (at repo root, empty or with fixtures)
```

pytest automatically adds the `conftest.py` directory to the path.

Or run pytest from the repo root with the `--rootdir` option:

```bash
python -m pytest tests/ -v
```

The `python -m pytest` form adds the current directory to `sys.path`.

</details>

<details>
<summary>Hint 3 — The cache step shows "cache miss" every time — why?</summary>

The cache key includes `${{ hashFiles('requirements.txt') }}`. If `requirements.txt` changes, the hash changes, and the cache misses. This is intentional — new dependencies require a fresh cache.

If you're getting misses with an unchanged `requirements.txt`, check:
1. Is `requirements.txt` committed to the repo? (`git status`)
2. Is the path to the file correct in the cache key?
3. Are you on the same OS/runner as when the cache was created? (`${{ runner.os }}` is part of the key)

A cache miss is not an error — it just means the pip install runs fresh. The next run with the same `requirements.txt` will be a cache hit.

</details>
