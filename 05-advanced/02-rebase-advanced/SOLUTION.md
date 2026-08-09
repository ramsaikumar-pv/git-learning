# Solution

## Before: `git log --oneline` (messy)
```
f9k5l7m Add logout
e8j4k6l fix tyoop
d7i3j5k Fix login
c6h2i4j WIP
b5g1h3i Add login func
a4f0g2h (main) Previous commit
```

5 messy commits. "WIP", "fix tyoop" — not something you want in a shared repo's history.

## Interactive rebase editor (what you type)
```
pick   b5g1h3i Add login func
squash c6h2i4j WIP
squash d7i3j5k Fix login
squash e8j4k6l fix tyoop
pick   f9k5l7m Add logout
```

The first `pick` stays — it becomes the base of the squashed commit. The three `squash` lines fold into it.

## Combined message editor (what you write)
```
Add login with input validation

# This is a combination of 4 commits.
# This is the 1st commit message:
Add login func
# This is the commit message #2:
WIP
...
```

Delete everything and type your clean message. Save.

## After: `git log --oneline`
```
n2p8q0r Add logout
m1o7p9q Add login with input validation
a4f0g2h (main) Previous commit
```

2 clean commits. The "WIP" noise is gone. The "logout" commit kept its message (it was `pick`, not `squash`).

Note: ALL commits after the rebase point have new hashes — including "Add logout" even though you didn't change it. Rebase replays commits in sequence; once the base changes, all downstream hashes change too.

## `cat app.py` — is the code intact?

Yes. Interactive rebase never loses code — it rewrites commit history, not file content. Squashing 4 commits means the combined changes of all 4 are now in 1 commit.
