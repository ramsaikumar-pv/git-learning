# Creating Branches

Branches are parallel worlds. Your `main` branch is production. You want to add a new feature without risking prod? Create a branch. Work there. Merge when you're confident.

In platform engineering terms: think of `main` as your prod cluster config and a feature branch as a staging environment — same baseline, isolated changes, merge when validated.

---

## Create and switch in one command

```bash
git switch -c feature/add-metrics
```

`-c` means "create". You're now on a new branch that starts from wherever `main` was.

Check where you are:

```bash
git branch
```

```
  main
* feature/add-metrics
```

The `*` shows your current branch.

---

## What actually happened?

A branch is just a pointer — a text file in `.git/refs/heads/` containing a commit hash. Creating a branch is almost instantaneous because Git doesn't copy files. It just creates a new label pointing to the same commit.

```
main          →  a3f9d12
feature/add-metrics  →  a3f9d12   (same commit, new label)
```

As you commit on the feature branch, it advances independently:

```
main                 →  a3f9d12
feature/add-metrics  →  b7e1f3a → c8f2g4b
```

---

## Switch between branches

```bash
git switch main                  # go back to main
git switch feature/add-metrics   # go back to feature
```

When you switch, your working directory changes to reflect that branch's state. Files that exist only on one branch appear and disappear.

---

## List all branches

```bash
git branch          # local branches
git branch -r       # remote branches
git branch -a       # all branches (local + remote)
```

---

## Delete a branch

Once merged, clean up:

```bash
git branch -d feature/add-metrics    # safe delete (blocks if unmerged)
git branch -D feature/add-metrics    # force delete (even if unmerged)
```

---

## Naming branches

No spaces. Use `/` as a namespace separator (many teams use `feature/`, `fix/`, `hotfix/`, `release/`). Keep names descriptive but short:

```
feature/add-prometheus-metrics
fix/null-pointer-login
hotfix/prod-db-connection
```
