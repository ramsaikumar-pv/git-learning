# Solution

## Part 1: Fast-forward merge output

```
Updating b7e1f3a..c8f2g4b
Fast-forward
 app.py | 1 +
 1 file changed, 1 insertion(+)
```

The word `Fast-forward` in the output confirms it. Git moved the `main` pointer forward to the feature branch's tip. No merge commit was created.

## Part 1: Log after fast-forward

```
* c8f2g4b (HEAD -> main) Add health endpoint
* b7e1f3a Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

Perfectly linear. No branching visible in the graph.

## Part 2: 3-way merge output

```
Merge made by the 'recursive' strategy.
 app.py | 1 +
 1 file changed, 1 insertion(+)
```

The phrase `recursive strategy` (or `ort` in newer Git versions) confirms a 3-way merge. A merge commit was created.

## Part 2: Log after 3-way merge

```
*   e4c1f8a (HEAD -> main) Merge branch 'feature/add-metrics'
|\
| * d9h3i5c (feature/add-metrics) Add metrics endpoint
* | f1e7c09 Add prod comment to config
|/
* c8f2g4b Add health endpoint
* b7e1f3a Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

The `|\` shows the fork, `|/` shows the rejoin. The `*` on the top line with two parents (`|` lines connecting to it) is the merge commit.

## Why fast-forward happens

Git checks: "Is the tip of the branch I'm merging a direct descendant of my current HEAD?" If yes → fast-forward. If no (branches diverged) → 3-way merge using the common ancestor as the base.

## git branch -d vs -D

`-d` is "safe delete" — it refuses if the branch contains commits not yet merged into the current branch. This prevents you from accidentally losing work. `-D` forces the delete regardless. Use `-D` only when you're sure you want to discard the unmerged commits.
