# Hints

<details>
<summary>Hint 1 — git push says "error: failed to push some refs" — what does that mean?</summary>

The remote has commits your local doesn't have. Git won't push because it would overwrite those changes. Pull first, resolve any conflicts, then push:

```bash
git pull
# resolve conflicts if any
git push
```

If you JUST created the remote repo and it has a README that GitHub auto-generated, this is why. Always create empty repos on GitHub (tick "no README") when connecting to an existing local repo.

</details>

<details>
<summary>Hint 2 — git push says "Permission denied (publickey)"</summary>

Your SSH key isn't being used correctly. Verify:

```bash
ssh -T git@github.com
```

Expected: `Hi ramsaikumar-pv! You've successfully authenticated...`

If that fails:
1. Make sure `~/.ssh/id_ed25519.pub` is added to GitHub (Settings → SSH and GPG keys)
2. Make sure `ssh-agent` is running: `eval "$(ssh-agent -s)"`
3. Add your key: `ssh-add ~/.ssh/id_ed25519`

</details>

<details>
<summary>Hint 3 — After git pull, my log doesn't show the GitHub commit — what happened?</summary>

Check which branch you pulled into. `git pull` pulls into your current branch. If you were on `feature/something`, it pulled `origin/feature/something`, not `origin/main`. Switch to `main` and try again:

```bash
git switch main
git pull
git log --oneline
```

</details>
