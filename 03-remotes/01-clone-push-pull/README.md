# Clone, Push, Pull 🌱

## 📖 In plain words

So far, everything you've done has lived only on your own laptop. This module connects that local work to GitHub, a website that stores a copy of your project in the cloud — what Git calls a **remote**.

Two directions matter: **push** sends your local commits up to GitHub (like uploading a file to Google Drive ☁️), and **pull** brings down commits that exist on GitHub but not on your machine yet. That's really the whole module — everything below is detail on how to do each of those safely.

---

## Clone an existing repo

```bash
git clone git@github.com:someuser/some-repo.git
```

This one command does four things for you automatically:
1. Creates a folder named `some-repo` on your machine
2. Downloads the *entire* project history — every commit, ever
3. Remembers where it came from, under the nickname `origin`
4. Switches you onto the default branch (usually `main`), ready to work

Up to now, you've only created repos with `git init` — you were the "author." Cloning is the "consumer" side: getting a copy of a project someone else already started.

---

## Add a remote to an existing local repo

You already have a local repo and created an empty GitHub repo. Link them:

```bash
git remote add origin git@github.com:ramsaikumar-pv/my-project.git
```

`origin` isn't a special keyword — it's just a nickname you (and Git, by convention) give to that GitHub URL, so you don't have to type the whole address every time. Almost everyone names their main remote `origin`.

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

`-u` links your local `main` branch to `origin`'s `main` branch, so Git remembers "these two go together." Ram's analogy nails it: it's like saving a contact in your phone 📱 — do it once, and afterward you can just say the name instead of dialing the full number.

After this one-time setup, every future push from this branch is simply:
```bash
git push
```

---

## Pull = fetch + merge

```bash
git pull
```

`git pull` does two steps in one: it downloads whatever's new on GitHub, then immediately merges it into your current branch. Under the hood it's exactly the same as running:

```bash
git fetch origin
git merge origin/main
```

If you'd rather look before you leap — see what changed before merging it into your own work — use `fetch` on its own instead.

---

## `git fetch` — download without merging

```bash
git fetch origin
git log --oneline --graph origin/main
```

This downloads the latest history from GitHub, but your current branch doesn't change at all yet — only Git's local record of `origin/main` updates. This gives you a safe way to review what's different before deciding whether to merge it in.

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

HTTPS prompts for a password (or requires a token) every time. SSH uses your key pair automatically — the padlock (public key 🔓) sits on GitHub, and only your private key 🔑 (kept on your machine) can open it. No typing passwords.

---

## ✅ Quick recap

- `git clone <url>` — download a full copy of someone else's repo (with history).
- `git remote add origin <url>` — link a local repo to a GitHub URL, nicknamed `origin`.
- `git push -u origin main` — first push, sets up tracking (do once). After that, just `git push`.
- `git pull` = `git fetch` + `git merge` in one step. `git fetch` alone lets you look before merging.
