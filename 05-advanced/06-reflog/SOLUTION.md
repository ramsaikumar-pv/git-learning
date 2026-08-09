# Solution

## After `git reset --hard HEAD~3`: `git log --oneline`
```
b4d0c2a (HEAD -> main) Previous commit (before the three)
```

The three "important work" commits are gone from `git log`. They're not reachable from HEAD.

## `git reflog`
```
b4d0c2a HEAD@{0}: reset: moving to HEAD~3
f9k5l7m HEAD@{1}: commit: Important work C
e8j4k6l HEAD@{2}: commit: Important work B
d7i3j5k HEAD@{3}: commit: Important work A
b4d0c2a HEAD@{4}: commit: Previous commit
```

The three commits are still there at `HEAD@{1}`, `{2}`, `{3}`. The reset removed them from the commit graph but NOT from the object store or reflog.

## `git switch -c recovery/lost-work f9k5l7m`
```
Switched to a new branch 'recovery/lost-work'
```

## `git log --oneline -5` on recovery branch
```
f9k5l7m (HEAD -> recovery/lost-work) Important work C
e8j4k6l Important work B
d7i3j5k Important work A
b4d0c2a main
```

All three commits are back. The branch pointer is at "Important work C", and the previous commits are its ancestors.

## After merging back to main
```
git log --oneline -5:
  c9h4m8n (HEAD -> main) Merge branch 'recovery/lost-work'
  f9k5l7m Important work C
  e8j4k6l Important work B
  d7i3j5k Important work A
  b4d0c2a Previous commit
```

Fully recovered. The commits are reachable from `main` again.

## What would have happened after 30+ days?

Git's garbage collection (`git gc`) removes unreachable objects after the reflog expiry period (30 days for unreachable commits). After that, the SHA-1 hashes are gone and recovery is not possible. This is the only real way to permanently lose Git commits — let them expire after they become unreachable and GC runs.

The practical takeaway: if you `reset --hard` something important, recover it within the same day. Don't wait.
