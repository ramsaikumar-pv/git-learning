# Task: Rebase a Branch onto Main

## Setup

You'll create a situation where your feature branch is behind `main`, then rebase to catch up.

## Steps

1. Start on `main` with at least one commit. Create a feature branch:

```bash
git switch -c feature/add-cache
```

2. Make a commit on the feature branch:

```bash
echo 'def cache_get(key): return None' >> app.py
git add app.py
git commit -m "Add cache stub"
```

3. Go back to `main` and make a commit there (simulating a teammate's work):

```bash
git switch main
echo "# Updated by teammate" >> config.yaml
git add config.yaml
git commit -m "Update config with team notes"
```

4. Check the current graph — branches have diverged:

```bash
git log --oneline --graph --all
```

5. Switch to your feature branch and rebase onto `main`:

```bash
git switch feature/add-cache
git rebase main
```

6. Check the graph again:

```bash
git log --oneline --graph --all
```

What changed? Is the history linear now?

7. Now merge the feature branch into `main`:

```bash
git switch main
git merge feature/add-cache
```

What kind of merge is this? Why?

---

## What do you see? What does it mean?

- Before rebase: what did the graph look like?
- After rebase: how did the graph change?
- After merging: what kind of merge happened and why?
- Did the commit hash of your feature branch commit change after rebase?
