# Challenge

## Challenge 1: Rebase with a conflict

Create a scenario where rebase encounters a conflict:

1. On `main`, change line 1 of `app.py` to something specific.
2. Create a feature branch from an older commit and also change line 1 of `app.py` differently.
3. Rebase the feature branch onto `main`.

Git will pause with a conflict. Resolve it, `git add`, then `git rebase --continue`.

---

## Challenge 2: Rebase multiple commits

1. Create a feature branch and make THREE commits (A, B, C).
2. Go to `main` and make one commit (D).
3. Rebase the feature branch onto `main`.

Git replays A, B, C on top of D. Run `git log --oneline --graph --all` after. Are all three commits present? Are their hashes the same as before?

---

## Challenge 3: `git pull --rebase`

When you pull from a remote, Git normally does a fetch + merge. This creates a merge commit for every pull where your local has diverged. Use `--rebase` instead:

```bash
git pull --rebase origin main
```

This fetches remote changes and replays your local commits on top — keeping history linear. Set it as the default:

```bash
git config --global pull.rebase true
```

Read the help and decide: would you set this globally? Why or why not?

---

## Bonus: `git rebase --onto`

Research `git rebase --onto`. It lets you rebase a range of commits onto any target — not just the branch tip. Example use case: you branched off a feature branch (not main) and now want to move just your commits onto main directly.

Draw the before/after diagram for this scenario in `notes.txt`.
