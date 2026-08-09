# Solution

## After starting bisect

```
git bisect start
git bisect bad HEAD
git bisect good <first-commit-hash>
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[c8f2g4b] Add gamma feature
```

Git checks out the middle commit. With 6 commits between good and bad, expect about 3 steps.

## Step-by-step

```
# Checked out: Add gamma feature
grep "BUG_INTRODUCED" notes.txt    → found!
git bisect bad
Bisecting: 0 revisions left to test after this (roughly 1 step)
[b7e1f3a] Add beta feature

# Checked out: Add beta feature
grep "BUG_INTRODUCED" notes.txt    → not found
git bisect good
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[a3f9d12] Refactor config

# Checked out: Refactor config
grep "BUG_INTRODUCED" notes.txt    → found!
git bisect bad
```

## Git announces the culprit

```
a3f9d12 is the first bad commit
commit a3f9d12abc...
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 17:00:00 2026

    Refactor config

:100644 100644 ...  notes.txt
```

Found in 3 steps instead of checking all 6 manually. With 200 commits, binary search takes at most 8 steps (log2(200) ≈ 7.6).

## After `git bisect reset`

```
Previous HEAD position was a3f9d12 Refactor config
Switched to branch 'main'
```

HEAD is back on `main`, pointing to the latest commit. The bisect session is fully cleaned up.

## The automated version

Using `git bisect run`:
```bash
git bisect start
git bisect bad HEAD
git bisect good <hash>
git bisect run bash -c 'grep -q "BUG_INTRODUCED" notes.txt && exit 1 || exit 0'
```

Output ends with the same culprit announcement, fully automated.
