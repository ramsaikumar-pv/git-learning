# Pull Requests 🌱

## 📖 In plain words

A pull request (PR) is not something Git itself knows about — it's a feature built by GitHub, on top of Git. In plain words: it's a formal way of saying "hey, please review my branch and merge it in if it looks good" — with comments, approvals, and discussion attached, right there on the page.

In an OpenShift context, think of a PR like a GitOps change review: your proposed config change sits in a branch, someone reviews it before it gets applied to the cluster. That review step is exactly what a PR gives you for code.

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

GitHub gives you three buttons for finishing a PR — each produces a different-looking history, but the end result (your code, now in `main`) is the same:

| Method | What it does | History |
|--------|-------------|---------|
| **Merge commit** | Standard 3-way merge, keeps every individual commit | Bushy graph |
| **Squash and merge** | Combines all your commits into a single new one | Clean, linear |
| **Rebase and merge** | Replays each commit onto main, no merge commit added | Clean, linear |

You don't need to decide this yourself every time — your team agrees on one option and sticks to it. Many platform teams prefer squash, since it keeps `main`'s history simple: one commit per feature, no clutter.

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

---

## ✅ Quick recap

- A PR = a GitHub feature (not a Git command) requesting review before merging a branch.
- Lifecycle: branch → commit → push → open PR → review → address feedback → merge → delete branch.
- Merge, squash, or rebase — three ways to finish a PR, each shaping history differently.
- Draft PRs signal "not ready for review yet" while still enabling CI and visibility.
