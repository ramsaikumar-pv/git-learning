# Task: Cherry-Pick a Specific Commit

## Scenario

You have a feature branch with three commits: a bug fix, a new feature, and some experimental work. Production needs only the bug fix. You'll cherry-pick just that commit to `main`.

## Setup

1. Start on `main`. Create a feature branch and make three commits:

```bash
git switch -c feature/mixed-work

# Commit 1: bug fix
echo "  timeout = 30  # bug fix: was 3" >> config.yaml
git add config.yaml
git commit -m "Fix connection timeout (was 3s, now 30s)"

# Commit 2: new feature
echo "def new_endpoint(): return 'v2'" >> app.py
git add app.py
git commit -m "Add v2 endpoint (experimental)"

# Commit 3: more experimental work
echo "# WIP: cache layer" >> app.py
git add app.py
git commit -m "WIP: cache layer sketch"
```

2. Check the log — note the hash of the bug fix commit (the first one):

```bash
git log --oneline
```

## Steps

3. Switch to `main`:

```bash
git switch main
```

4. Cherry-pick only the bug fix commit (use the hash from step 2):

```bash
git cherry-pick <bug-fix-hash>
```

5. Check the log:

```bash
git log --oneline
git log --oneline --graph --all
```

Is the bug fix on `main` now? Is the feature branch's other work there too?

6. Inspect the cherry-picked commit:

```bash
git show HEAD
```

Is the hash the same as the original? (It shouldn't be.)

7. Check `config.yaml` on main — is the timeout fix there?

```bash
grep timeout config.yaml
```

---

## What do you see? What does it mean?

- What hash does the cherry-picked commit get — same as the original or different?
- In `git log --graph --all`, where do the two branches stand relative to each other?
- Is the feature branch still intact after cherry-picking from it?
