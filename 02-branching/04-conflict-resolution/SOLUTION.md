# Solution

## After `git merge feature/change-port`
```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

## `git status` during conflict
```
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   app.py
```

"both modified" = conflict. The file needs manual resolution.

## The conflict markers in `app.py`
```python
def start_server(host="0.0.0.0",
<<<<<<< HEAD
                 port=3000):
=======
                 port=9090):
>>>>>>> feature/change-port
```

`HEAD` is `main` (your current branch = port 3000).
`feature/change-port` is the incoming branch (port 9090).

## After resolving (keeping 9090) and committing
```
[main e4c1f8a] Merge branch 'feature/change-port'
```

## `git log --oneline --graph --all`
```
*   e4c1f8a (HEAD -> main) Merge branch 'feature/change-port'
|\
| * d9h3i5c (feature/change-port) Change port to 9090 for staging
* | f1e7c09 Change port to 3000 for prod
|/
* b7e1f3a Add version comment to app
```

Both branches changed the same line → conflict. You resolved it → merge commit with two parents.

## Why Git can't resolve it automatically

Git's merge algorithms (recursive, ort) look at the common ancestor of both branches and apply changes from each side. When the SAME line was changed by BOTH sides, there's no unambiguous "apply this change" — both changes affect the same location. Git stops and asks you to be the authority.
