# Conflict Resolution

Git pauses and says: "You decide." That's a merge conflict.

A conflict happens when two branches change the same lines of the same file in different ways. Git can't guess which version you want, so it stops and asks you to choose.

You've already done this hands-on. This module codifies what you learned.

---

## What triggers a conflict?

```
Branch main:    line 5 says: port = 8080
Branch feature: line 5 says: port = 9090
```

Both changed the same line differently. Git has no algorithm to resolve this — only a human knows which is correct.

---

## What Git inserts when there's a conflict

```python
<<<<<<< HEAD
port = 8080
=======
port = 9090
>>>>>>> feature/update-port
```

- `<<<<<<< HEAD` — what your current branch (the one you're merging INTO) has
- `=======` — the dividing line
- `>>>>>>> feature/update-port` — what the incoming branch has

Everything between the markers is up to you. You delete the markers and leave only what you want.

---

## Resolving the conflict

1. Open the file in `vi`
2. Find the conflict markers (search with `/<<<`)
3. Decide what the file should contain
4. Delete all three marker lines and the version you're not keeping
5. Save the file

Then:

```bash
git add app.py        # mark as resolved
git commit            # seal the merge
```

If you're mid-rebase instead of mid-merge:
```bash
git add app.py
git rebase --continue
```

---

## Abort if you're stuck

Changed your mind? Don't want to resolve right now?

```bash
git merge --abort    # during a merge
git rebase --abort   # during a rebase
```

This takes you back to the state before you started. Nothing is lost.

---

## Check for remaining conflicts

After resolving, always run:

```bash
git status
git diff
```

`git status` shows you which files still have conflicts. If there are none, proceed with `git add` and `git commit`.

---

## Visualise the merge after resolution

```bash
git log --oneline --graph --all
```

You should see the merge commit with two parent lines joining into one. That's the resolved conflict, committed.
