# Task: Create and Resolve a Merge Conflict

You'll deliberately create a conflict, then resolve it yourself.

## Steps

1. Make sure you're on `main` with at least one commit. The file `app.py` should exist.

2. Create a feature branch:

```bash
git switch -c feature/change-port
```

3. On the feature branch, change the port in `app.py` from `8080` to `9090`. Stage and commit:

```bash
vi app.py
# Change: port=8080 → port=9090
git add app.py
git commit -m "Change port to 9090 for staging"
```

4. Switch back to `main` and change the same line to a DIFFERENT value (`3000`):

```bash
git switch main
vi app.py
# Change: port=8080 → port=3000
git add app.py
git commit -m "Change port to 3000 for prod"
```

5. Try to merge the feature branch:

```bash
git merge feature/change-port
```

Git should report a conflict.

6. See what's conflicting:

```bash
git status
```

7. Open `app.py` in `vi` and find the conflict markers. Decide: keep `9090` or `3000`? (Or something else.) Resolve it.

8. Mark as resolved and commit:

```bash
git add app.py
git commit
```

9. View the final result:

```bash
git log --oneline --graph --all
```

---

## What do you see? What does it mean?

- What exactly did the conflict markers look like in the file?
- Which version did you keep and why?
- What does the merge commit look like in the graph?
