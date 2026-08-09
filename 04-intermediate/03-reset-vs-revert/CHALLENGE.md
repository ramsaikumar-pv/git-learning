# Challenge

## Challenge 1: Revert a non-HEAD commit

Revert isn't limited to the last commit. Find a commit from 3 commits ago and revert it:

```bash
git log --oneline -6
git revert <hash-of-old-commit>
```

Git may encounter a conflict if later commits also changed the same file. Resolve it, then commit.

Why is reverting an old (non-HEAD) commit harder than reverting the latest one?

---

## Challenge 2: Reset to a specific commit hash

Instead of `HEAD~N`, reset to an exact hash:

```bash
git log --oneline
# note a hash from 3 commits ago
git reset --soft <that-hash>
git log --oneline
git status
```

How many commits disappeared? Where did all their changes go? Can you make a single new commit containing all of them?

---

## Challenge 3: Revert a merge commit

Reverting a merge commit requires specifying which parent to revert to:

```bash
git revert -m 1 <merge-commit-hash>
```

`-m 1` means "revert to the first parent" (usually main). Research: why is `-m` required? What does `-m 2` do?

Create a merge commit in your repo, then revert it with `-m 1`. Check the log before and after.

---

## Bonus: `git restore` vs `git reset`

`git restore` was added in Git 2.23 alongside `git switch` to split `git checkout`'s duties:

```bash
git restore app.py             # discard working directory changes (was: git checkout -- app.py)
git restore --staged app.py    # unstage (was: git reset HEAD app.py)
```

`git reset` is still needed for undoing commits. `git restore` handles working directory and staging. Practice both and understand when each applies.
