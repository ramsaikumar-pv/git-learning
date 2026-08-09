# Solution

## Before rebase: `git log --oneline --graph --all`
```
* c9g3h5d (HEAD -> feature/add-cache) Add cache stub
| * f1e7c09 (main) Update config with team notes
|/
* b7e1f3a Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

The branches have diverged. `feature/add-cache` is at `c9g3h5d`, `main` is at `f1e7c09`. They share the ancestor `b7e1f3a`.

## `git rebase main` output
```
Successfully rebased and updated refs/heads/feature/add-cache.
```

## After rebase: `git log --oneline --graph --all`
```
* d0h4i6e (HEAD -> feature/add-cache) Add cache stub
* f1e7c09 (main) Update config with team notes
* b7e1f3a Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

Perfectly linear. The commit `c9g3h5d` is gone — replaced by `d0h4i6e` (same changes, new hash, new parent). The feature branch is now "on top of" main.

## After `git merge feature/add-cache`
```
Updating f1e7c09..d0h4i6e
Fast-forward
 app.py | 1 +
```

A **fast-forward merge**. Because the feature branch is directly ahead of `main` (rebase made it linear), Git can just move the `main` pointer forward. No merge commit needed. This is the clean history that rebase enables.

## The commit hash changed

Before rebase: `c9g3h5d`
After rebase: `d0h4i6e`

Same changes, different hash — because the parent changed. The parent is now `f1e7c09` (main's latest) instead of `b7e1f3a`. Git computes the hash from the full commit content including parent, so a different parent → different hash. This is the key thing to understand about rebase: it rewrites commits.
