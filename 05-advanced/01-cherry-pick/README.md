# Cherry-Pick

Cherry-pick applies a specific commit from one branch onto another branch. You're not merging the whole branch — you're picking one commit and replaying it.

The analogy: you have 10 Helm chart changes across a feature branch. Prod needs just one of them right now — a critical timeout fix. Cherry-pick lets you apply just that one commit to the release branch without bringing everything else.

---

## The command

```bash
git cherry-pick a3f9d12
```

Git takes the changes introduced by commit `a3f9d12` and applies them as a new commit on your current branch. The new commit has a different hash but the same changes.

---

## Multiple commits

```bash
git cherry-pick a3f9d12 b7e1f3a   # pick two specific commits
git cherry-pick a3f9d12..b7e1f3a  # pick a range (exclusive start)
git cherry-pick a3f9d12^..b7e1f3a # pick a range (inclusive start)
```

---

## Cherry-pick with conflicts

If the cherry-picked changes conflict with the target branch:

```bash
# Git pauses with conflict markers
vi conflicted-file.py   # resolve
git add conflicted-file.py
git cherry-pick --continue
```

To abort:
```bash
git cherry-pick --abort
```

---

## The `--no-commit` flag

Apply the changes to the working directory and staging area WITHOUT creating a commit:

```bash
git cherry-pick --no-commit a3f9d12
git status      # changes are staged, not committed
git diff --staged  # review what you're about to commit
git commit -m "Custom message for this pick"
```

Useful when you want to combine multiple cherry-picks into one commit.

---

## When to use cherry-pick

| Scenario | Use cherry-pick? |
|----------|----------------|
| Hotfix from main needed on a release branch | Yes |
| Single bug fix from a feature branch that's not ready to merge | Yes |
| Moving ALL commits from one branch to another | No — use merge or rebase instead |
| Duplicating commits frequently | No — signals a workflow problem |

Cherry-pick creates duplicate commits (same changes, different hashes). If you later merge the source branch, you'll get the original commit AND the cherry-pick. This can cause confusion in the log. Use it surgically.
