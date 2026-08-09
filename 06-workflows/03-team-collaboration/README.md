# Team Collaboration

Git is a technical tool. But using it in a team is as much about conventions and communication as it is about commands. This module covers the practices that make shared repos work smoothly.

---

## Branch protection rules

On GitHub, go to Settings → Branches → Add branch protection rule.

Key rules for `main`:
- **Require a pull request before merging** — no direct pushes
- **Require approvals: 1 (or 2)** — at least one reviewer must approve
- **Require status checks to pass** — CI must be green before merge
- **Require branches to be up to date** — branch must be rebased/merged with main before merging
- **Do not allow bypassing the above settings** — even admins follow the rules

This turns `main` into a protected highway. Only reviewed, tested code enters.

---

## CODEOWNERS

`.github/CODEOWNERS` auto-assigns reviewers based on which files changed:

```
# Default owners for everything
*                   @ramsaikumar-pv

# Infrastructure files need platform team review
/infra/             @platform-team
*.yaml              @platform-team @ops-team

# Frontend owned by frontend team
/frontend/          @frontend-team

# Security team reviews auth changes
/auth/              @security-team
```

When a PR changes `infra/deploy.yaml`, GitHub automatically adds `@platform-team` and `@ops-team` as required reviewers.

---

## What makes a good PR

**Size**: < 400 lines changed. Reviewers can't focus on a 2000-line PR effectively.

**Title**: imperative, specific. "Add health check endpoint" not "health check stuff".

**Description**: answer:
- What changed?
- Why was this change needed?
- How was it tested?
- Any risks or caveats?

**Commits**: clean history. Either squash to one commit or keep atomic commits that make sense individually. No "WIP", "fix typo", "oops" in the final PR history.

**Screenshots/output**: for UI changes or CLI tools, show before/after.

---

## Code review etiquette

As a reviewer:
- Comment on the code, not the person ("This function could..." not "You wrote a bad function")
- Distinguish blocking vs non-blocking: prefix with `nit:` for non-blocking suggestions
- Ask questions rather than demand changes: "What's the reason for X?" often surfaces valid context
- Approve when confident, not when you've run out of things to say

As an author:
- Respond to every comment (even if just "Done" or "Won't fix: because X")
- Don't merge without resolving blocking comments
- Request a re-review after making changes

---

## Commit message conventions

Many teams adopt Conventional Commits:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `build`

Examples:
```
feat(auth): add OAuth2 login support
fix(db): prevent connection pool exhaustion
docs: update contributing guide
chore(deps): bump requests to 2.31.0
ci: add parallel test execution
```

With conventional commits, you can auto-generate changelogs and enforce semver bumps automatically.
