# Challenge

## Challenge 1: Cherry-pick a range

Your feature branch has 5 commits. Commits 2, 3, and 4 are ready for main but commit 5 is not.

```bash
git log --oneline feature/mixed-work
# note hashes of commits 2, 3, 4 (call them B, C, D)

git switch main
git cherry-pick B^..D   # inclusive range: B through D
```

Check the log. Did all three commits land on main? Are their hashes the same as on the feature branch?

---

## Challenge 2: Cherry-pick without committing

Cherry-pick three commits but combine them into ONE commit on main:

```bash
git cherry-pick --no-commit hash1
git cherry-pick --no-commit hash2
git cherry-pick --no-commit hash3
git status              # all changes are staged
git commit -m "Combined: fixes A, B, and C"
```

When would you use this? Compare the resulting commit history to cherry-picking each individually.

---

## Challenge 3: Cherry-pick between repos

Advanced scenario: you have two separate repos (not branches). Can you cherry-pick a commit from one repo into another?

Yes — using `git remote`:

```bash
# In repo-target:
git remote add source /path/to/source-repo
git fetch source
git cherry-pick source/main~2  # second commit from source's main
git remote remove source
```

This is obscure but useful for sharing commits across unrelated repos. Try it with two local repos.

---

## Bonus: `git cherry` (without -pick)

`git cherry` (no hyphen) compares two branches and shows which commits on one are not in the other — before you cherry-pick them:

```bash
git cherry main feature/mixed-work
```

```
+ a7e1f3b Fix connection timeout
+ c8f2g4b Add v2 endpoint
+ d9h3i5c WIP: cache layer sketch
```

`+` means "this commit is not in main." `-` means it already is (as a cherry-pick or merge). Use this to decide what to pick before you pick it.
