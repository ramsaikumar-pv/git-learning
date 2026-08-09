# 📚 Git Learning — Index

> This repo is a self-paced Git course progressing from zero to advanced.
> Work through modules in order. Each module has a README, TASK, HINTS, SOLUTION, and CHALLENGE file.
> Update PROGRESS.md as you go.

---

## 🗂️ 01 — Foundations
*Core Git concepts and the everyday workflow.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-what-is-git | VCS concepts, distributed vs centralised, why Git exists | 20 min | ✅ |
| 02-init-and-config | `git init`, `git config`, the `.git` folder | 20 min | ✅ |
| 03-staging-and-commits | `git add`, `git commit`, the 3-stage workflow | 30 min | ✅ |
| 04-viewing-history | `git log`, `--oneline`, `--graph`, commit hashes | 30 min | ✅ |

---

## 🗂️ 02 — Branching
*Working in parallel without breaking things.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-creating-branches | `git branch`, `git switch -c`, `git switch` | 30 min | ✅ |
| 02-merging | `git merge`, fast-forward vs 3-way merge | 30 min | ✅ |
| 03-rebasing | `git rebase` basics, rebase vs merge | 45 min | ⏳ |
| 04-conflict-resolution | Merge conflicts, manual resolution, conflict markers | 45 min | ✅ |

---

## 🗂️ 03 — Remotes
*Working with GitHub and collaborating.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-clone-push-pull | `git clone`, `git push`, `git pull`, `git fetch`, SSH | 45 min | ✅ |
| 02-forking | Forking a repo, upstream remotes, keeping in sync | 45 min | 🔄 |
| 03-pull-requests | Opening a PR, code review flow, merging PRs | 60 min | 🔄 |
| 04-assessment | Graded scenario covering Modules 1–3, hands-on checkpoints | 60 min | ⏳ |

---

## 🗂️ 04 — Intermediate
*Commands you'll reach for every week.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-diff | `git diff`, staged vs unstaged, comparing commits | 30 min | 🔄 |
| 02-stash | `git stash`, `stash pop`, `stash list`, named stashes | 30 min | ⏳ |
| 03-reset-vs-revert | `git reset`, `git revert`, `--soft` vs `--hard`, when to use which | 45 min | ⏳ |
| 04-gitignore | `.gitignore` patterns, global ignore, untracking files | 30 min | ⏳ |
| 05-tags | `git tag`, annotated vs lightweight, `git push --tags` | 30 min | ⏳ |

---

## 🗂️ 05 — Advanced
*Power user tools. Unlock after completing 01–04.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-cherry-pick | `git cherry-pick`, picking specific commits | 30 min | 🔒 |
| 02-rebase-advanced | Interactive rebase, squash, fixup, reorder commits | 60 min | 🔒 |
| 03-git-hooks | Pre-commit, post-merge hooks, automating checks | 45 min | 🔒 |
| 04-submodules | `git submodule`, nested repos, update workflows | 45 min | 🔒 |
| 05-bisect | `git bisect`, binary search for bugs | 30 min | 🔒 |
| 06-reflog | `git reflog`, recovering lost commits | 30 min | 🔒 |

---

## 🗂️ 06 — Workflows
*How real teams use Git.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-gitflow | Feature/release/hotfix branch strategy | 60 min | 🔒 |
| 02-trunk-based | Trunk-based development, short-lived branches | 45 min | 🔒 |
| 03-team-collaboration | Code owners, branch protection, review etiquette | 45 min | 🔒 |

---

## 🗂️ 07 — GitHub Actions
*Automate things when code is pushed.*

| Module | What You Learn | Est. Time | Status |
|--------|---------------|-----------|--------|
| 01-actions-basics | YAML workflow syntax, triggers, runners | 60 min | 🔒 |
| 02-ci-pipeline | Run tests on push, build artifacts | 60 min | 🔒 |
| 03-deploy-workflow | Deploy on merge to main | 60 min | 🔒 |

---

## ➕ How to Expand This Index

When you add a new module:
1. Add a row to the right category table above
2. Add the same entry to PROGRESS.md checklist
3. Set status to ⏳

When you add a new category:
1. Add a new `##` section here
2. Add it to PROGRESS.md
3. Create the directory as `08-<topic>/`

---

## 🔑 Status Legend

| Icon | Meaning |
|------|---------|
| ✅ | Completed hands-on |
| 🔄 | In progress |
| ⏳ | Up next |
| 🔒 | Locked — complete earlier modules first |
