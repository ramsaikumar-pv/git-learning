# Task: Create Pre-Commit and Commit-Msg Hooks

## Part 1: pre-commit hook — block debug prints

1. Create the hook:

```bash
vi .git/hooks/pre-commit
```

Paste this content:

```bash
#!/bin/bash
set -e

# Block debug print statements
if grep -rn "print(" *.py 2>/dev/null; then
    echo ""
    echo "BLOCKED: Found print() statements. Remove before committing."
    exit 1
fi

echo "pre-commit: OK"
exit 0
```

2. Make it executable:

```bash
chmod +x .git/hooks/pre-commit
```

3. Test it — add a print statement and try to commit:

```bash
echo 'print("debug: got here")' >> app.py
git add app.py
git commit -m "test commit"
```

What happens?

4. Remove the print statement and commit successfully:

```bash
vi app.py     # remove the print line
git add app.py
git commit -m "Clean commit without debug"
```

---

## Part 2: commit-msg hook — enforce format

5. Create the hook:

```bash
vi .git/hooks/commit-msg
```

```bash
#!/bin/bash
MSG=$(cat "$1")
if ! echo "$MSG" | grep -qE "^(feat|fix|docs|chore|refactor|test|ci):"; then
    echo ""
    echo "BLOCKED: Bad commit message format."
    echo "Must start with: feat|fix|docs|chore|refactor|test|ci:"
    echo "Example: fix: correct timeout handling"
    exit 1
fi
exit 0
```

```bash
chmod +x .git/hooks/commit-msg
```

6. Test with a bad message:

```bash
echo "test" >> app.py
git add app.py
git commit -m "made a change"    # should fail
```

7. Test with a good message:

```bash
git commit -m "chore: test commit msg hook"   # should succeed
```

---

## What do you see? What does it mean?

- What exit code causes Git to abort the commit?
- Where does the hook's output appear — in the commit log or on the terminal?
- Can you bypass both hooks at once? How?
