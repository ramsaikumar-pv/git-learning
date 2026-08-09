# Hints

<details>
<summary>Hint 1 — The hook runs but doesn't block the commit — why?</summary>

Check two things:

1. Is the hook executable? `ls -la .git/hooks/pre-commit` — it should show `-rwxr-xr-x`. If not: `chmod +x .git/hooks/pre-commit`

2. Does the hook exit with a non-zero code on failure? Exit code 0 = success = Git proceeds. Any non-zero exit code = failure = Git aborts. Make sure your script has `exit 1` on the failure path.

3. Is the shebang line correct? First line must be `#!/bin/bash` (or `#!/bin/sh`). Without it, the script may not be interpreted.

Test the hook script independently:
```bash
bash .git/hooks/pre-commit
echo "Exit code: $?"
```

</details>

<details>
<summary>Hint 2 — The commit-msg hook — where does $1 come from?</summary>

When Git calls the `commit-msg` hook, it passes the path to a temporary file containing the commit message as the first argument (`$1`). That's why the hook reads `$(cat "$1")` — it reads the file to get the message. You don't set `$1` yourself; Git provides it automatically.

</details>

<details>
<summary>Hint 3 — How do I share hooks with my team (they're not in Git)?</summary>

Several options:
1. Store hooks in a repo directory (e.g., `hooks/`) and tell people to symlink or copy them manually
2. Use `git config core.hooksPath hooks/` to point Git at a custom hooks directory that IS tracked
3. Use the [pre-commit framework](https://pre-commit.com/) (Python tool) — manages hooks via `.pre-commit-config.yaml`
4. Use Husky (for Node.js projects) — manages hooks via `package.json`

Option 2 is the most Git-native:
```bash
mkdir hooks
cp .git/hooks/pre-commit hooks/pre-commit
git config core.hooksPath hooks
git add hooks/
```

Now `.git/hooks/` is bypassed entirely — Git uses `hooks/` instead, which is tracked and shareable.

</details>
