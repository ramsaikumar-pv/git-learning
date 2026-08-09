# Interactive Rebase

Interactive rebase (`git rebase -i`) lets you rewrite your commit history before sharing it. You can squash messy "WIP" commits, fix typos in messages, reorder commits, or split a commit into two.

It's a power tool. Use it on local branches before pushing.

---

## Open the interactive rebase editor

```bash
git rebase -i HEAD~4    # rewrite the last 4 commits
git rebase -i main      # rewrite all commits since branching from main
```

Git opens your editor with a list like:

```
pick a3f9d12 Add server startup
pick b7e1f3a Fix typo in config
pick c8f2g4b WIP: half-done feature
pick d9h3i5c Actually finish the feature

# Rebase e5j4k6l..d9h3i5c onto e5j4k6l (4 commands)
#
# Commands:
# p, pick   = use commit
# r, reword = use commit, but edit the commit message
# e, edit   = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup  = like "squash", but discard this commit's log message
# d, drop   = remove commit
```

Each line is a commit (oldest at top, newest at bottom). Change the keyword to change the action.

---

## Squash: collapse commits

Change `pick` to `squash` (or `s`) to fold a commit into the one above it:

```
pick a3f9d12 Add server startup
squash b7e1f3a Fix typo in config
pick c8f2g4b WIP: half-done feature
squash d9h3i5c Actually finish the feature
```

Git opens another editor asking you to write the combined commit message for each squash.

---

## Fixup: squash and discard message

Like squash but silently discards the folded commit's message:

```
pick a3f9d12 Add server startup
fixup b7e1f3a Fix typo in config    # discards this message
```

Use `fixup` (or `f`) for "fixup commits" — minor corrections that don't deserve their own message.

---

## Reword: edit a commit message

```
reword a3f9d12 Add server startup   # Git will ask for a new message
pick b7e1f3a Fix typo
```

---

## Drop: delete a commit entirely

```
pick a3f9d12 Add server startup
drop b7e1f3a WIP debug prints      # this commit is removed
pick c8f2g4b Add health check
```

The commit is removed from history. If later commits depend on it, you may get conflicts.

---

## Reorder commits

Just change the order of lines:

```
pick c8f2g4b Add health check      # was third, now first
pick a3f9d12 Add server startup    # was first, now second
```

Git replays them in the new order.

---

## After interactive rebase

All modified commits get new hashes. If you've pushed this branch, you'll need to force push:

```bash
git push --force-with-lease origin feature/my-branch
```

Never do this on `main` or shared branches.
