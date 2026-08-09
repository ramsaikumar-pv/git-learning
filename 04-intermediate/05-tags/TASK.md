# Task: Tag Commits and Push Tags

## Steps

1. Check your commit history:

```bash
git log --oneline -5
```

2. Create a lightweight tag on the current commit:

```bash
git tag v0.1
```

3. Create an annotated tag for the same or next commit:

```bash
git tag -a v1.0 -m "Release 1.0 — first stable version"
```

4. List all tags:

```bash
git tag
```

5. Inspect both tags:

```bash
git show v0.1
git show v1.0
```

What's different between the two outputs?

6. Tag an older commit (use a hash from step 1):

```bash
git tag -a v0.0.1 <old-hash> -m "Initial alpha — pre-release"
```

7. List tags again. Are they in alphabetical or chronological order?

```bash
git tag
```

8. Push all tags to remote (if you have a remote set up):

```bash
git push origin --tags
```

Go to GitHub → your repo → Tags. Do you see the tags?

9. Delete the lightweight tag locally:

```bash
git tag -d v0.1
git tag
```

10. Make a new commit, then check out the tag:

```bash
echo "# v1.0 release" >> RELEASE_NOTES.md
git add RELEASE_NOTES.md
git commit -m "Add release notes"
git checkout v1.0
git log --oneline -3
```

What does "detached HEAD" mean?

```bash
git switch main    # go back to a branch
```

---

## What do you see? What does it mean?

- What extra information does an annotated tag show vs a lightweight tag?
- Why are tags listed in alphabetical order, not creation order?
- What is "detached HEAD state" and why is it important to know?
