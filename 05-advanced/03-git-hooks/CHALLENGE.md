# Challenge

## Challenge 1: post-commit notification

Create a hook that runs AFTER a successful commit and prints a summary:

```bash
#!/bin/bash
# .git/hooks/post-commit
BRANCH=$(git branch --show-current)
HASH=$(git rev-parse --short HEAD)
MSG=$(git log -1 --format="%s")
echo ""
echo "✓ Committed: [$BRANCH] $HASH — $MSG"
```

Make it executable. Commit something. Does the message appear?

---

## Challenge 2: pre-push hook that runs tests

```bash
#!/bin/bash
# .git/hooks/pre-push
echo "Running tests before push..."
python -m pytest tests/ 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Tests failed. Push aborted."
    exit 1
fi
echo "Tests passed. Pushing..."
exit 0
```

(If you don't have tests, use a simpler check like `python -c "import app"` or `python -m py_compile app.py`.)

Try pushing with a syntax error in `app.py` — does the hook catch it?

---

## Challenge 3: Shareable hooks with core.hooksPath

Move hooks into a tracked directory:

```bash
mkdir hooks
cp .git/hooks/pre-commit hooks/
cp .git/hooks/commit-msg hooks/
git config core.hooksPath hooks
git add hooks/
git commit -m "chore: add shared git hooks"
```

Now when someone clones this repo, running `git config core.hooksPath hooks` activates all the hooks. Document this in a README. Verify the hooks still fire.

---

## Bonus: pre-receive hook (server-side)

Server-side hooks run on the remote server, not locally. The most important is `pre-receive` — it runs on the GitHub/GitLab server when someone pushes. This is how CI systems and protected branches work. Research: why can't you set server-side hooks on github.com? (Hint: look at GitHub Apps and branch protection rules — these are GitHub's replacement for server-side hooks.)
