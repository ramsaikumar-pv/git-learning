# Solution

## Setup: `git log --oneline` on feature branch
```
d9h3i5c (HEAD -> feature/mixed-work) WIP: cache layer sketch
c8f2g4b Add v2 endpoint (experimental)
a7e1f3b Fix connection timeout (was 3s, now 30s)   ← this one
b4d0c2a (main) Previous main commit
```

Note the hash of the bug fix: `a7e1f3b`.

## After `git cherry-pick a7e1f3b` on main

```
[main e5j4k6l] Fix connection timeout (was 3s, now 30s)
 1 file changed, 1 insertion(+)
```

## `git log --oneline` on main
```
e5j4k6l (HEAD -> main) Fix connection timeout (was 3s, now 30s)
b4d0c2a Previous main commit
```

## `git log --oneline --graph --all`
```
* d9h3i5c (feature/mixed-work) WIP: cache layer sketch
* c8f2g4b Add v2 endpoint (experimental)
* a7e1f3b Fix connection timeout (was 3s, now 30s)
| * e5j4k6l (HEAD -> main) Fix connection timeout (was 3s, now 30s)
|/
* b4d0c2a Previous main commit
```

Notice: the bug fix commit appears TWICE in the graph — once on the feature branch (`a7e1f3b`) and once on main (`e5j4k6l`). Same changes, different hashes. If you later merge the feature branch, Git is smart enough to not double-apply the changes (it detects the content is the same), but the duplicate commits will be visible in the log.

## `git show HEAD`
The cherry-picked commit has a new hash `e5j4k6l`. Same diff, same author, same message — but different hash (because the parent is different: it's now main's previous commit, not the feature branch's context).

## The feature branch is untouched
The feature branch still has all three commits. Cherry-pick is non-destructive on the source branch.
