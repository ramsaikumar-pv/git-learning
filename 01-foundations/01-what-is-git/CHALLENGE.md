# Challenge

## Challenge 1: Find the object behind HEAD

Git stores everything in `.git/objects/`. Let's trace HEAD to the actual stored object.

1. Read HEAD: `cat .git/HEAD` → it gives you a ref like `ref: refs/heads/main`
2. Read that ref: `cat .git/refs/heads/main` → it gives you a commit hash
3. Use Git to inspect that object:

```bash
git cat-file -t <hash>    # shows the type (should be "commit")
git cat-file -p <hash>    # shows the content of the commit object
```

What fields does a raw commit object contain? Can you find the `tree` field? What do you think that points to?

---

## Challenge 2: Compare two version control philosophies

Research the difference between **distributed** version control (like Git) and **centralised** version control (like SVN or Perforce).

- In a distributed system, where is the full history stored?
- What happens if the central server goes down?
- Why does this matter for a platform team working across multiple clusters or regions?

Write a 3-sentence answer in `notes.txt`.

---

## Bonus: What's in `.git/objects/`?

List the contents of `.git/objects/`. You'll see two-character subdirectories. Each object's filename is the rest of its SHA-1 hash. Git packs these into packfiles over time for efficiency.

Run `git count-objects -v` to see stats about loose objects vs packed objects.
