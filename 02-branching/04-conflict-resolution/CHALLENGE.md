# Challenge

## Challenge 1: Multi-file conflict

Create a merge conflict in TWO files simultaneously:

1. On `main`, change `app.py` line 1 AND `config.yaml` line 2.
2. On a feature branch (branching from before those changes), change the same lines differently.
3. Merge. Resolve both conflicts. Commit.

How does `git status` show multiple conflicting files? Do you resolve them in any order?

---

## Challenge 2: Accept an entire side without editing

Sometimes you know one side is completely right and the other side is completely wrong. Instead of manually editing:

```bash
# Keep only what's in HEAD (current branch) for this file
git checkout --ours app.py
git add app.py

# Keep only what's in the incoming branch for this file
git checkout --theirs app.py
git add app.py
```

Set up a conflict and resolve it using `--ours` for one file and `--theirs` for another. Then commit.

---

## Challenge 3: Conflict during rebase

Rebase conflicts work slightly differently from merge conflicts. Create a scenario where rebasing causes a conflict:

1. On `main`: commit a change to line 1 of `app.py`.
2. On `feature/x`: commit a different change to the same line (starting from before step 1).
3. Rebase `feature/x` onto `main`.

Resolve the conflict, then `git rebase --continue`. Notice: after continuing, the commit message comes from the ORIGINAL feature commit, not from you. Why? What's different from a merge conflict resolution?

---

## Bonus: A three-way conflict

A three-way conflict is actually impossible in Git's conflict markers (they only show two sides). But explore what happens when you rebase a branch that has its OWN merge commits. What does `git rebase` do with merge commits by default? (Research: `git rebase --rebase-merges`)
