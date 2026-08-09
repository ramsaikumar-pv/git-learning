# Pull Requests

A pull request (PR) is not a Git concept — it's a GitHub feature. It's a request to merge your branch into another branch, with a conversation layer on top.

In an OpenShift context, think of a PR like a Gitops change review: your proposed config change is in a branch, someone reviews it before it gets applied to the cluster. PRs are the code review gate.

---

## The PR lifecycle

```
1. Create a branch         →  git switch -c feature/my-change
2. Make commits            →  git add && git commit
3. Push the branch         →  git push origin feature/my-change
4. Open a PR on GitHub     →  UI or gh CLI
5. Code review happens     →  comments, requests for changes
6. Address feedback        →  new commits on the same branch
7. Merge the PR            →  squash / merge commit / rebase merge
8. Delete the branch       →  GitHub offers this after merge
```

---

## Opening a PR

After pushing your branch, GitHub usually shows a banner: "Compare & pull request." Click it.

Or go to: `github.com/your/repo/compare/feature/my-change`

Fill in:
- **Title**: the change in one line
- **Description**: why, what, any context reviewers need
- **Reviewers**: who should look at this
- **Labels**: bug, feature, documentation, etc.

---

## What reviewers can do

- Leave line comments on specific changes
- Approve (✅) or request changes (🔄)
- Start a review (batches comments before submitting)
- Suggest direct code edits (you can accept in one click)

---

## Merge options (on GitHub)

| Method | What it does | History |
|--------|-------------|---------|
| **Merge commit** | 3-way merge, keeps all commits | Bushy graph |
| **Squash and merge** | All commits → one commit | Clean, linear |
| **Rebase and merge** | Replays commits on main, no merge commit | Clean, linear |

Your team picks one convention and sticks to it. Many platform teams prefer squash for clean history.

---

## After merge

GitHub offers "Delete branch" — do it. The commits are preserved in main; the branch pointer is just cleaned up.

Then locally:
```bash
git switch main
git pull                      # get the merged commit
git branch -d feature/my-change   # delete local branch
```

---

## Draft PRs

Open a PR as "Draft" to signal it's not ready for review yet but you want CI to run, or you want visibility.

```bash
# via gh CLI
gh pr create --draft --title "WIP: my feature"
```
