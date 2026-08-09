# Forking 🌱

## 📖 In plain words

A fork is simply your own personal copy of someone else's GitHub repo — created with one click, living under your own account. Why would you need this? Because you probably don't have permission to push directly to *their* repo. A fork gives you a version you fully own and can freely experiment on, without touching their original.

Ram's analogy: forking is like vendoring a community operator into your own org namespace 📦. You take the upstream code, customise it for your needs, and can still track the original for updates later.

---

## When you need to fork

- Contributing to an open-source project you don't own
- Customising a shared tool for your team without affecting the main repo
- Taking ownership of an abandoned repo

---

## Fork workflow

```
upstream (original)       your fork          your local
github.com/owner/repo  →  github.com/you/repo  →  ~/repo
                                                ↑
                                           git clone
```

The key thing to understand: you push to *your* fork, never directly to the original. The original repo (called `upstream`) only ever receives your changes if you open a pull request and the owner accepts it.

---

## Step 1: Fork on GitHub

Click the "Fork" button on any repo's GitHub page. GitHub creates `github.com/ramsaikumar-pv/repo-name` as your copy.

---

## Step 2: Clone YOUR fork

```bash
git clone git@github.com:ramsaikumar-pv/repo-name.git
cd repo-name
```

---

## Step 3: Add the original as `upstream`

Right now you only have one remote — `origin` — and it points to YOUR fork. To be able to pull in updates from the original project later, add it as a second remote, named `upstream` by convention:

```bash
git remote add upstream git@github.com:original-owner/repo-name.git
git remote -v
```

```
origin    git@github.com:ramsaikumar-pv/repo-name.git (fetch)
origin    git@github.com:ramsaikumar-pv/repo-name.git (push)
upstream  git@github.com:original-owner/repo-name.git (fetch)
upstream  git@github.com:original-owner/repo-name.git (push)
```

---

## Step 4: Keep your fork in sync with upstream

Forks can go stale — the original project keeps moving while your copy stands still. When the original repo gets new commits, here's how to catch your fork up:

```bash
git fetch upstream               # download upstream's changes
git switch main                  # be on your main
git merge upstream/main          # merge upstream into your main
git push origin main             # push to your fork
```

Or with rebase for a cleaner history:

```bash
git fetch upstream
git rebase upstream/main
git push --force-with-lease origin main
```

---

## Naming convention

| Remote name | Points to |
|-------------|-----------|
| `origin` | Your fork |
| `upstream` | The original repo |

This is the universal convention. Don't deviate from it — every Git tutorial and every teammate will assume `origin` = your fork, `upstream` = the source.

---

## ✅ Quick recap

- Fork = your own personal copy of someone else's repo, made with one click on GitHub.
- You push to your fork (`origin`) — never directly to the original (`upstream`).
- `git remote add upstream <url>` — lets you pull in the original's new commits later.
- Contributing back happens via a pull request (next module).
