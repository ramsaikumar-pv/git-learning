# Task: Push to GitHub and Pull Changes

You'll need a GitHub account and your SSH key set up (you've already done this).

## Part 1: Push a local repo to GitHub

1. On GitHub.com, create a new empty repository (no README, no .gitignore — completely empty).

2. Copy the SSH URL: `git@github.com:ramsaikumar-pv/your-repo-name.git`

3. In your local practice repo, add the remote:

```bash
git remote add origin git@github.com:ramsaikumar-pv/your-repo-name.git
git remote -v
```

4. Rename your default branch to `main` if it isn't already:

```bash
git branch -M main
```

5. Push:

```bash
git push -u origin main
```

Go to GitHub — refresh the page. Do you see your commits?

---

## Part 2: Simulate a pull

1. On GitHub, click on a file, click the pencil (edit) icon, make a small change, and commit it directly on GitHub.

2. Back in your terminal, check what's new:

```bash
git fetch origin
git log --oneline --graph origin/main
```

3. Pull the change:

```bash
git pull
```

4. Verify:

```bash
git log --oneline
cat <the file you edited>
```

---

## Part 3: Clone a repo

Clone any public repo you like — your own, or a small one you're familiar with:

```bash
git clone git@github.com:ramsaikumar-pv/your-repo-name.git cloned-copy
ls cloned-copy
cd cloned-copy
git remote -v
git log --oneline -5
```

---

## What do you see? What does it mean?

- After `git push -u`, what does `git remote -v` show?
- What does `git fetch` vs `git pull` do differently?
- In the cloned repo, what is the remote called and where does it point?
