# Challenge

## Challenge 1: Make a change in your fork and sync back

1. On your fork, create a branch: `git switch -c test-fork-change`
2. Edit a file, commit it, push to your fork: `git push origin test-fork-change`
3. Now sync main with upstream (as if time passed and upstream moved):
   ```bash
   git fetch upstream
   git switch main
   git merge upstream/main
   git push origin main
   ```
4. Is your `test-fork-change` branch still there? Is it behind `main` now?

---

## Challenge 2: Simulate upstream moving while you're working

1. Have your fork's `main` synced with upstream.
2. Create a feature branch and make 2 commits on it.
3. (Imagine) upstream gets 3 new commits (simulate by pushing to the upstream if you own it, or find a repo that's actively receiving commits).
4. Fetch upstream, rebase your feature branch on top of `upstream/main`:
   ```bash
   git fetch upstream
   git switch feature/my-work
   git rebase upstream/main
   ```

This is the full fork contribution workflow used in real open-source projects.

---

## Challenge 3: Remove a remote

You added `backup` in a previous challenge. Remove it:

```bash
git remote remove backup
git remote -v
```

What happens to any commits that were only on the backup remote? (Answer: nothing — commits are local objects; remotes are just names/URLs.)

---

## Bonus: GitHub's "Sync fork" button

GitHub now has a "Sync fork" button that does `fetch upstream + merge` automatically through the GitHub UI. Try it. Does it do the same as the manual steps? When might you prefer the manual approach? (Think: conflicts, rebase vs merge preference.)
