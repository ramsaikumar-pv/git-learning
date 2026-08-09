# Solution

## Before stash: `git status`
```
On branch main
Changes not staged for commit:
  modified:   app.py
```

## After `git stash push -m "WIP: new feature function"`: `git status`
```
On branch main
nothing to commit, working tree clean
```

The changes are gone from the working directory — saved in the stash stack.

## `git stash list`
```
stash@{0}: On main: WIP: new feature function
```

## After `git stash pop`: `git status`
```
On branch main
Changes not staged for commit:
  modified:   app.py
```

Your work is back exactly as it was. The stash entry is consumed (removed from the list).

## With two stashes: `git stash list`
```
stash@{0}: On main: config tweak
stash@{1}: On main: WIP: new feature function
```

`stash@{0}` is always the MOST RECENT (last in, first out — like a stack). The feature work is `stash@{1}` because it was saved earlier.

## After `git stash apply stash@{1}`: `git stash list`
```
stash@{0}: On main: config tweak
stash@{1}: On main: WIP: new feature function
```

The stash is still there. `apply` restores without consuming. You need `git stash drop stash@{1}` to remove it.

## pop vs apply

`git stash pop` = apply + drop (one step)
`git stash apply` = restore only (stash stays)

Use `apply` when you're unsure and want to keep the stash as a backup while you verify everything looks right.
