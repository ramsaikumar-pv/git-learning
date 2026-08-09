# git stash 🌱

## 📖 In plain words

Imagine you're halfway through editing a file, it's not ready to commit yet, but suddenly you need a clean, empty working directory — maybe to switch branches, or handle an urgent fix. You don't want to commit unfinished work, but you also don't want to lose it.

`git stash` is Git's answer: it temporarily puts your uncommitted changes aside (like putting them in a drawer), giving you back a clean working directory. When you're ready, you pull them back out exactly as they were.

Here's the scenario that makes it click: you're in the middle of a half-done config change when your pager goes off — production is down, you need to switch to a hotfix branch right now. You can't commit half-done work. That's exactly what `git stash` is for.

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

Your working directory is now clean — `git status` shows nothing changed, as if you never touched anything. Your edits aren't gone, though; they're safely tucked away. Now you're free to switch branches, pull, or do whatever the urgent thing was.

---

## Get your changes back

```bash
git stash pop
```

This brings your edits back out of the drawer and removes them from the stash list — as if you'd never stashed them at all.

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

Think of this as a stack of drawers. Stashes are numbered `{0}`, `{1}`, and so on, with `{0}` always being the one you stashed most recently.

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

A gotcha worth knowing: by default, stash only saves files Git already knows about (tracked files). Brand-new files you just created (untracked) get left behind:

```bash
git stash -u        # -u = include untracked files too
git stash --all     # include untracked AND ignored files
```

---

## ✅ Quick recap

- `git stash` — shelve uncommitted changes, get a clean working directory.
- `git stash pop` — bring the most recent stash back and remove it from the list.
- `git stash list` — see everything you've stashed.
- `git stash -u` — also stash new (untracked) files, not just edits to existing ones.
