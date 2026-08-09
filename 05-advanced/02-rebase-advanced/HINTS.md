# Hints

<details>
<summary>Hint 1 — The interactive rebase editor is confusing — how do I edit it in vi?</summary>

In `vi`:
1. Use arrow keys to navigate to the line you want to change
2. Press `0` to go to the start of the line
3. Press `cw` to "change word" — deletes the current word and enters insert mode
4. Type the new command (`squash`, `fixup`, `reword`, etc.)
5. Press `Esc`
6. Repeat for other lines
7. When done: `:wq` to save and close

Alternatively, if `vi` is frustrating, temporarily use a simpler editor:
```bash
GIT_EDITOR=nano git rebase -i HEAD~5
```

</details>

<details>
<summary>Hint 2 — Rebase hit a conflict mid-way — what do I do?</summary>

Git pauses at the conflicting commit. Resolve it normally:

```bash
vi conflicted-file.py     # find and remove conflict markers
git add conflicted-file.py
git rebase --continue
```

If there are more commits to replay, Git may pause again. Repeat until it finishes. If overwhelmed:

```bash
git rebase --abort   # returns to before you started the rebase
```

</details>

<details>
<summary>Hint 3 — After interactive rebase, git push fails — why?</summary>

Your local branch's history was rewritten (new hashes). The remote still has the old hashes. They've diverged. You need to force push:

```bash
git push --force-with-lease origin feature/cleanup-me
```

`--force-with-lease` is safer than `--force`: it fails if the remote has commits you haven't seen (protecting against overwriting someone else's push).

NEVER force push to `main` or any shared branch. Only do this on your own feature branches.

</details>
