# Solution

## Part 1: After `git revert HEAD`

```
git log --oneline -5:
  c5d2e3f Revert "Introduce bug accidentally"
  a3f9d12 Introduce bug accidentally
  b7e1f3a Previous commit
```

Two new facts:
1. The bug commit is STILL in history — revert never removes commits.
2. A new commit exists that undoes the changes.

`tail -5 app.py` — the "THIS IS A BUG" line is gone. The revert commit added the inverse diff (a deletion of that line).

## Part 2: After `git reset --soft HEAD~1`

```
git status:
On branch main
Changes to be committed:
  modified:   config.yaml

git log --oneline -3:
  a3f9d12 Change A
  ...
```

"Change B" is gone from the log but the changes are in the staging area. `git status` shows `config.yaml` as staged. You can now edit the commit message or add/remove things before committing again.

## Part 3: After `git reset --hard HEAD~1`

```
git log --oneline -3:
  a3f9d12 Change A
  ...

cat app.py:
  (no "DELETE EVERYTHING" line)
```

The commit is gone and the working directory change is gone. Truly reset.

## Can you recover from `--hard`?

Yes, with reflog:

```bash
git reflog
# shows:
a3f9d12 HEAD@{0}: reset: moving to HEAD~1
terrible123 HEAD@{1}: commit: This commit is terrible

git reset --hard terrible123   # go back to where you were
```

Reflog is Git's black box recorder — it tracks every HEAD movement. The "terrible" commit still exists in the object store until Git runs garbage collection. This is your safety net.

## Summary table

| Command | Commit gone? | Changes staged? | Changes in workdir? |
|---------|-------------|-----------------|---------------------|
| `revert` | No (new commit added) | No | No |
| `reset --soft` | Yes | Yes ✅ | Yes |
| `reset --mixed` | Yes | No | Yes ✅ |
| `reset --hard` | Yes | No | No ⚠️ |
