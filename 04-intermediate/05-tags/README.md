# Tags 🌱

## 📖 In plain words

A tag is a permanent bookmark 🔖 on one specific commit. The key difference from a branch: branches keep moving forward as you add commits, but a tag never moves — once placed, it always points to that exact same commit, forever. That makes tags perfect for marking "this exact point in history was version 1.0."

In platform terms: tags are like release manifests. `v1.2.3` on a commit is the contract that says "this is what's running in prod."

---

## Two types of tags

### Lightweight tag

The simple version: just a label pointing at a commit, nothing more.

```bash
git tag v1.0
```

### Annotated tag (preferred for releases)

The fuller version: it stores extra info too — who created it, when, and a message explaining what this release is. It can even be cryptographically signed to prove authenticity.

```bash
git tag -a v1.0 -m "Release 1.0 — initial stable release"
```

Simple rule: use annotated tags for anything that matters (releases). Use lightweight tags only for quick, throwaway local bookmarks.

---

## List tags

```bash
git tag
git tag -l "v1.*"    # filter by pattern
```

---

## Inspect a tag

```bash
git show v1.0
```

For an annotated tag, you see the tag object (author, date, message) then the commit it points to. For a lightweight tag, you go straight to the commit.

---

## Tag a past commit

```bash
git log --oneline
git tag -a v0.9 a3f9d12 -m "Retroactive beta tag"
```

You can tag any commit in history, not just HEAD.

---

## Push tags to remote

Tags don't push automatically:

```bash
git push origin v1.0       # push one specific tag
git push origin --tags     # push ALL tags
```

---

## Delete a tag

```bash
git tag -d v1.0                        # delete local tag
git push origin --delete v1.0          # delete remote tag
```

---

## Checkout a tag (detached HEAD)

```bash
git checkout v1.0
```

This puts you in what's called "detached HEAD" state — you're looking at the tagged commit, but you're not "on" any branch. It's perfectly safe for just looking around. But if you make new commits here, they won't belong to any branch and can be easy to lose track of. So: fine for inspecting, risky for committing. To actually work on a release, create a proper branch starting from the tag instead:

```bash
git switch -c hotfix/v1.0-patch v1.0
```

---

## ✅ Quick recap

- Tags = permanent bookmarks on a commit. Unlike branches, they never move.
- Lightweight tag — just a pointer. Annotated tag (`-a -m`) — has a message, preferred for releases.
- Tags don't push automatically — use `git push origin --tags`.
- Checking out a tag = "detached HEAD." To work on it, branch off it first.
