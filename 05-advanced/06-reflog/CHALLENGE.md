# Challenge

## Challenge 1: Recover from a bad rebase

1. Make 3 commits on a feature branch.
2. Rebase them onto main (which has diverged).
3. The rebase went wrong (or you changed your mind).
4. Use `git reflog` to find the pre-rebase state and restore it:

```bash
git reflog | grep "rebase"
git reset --hard HEAD@{N}   # where N is the entry before the rebase started
```

---

## Challenge 2: Track down what you did yesterday

```bash
git reflog --since="yesterday"
git reflog --since="2 hours ago"
```

What operations did you perform? Can you reconstruct your last session from the reflog alone?

---

## Challenge 3: Expire and clean up

Research `git gc` and reflog expiry:

```bash
git gc --prune=now    # removes unreachable objects immediately (DANGEROUS in normal use)
git reflog expire --expire=now --all  # expires all reflog entries now (DANGEROUS)
```

Don't actually run these unless you're in a throwaway test repo. Instead:
- What are the default expiry settings?
- How would you change them (globally or per-repo)?
- When would you legitimately want to force GC?

---

## Bonus: The ORIG_HEAD safety pointer

Git sets `ORIG_HEAD` before any operation that significantly changes HEAD (merge, rebase, reset). This gives you a one-step undo:

```bash
git reset --hard ORIG_HEAD   # undo the last merge or rebase
```

Test it: do a merge, then immediately undo it with `ORIG_HEAD`. Is it faster than finding the hash in reflog? What's the limitation of `ORIG_HEAD` vs reflog? (Hint: ORIG_HEAD is overwritten by the next big operation.)
