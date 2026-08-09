# Task: Add and Use a Git Submodule

You'll need two repos: your main repo and a small external repo to add as a submodule. Use a public GitHub repo (e.g., a simple utility) or create a second test repo.

## Setup: Create a second repo to use as submodule

1. On GitHub, create a new repo called `my-shared-lib`. Add one file to it:

```bash
# In the my-shared-lib repo:
echo 'def shared_util(): return "from shared lib"' > util.py
git add util.py && git commit -m "Initial shared lib"
git push origin main
```

## Steps

2. Back in your main learning repo, add the shared lib as a submodule:

```bash
git submodule add git@github.com:ramsaikumar-pv/my-shared-lib.git libs/shared
```

3. Check what was created:

```bash
ls libs/
cat .gitmodules
git status
```

4. Commit the submodule:

```bash
git add .gitmodules libs/shared
git commit -m "Add my-shared-lib as submodule"
```

5. Check the submodule status:

```bash
git submodule status
```

6. Clone your repo somewhere else and see what happens to the submodule:

```bash
cd /tmp
git clone git@github.com:ramsaikumar-pv/your-main-repo.git test-clone
cd test-clone
ls libs/shared/    # empty!
```

7. Initialise the submodule:

```bash
git submodule update --init
ls libs/shared/    # now has content
```

8. Back in your main repo, update the submodule to a newer commit (if you add a commit to `my-shared-lib`):

```bash
cd libs/shared
git log --oneline
git fetch
git checkout main
cd ../..
git add libs/shared
git commit -m "Update shared-lib to latest"
```

---

## What do you see? What does it mean?

- What does `.gitmodules` contain?
- In `git log` of the parent repo, what does the submodule show as changed when you update it?
- Why is the submodule directory on "detached HEAD"?
