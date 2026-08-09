# Task: Create and Switch Between Branches

## Setup

Make sure you have at least one commit in your repo (from module 03). Check:

```bash
git log --oneline
```

## Steps

1. See which branch you're on:

```bash
git branch
```

2. Create a new branch called `feature/add-logging` and switch to it:

```bash
git switch -c feature/add-logging
```

3. Confirm the switch:

```bash
git branch
```

4. Create a new file on this branch:

```bash
echo "import logging" > logging_config.py
git add logging_config.py
git commit -m "Add logging configuration"
```

5. Check the log — notice where HEAD is:

```bash
git log --oneline --graph --all
```

6. Switch back to `main`:

```bash
git switch main
```

7. List the files in your directory:

```bash
ls
```

Is `logging_config.py` there?

8. Switch back to your feature branch:

```bash
git switch feature/add-logging
ls
```

Is `logging_config.py` back?

9. Create a second branch from `main` (not from the feature branch):

```bash
git switch main
git switch -c feature/update-config
```

10. Run `git log --oneline --graph --all`:

```bash
git log --oneline --graph --all
```

---

## What do you see? What does it mean?

- Where did `logging_config.py` go when you switched to `main`?
- What does `--all` show in `git log` that `git log` without it doesn't?
- What's the parent commit of `feature/update-config`?
