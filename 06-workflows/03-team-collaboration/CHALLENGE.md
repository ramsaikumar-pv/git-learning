# Challenge

## Challenge 1: CODEOWNERS with multiple owners

Update your CODEOWNERS to require two approvers for sensitive files:

```
# Two owners required (both must approve)
/infra/     @ramsaikumar-pv @second-collaborator
*.key       @ramsaikumar-pv
```

Research: if `@second-collaborator` doesn't exist on GitHub, does CODEOWNERS silently fail or visibly error? How would you test this?

---

## Challenge 2: Conventional Commits changelog

Install `git-cliff` or `conventional-changelog` and auto-generate a CHANGELOG from your conventional commit history:

```bash
# Using git-cliff (Rust tool, very fast)
# Install: https://github.com/orhun/git-cliff
git cliff --output CHANGELOG.md
cat CHANGELOG.md
```

This reads your `feat:`, `fix:`, `chore:` commits and generates grouped release notes automatically. Compare the output to your `git log`. Is there anything in the log that doesn't appear in the changelog?

---

## Challenge 3: Write a CONTRIBUTING.md

Write a `CONTRIBUTING.md` at the repo root that documents:
1. How to set up the repo locally
2. Branch naming convention (`feature/`, `fix/`, `chore/`)
3. Commit message format (conventional commits)
4. PR requirements (size, description format, testing)
5. Review etiquette expectations

This is what real open-source and team repos use to onboard new contributors. Commit it and open a PR.

---

## Bonus: Draft PRs and WIP

GitHub's "Draft PR" feature lets you open a PR that isn't ready for review:

```bash
gh pr create --draft --title "feat: WIP new metrics endpoint"
```

Draft PRs:
- Are visible to the team
- CI runs on them (get early signal)
- Cannot be merged
- Can be converted to "ready for review" when done

When would you prefer a draft PR over working on a local branch? (Think: getting early CI feedback, sharing progress, coordinating with teammates.)
