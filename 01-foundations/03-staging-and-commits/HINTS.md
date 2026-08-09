# Hints

<details>
<summary>Hint 1 — git status says "nothing to commit, working tree clean" — did I do something wrong?</summary>

No — that means everything in your working directory matches the last commit. Git has nothing new to track. Try editing one of the files (open `app.py` in `vi`, add a line, save and quit with `:wq`), then run `git status` again.

</details>

<details>
<summary>Hint 2 — I staged the wrong file. How do I undo git add without losing my edits?</summary>

Use `git restore --staged <filename>`. This moves the file back out of the staging area but keeps your edits in the working directory. Your changes are not lost — Git just won't include that file in the next commit. Run `git status` to confirm.

</details>

<details>
<summary>Hint 3 — I forgot to write a message and git commit opened vi — how do I get out?</summary>

You're in `vi`. To write a message and commit:
1. Press `i` to enter insert mode
2. Type your commit message on the first line
3. Press `Esc`
4. Type `:wq` and press Enter

To abort the commit entirely (empty message cancels it):
1. Press `Esc`
2. Type `:q!` and press Enter

Git will say "Aborting commit due to empty commit message."

</details>
