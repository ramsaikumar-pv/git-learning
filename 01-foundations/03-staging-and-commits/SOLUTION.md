# Solution

## After `git status` (before any staging)
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py
        config.yaml

nothing added to commit but untracked files present
```

`Untracked` means Git sees the files but isn't watching them yet. You haven't told Git to care about them.

## After `git add app.py`
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   app.py

Untracked files:
        config.yaml
```

`app.py` moved from "Untracked" to "Changes to be committed" — it's now in the staging area. `config.yaml` is still untracked.

## After first `git commit`
```
[main (root-commit) a3f9d12] Add app entrypoint and initial config
 2 files changed, 15 insertions(+)
 create mode 100644 app.py
 create mode 100644 config.yaml
```

## After editing `app.py` and running `git status`
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app.py
```

Git now knows `app.py` — it's tracked. The modification shows as "not staged" because you edited it *after* the last commit.

## Final `git log --oneline`
```
b7e1f3a Add version comment to app
a3f9d12 Add app entrypoint and initial config
```

Two commits, two hashes, two checkpoints in history. The most recent is at the top.

---

## Why staging exists

Most VCS tools commit everything you've changed. Git gives you a staging area so you can craft commits precisely — this file goes in, that file waits. On a platform team, this matters: you might have three files changed during debugging but only want to commit the actual fix, not your debug print statements.
