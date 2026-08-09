# Solution

## After push: what GitHub shows
GitHub detects the new branch and shows a yellow banner:
"feature/add-readme-section had recent pushes — Compare & pull request"

## The PR: Files changed tab
Each file shows a green/red diff — lines added in green (`+`), lines removed in red (`-`). This is the same diff format as `git diff`, just rendered in the browser.

## After squash merge: `git log --oneline -3`
```
f4a2d1e (HEAD -> main, origin/main) Add architecture overview and contact info to README (#1)
b7e1f3a Add version comment to app
a3f9d12 Add app entrypoint and initial config
```

Only ONE commit appeared, not two. The squash merge collapsed "Add architecture overview section" and "Add contact info" into a single commit. The commit message includes the PR number `(#1)` — GitHub adds this automatically as a link back to the PR.

## `git branch -d feature/add-readme-section`
```
Deleted branch feature/add-readme-section (was c8f2a9b).
```

Or if it fails due to hash mismatch: `git branch -D feature/add-readme-section`

## Why squash?

Your two commits ("Add architecture overview" and "Add contact info") were small, iterative steps — the kind of thing you commit during development. But `main`'s history shouldn't show every intermediate step. A squash merge says: "From main's perspective, this was one logical change." Clean, professional, easy to read with `git log`.

## The PR number (#1)

GitHub assigns each PR a number. The squash commit message includes `(#1)` which is a GitHub hyperlink — anyone reading the log can jump directly to the PR, see the original commits, the review comments, and the discussion. This is the permanent record.
