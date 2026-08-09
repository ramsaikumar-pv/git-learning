# Challenge

## Challenge 1: Cross-fork PR

Fork a repo. Make a change on a feature branch in your fork. Open a PR from your fork's branch to the original repo's `main`.

This is the standard open-source contribution flow:
- Your fork's branch: `ramsaikumar-pv/repo:feature/fix-typo`
- Target: `original-owner/repo:main`

GitHub makes this the default when you open a PR from a fork. Observe how the PR page shows two different repos in the branch comparison.

---

## Challenge 2: Review someone else's PR

If you have a colleague also doing this course, swap repos:
1. They open a PR on your repo
2. You review it: leave comments, request changes
3. They address your feedback with new commits
4. You approve and merge

If no colleague is available: open a PR on a real open-source project (find a "good first issue" labelled PR). Even if it's not merged, you'll see the full review flow.

---

## Challenge 3: Branch protection rules

On your GitHub repo:
1. Settings → Branches → Add branch protection rule
2. Pattern: `main`
3. Enable: "Require a pull request before merging"
4. Enable: "Require approvals: 1"

Now try to push directly to main:
```bash
echo "direct push" >> README.md
git add . && git commit -m "Direct push attempt"
git push origin main
```

What error do you get? This is how real teams protect their production branch.

---

## Bonus: gh CLI

Install the GitHub CLI (`gh`) if you haven't:
```bash
# Ubuntu/WSL
sudo apt install gh
gh auth login
```

Then:
```bash
gh pr create --title "My PR" --body "Description"
gh pr list
gh pr view 1
gh pr merge 1 --squash
```

The CLI is faster than the GitHub UI for PR operations — especially useful in platform engineering automation.
