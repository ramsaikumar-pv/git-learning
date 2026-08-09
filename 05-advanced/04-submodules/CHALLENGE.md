# Challenge

## Challenge 1: Update all submodules at once

If you have multiple submodules:

```bash
git submodule update --remote --merge
```

`--remote` fetches the latest from each submodule's tracked branch (instead of the pinned commit). `--merge` merges it into your local submodule checkout. 

After running this, `git status` will show changed submodules. Commit them to update the pinned versions in the parent repo.

When would you use `--remote` vs just the standard `update`?

---

## Challenge 2: Remove a submodule

Removing a submodule requires several steps:

```bash
git submodule deinit libs/shared          # unregisters the submodule
git rm libs/shared                         # removes the gitlink and directory
rm -rf .git/modules/libs/shared           # removes the cached submodule repo
```

Then commit the removal. Verify `.gitmodules` no longer contains the entry.

---

## Challenge 3: Nested submodules

A submodule can itself have submodules. Clone a repo that has nested submodules:

```bash
git clone --recurse-submodules <url>
```

The `--recurse-submodules` flag handles all levels of nesting. Check what `git submodule status --recursive` shows.

In practice: nested submodules become very difficult to manage. This is one reason many teams move away from submodules toward proper package management.

---

## Bonus: Compare submodules to git subtree

`git subtree` is an alternative to `git submodule` that doesn't require special init steps after cloning. Research the difference:

- Submodules: pointer to external repo, external history separate
- Subtrees: external code merged directly into your repo tree, history combined

Which would you use for a shared Kubernetes operator that multiple teams depend on?
