# Challenge

## Challenge 1: Bisect with a real test

Write a Python script (`tests/test_notes.py`) that passes when the bug isn't present and fails when it is:

```python
# tests/test_notes.py
with open("notes.txt") as f:
    content = f.read()
assert "BUG_INTRODUCED" not in content, "Bug found in notes.txt"
print("Test passed")
```

Run a full automated bisect:

```bash
git bisect start
git bisect bad HEAD
git bisect good <hash>
git bisect run python tests/test_notes.py
```

Watch Git find the bug without any manual interaction.

---

## Challenge 2: Skip bad commits

Simulate a compile error: mark one commit as unskippable. During bisect, run:

```bash
git bisect skip
```

Git will note it can't be sure which adjacent commit is the first bad one. Research the output message — does bisect still find the culprit, or does it need more information?

---

## Challenge 3: Bisect a performance regression

Bisect isn't just for bugs. Time-based bisecting:

1. Create 8 commits, one of which makes a function "slow" (replace `pass` with a `time.sleep(0.5)`)
2. Write a test script that times the function and exits 1 if it takes > 0.1s
3. Use `git bisect run` to find the slow commit automatically

---

## Bonus: Bisect by date

```bash
git bisect start
git bisect bad HEAD
git bisect good --before="2 weeks ago"   # all commits more than 2 weeks old are "good"
```

This bisects by date rather than requiring you to know a specific "known good" hash. Useful when you know "this worked last week" but don't know which commit.
