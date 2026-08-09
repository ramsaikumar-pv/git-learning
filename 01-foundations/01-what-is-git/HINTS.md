# Hints

<details>
<summary>Hint 1 — Not seeing a .git folder?</summary>

Hidden folders start with a dot. Your shell might hide them by default. Try `ls -la` instead of just `ls`. The `-a` flag shows hidden files and directories.

</details>

<details>
<summary>Hint 2 — HEAD says "ref: refs/heads/main" — what does that mean?</summary>

HEAD is Git's way of saying "you are here." It points to a branch name (like `main`), which itself points to the latest commit on that branch. So HEAD → main → latest commit. It's a pointer to a pointer.

</details>

<details>
<summary>Hint 3 — git log shows nothing or errors?</summary>

If `git log` says "fatal: your current branch 'main' does not have any commits yet", the repo has been initialised but nothing has been committed. That's fine — it means you're in a brand-new repo. Skip step 7 and move on to the next module where you'll make your first commit.

If `git log` errors with "not a git repository", you need to `cd` to the root of `git-learning/` first — that's where `.git/` lives.

</details>
