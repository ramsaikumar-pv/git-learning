# Staging and Commits

You know Ram's analogy: the staging area is like a photographer arranging a shot before clicking the shutter. You don't have to photograph everything in the room — just what you want in the frame.

---

## The three-zone model

```
Working Directory   →   Staging Area (Index)   →   Repository
  (edit files)          (git add)                  (git commit)
```

- **Working Directory**: your normal filesystem. Edit freely.
- **Staging Area**: a preview of what the next commit will contain. Nothing is permanent yet.
- **Repository**: the commit is saved. SHA-1 hash assigned. Permanent (unless you explicitly rewrite history).

---

## Stage a file

```bash
git add app.py          # stage one file
git add config.yaml     # stage another
git add .               # stage everything that changed
```

`git add` does NOT save anything permanently. It moves a snapshot of the file into the staging area. If you edit the file again after `git add`, you need to `git add` again.

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

The `a3f9d12` is the commit hash — the fingerprint of this snapshot.

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

Every commit is a checkpoint. You can go back to any of them.
