# reset vs revert

Two ways to undo. One is safe. One is dangerous. Choose wrong and you lose work or break your team's repo.

---

## git revert — the safe undo

`git revert` creates a NEW commit that undoes the changes from a previous commit. Your history stays intact. The mistake is still in history — plus a new commit saying "this was wrong, here's the fix."

```bash
git revert a3f9d12
```

Git opens your editor for a commit message (default: "Revert 'Add broken feature'"). Save and close. A new commit appears.

```
git log --oneline:
  c5d2e3f Revert "Add broken feature"
  a3f9d12 Add broken feature
  b7e1f3a Initial commit
```

**Use revert on shared branches (main, release).** You can't change shared history — that would break everyone else's repos. Revert adds a commit instead of removing one.

---

## git reset — the dangerous undo

`git reset` moves the branch pointer backwards. It actually changes where your branch points. Three modes:

### `--soft` — undo the commit, keep changes staged

```bash
git reset --soft HEAD~1
```

The commit is gone from log. Your changes are back in the staging area. Nothing lost.

### `--mixed` (default) — undo the commit, unstage changes

```bash
git reset HEAD~1
# same as:
git reset --mixed HEAD~1
```

The commit is gone. Your changes are in the working directory (unstaged). Nothing lost.

### `--hard` — undo the commit, discard changes ⚠️

```bash
git reset --hard HEAD~1
```

The commit is gone. Your changes are **gone**. No recovery without `git reflog`. This is the nuclear option.

---

## The decision tree

| Situation | Use |
|-----------|-----|
| Undo on a shared/public branch | `git revert` |
| Undo on a local-only branch | `git reset` (any mode) |
| Undo commit but keep changes staged | `git reset --soft` |
| Undo commit and unstage changes | `git reset --mixed` (default) |
| Undo commit and delete all changes | `git reset --hard` ⚠️ |

---

## HEAD~1 notation

`HEAD~1` means "one commit before HEAD." `HEAD~3` means "three commits before HEAD." You can also use a commit hash: `git reset --soft a3f9d12`.
