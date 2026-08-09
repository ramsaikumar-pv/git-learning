# Git Submodules 🌱

## 📖 In plain words

A submodule is a Git repo living inside another Git repo. It lets your project depend on someone else's code, pinned at one exact commit — without physically copying their files into your own history. Your repo just remembers "use exactly this version of that other repo."

Platform analogy: submodules are like a Helm chart dependency with a pinned version. Your repo records exactly which version of the external repo you're using. When the external repo updates, you explicitly choose when to adopt the update.

---

## Add a submodule

```bash
git submodule add git@github.com:some-org/some-lib.git libs/some-lib
```

This:
1. Clones `some-lib` into `libs/some-lib/`
2. Creates a `.gitmodules` file in your repo root
3. Records the current commit hash of the submodule

```bash
cat .gitmodules
```

```
[submodule "libs/some-lib"]
    path = libs/some-lib
    url = git@github.com:some-org/some-lib.git
```

Stage and commit:

```bash
git add .gitmodules libs/some-lib
git commit -m "Add some-lib as submodule"
```

---

## Clone a repo with submodules

A plain `git clone` doesn't download submodule contents. You get empty directories.

```bash
git clone --recurse-submodules git@github.com:you/your-repo.git
```

Or if you already cloned:

```bash
git submodule update --init
git submodule update --init --recursive  # nested submodules
```

---

## Update a submodule to a newer commit

```bash
cd libs/some-lib
git fetch
git checkout main   # or a specific tag
cd ../..
git add libs/some-lib
git commit -m "Update some-lib to latest main"
```

Submodules don't auto-update — you choose when to move to a newer commit.

---

## List submodules

```bash
git submodule status
```

```
 a3f9d12 libs/some-lib (v1.2.3)
```

The hash shown is the commit your parent repo has pinned the submodule to.

---

## Common problems

| Problem | Fix |
|---------|-----|
| Empty submodule directory | `git submodule update --init` |
| Submodule on detached HEAD | Normal — submodules always live on a specific commit |
| Teammate committed wrong submodule hash | Review the `.gitmodules` diff and the submodule diff before merging |

---

## When NOT to use submodules

Submodules have a reputation for being confusing. Modern alternatives:
- For packages: use a proper package manager (pip, npm, helm)
- For vendoring: copy the code and don't use submodules
- For shared internal code: publish it as a package or use a monorepo

Submodules are appropriate for: pinning an external repo at a specific version when you can't use a package manager.

---

## ✅ Quick recap

- Submodule = a Git repo nested inside another, pinned at one exact commit.
- `git clone --recurse-submodules` — clone and pull submodule contents in one step.
- Submodules never auto-update — you explicitly choose when to bump the pinned commit.
- Often confusing in practice — prefer a package manager when one is available.
