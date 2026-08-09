# Challenge

## Challenge 1: Multiple remotes

A repo can have multiple remotes. Add a second remote:

```bash
git remote add backup git@github.com:ramsaikumar-pv/my-project-backup.git
git remote -v
```

Push to both:
```bash
git push origin main
git push backup main
```

When would you have multiple remotes? (Think: a fork scenario, or mirroring a repo.)

---

## Challenge 2: Push a non-main branch

```bash
git switch -c feature/experiment
echo "test" >> notes.txt
git add notes.txt
git commit -m "Experiment"
git push origin feature/experiment
```

Go to GitHub. Can you see the new branch? What options does GitHub show you for that branch?

---

## Challenge 3: Simulate a diverged history

1. Make a commit on your local `main`.
2. Make a DIFFERENT commit on GitHub (edit a file directly).
3. Try `git push` — it will fail. Read the error.
4. `git pull` — what merge strategy does Git use?
5. Push again.

This is the most common daily Git situation in a team: local and remote diverged, pull first then push.

---

## Bonus: `git push --force-with-lease`

Research the difference between `git push --force` and `git push --force-with-lease`. Which is safer and why? When would you need either one? (Hint: think about rebasing a branch you've already pushed.)
