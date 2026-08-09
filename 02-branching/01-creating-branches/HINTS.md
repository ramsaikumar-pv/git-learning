# Hints

<details>
<summary>Hint 1 — I accidentally created the branch from the wrong starting point. How do I fix it?</summary>

Delete the branch and recreate it from the correct starting point:

```bash
git branch -D wrong-branch
git switch main                          # or whatever branch you want to start from
git switch -c correct-branch
```

Make sure you don't have uncommitted work on the wrong branch first — use `git stash` to save it if needed (covered in module 04-02).

</details>

<details>
<summary>Hint 2 — The file disappeared when I switched branches — is my work lost?</summary>

No. The file exists on your feature branch. Git swaps out your working directory to match whichever branch you're on. Switch back to `feature/add-logging` and the file will reappear. Git stores the file in its object database — switching branches just changes which version of the tree is checked out.

</details>

<details>
<summary>Hint 3 — git switch says "error: Your local changes to the following files would be overwritten"</summary>

You have uncommitted changes on your current branch that would be clobbered by switching. Git is protecting you. Options:
1. Commit your changes first: `git add . && git commit -m "WIP"`
2. Stash them: `git stash` (covered in module 04-02)
3. Discard them (dangerous): `git restore .`

Option 1 or 2 is almost always the right move.

</details>
