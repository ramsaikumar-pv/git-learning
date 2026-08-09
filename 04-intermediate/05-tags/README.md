# Tags

Tags are named bookmarks for specific commits. Where branches move forward as you add commits, tags stay fixed — they mark a commit forever. Use them to label releases.

In platform terms: tags are like release manifests. `v1.2.3` on a commit is the contract that says "this is what's running in prod."

---

## Two types of tags

### Lightweight tag

Just a pointer to a commit. No extra info. Like a branch that never moves.

```bash
git tag v1.0
```

### Annotated tag (preferred for releases)

A full Git object with a message, author, and date. Can be GPG-signed.

```bash
git tag -a v1.0 -m "Release 1.0 — initial stable release"
```

Use annotated tags for anything that matters. Use lightweight for quick local bookmarks.

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

This puts you in "detached HEAD" state — you're looking at the tagged commit but not on any branch. Safe for inspecting; dangerous for committing (commits won't belong to any branch). To work on a release, create a branch from the tag:

```bash
git switch -c hotfix/v1.0-patch v1.0
```
