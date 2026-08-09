# Task: Clean Up History with Interactive Rebase

## Setup: Create messy history

1. Make a series of messy commits on a feature branch:

```bash
git switch -c feature/cleanup-me

echo "def login(): pass" >> app.py
git add app.py
git commit -m "Add login func"

echo "# TODO: validate input" >> app.py
git add app.py
git commit -m "WIP"

echo "  if not user: raise" >> app.py
git add app.py
git commit -m "Fix login"

echo "# typo fix" >> app.py
git add app.py
git commit -m "fix tyoop"

echo "def logout(): pass" >> app.py
git add app.py
git commit -m "Add logout"
```

2. See the messy history:

```bash
git log --oneline
```

You have 5 commits. The goal: squash them into 2 clean commits.
- Commit 1: "Add login with input validation"
- Commit 2: "Add logout"

## Steps

3. Open interactive rebase for the last 5 commits:

```bash
git rebase -i HEAD~5
```

4. In the editor, change the lines to:

```
pick   <hash1>  Add login func
squash <hash2>  WIP
squash <hash3>  Fix login
squash <hash4>  fix tyoop
pick   <hash5>  Add logout
```

Save and close the file.

5. Git opens another editor for the squashed commit message. Replace everything with:

```
Add login with input validation
```

Save and close.

6. Check the result:

```bash
git log --oneline
```

How many commits are there now?

7. Verify the code is still intact:

```bash
cat app.py
```

---

## What do you see? What does it mean?

- How many commits remain after squashing?
- Did the logout commit keep its original hash?
- What happened to the "WIP", "Fix login", and "fix tyoop" messages?
