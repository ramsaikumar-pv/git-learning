# Staging and Commits 🌱

## 📖 In plain words

This module puts the three zones from the last lesson into action. In short:

1. You edit a file (**Working Directory**).
2. You tell Git "include this in my next save" using `git add` (**Staging Area**).
3. You actually save it with `git commit` (**Repository**) — permanently, forever.

Ram's own analogy is a great one to hold onto: the staging area is like a photographer arranging a shot before clicking the shutter 📸. You don't have to photograph everything in the room — just what you want in the frame. Same with Git: you choose exactly which changes go into each commit.

---

## The three-zone model

```
Working Directory   →   Staging Area (Index)   →   Repository
  (edit files)          (git add)                  (git commit)
```

- **Working Directory**: your normal filesystem. Edit freely, nothing is tracked yet.
- **Staging Area**: a preview of what the next commit will contain. Nothing is permanent yet — you can still change your mind.
- **Repository**: the commit is saved for good, with a unique ID (hash) attached. Permanent, unless you deliberately rewrite history later (an advanced topic).

---

## Stage a file

```bash
git add app.py          # stage one file
git add config.yaml     # stage another
git add .               # stage everything that changed
```

Important beginner gotcha: `git add` does **not** save anything permanently — it just moves a copy of the file's current state into the staging area, like putting it in the camera's frame. If you keep editing the file *after* `git add`, those newer edits aren't staged yet — you'd need to run `git add` again to include them.

---

## Check what's staged

```bash
git status
```

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   app.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   config.yaml
```

Read this output carefully. Git is telling you:
- `app.py` is staged (will go into the next commit)
- `config.yaml` was modified but not staged yet

---

## Commit the staged snapshot

```bash
git commit -m "Add initial app and config"
```

```
[main (root-commit) a3f9d12] Add initial app and config
 1 file changed, 10 insertions(+)
```

The `a3f9d12` is the commit hash — think of it as a fingerprint 🔍 for this exact snapshot. No two commits ever get the same one.

---

## Write good commit messages

Bad: `git commit -m "fix"`
Good: `git commit -m "Fix null pointer in login handler"`

The rule: finish the sentence "If applied, this commit will ___". Your message completes that blank.

---

## Unstage a file

Changed your mind? Remove something from the staging area without losing edits:

```bash
git restore --staged config.yaml
```

This only removes it from staging — your file edits are still there.

---

## The cycle repeats

```
edit → git add → git commit → edit → git add → git commit
```

Every commit is a checkpoint you can return to, like a save point in a video game. This loop — edit, stage, commit — is what you'll do dozens of times a day once this becomes second nature.

---

## ✅ Quick recap

- `git add <file>` — stage a file (preview it for the next commit). Not saved yet.
- `git status` — see what's staged vs. not staged.
- `git commit -m "message"` — permanently save the staged snapshot.
- `git restore --staged <file>` — undo a stage, keep your edits.
