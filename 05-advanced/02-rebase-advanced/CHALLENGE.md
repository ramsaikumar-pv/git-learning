# Challenge

## Challenge 1: Reorder and drop

Create 4 commits in this order: A (feature), B (debug print), C (another feature), D (cleanup).

Use interactive rebase to:
1. Drop commit B (the debug print)
2. Move commit D before commit C

Result: A, D, C (in that order, with B gone).

Verify the code still works (no conflicts from reordering — make sure the changes are independent first).

---

## Challenge 2: Split a commit

You have one commit that mixed two unrelated changes. Split it:

1. In interactive rebase, mark that commit as `edit`
2. Git pauses at that commit
3. Unstage everything: `git reset HEAD~1`
4. Stage and commit only part 1: `git add -p`
5. Stage and commit part 2: `git add -p && git commit -m "..."`
6. `git rebase --continue`

Now `git log --oneline` should show two commits where there was one.

---

## Challenge 3: Autosquash with fixup commits

Git has a shortcut for fixup commits. When you make a fixup commit:

```bash
git commit --fixup=<original-hash>
```

The message is automatically set to `fixup! <original message>`.

Then:
```bash
git rebase -i --autosquash HEAD~5
```

Git automatically puts fixup commits in the right position and changes their keyword to `fixup`. Check the rebase editor — the ordering and keywords are done for you.

---

## Bonus: Interactive rebase for the whole branch

```bash
git rebase -i $(git merge-base HEAD main)
```

`git merge-base HEAD main` finds the common ancestor of your branch and main — the point where you diverged. This lets you interactive-rebase ALL commits on your branch without knowing exactly how many there are. Useful before opening a PR to clean up everything in one shot.
