# Task: Read Your Commit History

## Setup

Make sure you've completed module 03 and have at least two commits in your repo. If not, go back and do that first.

## Steps

1. See the full log:

```bash
git log
```

How many commits do you have? What's the full hash of the most recent one?

2. Switch to one-line format:

```bash
git log --oneline
```

3. Show the graph (even if you only have one branch, the structure is still visible):

```bash
git log --oneline --graph --all
```

4. Show only the last 3 commits:

```bash
git log --oneline -3
```

5. Inspect a specific commit — replace `<hash>` with the first 7 characters of any commit in your log:

```bash
git show <hash>
```

What information does `git show` give you that `git log` doesn't?

6. Find all commits that touched `app.py`:

```bash
git log --oneline -- app.py
```

7. Show the actual changes (diffs) in each commit for `app.py`:

```bash
git log -p -- app.py
```

8. Make one more commit: edit `config.yaml` (change the port from 8080 to 9090), stage and commit it. Then run `git log --oneline` again.

---

## What do you see? What does it mean?

- What's the difference between `git log` and `git show`?
- Why does the hash in `git log --oneline` only show 7 characters when the full hash is 40?
- What does `HEAD -> main` mean in the log output?
