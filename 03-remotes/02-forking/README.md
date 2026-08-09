# Forking

A fork is a copy of someone else's repo, living under your GitHub account. It lets you experiment and contribute without write access to the original.

Infrastructure analogy: forking is like vendoring a community operator into your own org namespace. You take the upstream code, customise it for your needs, and can still track the original for updates.

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

You push to your fork. The original (`upstream`) only receives changes when you open a pull request.

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

By default, `origin` points to YOUR fork. Add the original as a second remote:

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

When the original repo gets new commits, sync them to your fork:

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

This is the universal convention. Don't deviate from it.
