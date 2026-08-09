# Solution

## After step 5: `git log --oneline --graph --all`
```
* c8f2g4b (HEAD -> feature/add-logging) Add logging configuration
* b7e1f3a (main) Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

`HEAD` is on `feature/add-logging`. The new commit is ahead of `main`. `main` is still pointing at the old commit.

## After step 7: `ls` on `main`
```
app.py  config.yaml  README.md  TASK.md  ...
```

`logging_config.py` is NOT there. When you switched to `main`, Git updated your working directory to match the `main` branch's tree. The file wasn't part of `main`'s last commit, so it's gone from view — but it's safe on the feature branch.

## After step 10: `git log --oneline --graph --all`
```
* c8f2g4b (feature/add-logging) Add logging configuration
* b7e1f3a (HEAD -> main, feature/update-config) Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

Both `main` and `feature/update-config` point to the same commit — `b7e1f3a`. They're both "at" that point. As you commit on `feature/update-config`, it will diverge from `main`.

## Why it works this way

A Git branch is a 41-byte file containing a commit hash. That's it. Creating a branch is O(1) — it doesn't matter how big your repo is. This is why Git branching is so cheap compared to older VCS tools where branching meant copying the entire codebase. Think of it like creating a new symlink in Kubernetes — the underlying object is the same, you're just adding a new name pointing to it.
