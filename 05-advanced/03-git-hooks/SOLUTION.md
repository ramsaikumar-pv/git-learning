# Solution

## pre-commit hook blocking a print statement

After `git add app.py` and `git commit -m "test commit"`:

```
app.py:5:print("debug: got here")

BLOCKED: Found print() statements. Remove before committing.
```

Exit code 1 caused Git to abort. The commit was not created. `git log --oneline` still shows the previous commit — nothing new.

## After removing print and committing:
```
pre-commit: OK
[main a3f9d12] Clean commit without debug
```

The hook's `echo "pre-commit: OK"` appears on the terminal. The commit succeeds because the hook exited 0.

## commit-msg hook blocking a bad message:
```
$ git commit -m "made a change"

BLOCKED: Bad commit message format.
Must start with: feat|fix|docs|chore|refactor|test|ci:
Example: fix: correct timeout handling
```

## commit-msg hook passing a good message:
```
$ git commit -m "chore: test commit msg hook"
[main b7e1f3a] chore: test commit msg hook
```

## Key facts

- Exit code 0 → Git proceeds
- Any non-zero exit code → Git aborts the action
- Hook output goes to the terminal, not the commit log
- Bypass both hooks: `git commit --no-verify -m "..."`

## Why hooks belong to `.git/` and not the repo

`.git/` is not tracked by Git (it's Git's own database). This is intentional — hooks can run arbitrary shell commands, and automatically executing untrusted hooks from a `git clone` would be a massive security risk. By requiring manual setup, you're opting in consciously.

This is why "run `cp hooks/* .git/hooks/` after cloning" appears in many project README files.
