# Task: Explore What Git Tracks

You won't run Git commands yet — this exercise is about *observing* Git from the outside so you understand what you're working with before you touch it.

## Steps

1. Open a terminal and navigate to this module directory:

```bash
cd git-learning/01-foundations/01-what-is-git
```

2. Look at the files here:

```bash
ls -la
```

You should see: `README.md`, `TASK.md`, `HINTS.md`, `SOLUTION.md`, `CHALLENGE.md`, `notes.txt`.

3. Open `notes.txt` and read it. This is your "working directory" — files you can see and edit.

4. Now go up to the root of the repo and look for the hidden `.git` folder:

```bash
cd ../../..
ls -la
```

Do you see `.git`? That's the Git database — the repository.

5. Peek inside `.git` without modifying anything:

```bash
ls .git/
```

6. Look at the HEAD file:

```bash
cat .git/HEAD
```

7. Now run:

```bash
git log --oneline -5
```

---

## What do you see? What does it mean?

- What is `.git/HEAD` pointing to?
- What does each line in `git log --oneline` represent?
- Can you match a commit hash to the concept of a "snapshot"?

Write your answers in `notes.txt` before moving on.
