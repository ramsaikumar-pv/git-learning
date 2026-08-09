# Hints

<details>
<summary>Hint 1 — Rebase paused with a conflict — what do I do?</summary>

Git paused because it couldn't automatically apply one of your commits on top of the new base. You need to:

1. Open the conflicted file and resolve the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
2. `git add <resolved-file>`
3. `git rebase --continue`

Do NOT `git commit` — `git rebase --continue` handles the commit step during rebase.

If you want to give up entirely: `git rebase --abort` takes you back to before you started the rebase.

</details>

<details>
<summary>Hint 2 — I expected a linear graph after rebase but it still looks forked — why?</summary>

Run `git log --oneline --graph --all`. The `--all` flag shows ALL branches. After rebase, the feature branch is linear on top of main — but the graph might look forked if you have other branches still pointing at old commits. Focus on the path from `HEAD` back through `main` — that should be linear after a successful rebase.

</details>

<details>
<summary>Hint 3 — Why did the commit hash change after rebase?</summary>

A commit's hash is computed from its content, author, timestamp, AND its parent hash. After rebasing, your commit now has a different parent (the tip of main) than it had before. Different parent → different hash. The changes you made are identical, but the commit is a new object. This is why the golden rule says never rebase shared commits — the hash changed, so anyone who had the old hash is now diverged from you.

</details>
