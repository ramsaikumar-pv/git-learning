# Hints

<details>
<summary>Hint 1 — I don't see the "Compare & pull request" banner on GitHub</summary>

GitHub shows this banner for a few minutes after you push. If it's gone:
1. Go to your repo on GitHub
2. Click the "Pull requests" tab
3. Click "New pull request"
4. In the "compare:" dropdown, select `feature/add-readme-section`
5. Click "Create pull request"

Alternatively, navigate directly to:
`https://github.com/ramsaikumar-pv/REPO/compare/feature/add-readme-section`

</details>

<details>
<summary>Hint 2 — After squash merge and pull, the branch deletion fails locally</summary>

If you merged on GitHub and pulled locally, your local branch is now "unmerged" from Git's perspective — the squash commit has a different hash than your original commits. Use force delete:

```bash
git branch -D feature/add-readme-section
```

The `-D` (capital) forces deletion even when Git thinks the branch hasn't been merged. The code is safely in `main` — the original commits are just represented by a different squash commit hash.

</details>

<details>
<summary>Hint 3 — How do I see and respond to review comments?</summary>

On GitHub, go to your PR. Under the "Files changed" tab, you'll see inline comments. Under "Conversation," you see the full thread. To respond:
1. Push new commits to the same branch
2. GitHub automatically updates the PR with the new commits
3. Reply to each comment thread
4. When all discussions are resolved, the PR is ready to merge

You don't need to close and reopen a PR to add commits — just push to the same branch.

</details>
