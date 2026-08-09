# Viewing History

Every commit you've ever made is stored. `git log` is how you read that history — the full audit trail.

---

## The default log

```bash
git log
```

```
commit a3f9d12b4e7c8f1d2e3a4b5c6d7e8f9a0b1c2d3e
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 14:30:00 2026 +0530

    Add app entrypoint and initial config
```

Too verbose for daily use. The hash is 40 characters. But you get full author info and timestamp.

---

## One-line format — what you'll actually use

```bash
git log --oneline
```

```
a3f9d12 Add app entrypoint and initial config
b7e1f3a Add version comment to app
```

Short hash (7 chars — enough to be unique in any normal repo) + message. Scan a week of commits in seconds.

---

## Visualise branches

You loved this one when you first saw it:

```bash
git log --oneline --graph --all
```

```
* b7e1f3a (HEAD -> main) Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

With branches it looks like:
```
*   e4c1f8a (HEAD -> main) Merge branch 'feature/login'
|\
| * d3b9a21 (feature/login) Add login handler
| * c2a8b10 Add auth middleware
* | f1e7c09 Fix health check endpoint
|/
* a3f9d12 Initial commit
```

That `--graph` output is Git's commit graph rendered in ASCII. Each `*` is a commit. Lines show parent-child relationships.

---

## Filter the log

```bash
git log --oneline -5                    # last 5 commits only
git log --oneline --author="Ram"        # commits by a specific author
git log --oneline --since="2 weeks ago" # commits in a date range
git log --oneline -- app.py             # commits that touched app.py
```

---

## Inspect a specific commit

```bash
git show a3f9d12
```

Shows the full diff of that one commit: what changed, what was added, what was removed.

---

## Find what changed in a file over time

```bash
git log --oneline -- config.yaml
git log -p -- config.yaml       # -p shows the actual diffs
```

---

## Commit hashes are fingerprints

Every hash is a SHA-1 of the commit's content — author, timestamp, message, parent hash, and the full file tree. Change one byte and the hash changes completely. This is how Git guarantees integrity. You can't tamper with a commit without changing its hash (and all subsequent hashes).

Ram spotted this himself. That's the key insight.
