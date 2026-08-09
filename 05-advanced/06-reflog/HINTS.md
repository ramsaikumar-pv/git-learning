# Hints

<details>
<summary>Hint 1 — I can't find the lost commit hash in reflog — too many entries</summary>

Filter with `grep`:

```bash
git reflog | grep "Important work C"
git reflog | head -20   # just the most recent 20 entries
```

Or use the `--since` option:

```bash
git reflog --since="10 minutes ago"
```

The reflog shows newest first. The commits you just reset away should be near the top, just after the reset entry.

</details>

<details>
<summary>Hint 2 — I recovered the branch but `git log` shows some commits in wrong order</summary>

When you merge the recovery branch into main, the commits become part of main's history. The log shows them merged in correctly. If the order looks unexpected, check `git log --oneline --graph` to see the full picture including the merge commit.

If you want a linear history (no merge commit), use:
```bash
git switch main
git rebase recovery/lost-work
```

Instead of merge.

</details>

<details>
<summary>Hint 3 — The deleted branch isn't showing in reflog with grep "temp-branch"</summary>

When you deleted the branch, Git recorded the checkout-away in reflog but used HEAD's movement, not the branch name. Try:

```bash
git reflog | grep "temp"
# or
git reflog | grep "Temp branch commit"
```

The last commit on `temp-branch` will appear as a regular commit entry. Find the hash next to "Temp branch commit" and create the branch from there.

</details>
