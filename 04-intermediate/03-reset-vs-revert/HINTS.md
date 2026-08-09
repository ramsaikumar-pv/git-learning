# Hints

<details>
<summary>Hint 1 — git revert opened vi and I'm stuck</summary>

You're editing the revert commit message. The default text is fine. To accept and close:
1. Press `Esc` to exit insert mode
2. Type `:wq` and press Enter

If you want to abort the revert: `:q!` then Enter. The revert is cancelled, no commit is created.

</details>

<details>
<summary>Hint 2 — After reset --soft, my changes are staged but I wanted to commit something else — how do I unstage?</summary>

`git restore --staged <file>` unstages a specific file. Or `git restore --staged .` to unstage everything. The changes go back to the working directory (unstaged) but are not lost.

This is actually a common workflow:
1. Made a commit you realise includes too much
2. `git reset --soft HEAD~1` — uncommit, keep changes staged
3. `git restore --staged <wrong-file>` — unstage what shouldn't be in the commit
4. `git commit -m "refined message"` — commit only what should be

</details>

<details>
<summary>Hint 3 — I used git reset --hard and lost something I wanted. Can I recover it?</summary>

Yes, usually. `git reflog` records every move HEAD makes, including resets. Run:

```bash
git reflog
```

Find the commit hash from before the reset. Then:

```bash
git checkout <hash>        # detached HEAD — just looking
# or
git reset --hard <hash>    # restore to that point
# or
git cherry-pick <hash>     # apply that commit on top of current HEAD
```

This is exactly why module 05-06 covers reflog — it's your safety net for `git reset --hard`.

</details>
