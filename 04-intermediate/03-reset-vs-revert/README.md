# reset vs revert 🌱

## 📖 In plain words

Both `git revert` and `git reset` are ways to "undo" a commit — but they undo in very different ways, and mixing them up can cause real trouble.

The simplest way to remember the difference: **revert adds a new commit that cancels out the old one** (nothing is deleted, history grows). **reset actually rewinds your branch**, as if the commit never happened (history shrinks, and depending on the mode, your work can disappear too). Read carefully here — this is one topic worth going slow on.

---

## git revert — the safe undo ✅

`git revert` doesn't erase anything. It looks at what a past commit changed, and creates a brand-new commit that applies the *opposite* change. Your history stays fully intact — the original mistake is still visible, sitting right next to the new commit that says "this was wrong, here's the fix."

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

**Rule of thumb: use revert on shared branches (`main`, release branches).** Since it only ever *adds* a commit and never erases one, it's always safe for history that other people also have a copy of.

---

## git reset — the dangerous undo ⚠️

Where revert adds a new commit, `git reset` actually rewinds your branch to an earlier point — like pretending the last commit never happened. This is more powerful, and more risky, because depending on the mode you choose, your actual file changes can be thrown away completely.

There are three modes, each keeping progressively less:

### `--soft` — undo the commit, keep changes staged (safest reset)

```bash
git reset --soft HEAD~1
```

The commit disappears from the log — but don't worry, your edits aren't gone. They land right back in the staging area, ready to be committed again (maybe with a better message this time).

### `--mixed` (the default, if you don't specify a mode) — undo the commit, unstage changes

```bash
git reset HEAD~1
# same as:
git reset --mixed HEAD~1
```

The commit disappears. Your edits are still there in your files, but no longer staged — you'd need to `git add` them again before committing.

### `--hard` — undo the commit, discard changes ⚠️⚠️

```bash
git reset --hard HEAD~1
```

This is the one to be careful with. The commit disappears **and** your file changes are deleted too — not just unstaged, actually gone from disk. There's no safety net for this except `git reflog` (an advanced-topic escape hatch, module 05-06). Before running `--hard`, always double-check you're not throwing away work you still need.

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

`HEAD` always means "where you are right now." So `HEAD~1` means "one commit before where I am now," and `HEAD~3` means "three commits back." You can also target a specific commit directly by its hash instead: `git reset --soft a3f9d12`.

---

## ✅ Quick recap

- `git revert <commit>` — safe undo, adds a new commit that cancels the old one. Use on shared branches.
- `git reset --soft` — undo commit, keep changes staged.
- `git reset --mixed` (default) — undo commit, keep changes but unstaged.
- `git reset --hard` — undo commit AND delete the changes. Use with real caution.
