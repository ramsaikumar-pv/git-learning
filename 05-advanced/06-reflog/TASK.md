# Task: Use reflog to Recover Lost Commits

## Part 1: Lose some commits intentionally

1. Make three commits you'll "lose":

```bash
echo "important work A" >> notes.txt && git add notes.txt && git commit -m "Important work A"
echo "important work B" >> notes.txt && git add notes.txt && git commit -m "Important work B"
echo "important work C" >> notes.txt && git add notes.txt && git commit -m "Important work C"
```

2. Check the log — note the hash of the first "important work" commit:

```bash
git log --oneline -5
```

3. Reset hard to 3 commits ago:

```bash
git reset --hard HEAD~3
```

4. Check the log — are the commits gone?

```bash
git log --oneline -5
```

---

## Part 2: Find and recover with reflog

5. Look at the reflog:

```bash
git reflog
```

Can you see the three commits you just "lost"?

6. Find the hash of "Important work C" in the reflog.

7. Recover by creating a branch there:

```bash
git switch -c recovery/lost-work <hash-of-important-work-C>
git log --oneline -5
```

Are your three commits back?

8. Now merge them back to main:

```bash
git switch main
git merge recovery/lost-work
git log --oneline -5
```

---

## Part 3: Recover a deleted branch

9. Create a branch, make a commit, delete the branch:

```bash
git switch -c temp-branch
echo "temp work" >> notes.txt
git add notes.txt && git commit -m "Temp branch commit"
git switch main
git branch -D temp-branch
```

10. Recover it using reflog:

```bash
git reflog | grep temp-branch
git switch -c temp-branch <hash>
```

---

## What do you see? What does it mean?

- After `git reset --hard HEAD~3`, did `git log` show the commits?
- Did `git reflog` still show them?
- What would have happened if you'd waited 30+ days to recover?
