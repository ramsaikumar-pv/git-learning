# Challenge

## Challenge 1: Parallel features

Simulate two feature branches developed simultaneously:

1. Create `feature/login` from `develop`, make 2 commits.
2. Create `feature/dashboard` from `develop`, make 2 commits.
3. Merge `feature/login` into `develop` first.
4. Merge `feature/dashboard` into `develop`.

Was there a conflict? What does the graph look like? Would there have been a conflict if you'd rebased instead of merged?

---

## Challenge 2: Release branch bug

During release testing, you find a bug that also exists in `develop`. Fix it on the release branch:

```bash
git switch release/1.1
vi app.py   # fix the bug
git add app.py
git commit -m "fix: resolve issue found in release testing"
```

After finishing the release (merge to main + develop), verify `develop` has the fix. Run `git log develop --oneline` and `grep` for the commit.

---

## Challenge 3: Emergency hotfix mid-feature

You're halfway through a feature when a prod hotfix is needed:

1. On `feature/big-feature`, you have uncommitted work.
2. Stash it: `git stash push -m "WIP feature work"`
3. Switch to `main`, create `hotfix/critical`
4. Apply the fix, merge into main and develop
5. Come back to your feature, pop the stash, continue

Run `git log --oneline --graph --all` at the end to see the full picture.

---

## Bonus: When did teams abandon Gitflow?

Read the original author's 2020 note at the top of the Gitflow article (search "A successful Git branching model"). What did Vincent Driessen say about when NOT to use Gitflow? How does this connect to the rise of continuous delivery?
