# git stash

You're in the middle of a half-done config change when your pager goes off: production is down, you need to switch to a hotfix branch immediately. But you can't commit half-done work.

That's exactly what `git stash` is for. It shelves your uncommitted changes — both staged and unstaged — and gives you a clean working directory.

Infrastructure analogy: stash is like pushing your in-progress config change to the side of the desk mid-incident. You know it's there. You'll come back to it. But right now you need a clean surface.

---

## Stash your changes

```bash
git stash
```

Output:
```
Saved working directory and index state WIP on main: a3f9d12 Add app
```

Your working directory is now clean. `git status` shows nothing. You can switch branches, pull, do whatever you need.

---

## Get your changes back

```bash
git stash pop
```

This restores your changes and removes the stash entry. The working directory is back to how it was.

Or, to restore without removing the stash entry (keep it for later):

```bash
git stash apply
```

---

## See all stashes

```bash
git stash list
```

```
stash@{0}: WIP on main: a3f9d12 Add app
stash@{1}: WIP on feature/login: b7e1f Add auth
```

Stashes are numbered `{0}`, `{1}`, etc. `{0}` is always the most recent.

---

## Named stashes

Generic "WIP" messages get confusing fast. Name your stashes:

```bash
git stash push -m "half-done prometheus config"
```

```
Saved working directory and index state On main: half-done prometheus config
```

Now `git stash list` shows the descriptive name.

---

## Apply a specific stash

```bash
git stash apply stash@{1}   # apply the second-most-recent stash
git stash pop stash@{2}     # pop a specific stash
```

---

## Drop a stash

```bash
git stash drop stash@{0}    # delete one stash
git stash clear             # delete ALL stashes ⚠️
```

---

## Stash untracked files too

By default, stash only saves tracked files (files Git already knows about). New untracked files are left behind:

```bash
git stash -u        # -u = include untracked files
git stash --all     # include untracked AND ignored files
```
