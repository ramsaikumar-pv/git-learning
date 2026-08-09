# Task: Set Up a Collaborative Repo

## Part 1: Branch Protection

1. On GitHub, go to your practice repo.
2. Settings → Branches → Add branch protection rule.
3. Branch name pattern: `main`
4. Enable:
   - "Require a pull request before merging"
   - "Require approvals: 1" (you'll approve your own PRs for practice)
   - "Require status checks" (if you have CI set up from module 07)
5. Save.

6. Try to push directly to main:

```bash
echo "direct push" >> README.md
git add README.md
git commit -m "chore: test direct push"
git push origin main
```

What error do you get?

---

## Part 2: CODEOWNERS

7. Create the CODEOWNERS file:

```bash
mkdir -p .github
vi .github/CODEOWNERS
```

Add:
```
*                 @ramsaikumar-pv
*.yaml            @ramsaikumar-pv
/docs/            @ramsaikumar-pv
```

8. Commit and push via a PR (since direct push is now blocked):

```bash
git switch -c chore/add-codeowners
git add .github/CODEOWNERS
git commit -m "chore: add CODEOWNERS file"
git push origin chore/add-codeowners
```

Open a PR on GitHub. Does GitHub show you as a required reviewer automatically?

---

## Part 3: Conventional Commits practice

9. Make three commits using the conventional commit format:

```bash
echo "# feature" >> app.py && git add app.py && git commit -m "feat(api): add v2 endpoint stub"
echo "# docs" >> README.md && git add README.md && git commit -m "docs: add API section to README"
echo "# fix" >> app.py && git add app.py && git commit -m "fix(api): handle None input in v2 endpoint"
```

10. View your log:

```bash
git log --oneline -5
```

---

## What do you see? What does it mean?

- What error did you get when pushing directly to main?
- What happens to your PR when you're the only reviewer and you've required an approval?
- How would CODEOWNERS change your workflow if there were two real team members?
