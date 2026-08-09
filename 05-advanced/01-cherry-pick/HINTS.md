# Hints

<details>
<summary>Hint 1 — I cherry-picked the wrong commit — how do I undo it?</summary>

If the cherry-pick already committed:
```bash
git revert HEAD          # create a new commit undoing it (safe, preserves history)
# or
git reset --hard HEAD~1  # remove the commit entirely (only safe if not pushed)
```

If cherry-pick is still in progress (conflict state):
```bash
git cherry-pick --abort  # returns to pre-cherry-pick state
```

</details>

<details>
<summary>Hint 2 — git cherry-pick failed with "nothing to commit" — why?</summary>

The changes from the cherry-picked commit already exist in your current branch. Git detects that applying this commit would result in no change — the code is already there. This happens when:

1. You already merged or cherry-picked this commit before
2. The commit's changes were independently written on your current branch

Use `git cherry-pick --skip` to skip this commit and continue if you're picking a range, or just accept that there's nothing to do.

</details>

<details>
<summary>Hint 3 — How do I find the exact commit hash of the bug fix when there are many commits?</summary>

Use `git log` with search:

```bash
git log --oneline --grep="timeout"     # search commit messages
git log --oneline -S "timeout = 30"    # search diff content (pickaxe)
git log --oneline feature/mixed-work   # show all commits on the feature branch
```

The `-S` "pickaxe" is especially useful — it finds the commit that added or removed a specific string. This is how you track down exactly which commit introduced a change.

</details>
