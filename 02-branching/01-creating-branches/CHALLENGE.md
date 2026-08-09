# Challenge

## Challenge 1: Branch from a specific commit (not HEAD)

Create a branch starting from a specific past commit — not the latest one:

```bash
git log --oneline           # find a commit hash from a few commits back
git switch -c hotfix/old-base <hash>
git log --oneline --graph --all
```

Where does this new branch start? What would you use this for in a real workflow? (Think: hotfix on an older release.)

---

## Challenge 2: Rename a branch

You named a branch badly. Rename it without losing any commits:

```bash
git branch -m feature/add-logging feature/structured-logging
git branch
```

Did the commits on that branch survive the rename?

---

## Challenge 3: Track branch divergence

1. On `main`, create a commit.
2. On `feature/structured-logging`, create a different commit.
3. Run `git log --oneline --graph --all`.

Draw the graph on paper (or in `notes.txt`) — two paths diverging from a common ancestor. This is what branches look like before merging.

---

## Bonus: What's the difference between `git checkout -b` and `git switch -c`?

Both create and switch to a new branch. `git checkout -b` is the old way; `git switch -c` is the modern way (added in Git 2.23). The `switch` command only deals with branches, making its intent clear. `checkout` does too many things (switches branches, restores files). Try both and see that they work the same. Prefer `switch` going forward.
