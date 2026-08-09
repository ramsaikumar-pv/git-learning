# Challenge

## Challenge 1: Partial staging with git add -p

You've edited multiple parts of a single file but only want to commit one of those changes.

1. Open `app.py` and make two separate changes: add a comment at the top, and change a value lower in the file.
2. Instead of `git add app.py`, run:

```bash
git add -p app.py
```

Git will show you each "hunk" (block of changes) and ask: `Stage this hunk [y,n,q,a,d,s,?]?`

- Press `y` to stage a hunk
- Press `n` to skip it
- Press `?` to see all options

Stage only the top comment, skip the other change. Then `git status` — what do you see? Can a file be both staged and not staged at the same time?

---

## Challenge 2: Amend the last commit

You committed but forgot to include a file. Fix it without creating a new commit:

```bash
git add forgotten.txt
git commit --amend --no-edit
```

Run `git log --oneline` before and after. Did the hash change? Why?

---

## Challenge 3: Write a multi-line commit message

```bash
git commit
```

(Without `-m` — this opens your editor.)

Write a subject line, leave a blank line, then write a body paragraph explaining the change. Check it with:

```bash
git log
git log --oneline
```

What shows in `--oneline`? What shows in the full `log`? Why does the blank line matter?

---

## Bonus: What's the difference between `git add .` and `git add -A`?

Research it and write a one-sentence answer in `notes.txt`. Hint: it's about deleted files.
