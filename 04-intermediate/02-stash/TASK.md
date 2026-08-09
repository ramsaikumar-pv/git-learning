# Task: Stash and Restore Changes

## Scenario

You're editing `app.py` to add a new feature. Mid-edit, you need to switch to a hotfix branch to patch something urgent. You'll use stash to safely shelve your work.

## Steps

1. Edit `app.py` — add a new function at the bottom. Don't commit:

```bash
vi app.py
# Add: def new_feature(): return "coming soon"
```

2. Check status — you have unstaged changes:

```bash
git status
```

3. Stash with a name:

```bash
git stash push -m "WIP: new feature function"
```

4. Check status again — is the working directory clean?

```bash
git status
git stash list
```

5. Switch to a "hotfix" branch and make a quick fix:

```bash
git switch -c hotfix/urgent-patch
echo "# HOTFIX" >> config.yaml
git add config.yaml
git commit -m "Apply urgent config hotfix"
git switch main
git merge hotfix/urgent-patch
```

6. Now restore your stash:

```bash
git stash pop
```

7. Verify your in-progress work is back:

```bash
git status
git diff
```

8. Now test multiple stashes. Make another change, stash it:

```bash
echo "# another change" >> config.yaml
git stash push -m "config tweak"
git stash list
```

9. Apply only the first stash (the feature work, `stash@{1}`):

```bash
git stash apply stash@{1}
git stash list   # is the stash still there?
```

10. Drop the applied stash:

```bash
git stash drop stash@{1}
```

---

## What do you see? What does it mean?

- What did `git status` show before and after `git stash`?
- What's the difference between `git stash pop` and `git stash apply`?
- In `git stash list`, which entry is `stash@{0}` — oldest or newest?
