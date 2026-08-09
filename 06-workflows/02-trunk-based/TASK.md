# Task: Practice Trunk-Based Development

## Scenario

You're on a team using TBD. You'll make several small commits directly (or via very short branches) and implement a feature flag.

## Steps

1. Make sure you're on `main` with a clean working tree.

2. Make a direct small commit to `main` (TBD-style):

```bash
echo "# updated log format" >> app.py
git add app.py
git commit -m "chore: update log format comment"
```

3. Create a short-lived branch for a slightly larger change:

```bash
git switch -c short/add-feature-flags
```

4. Add a feature flags module:

```bash
cat > feature_flags.py << 'EOF'
FEATURE_FLAGS = {
    "new_metrics_endpoint": False,
    "enhanced_logging": True,
}

def is_enabled(flag_name: str) -> bool:
    return FEATURE_FLAGS.get(flag_name, False)
EOF
git add feature_flags.py
git commit -m "feat: add feature flags module"
```

5. Add usage in `app.py`:

```bash
echo "# TODO: use feature_flags.is_enabled() here" >> app.py
git add app.py
git commit -m "chore: note where to use feature flags"
```

6. Squash merge back to `main` immediately (< 1 day branch lifetime):

```bash
git switch main
git merge --squash short/add-feature-flags
git commit -m "feat: add feature flags module with usage notes"
git branch -d short/add-feature-flags
```

7. Run `git log --oneline -5`. Notice: the two feature branch commits became one clean squash commit.

8. Now toggle the feature flag:

```bash
vi feature_flags.py
# Change: "new_metrics_endpoint": False  →  True
git add feature_flags.py
git commit -m "feat(flag): enable new_metrics_endpoint for all users"
```

This is a "flag flip" — the code was already deployed, now you're enabling the feature.

---

## What do you see? What does it mean?

- How does the `git log` graph look in TBD vs the Gitflow graph you made?
- What's the difference between "deploying code" and "releasing a feature" in TBD?
- Why is CI mandatory for TBD but optional for Gitflow?
