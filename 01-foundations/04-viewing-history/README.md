# Viewing History 🌱

## 📖 In plain words

Every commit you've ever made is still sitting there, saved. `git log` is simply how you *read* that history back — like scrolling through the "Save" history of a document, except every entry is permanent and has a message explaining what changed.

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

This is too wordy for everyday use — that hash is 40 characters long! But notice it does give you the full picture: who committed, when, and why.

---

## One-line format — what you'll actually use

```bash
git log --oneline
```

```
a3f9d12 Add app entrypoint and initial config
b7e1f3a Add version comment to app
```

This is the version you'll actually use day to day: a short hash (7 characters — still unique enough for any normal-sized project) plus the message. You can scan a week's worth of commits in a few seconds.

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

That `--graph` output is Git's history drawn out as a picture, using plain text characters. Each `*` is one commit. The lines connecting them show which commit came from which — so you can literally see branches split apart and merge back together.

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

## Commit hashes are fingerprints 🔍

Here's the "why" behind those hashes, in plain words: each hash is calculated *from* the commit's content — who made it, when, the message, which commit came before it, and the full state of every file. Change even one letter anywhere in there, and the hash comes out completely different.

This is why hashes are such a reliable fingerprint — nobody can quietly edit a past commit without the hash (and every hash after it) changing too. It's Git's built-in tamper-detection.

---

## ✅ Quick recap

- `git log` — full history (verbose).
- `git log --oneline` — the version you'll use daily.
- `git log --oneline --graph --all` — see branches visually.
- `git show <hash>` — see exactly what one commit changed.
- Hashes are fingerprints — a snapshot's unique, tamper-evident ID.
