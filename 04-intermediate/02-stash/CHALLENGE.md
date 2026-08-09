# Challenge

## Challenge 1: Stash on a feature branch, pop on main

1. On a feature branch, make some changes and stash them.
2. Switch to `main`.
3. Pop the stash there.

Does the stash work across branches? Are your changes now applied to `main`? What are the risks of doing this?

---

## Challenge 2: Stash only part of your changes

You've changed both `app.py` and `config.yaml`. You want to stash only the `config.yaml` changes and keep working on `app.py`.

```bash
git stash push -m "config changes only" config.yaml
```

Run `git status` and `git stash list` after. What happened to `app.py`? Is `config.yaml` in the stash?

---

## Challenge 3: Create a branch from a stash

Git can create a branch directly from a stash entry — useful when you realise your "quick stashed change" should actually be a proper feature branch:

```bash
git stash branch feature/from-stash stash@{0}
```

This creates the branch, checks it out, and applies the stash. If there are no conflicts, it also drops the stash. Run `git log --oneline` and `git status` afterwards.

---

## Bonus: Stash only staged changes

```bash
git stash push --staged
```

This stashes only what you've staged, leaving unstaged changes in the working directory. When would this be useful? (Think: you staged a clean change but also have dirty debug edits you want to keep visible while you switch context.)
