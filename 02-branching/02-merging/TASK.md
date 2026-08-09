# Task: Merge Branches

You'll create both types of merges in this exercise — fast-forward and 3-way.

## Part 1: Fast-forward merge

1. Make sure `main` has at least one commit. Check:

```bash
git log --oneline
```

2. Create a feature branch:

```bash
git switch -c feature/add-health
```

3. Add a file and commit:

```bash
echo 'def health(): return "OK"' >> app.py
git add app.py
git commit -m "Add health endpoint"
```

4. Switch to `main` — do NOT make any commits here:

```bash
git switch main
```

5. Merge:

```bash
git merge feature/add-health
```

What kind of merge happened? How do you know?

6. Check the log:

```bash
git log --oneline --graph --all
```

7. Delete the merged branch:

```bash
git branch -d feature/add-health
```

---

## Part 2: 3-way merge

1. Create another feature branch:

```bash
git switch -c feature/add-metrics
```

2. Commit something on this branch:

```bash
echo 'def metrics(): return {"requests": 0}' >> app.py
git add app.py
git commit -m "Add metrics endpoint"
```

3. Switch to `main` and make a DIFFERENT commit there:

```bash
git switch main
echo "# Production config" >> config.yaml
git add config.yaml
git commit -m "Add prod comment to config"
```

4. Merge the feature branch into `main`:

```bash
git merge feature/add-metrics
```

Git may open your editor for a merge commit message. Save and close it.

5. View the graph:

```bash
git log --oneline --graph --all
```

---

## What do you see? What does it mean?

- What output tells you a fast-forward happened vs a 3-way merge?
- In the graph, how can you tell which commit has two parents?
- Why does `git branch -d` work after merging but would require `-D` if the branch wasn't merged?
