# Task: Undo Commits with reset and revert

## Part 1: git revert (safe undo)

1. Create a "mistake" commit:

```bash
echo "THIS IS A BUG" >> app.py
git add app.py
git commit -m "Introduce bug accidentally"
```

2. Check the log — see the bad commit:

```bash
git log --oneline -4
```

3. Revert it:

```bash
git revert HEAD
```

Git opens your editor — accept the default message or write your own. Save and close.

4. Check the log again:

```bash
git log --oneline -5
```

How many commits are there now? Is the bug commit still in history?

5. Check `app.py` — is the bug gone?

```bash
tail -5 app.py
```

---

## Part 2: git reset --soft

6. Make two quick commits:

```bash
echo "# change A" >> config.yaml && git add . && git commit -m "Change A"
echo "# change B" >> config.yaml && git add . && git commit -m "Change B"
git log --oneline -4
```

7. Undo the last commit but keep changes staged:

```bash
git reset --soft HEAD~1
git status
git log --oneline -3
```

What's in the staging area? Is "Change B" in the log?

---

## Part 3: git reset --hard (careful!)

8. Make a commit you definitely don't want:

```bash
echo "DELETE EVERYTHING" >> app.py
git add app.py
git commit -m "This commit is terrible"
```

9. Discard it completely:

```bash
git reset --hard HEAD~1
git log --oneline -3
cat app.py
```

Is "DELETE EVERYTHING" in `app.py` now?

---

## What do you see? What does it mean?

- After revert, how many total commits changed in the log?
- After `reset --soft`, where did "Change B" go?
- After `reset --hard`, can you get those changes back? (Run `git reflog` to investigate.)
