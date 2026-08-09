# Hints

<details>
<summary>Hint 1 — After creating .gitignore, the files are still showing in git status</summary>

Check that:
1. The `.gitignore` file is in the right place (repo root, same level as `.git/`)
2. Your patterns are correct — a trailing slash means "directory," no trailing slash means "file or directory"
3. The files aren't already tracked (committed)

Test a specific file: `git check-ignore -v <filename>`. If it says nothing, that file isn't matched by any pattern. Review your `.gitignore` pattern carefully. A common mistake: putting a `/` before the pattern makes it root-relative only.

</details>

<details>
<summary>Hint 2 — I accidentally committed .env — how do I remove it from ALL of history?</summary>

`git rm --cached .env` removes it from future commits, but the file remains in previous commits' history. If the secret was sensitive:

1. Rotate the secret immediately (invalidate the old one) — this is step 1 regardless of what else you do.
2. Use `git filter-repo` (or the older `BFG Repo Cleaner`) to rewrite history and remove the file from all commits.
3. Force push (if shared, coordinate with your team).

For a local-only repo, history rewriting is fine. For shared repos, this is disruptive. The real lesson: set up `.gitignore` BEFORE you `git init`. Secrets in git history are considered permanently leaked.

</details>

<details>
<summary>Hint 3 — git rm --cached deleted my file from disk — how do I get it back?</summary>

`git rm --cached` should NOT delete the file from disk — it only removes it from Git's index (tracking). If your file disappeared, you may have run `git rm` (without `--cached`), which deletes both from tracking AND from disk.

Recover with:
```bash
git show HEAD:credentials.txt > credentials.txt    # restore from last commit
```

Or if not committed yet: the file may be in trash/recycle bin.

Always use `--cached` when you want to untrack but keep the local file.

</details>
