# Hints

<details>
<summary>Hint 1 — I can't find the conflict markers in the file — where are they?</summary>

In `vi`, search for them:
- Press `/` then type `<<<<` and press Enter
- Press `n` to jump to the next conflict marker

If there are multiple conflicts in one file, repeat `n` to find them all. You must resolve every single conflict block before Git will let you complete the merge.

</details>

<details>
<summary>Hint 2 — I resolved the conflict but git status still shows the file as conflicted</summary>

You need to stage the file after resolving. Git uses the staging area to track which conflicted files you've resolved:

```bash
git add app.py
git status
```

After `git add`, the file should move from "both modified" to "Changes to be committed." If `git status` still shows other files with conflicts, resolve those too before committing.

</details>

<details>
<summary>Hint 3 — I accidentally left a conflict marker in the file and committed. How do I fix it?</summary>

Make a new commit that removes the marker:

```bash
vi app.py            # remove the stray marker
git add app.py
git commit -m "Fix leftover conflict marker"
```

Or amend the last commit (if you haven't pushed):

```bash
vi app.py
git add app.py
git commit --amend --no-edit
```

Lesson: always run `git diff` before committing to check your changes look sane.

</details>
