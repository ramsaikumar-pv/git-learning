# Clone, Push, Pull

You've been working locally. Now it's time to connect to the cloud. GitHub is the remote — think of it like the upstream Helm chart repo in ArgoCD. You pull from it to get updates; you push to it to publish your changes.

---

## Clone an existing repo

```bash
git clone git@github.com:someuser/some-repo.git
```

This:
1. Creates a directory named `some-repo`
2. Downloads the full history
3. Sets up `origin` as the remote name pointing to that URL
4. Checks out the default branch (`main`)

You've been on the "author" side. Clone is the "consumer" side.

---

## Add a remote to an existing local repo

You already have a local repo and created an empty GitHub repo. Link them:

```bash
git remote add origin git@github.com:ramsaikumar-pv/my-project.git
```

`origin` is just a name — a nickname for the URL. By convention it's always `origin`.

Check it:
```bash
git remote -v
```
```
origin  git@github.com:ramsaikumar-pv/my-project.git (fetch)
origin  git@github.com:ramsaikumar-pv/my-project.git (push)
```

---

## First push — set the upstream

```bash
git push -u origin main
```

`-u` sets the upstream tracking: your local `main` → `origin/main`. You only do this once. It's like saving a contact in your phone — do it once, never need the full number again.

After this, just:
```bash
git push
```

---

## Pull = fetch + merge

```bash
git pull
```

This fetches the latest commits from the remote and merges them into your current branch. Equivalent to:

```bash
git fetch origin
git merge origin/main
```

Use `fetch` when you want to see what changed before merging it.

---

## `git fetch` — download without merging

```bash
git fetch origin
git log --oneline --graph origin/main
```

Your local branch stays where it is. `origin/main` updates. You can review what's different before deciding to merge or rebase.

---

## SSH vs HTTPS

You've set up SSH (`~/.ssh/id_ed25519`) — always use the SSH URL:
```
git@github.com:ramsaikumar-pv/my-project.git
```

Not the HTTPS URL:
```
https://github.com/ramsaikumar-pv/my-project.git
```

HTTPS prompts for a password (or requires a token). SSH uses your key automatically.
