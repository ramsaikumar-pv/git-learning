# Hints

<details>
<summary>Hint 1 — After cloning, the submodule directory is empty — how do I fix it?</summary>

```bash
git submodule update --init
```

Or clone with `--recurse-submodules` next time:

```bash
git clone --recurse-submodules <url>
```

Or set it as a global default (convenient if you work with submodule-heavy repos often):

```bash
git config --global submodule.recurse true
```

After this, `git pull` will also update submodules automatically.

</details>

<details>
<summary>Hint 2 — The submodule shows "detached HEAD" — is that a problem?</summary>

No. Submodules always live on a specific commit, not a branch. The parent repo records a commit hash for each submodule — not a branch name. When you run `git submodule update`, Git checks out exactly that commit, putting the submodule into detached HEAD state.

This is by design. If submodules tracked branches, they'd automatically pull in new commits — which would break the pinned-version guarantee. You explicitly update the pinned commit when you're ready.

To work on the submodule itself (add commits), switch it to a branch first:
```bash
cd libs/shared
git switch main
# make changes, commit, push
cd ../..
git add libs/shared   # update the pinned commit in parent repo
```

</details>

<details>
<summary>Hint 3 — `git diff` shows a weird "Subproject commit" diff — what does that mean?</summary>

When you update a submodule to a new commit:

```
diff --git a/libs/shared b/libs/shared
index a3f9d12..b7e1f3a 160000
--- a/libs/shared
+++ b/libs/shared
@@ -1 +1 @@
-Subproject commit a3f9d12abc...
+Subproject commit b7e1f3abc...
```

The parent repo stores the submodule as a single entry in its tree — a "gitlink" — which is just the hash of the submodule's commit. Updating the submodule changes that hash, which shows up as a diff in the parent repo.

This diff in the parent repo IS the version bump record. It's how you track which version of the submodule each parent commit was using.

</details>
