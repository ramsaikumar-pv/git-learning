# Creating Branches 🌱

## 📖 In plain words

A branch is a separate copy of your project where you can make changes safely, without touching the "real" version until you're ready.

Ram's own analogy fits perfectly: branches are parallel worlds 🌍🌍. Your `main` branch is the "real" world — the stable version everyone relies on. When you want to try something new (a feature, a fix, an experiment), you create a branch: a parallel world that starts out identical to `main`, but where your changes don't affect anyone else. If it works out, you bring those changes back into `main`. If it doesn't, you just delete the branch — no harm done.

In platform engineering terms: think of `main` as your prod cluster config and a feature branch as a staging environment — same starting point, isolated changes, merge when validated.

---

## Create and switch in one command

```bash
git switch -c feature/add-metrics
```

`-c` means "create". This one command does two things at once: it creates a brand-new branch called `feature/add-metrics`, and immediately moves you onto it. It starts out as an exact copy of wherever `main` currently is.

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

Here's a beginner-friendly way to picture a branch: it's just a **name that points at a commit** — like a sticky note 🏷️ stuck on one specific snapshot. It's not a copy of all your files. That's exactly why creating a branch is instant — Git isn't duplicating anything, it's just writing a new sticky note that happens to point at the same place `main` does.

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

When you switch, the files on your computer actually change to match that branch's version — as if by magic. If a file only exists on the feature branch, it'll appear when you switch there and vanish when you switch back to `main`. This is normal and expected, not a bug!

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

---

## ✅ Quick recap

- A branch = a movable sticky note pointing at a commit. Creating one is instant.
- `git switch -c <name>` — create and move to a new branch.
- `git switch <name>` — move between existing branches.
- `git branch -d <name>` — delete a branch once it's merged.
