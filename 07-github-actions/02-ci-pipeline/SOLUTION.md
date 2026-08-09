# Solution

## Successful CI run output

```
Run pytest tests/ -v
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-7.4.0
collected 2 items

tests/test_app.py::test_health_check PASSED                             [ 50%]
tests/test_app.py::test_start_server PASSED                             [100%]

============================== 2 passed in 0.03s ==============================
```

Both tests pass. The job exits 0. GitHub marks the workflow run as ✅.

## CI run with failing test

```
tests/test_app.py::test_fail FAILED                                     [100%]

====================================== FAILURES =====================================
__________________________ test_fail ___________________________
    def test_fail():
>       assert False
E       assert False
=============================================================================
FAILED tests/test_app.py::test_fail - assert False
========================= 1 failed, 2 passed in 0.04s ============================
```

Pytest exits with code 1. The step fails. GitHub marks the job ❌.

## Timing: cold vs warm cache

Cold (first run, no cache): pip install takes ~45 seconds
Warm (cache hit): pip install takes ~5 seconds

On a busy PR repo with many pushes per day, this 40-second saving per run adds up significantly.

## What lint catches that tests don't

- Unused imports (`import os` but `os` is never used)
- Undefined names (variables used before assignment — sometimes)
- Code style violations (line length, spacing)
- Potential logic errors (comparison to None using `==` instead of `is`)

Tests verify behaviour. Lint verifies code quality and style. Both are necessary.

## Impact on PR mergeability

With branch protection set to "Require status checks: CI" — a PR with red CI cannot be merged. GitHub shows a red ❌ on the PR page and the "Merge" button is greyed out. This is the enforcement mechanism that makes CI mandatory.
