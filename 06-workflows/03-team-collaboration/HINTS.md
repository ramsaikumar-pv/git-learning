# Hints

<details>
<summary>Hint 1 — I enabled "require approvals" but now I can't merge my own PRs — how do I approve my own PR?</summary>

You can't approve your own PR on GitHub (it's blocked by design — you can't review your own work). Options:

1. **Temporarily remove the rule**: Settings → Branches → Edit → uncheck "Require approvals" → save → merge → re-enable.

2. **Bypass as admin**: Enable "Allow specified actors to bypass required pull requests" and add yourself.

3. **Have a collaborator**: Add a GitHub friend as a collaborator (Settings → Collaborators) and have them review your PR for real.

For this learning exercise, option 1 is fine — you're learning the workflow, not enforcing it on yourself.

</details>

<details>
<summary>Hint 2 — My CODEOWNERS file isn't working — the reviewer isn't being auto-added</summary>

Check:
1. File is in `.github/CODEOWNERS` (capital C, capital O)
2. The pattern syntax is correct (same as `.gitignore`)
3. The file is committed to the **default branch** (`main`) — CODEOWNERS on a PR branch doesn't work
4. The GitHub username is spelled correctly: `@exact-username` with the `@` symbol

Test by going to "Pull requests" → "New pull request" → check if reviewers are auto-populated in the sidebar.

</details>

<details>
<summary>Hint 3 — What's the difference between "Require approvals" and "Require reviews from CODEOWNERS"?</summary>

- **Require approvals: N** — any N reviewers must approve, regardless of who they are
- **Require review from Code Owners** — specifically the people in CODEOWNERS for the changed files must approve, not just anyone

You can (and should) enable both. "Require code owner review" ensures the RIGHT people review changes to sensitive files. "Require N approvals" ensures a minimum number of reviewers overall. Enable both under branch protection rules.

</details>
