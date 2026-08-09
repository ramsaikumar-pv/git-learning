# Challenge

## Challenge 1: Custom log format

Git supports format strings. Try these:

```bash
git log --pretty=format:"%h %an %ar %s"
```

- `%h` — short hash
- `%an` — author name
- `%ar` — relative date ("3 days ago")
- `%s` — subject (first line of message)

Design your own format. What information do you find most useful at a glance?

---

## Challenge 2: Find when a specific line was introduced

Use `git log -S` (the "pickaxe") to find the commit that first introduced a specific string:

```bash
git log -S "health_check" --oneline
```

This searches the diff content across all commits for when `health_check` was added or removed. Useful for tracking down when a feature was introduced or a bug was added.

Try it with a string you know is in `app.py`.

---

## Challenge 3: Blame a file

```bash
git blame app.py
```

`git blame` shows every line of a file alongside the commit that last changed it. Each line tells you: who wrote it, when, and in which commit. This is the forensics tool for "who broke line 42?"

Now try: `git blame -L 1,3 app.py` — only annotate lines 1 to 3.

---

## Bonus: Log across all branches

Create a second branch, make a commit on it, then switch back to `main` and run:

```bash
git log --oneline --graph --all
```

See how the graph forks? The `--all` flag shows commits on every branch, not just the one you're on. Without `--all`, you only see commits reachable from HEAD.
