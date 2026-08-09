# Git Hooks

Hooks are scripts that Git runs automatically at specific points in its workflow. They live in `.git/hooks/`. They're the closest thing Git has to admission webhooks in OpenShift — pre-flight checks that run before an action completes.

---

## Where hooks live

```bash
ls .git/hooks/
```

```
applypatch-msg.sample   pre-applypatch.sample   pre-rebase.sample
commit-msg.sample       pre-commit.sample       pre-receive.sample
post-commit.sample      prepare-commit-msg.sample update.sample
```

Git ships samples for every hook. To activate one: remove the `.sample` extension and make it executable.

---

## Most useful hooks

| Hook | When it runs | Common use |
|------|-------------|------------|
| `pre-commit` | Before a commit is created | Lint, format check, secret detection |
| `commit-msg` | After you write the commit message | Enforce message format |
| `pre-push` | Before pushing to remote | Run tests |
| `post-commit` | After a commit | Notifications, side effects |
| `post-merge` | After a merge | Install dependencies |
| `pre-rebase` | Before a rebase starts | Safety check |

---

## Create a pre-commit hook

```bash
vi .git/hooks/pre-commit
```

```bash
#!/bin/bash
# Fail if any Python file has debug print statements
if grep -r "print(" *.py; then
    echo "ERROR: Remove debug print() statements before committing"
    exit 1
fi
exit 0
```

Make it executable:

```bash
chmod +x .git/hooks/pre-commit
```

Now try committing with a `print()` in your Python file — Git will refuse.

---

## commit-msg hook: enforce message format

```bash
#!/bin/bash
# Require commit messages to start with a type prefix
MSG=$(cat "$1")
if ! echo "$MSG" | grep -qE "^(feat|fix|docs|chore|refactor|test|ci):"; then
    echo "ERROR: Commit message must start with feat|fix|docs|chore|refactor|test|ci:"
    echo "Example: feat: add login endpoint"
    exit 1
fi
exit 0
```

---

## Hooks are local and not committed

`.git/hooks/` is inside `.git/` — it's NOT tracked by Git. Each developer's hooks are local only. If you want shared hooks, use a tool like Husky (for Node projects) or pre-commit (Python) that manages hooks via a config file that IS committed.

---

## Bypass a hook (emergency only)

```bash
git commit --no-verify -m "Emergency: bypass hooks"
```

This skips all pre-commit and commit-msg hooks. Use only in genuine emergencies — it defeats the whole point of having hooks.
