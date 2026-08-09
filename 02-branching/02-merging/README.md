# Merging 🌱

## 📖 In plain words

You've finished your work on a feature branch — your "parallel world" 🌍. Now you want those changes to become part of `main`, the "real" world. That's what merging does: it brings two branches back together into one.

Git picks one of two ways to do this, automatically, depending on what's happened to `main` in the meantime. You don't choose — Git figures out which one applies.

---

## Fast-forward merge

This is the simple case: if nobody else touched `main` while you were working, Git doesn't need to combine anything — it just slides the `main` sticky note forward to where your branch already is. Nothing to reconcile, so no special "merge commit" gets created.

```
Before:
  main → a3f9d12
  feature/login → c8f2g4b → d9h3i5c

After fast-forward:
  main → d9h3i5c   (same as feature/login)
  feature/login → d9h3i5c
```

No new commit is created, and the history stays a simple straight line. It's called a "fast-forward" because Git is just fast-forwarding the `main` label ahead — like skipping to the end of a video, not editing it.

```bash
git switch main
git merge feature/login
```

```
Updating a3f9d12..d9h3i5c
Fast-forward
 app.py | 5 +++++
```

---

## 3-way merge

Now the more common real-world case: `main` moved on while you were away — a teammate merged something else, or you made an extra commit directly on `main`. Git can no longer just slide the pointer forward, because that would throw away the other work. Instead, Git creates a special **merge commit** — a single commit that has *two* parents, stitching both histories together:

```
Before:
  main → f1e7c09
  feature/login → d9h3i5c

After 3-way merge:
  main → e4c1f8a (merge commit with two parents: f1e7c09 and d9h3i5c)
```

```bash
git switch main
git merge feature/login
```

```
Merge made by the 'recursive' strategy.
 login.py | 10 ++++++++++
```

Git opens your editor to write a merge commit message. The default "Merge branch 'feature/login'" is fine.

---

## The merge commit in the log

```
git log --oneline --graph --all
```

```
*   e4c1f8a (HEAD -> main) Merge branch 'feature/login'
|\
| * d9h3i5c (feature/login) Add login handler
| * c8f2g4b Add auth middleware
* | f1e7c09 Fix health check
|/
* a3f9d12 Initial commit
```

That's the graph you called "beautiful" the first time you saw it. The `|\ ` shows the branch splitting off, and `|/` shows it rejoining `main` at the merge commit.

---

## After merging: clean up

```bash
git branch -d feature/login
```

This only removes the sticky-note label `feature/login` — it does **not** delete any commits. All that work is still saved in history, still reachable by walking back through the merge commit. You're just tidying up a label you no longer need.

---

## ✅ Quick recap

- **Fast-forward merge**: `main` hasn't moved — Git just slides the pointer forward. No new commit.
- **3-way merge**: `main` has moved — Git creates a merge commit with two parents, combining both histories.
- `git branch -d <name>` after merging — deletes the label only, not the history.
