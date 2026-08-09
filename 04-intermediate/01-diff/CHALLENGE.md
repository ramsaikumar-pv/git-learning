# Challenge

## Challenge 1: Diff between branches

Create two branches that have diverged:

1. On `main`: edit line 1 of `app.py`.
2. On `feature/x`: edit line 3 of `app.py`.
3. Diff the branches:

```bash
git diff main feature/x
git diff main feature/x -- app.py
git diff main feature/x --stat
```

Which branch's changes show as `+` and which as `-`? What determines the direction of the diff?

---

## Challenge 2: Diff specific lines with context

By default, `git diff` shows 3 lines of context around each change. Change this:

```bash
git diff -U10 HEAD~1 HEAD        # 10 lines of context
git diff -U0 HEAD~1 HEAD         # no context at all
```

Why would you ever want `-U0`? (Think: large files where you just want to see exactly what changed, nothing else.)

---

## Challenge 3: Create a patch file

```bash
git diff HEAD~1 HEAD > my-changes.patch
cat my-changes.patch
```

This is the raw diff format that can be emailed or applied elsewhere:

```bash
git apply my-changes.patch
```

Research: how was this used before GitHub existed? (Think: `git format-patch` and emailing patches to mailing lists — this is still how the Linux kernel receives contributions.)

---

## Bonus: diff a binary file

Add a binary file (like a PNG) to your repo, commit it, change it, and run `git diff`. What happens? How does Git handle binary diffs? Research `git diff --binary` and `git lfs` for large binary files.
