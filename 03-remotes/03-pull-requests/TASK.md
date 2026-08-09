# Task: Open, Review, and Merge a Pull Request

You need a GitHub repo with your code. Use the one you set up in module 03-01.

## Steps

1. Create a feature branch locally:

```bash
git switch -c feature/add-readme-section
```

2. Edit `README.md` (or any file) — add a new section. Commit it:

```bash
vi README.md
git add README.md
git commit -m "Add architecture overview section to README"
```

3. Make one more commit on the same branch (so your PR has multiple commits):

```bash
echo "Contact: ram@example.com" >> README.md
git add README.md
git commit -m "Add contact info to README"
```

4. Push the branch:

```bash
git push origin feature/add-readme-section
```

5. Go to GitHub. Click the "Compare & pull request" banner (or go to the repo's Pull Requests tab and click "New pull request").

6. Fill in:
   - Title: "Add architecture overview and contact info to README"
   - Description: "This PR adds two new sections to the README that were missing..."
   - Leave it for yourself to review.

7. Open the PR. Browse the "Files changed" tab — do you see your diffs?

8. Leave a review comment on a specific line (click the `+` next to a line number).

9. Approve your own PR and merge it using **Squash and merge**.

10. After merge, delete the branch on GitHub when prompted.

11. Pull the changes locally:

```bash
git switch main
git pull
git log --oneline -3
git branch -d feature/add-readme-section
```

---

## What do you see? What does it mean?

- How many commits does `git log` show after squash merge — 1 or 2?
- What happened to the individual commit messages from your branch?
- Why does "Delete branch" appear on GitHub after merging?
