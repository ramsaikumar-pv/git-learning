# Trunk-Based Development

Trunk-based development (TBD) is the opposite of Gitflow. Instead of long-lived branches, everyone commits directly to `main` (the "trunk") — or uses very short-lived branches (< 1 day) that merge immediately.

This is how Google, Facebook, and most high-velocity engineering teams work.

---

## Core rules

1. **One shared branch**: everyone works on `main` (or very short-lived branches off it).
2. **Small, frequent commits**: merge at least once a day. Never let a branch live longer than 1-2 days.
3. **CI is mandatory**: automated tests run on every commit. If tests fail, the team stops and fixes immediately.
4. **Feature flags**: if a feature isn't ready to be shown to users, hide it behind a flag — don't use a branch.
5. **Branch protection**: `main` is always deployable. Never merge broken code.

---

## Why it works

Long-lived branches accumulate divergence. The longer a branch lives, the bigger the merge conflict when it lands. TBD eliminates this by keeping branches short and integrating constantly.

The Accelerate book (2018) found that high-performing engineering teams use TBD significantly more than Gitflow. The key enabler: fast CI.

---

## Feature flags

Instead of branching, use flags:

```python
FEATURE_FLAGS = {
    "new_dashboard": False,   # not ready yet
    "dark_mode": True,        # shipped to all
}

if FEATURE_FLAGS["new_dashboard"]:
    render_new_dashboard()
else:
    render_legacy_dashboard()
```

Commit the code to `main` behind the flag. When ready, flip the flag (often via a config change, not a code deployment). This separates "code deployment" from "feature release."

---

## Short-lived branches (for teams not yet ready to commit to trunk directly)

```bash
# branch lives < 24 hours
git switch -c feature/fix-login
# make 1-3 commits
git switch main
git merge --squash feature/fix-login
git commit -m "feat: fix login timeout"
git branch -d feature/fix-login
```

Squash merge keeps `main`'s history clean.

---

## Comparison to Gitflow

| | Gitflow | Trunk-Based |
|---|---------|------------|
| Branch lifetime | Days to weeks | Hours to days |
| Release cadence | Scheduled releases | Continuous delivery |
| CI requirement | Optional | Mandatory |
| Feature hiding | Not built in | Feature flags |
| Merge conflicts | Big and rare | Small and frequent |
| Team size | Works for any size | Scales best with CI culture |
