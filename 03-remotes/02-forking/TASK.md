# Task: Fork a Repo and Set Up Upstream

## Steps

1. Find a small public GitHub repo to fork. Options:
   - A repo you want to contribute to
   - `github.com/octocat/Hello-World` (GitHub's demo repo)
   - Any small open-source tool you use

2. On GitHub, click the **Fork** button. Select your account as the destination.

3. Clone YOUR fork (not the original):

```bash
git clone git@github.com:ramsaikumar-pv/REPO-NAME.git
cd REPO-NAME
```

4. Check the current remotes:

```bash
git remote -v
```

Only `origin` exists, pointing to your fork.

5. Add the original as `upstream`:

```bash
git remote add upstream git@github.com:ORIGINAL-OWNER/REPO-NAME.git
git remote -v
```

Now you should see both `origin` and `upstream`.

6. Fetch from upstream (you won't merge yet — just look):

```bash
git fetch upstream
git log --oneline upstream/main -5
```

7. Check if your fork is behind upstream:

```bash
git log --oneline HEAD..upstream/main
```

If this shows commits, your fork is behind and needs syncing.

8. Sync your fork:

```bash
git merge upstream/main
git push origin main
```

9. Verify on GitHub — your fork should show "This branch is up to date with ORIGINAL-OWNER/REPO-NAME."

---

## What do you see? What does it mean?

- What's the difference between `origin` and `upstream`?
- What does `HEAD..upstream/main` mean in the log command?
- If upstream gets 10 new commits while you're working, how would you sync?
