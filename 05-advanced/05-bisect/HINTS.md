# Hints

<details>
<summary>Hint 1 — I lost track of which commit I'm testing during bisect — how do I check?</summary>

```bash
git bisect log        # full log of all good/bad markings so far
git bisect visualize  # opens gitk (if installed) to show the remaining candidates
```

Or simply:
```bash
git log --oneline -1   # what commit am I on right now?
```

Git also prints the current commit info and how many steps remain after each `good`/`bad` marking.

</details>

<details>
<summary>Hint 2 — Bisect checked out a commit and now my files look wrong — am I on a branch?</summary>

No — bisect puts you in detached HEAD state at each test commit. This is normal. Your files will reflect that historical commit's state. After `git bisect reset`, you go back to the branch you started on.

Don't commit anything during bisect (unless you specifically need to). Just test and mark good/bad.

</details>

<details>
<summary>Hint 3 — How do I automate the testing so I don't have to manually mark good/bad?</summary>

Write a test script that exits 0 if the bug is absent, non-zero if present:

```bash
# test-for-bug.sh
#!/bin/bash
if grep -q "BUG_INTRODUCED" notes.txt; then
    exit 1   # bug found = bad commit
fi
exit 0       # no bug = good commit
```

Then:
```bash
git bisect start
git bisect bad HEAD
git bisect good <hash>
git bisect run bash test-for-bug.sh
```

Git automatically runs the script on each candidate commit and marks it good or bad. It finds the culprit without any manual steps.

</details>
