# Task: Stage Files and Make Commits

## Setup

Navigate into this module's directory (or use your practice repo from module 02):

```bash
cd git-learning/01-foundations/03-staging-and-commits
```

The files `app.py` and `config.yaml` are already here for you to work with.

## Steps

1. Check what Git sees right now:

```bash
git status
```

2. Stage just `app.py`:

```bash
git add app.py
```

3. Check status again — notice what changed:

```bash
git status
```

4. Now stage `config.yaml` too:

```bash
git add config.yaml
```

5. Make your first commit:

```bash
git commit -m "Add app entrypoint and initial config"
```

6. Check the log:

```bash
git log --oneline
```

7. Now edit `app.py` — add a comment at the top: `# version 2`. Save it.

8. Check status again:

```bash
git status
```

9. Stage ONLY `app.py` (not `config.yaml`):

```bash
git add app.py
```

10. Try unstaging it, then re-staging it:

```bash
git restore --staged app.py
git status
git add app.py
git commit -m "Add version comment to app"
```

11. View the full log:

```bash
git log --oneline
```

---

## What do you see? What does it mean?

- After step 3, what did `git status` show that step 1 didn't?
- After step 8, why does `git status` show `app.py` as modified even after you committed it in step 5?
- What are the two commit hashes in your log? How are they different?
