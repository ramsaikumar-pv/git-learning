# Hints

<details>
<summary>Hint 1 — Git opened an editor for the merge commit message — how do I save and close it?</summary>

You're in `vi`. The default message "Merge branch 'feature/add-metrics'" is already written. To accept it:
1. Press `Esc` to make sure you're not in insert mode
2. Type `:wq` and press Enter

To write a custom message: press `i`, edit the first line, then `Esc` → `:wq`.

</details>

<details>
<summary>Hint 2 — How do I force a 3-way merge even when fast-forward is possible?</summary>

Use `--no-ff` (no fast-forward):

```bash
git merge --no-ff feature/add-health
```

This always creates a merge commit, even if a fast-forward was possible. Some teams mandate this so every feature branch merge appears visually in the log. Others prefer the clean linear history of fast-forward. Both are valid — it's a team convention.

</details>

<details>
<summary>Hint 3 — Merge says "Already up to date" — what does that mean?</summary>

It means the branch you're merging is already an ancestor of your current branch — there's nothing new to bring in. This happens if you merge a branch you've already merged, or if both branches point to the same commit. Check `git log --oneline --graph --all` to see the relationship.

</details>
