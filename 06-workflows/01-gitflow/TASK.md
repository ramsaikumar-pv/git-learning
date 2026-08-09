# Task: Simulate a Gitflow Release

You'll set up the Gitflow branch structure, release a feature, and ship a hotfix.

## Setup

1. Make sure `main` has at least one commit. Create a `develop` branch:

```bash
git switch main
git switch -c develop
```

## Part 1: Feature development

2. Create a feature branch from `develop`:

```bash
git switch -c feature/add-notifications develop
echo "def notify(msg): print(msg)" >> app.py
git add app.py
git commit -m "feat: add notification function"
```

3. Merge feature back to `develop` (always use `--no-ff` in Gitflow):

```bash
git switch develop
git merge --no-ff feature/add-notifications -m "Merge feature/add-notifications into develop"
git branch -d feature/add-notifications
```

## Part 2: Release

4. Cut a release branch:

```bash
git switch -c release/1.0 develop
```

5. Apply a bug fix found during QA:

```bash
echo "# QA fix: validate msg not None" >> app.py
git add app.py
git commit -m "fix: validate notification message"
```

6. Finish the release — merge into `main` and tag:

```bash
git switch main
git merge --no-ff release/1.0 -m "Release 1.0"
git tag -a v1.0 -m "Version 1.0"
```

7. Merge release back into `develop` (to carry the QA fix):

```bash
git switch develop
git merge --no-ff release/1.0 -m "Merge release/1.0 into develop"
git branch -d release/1.0
```

## Part 3: Hotfix

8. A critical bug is found in production. Branch from `main`:

```bash
git switch main
git switch -c hotfix/1.0.1
echo "# HOTFIX: prevent crash on empty msg" >> app.py
git add app.py
git commit -m "fix: prevent crash on empty notification message"
```

9. Merge hotfix into `main` and `develop`:

```bash
git switch main
git merge --no-ff hotfix/1.0.1 -m "Hotfix 1.0.1"
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git switch develop
git merge --no-ff hotfix/1.0.1 -m "Merge hotfix/1.0.1 into develop"
git branch -d hotfix/1.0.1
```

10. View the full graph:

```bash
git log --oneline --graph --all
```

---

## What do you see? What does it mean?

- How does the graph look compared to a simple main/feature workflow?
- Why must a hotfix merge into BOTH `main` and `develop`?
- What happens if you forget to merge the release branch back into `develop`?
