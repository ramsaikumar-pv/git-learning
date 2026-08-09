# Solution

## `git log --oneline -5` after the workflow

```
f5d8e2a (HEAD -> main) feat(flag): enable new_metrics_endpoint for all users
e4c7d1b feat: add feature flags module with usage notes
d3b6c0a chore: update log format comment
c2a5b9c Previous commit
```

Linear. No branches visible. No merge commits. This is TBD's "clean highway" history.

Compare to Gitflow's graph — that was a web of merge commits. TBD (with squash merges) looks like a straight line.

## "Deploying code" vs "releasing a feature"

| | Gitflow | TBD with flags |
|--|---------|---------------|
| Code in main | On release merge | On every commit (behind flag) |
| Feature visible to users | On deploy | On flag flip |
| Rollback | Revert commit or hotfix | Flip the flag back |
| Deploy risk | Large (release branch) | Small (incremental) |

In TBD, you deploy `main` to production multiple times a day. Features hidden behind `False` flags are in production but not visible. When the flag goes `True`, no deployment needed — it's already there. This is called "continuous deployment" when fully automated.

## Why CI is mandatory for TBD

In Gitflow, broken code stays on a feature branch. It never reaches `main` until it's reviewed and merged. Natural gate.

In TBD, broken code goes to `main` immediately. Without automated CI checking every commit, you'd ship broken code to production constantly. CI is the gate that Gitflow's long-lived branches provided manually.

TBD makes the automated tests ESSENTIAL — they're your primary protection mechanism.
