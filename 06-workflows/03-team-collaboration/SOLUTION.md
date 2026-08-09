# Solution

## Error when pushing directly to protected main

```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: error: Required status check "ci" is failing.
remote: error: Changes must be made through a pull request.
To github.com:ramsaikumar-pv/my-repo.git
 ! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'git@github.com:...'
```

GitHub rejected the push. The protection rule is working.

## CODEOWNERS taking effect

When you open a PR that changes `.yaml` files, GitHub automatically adds you as a required reviewer in the right sidebar under "Reviewers." The PR shows: "1 approval required from code owners."

## `git log --oneline` with conventional commits

```
e4c7d1b fix(api): handle None input in v2 endpoint
d3b6c0a docs: add API section to README
c2a5b9c feat(api): add v2 endpoint stub
```

The `type(scope): description` format makes the log scannable:
- Immediately know if something is a feature, fix, or chore
- Easy to filter: `git log --oneline --grep="^feat"` shows only features
- Machines can parse this: tools like `semantic-release` read conventional commits and auto-bump the version (feat → minor, fix → patch)

## Why team conventions matter more than the tool

Git gives you flexibility. Teams restrict that flexibility with conventions so everyone's repo looks the same and reviews are predictable. Branch protection rules enforce the convention technically. CODEOWNERS encode domain knowledge ("who owns this?"). Conventional commits make history readable.

None of these are Git features per se — they're team practices layered on top of Git that make large-team collaboration tractable.
