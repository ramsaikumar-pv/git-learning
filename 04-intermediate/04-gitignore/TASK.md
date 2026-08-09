# Task: Create and Use .gitignore

## Steps

1. Create some files that shouldn't be committed:

```bash
echo "SECRET_KEY=abc123" > .env
echo "some compiled output" > app.pyc
mkdir -p __pycache__ && echo "bytecode" > __pycache__/app.cpython-39.pyc
echo "debug output" > debug.log
```

2. Check `git status` — Git sees all these files as untracked:

```bash
git status
```

3. Create a `.gitignore` file:

```bash
vi .gitignore
```

Add these patterns:
```
.env
*.pyc
__pycache__/
*.log
```

Save and exit.

4. Check `git status` again:

```bash
git status
```

Are the ignored files still showing?

5. Verify a specific file is ignored:

```bash
git check-ignore -v .env
git check-ignore -v debug.log
```

6. Stage and commit the `.gitignore`:

```bash
git add .gitignore
git commit -m "Add gitignore for Python and secrets"
```

7. Now test the "already tracked" problem. Create and commit a file that shouldn't be tracked:

```bash
echo "password=hunter2" > credentials.txt
git add credentials.txt
git commit -m "Oops, committed credentials"
```

8. Add `credentials.txt` to `.gitignore`. Then try to ignore it — notice it's still tracked:

```bash
echo "credentials.txt" >> .gitignore
git status    # still shows as tracked!
```

9. Fix it — untrack the file:

```bash
git rm --cached credentials.txt
git add .gitignore
git commit -m "Stop tracking credentials, add to gitignore"
git status
```

---

## What do you see? What does it mean?

- After step 4, which files disappeared from `git status`?
- After step 8, why was `credentials.txt` still showing even though it was in `.gitignore`?
- What does `git rm --cached` do differently from `git rm`?
