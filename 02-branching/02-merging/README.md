# Merging

You've done your work on a feature branch. Now you want those changes in `main`. That's merging — bringing two branches back together.

Git has two merge strategies. Which one it uses depends on the shape of the commit graph.

---

## Fast-forward merge

If `main` hasn't moved since you branched off, Git doesn't need to create a merge commit. It just moves the `main` pointer forward to where your branch is:

```
Before:
  main → a3f9d12
  feature/login → c8f2g4b → d9h3i5c

After fast-forward:
  main → d9h3i5c   (same as feature/login)
  feature/login → d9h3i5c
```

No new commit is created. History stays linear. This is called a fast-forward because Git "fast-forwards" the pointer.

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

If `main` has moved on while you were working (someone else committed to it, or you committed to it yourself), Git can't just move the pointer. It needs to create a **merge commit** that has two parents:

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

That's the graph Ram called "beautiful." The `|\ ` and `|/` show the fork and rejoin.

---

## After merging: clean up

```bash
git branch -d feature/login
```

The branch pointer is deleted. The commits are still in history — they're still reachable through the merge commit.
