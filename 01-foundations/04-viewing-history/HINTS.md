# Hints

<details>
<summary>Hint 1 — git show shows too much — how do I just see the commit message and stats?</summary>

Use `git show --stat <hash>`. This shows the commit metadata plus which files changed and how many lines, without the full diff. For an even shorter view, `git show --name-only <hash>` just lists the filenames that changed.

</details>

<details>
<summary>Hint 2 — What does HEAD → main mean in git log output?</summary>

`HEAD` is Git's pointer to "where you are right now." It points to a branch (`main`), which itself points to the latest commit on that branch. So `HEAD → main → a3f9d12` means: you're on `main`, and the latest commit on `main` is `a3f9d12`. When you make a new commit, `main` advances to the new hash and HEAD follows. Think of HEAD as the cursor in a text editor — it shows your current position.

</details>

<details>
<summary>Hint 3 — git log -p shows too much — how do I navigate it?</summary>

`git log -p` opens in a pager (usually `less`). Use:
- `space` or `f` to go forward a page
- `b` to go back
- `q` to quit
- `/pattern` to search for text
- `n` / `N` to jump to next/previous search hit

If you'd rather not use a pager: `git log -p --no-pager -- app.py`

</details>
