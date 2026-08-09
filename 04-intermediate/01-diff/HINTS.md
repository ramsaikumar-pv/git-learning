# Hints

<details>
<summary>Hint 1 — git diff shows nothing even though I edited a file</summary>

Two possibilities:
1. You staged the file with `git add` before running `git diff`. Use `git diff --staged` instead — that shows staged changes.
2. The file isn't being tracked yet (new file). `git diff` only works on tracked files. For a new untracked file, add it first: `git add <file>`, then `git diff --staged`.

Check `git status` first — it always tells you the current state clearly.

</details>

<details>
<summary>Hint 2 — The @@ line in the diff — what does it mean?</summary>

`@@ -1,4 +1,5 @@` means:
- `-1,4` — in the OLD file, this hunk starts at line 1 and covers 4 lines
- `+1,5` — in the NEW file, this hunk starts at line 1 and covers 5 lines

The difference (4 → 5 lines) is because one line was added. The `-` and `+` here refer to the files, not additions/removals. Confusingly, the actual added/removed lines use `+` and `-` too — but those appear at the start of each line in the diff body.

</details>

<details>
<summary>Hint 3 — How do I diff between my local branch and the remote?</summary>

```bash
git fetch origin
git diff main origin/main         # local main vs remote main
git diff HEAD origin/main         # current HEAD vs remote main
```

`git fetch` updates your local copy of `origin/main` without merging. Then you can diff against it to see what's different before pulling.

</details>
