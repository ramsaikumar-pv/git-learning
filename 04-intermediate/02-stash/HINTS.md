# Hints

<details>
<summary>Hint 1 — git stash pop says "No stash entries found"</summary>

You don't have any stashes saved. Either:
- You didn't run `git stash` (or `git stash push`) yet
- You already popped all of them

Run `git stash list` to see what's saved. If empty, go back to step 3 and stash something first.

</details>

<details>
<summary>Hint 2 — I lost my stash — can I recover it?</summary>

Yes, sometimes. Git stash objects are stored in the object database. Even after `git stash drop`, the objects may still be there for a while. Try:

```bash
git fsck --unreachable | grep commit | cut -d" " -f3 | xargs git log --merges --no-walk --oneline
```

Or more practically, use `git reflog` (module 05-06) which records every stash creation. In a pinch: `git stash show -p stash@{0}` before dropping shows you what you're about to lose.

Prevention: always name your stashes (`git stash push -m "name"`) so you know what's in them before applying.

</details>

<details>
<summary>Hint 3 — git stash pop failed with a conflict — what now?</summary>

Stash pop conflicts happen when the branch has changed since you stashed and the conflicting lines can't auto-merge. Git leaves conflict markers in the file:

```bash
vi app.py              # resolve the conflict markers
git add app.py         # mark resolved
git stash drop         # stash pop already failed, so the stash is still there — drop it manually
```

Note: unlike `git merge --abort`, there's no `git stash pop --abort`. Resolve the conflict and drop the stash manually.

</details>
