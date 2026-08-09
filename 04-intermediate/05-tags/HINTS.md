# Hints

<details>
<summary>Hint 1 — git show v1.0 shows too much — how do I just see the tag message?</summary>

```bash
git cat-file -p v1.0
```

This shows the raw tag object — type, tagger, date, and message. To see just the tag message (no diff):

```bash
git show v1.0 --no-patch
```

Or for a list of all tags with their messages:

```bash
git tag -n       # -n shows the first line of each tag's message
git tag -n 5     # shows up to 5 lines
```

</details>

<details>
<summary>Hint 2 — After git checkout v1.0, Git warns about detached HEAD — what can I safely do here?</summary>

In detached HEAD, you can:
- Browse files — completely safe
- Run `git log`, `git diff`, `git show` — safe
- Make experimental commits — these commits aren't on any branch, so if you switch away they'll become unreachable (eventually garbage collected)

If you make commits and want to keep them:
```bash
git switch -c recovery-branch     # creates a branch at current position
```

This saves your work. Then merge it wherever you need.

</details>

<details>
<summary>Hint 3 — I pushed a wrong tag to remote — how do I fix it?</summary>

Delete locally:
```bash
git tag -d v1.0-wrong
```

Delete on remote:
```bash
git push origin --delete v1.0-wrong
```

Recreate correctly:
```bash
git tag -a v1.0 <correct-hash> -m "Correct message"
git push origin v1.0
```

Note: if others have already pulled the wrong tag, they'll need to delete it locally too: `git tag -d v1.0-wrong && git fetch --tags`. Coordinate before deleting remote tags.

</details>
