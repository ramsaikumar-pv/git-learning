# Task: Use git diff to Inspect Changes

## Setup

Make sure you have at least 2 commits in your practice repo and the files `app.py` and `config.yaml` exist.

## Steps

1. Edit `app.py` — add a comment at the top and change the port number. Don't stage yet:

```bash
vi app.py
```

2. See unstaged changes:

```bash
git diff
```

Read the output carefully. Which lines changed? What do `+` and `-` mean?

3. Stage only `app.py`:

```bash
git add app.py
```

4. Now run both:

```bash
git diff           # unstaged
git diff --staged  # staged
```

What does each show now?

5. Also edit `config.yaml` (don't stage it):

```bash
vi config.yaml
```

6. Run:

```bash
git diff           # shows only config.yaml now (app.py is staged)
git diff --staged  # shows only app.py (config.yaml is not staged)
```

7. Commit what's staged:

```bash
git commit -m "Update server message and port"
```

8. Now compare the last two commits:

```bash
git diff HEAD~1 HEAD
git diff HEAD~1 HEAD --stat
```

9. Compare the two commits for a specific file only:

```bash
git diff HEAD~1 HEAD -- app.py
```

---

## What do you see? What does it mean?

- What is the difference between `git diff` and `git diff --staged`?
- After staging `app.py` but before staging `config.yaml`, why does `git diff` show only one file?
- What does `@@` at the start of a diff hunk tell you?
