# Task: Find the Bug with git bisect

## Setup: Plant a bug in history

You'll create a series of commits, one of which "introduces a bug" (a specific line in a file), then use bisect to find exactly which commit it was.

1. Make sure you're on `main` with a clean working directory.

2. Create 6 commits, one of which plants the bug:

```bash
echo "feature: alpha" >> notes.txt && git add notes.txt && git commit -m "Add alpha feature"
echo "feature: beta" >> notes.txt && git add notes.txt && git commit -m "Add beta feature"
echo "BUG_INTRODUCED=true" >> notes.txt && git add notes.txt && git commit -m "Refactor config"
echo "feature: gamma" >> notes.txt && git add notes.txt && git commit -m "Add gamma feature"
echo "feature: delta" >> notes.txt && git add notes.txt && git commit -m "Add delta feature"
echo "feature: epsilon" >> notes.txt && git add notes.txt && git commit -m "Add epsilon feature"
```

The "bug" is the line `BUG_INTRODUCED=true` added in the "Refactor config" commit.

3. Check the log — note the hash of a "known good" commit (before the bug):

```bash
git log --oneline
```

Note: the first commit in the log (bottom) is your good baseline.

## Steps

4. Start bisect, marking HEAD (current) as bad and the first commit as good:

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-commit-hash>
```

5. At each step, test whether the bug is present:

```bash
grep "BUG_INTRODUCED" notes.txt
```

If the line is there: `git bisect bad`
If it's not there: `git bisect good`

6. Repeat until Git announces the first bad commit.

7. Reset:

```bash
git bisect reset
git log --oneline
```

Are you back on HEAD?

---

## What do you see? What does it mean?

- How many steps did bisect take to find the bug?
- What information does Git print when it finds the first bad commit?
- After `git bisect reset`, where is HEAD?
