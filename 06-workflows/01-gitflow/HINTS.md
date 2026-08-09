# Hints

<details>
<summary>Hint 1 — Why does Gitflow always use --no-ff for merges?</summary>

`--no-ff` (no fast-forward) always creates a merge commit, even when a fast-forward is possible. In Gitflow, this is mandatory because it preserves the "shape" of the feature branch in the history. You can look at the graph and clearly see "this is where feature/X was integrated." Without `--no-ff`, fast-forward merges create a flat linear history where it's impossible to see which commits belonged together as a feature unit.

For the same reason, Gitflow uses `--no-ff` for release and hotfix merges — each merge is a recorded event in the history.

</details>

<details>
<summary>Hint 2 — I forgot to merge the release branch back into develop — how do I fix it?</summary>

Just do the merge now:

```bash
git switch develop
git merge --no-ff release/1.0 -m "Merge release/1.0 into develop (delayed)"
```

Even after you've merged into main and deleted the release branch, the release branch's commits are reachable from main. If you deleted the branch, find the commit hash from `git log main`:

```bash
git log main --oneline -5
# find the release merge commit
git merge --no-ff <hash-of-release-merge-commit>
```

The critical thing is that `develop` must include the QA fixes made on the release branch. If it doesn't, those fixes are in `main` but not in the next development cycle.

</details>

<details>
<summary>Hint 3 — Is there a tool to automate Gitflow commands?</summary>

Yes: `git flow` is a CLI extension that automates the multi-step Gitflow operations:

```bash
# Install (Ubuntu/WSL)
sudo apt install git-flow

git flow init          # sets up branch names
git flow feature start my-feature
git flow feature finish my-feature   # merges, deletes branch
git flow release start 1.0
git flow release finish 1.0   # merges to main AND develop, tags
git flow hotfix start 1.0.1
git flow hotfix finish 1.0.1
```

It's a convenience wrapper for exactly what you did manually in this task. Learning the manual commands first (as you have) means you understand what `git flow` is actually doing.

</details>
