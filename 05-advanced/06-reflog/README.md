# git reflog 🌱

## 📖 In plain words

This is the safety net you didn't know you had. `git reflog` quietly records every single move `HEAD` has ever made on your machine — every commit, reset, checkout, rebase, merge. Think of it as Git's flight recorder, logging everything in the background whether you asked it to or not.

Here's why that matters: even after something scary like `git reset --hard` seems to delete your work, the actual commits usually still exist behind the scenes (until Git's garbage collector eventually cleans them up, typically after 90 days). Reflog is how you find and recover them.

---

## See the reflog

```bash
git reflog
```

```
b7e1f3a HEAD@{0}: commit: Add health check
a3f9d12 HEAD@{1}: reset: moving to HEAD~1
c8f2g4b HEAD@{2}: commit: Terrible commit I reset away
d9h3i5c HEAD@{3}: merge feature/login: Merge made by recursive
e5j4k6l HEAD@{4}: checkout: moving from feature/login to main
```

Each line: `<hash> HEAD@{N}: <action>: <description>`

`HEAD@{0}` = current. `HEAD@{1}` = one move ago. `HEAD@{10}` = ten moves ago.

---

## Recover a deleted commit

You ran `git reset --hard HEAD~2`. Two commits gone. Reflog to the rescue:

```bash
git reflog
# find the commit you want: say it was c8f2g4b HEAD@{2}

git reset --hard c8f2g4b   # restore to that point
# or
git cherry-pick c8f2g4b    # apply just that commit on current branch
# or
git switch -c recovery-branch c8f2g4b  # create a branch there
```

---

## Recover a deleted branch

You ran `git branch -D feature/important` by mistake. The commits are still in the object database:

```bash
git reflog
# find the last commit that was on feature/important
# e.g., e5j4k6l HEAD@{5}: checkout: moving from feature/important to main

git switch -c feature/important e5j4k6l
```

Branch recovered.

---

## Reflog for a specific branch

```bash
git reflog show main       # only shows moves on the main branch
git reflog show HEAD       # default (HEAD movements)
```

---

## Expiry

Reflog entries expire. Defaults:
- Reachable entries: 90 days
- Unreachable entries: 30 days

After expiry, `git gc` removes them permanently. This is why you can't recover commits deleted months ago.

---

## Reflog vs git log

| `git log` | `git reflog` |
|-----------|-------------|
| Shows commit graph (reachable commits) | Shows every HEAD movement |
| Doesn't show reset-away commits | Shows "lost" commits |
| Permanent | Expires |
| Shared (pushed to remote) | Local only |

---

## ✅ Quick recap

- `git reflog` — a local log of every place `HEAD` has pointed, even after resets or deletions.
- Recover "lost" work: find the commit hash in reflog, then `reset --hard`, `cherry-pick`, or branch from it.
- Reflog entries eventually expire (~90 days) — it's a safety net, not permanent history.
- Local only — reflog never gets pushed or shared with anyone else.
