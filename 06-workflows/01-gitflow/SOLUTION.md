# Solution

## Final graph: `git log --oneline --graph --all`

```
*   h3p9q1r (HEAD -> develop) Merge hotfix/1.0.1 into develop
|\
| *   g2o8p0q (tag: v1.0.1, main) Hotfix 1.0.1
| |\
| | * f1n7o9p (hotfix/1.0.1 was here) fix: prevent crash on empty msg
| |/
* |   e0m6n8o Merge release/1.0 into develop
|\ \
| * | d9l5m7n (tag: v1.0, main~1) Release 1.0
| |\|
| | * c8k4l6m fix: validate notification message
| |/
| * b7j3k5l (was feature/add-notifications) feat: add notification function
|/
* a6i2j4k (main base) Initial commit
```

That graph looks complex — that's Gitflow. Every merge creates a visible record of every integration event.

## Why hotfix merges into both

If you only merge the hotfix into `main`:
- `main` is fixed (production is fine)
- `develop` still has the bug

The NEXT release will reintroduce the bug because `develop` is the source for releases. You'd be shipping a known bug again.

Always: hotfix → `main` (fix prod) + hotfix → `develop` (fix the future).

## What if you forget the develop merge

`develop` won't have the hotfix. Next release branch from `develop` won't include the fix. When that release merges to `main`, the previously fixed bug reappears. This is called a regression.

## Tags in the graph

`git log --graph --all` shows tags like `(tag: v1.0, main)` next to the commits they point to. After the workflow, running `git tag` shows `v1.0` and `v1.0.1` — the release history is captured in Git's tag objects.
