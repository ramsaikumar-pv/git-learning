# Cherry-Pick 🌱

## 📖 In plain words

Merge and rebase both bring over an *entire branch's* worth of commits. Cherry-pick is more surgical: it grabs just one specific commit from anywhere in history and replays it onto your current branch — like picking a single cherry off a tree instead of taking the whole branch.

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

Worth remembering: cherry-pick creates a duplicate commit — same changes, but a brand-new hash. If you later merge the branch you cherry-picked from, you'll end up with both the original commit AND the cherry-picked copy in your log. That's fine occasionally, but confusing if overused — use cherry-pick surgically, not as your default way of moving code around.

---

## ✅ Quick recap

- Cherry-pick = apply one specific commit onto your current branch, not the whole branch.
- `git cherry-pick <hash>` — the new commit has the same changes but a different hash.
- Good for: hotfixes that need to land on a release branch without the rest of a feature.
- Overusing it creates duplicate commits — use sparingly.
