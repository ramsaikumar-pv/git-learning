# Conflict Resolution 🌱

## 📖 In plain words

A merge conflict is Git pausing mid-merge and saying "you decide!" 🤷 — it happens when two branches changed the *exact same lines* of the *exact same file*, in different ways. Git is smart enough to auto-combine most changes, but if two people edited the same spot, there's no safe guess to make. So it stops and hands the decision to you.

This isn't an error, and it isn't something to be afraid of — it's completely normal, and you've already resolved one yourself. This module puts a name to what you already did.

---

## What triggers a conflict?

```
Branch main:    line 5 says: port = 8080
Branch feature: line 5 says: port = 9090
```

Both branches changed line 5, but to different values. There's no rule Git can apply to guess which one you actually want — only a human knows which is correct. So Git marks the spot and waits for you.

---

## What Git inserts when there's a conflict

When this happens, Git doesn't just show an error — it edits the file itself, inserting special marker lines around the disagreement so you can see both versions side by side:

```python
<<<<<<< HEAD
port = 8080
=======
port = 9090
>>>>>>> feature/update-port
```

- `<<<<<<< HEAD` — the start marker. Everything below this, down to the `=======` line, is what **your current branch** has.
- `=======` — the dividing line between the two versions.
- `>>>>>>> feature/update-port` — the end marker. Everything above this, up from `=======`, is what the **incoming branch** has.

Your job: decide what the file *should* say — maybe one side, maybe the other, maybe a mix of both — then delete all three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) along with whichever version you're not keeping. Nothing about this is automatic; Git just shows you the disagreement clearly.

---

## Resolving the conflict

1. Open the file in `vi`
2. Find the conflict markers (search with `/<<<`)
3. Decide what the file should contain
4. Delete all three marker lines and the version you're not keeping
5. Save the file

Then:

```bash
git add app.py        # mark as resolved
git commit            # seal the merge
```

If you're mid-rebase instead of mid-merge:
```bash
git add app.py
git rebase --continue
```

---

## Abort if you're stuck

Changed your mind? Don't want to resolve right now?

```bash
git merge --abort    # during a merge
git rebase --abort   # during a rebase
```

This takes you back to the state before you started. Nothing is lost.

---

## Check for remaining conflicts

After resolving, always run:

```bash
git status
git diff
```

`git status` shows you which files still have conflicts. If there are none, proceed with `git add` and `git commit`.

---

## Visualise the merge after resolution

```bash
git log --oneline --graph --all
```

You should see the merge commit with two parent lines joining into one. That's the resolved conflict, committed.

---

## ✅ Quick recap

- A conflict = two branches edited the same lines differently. Git can't guess, so it asks you.
- Git marks the spot with `<<<<<<<`, `=======`, `>>>>>>>` — delete all three, keep only what you want.
- `git add <file>` then `git commit` (or `git rebase --continue`) to finish.
- `git merge --abort` / `git rebase --abort` — bail out and go back to before you started, no harm done.
