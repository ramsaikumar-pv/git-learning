# 🗂️ Git Learning Progress — Ram (ramsaikumar-pv)

> Check off each item only after running the commands hands-on in a real terminal.
> Reading or watching is not the same as doing. Be honest with yourself. 🎯
> Update "Last Session" at the bottom after every session.

---

## 📦 01 — Foundations

- [x] What version control is and why it matters
- [x] Distributed vs centralised VCS
- [x] `git init` — initialise a repo, understand the `.git` folder
- [x] `git config` — set name and email
- [x] `git status` — read what Git is telling you
- [x] `git add <file>` — stage a file
- [x] `git add .` — stage everything
- [x] `git commit -m "msg"` — save a snapshot
- [x] The 3-stage workflow: Working Dir → Staging → Repo
- [x] `git log` — full commit history
- [x] `git log --oneline` — compact view
- [x] `git log --graph` — visual branch history
- [x] Commit hashes (SHA-1) — what they are and why they're unique

---

## 🌿 02 — Branching

- [x] `git branch` — list branches
- [x] `git switch -c <name>` — create and switch to a new branch
- [x] `git switch <name>` — move between branches
- [x] File contents change when switching branches (experienced this!)
- [x] `git merge <branch>` — merge into current branch
- [x] Fast-forward merge
- [x] 3-way merge
- [x] `git branch -d <name>` — delete a merged branch
- [x] Merge conflicts — what triggers them
- [x] Reading Git's conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- [x] Resolving a conflict manually in the editor
- [x] `git add` after resolving — mark as resolved
- [x] `git commit` — seal the merge
- [ ] `git rebase` — basics (linear history)
- [ ] Rebase vs merge — when to use which

---

## ☁️ 03 — Remotes

- [x] `git remote add origin <url>` — link local repo to GitHub
- [x] `git remote -v` — inspect remotes
- [x] `git push -u origin main` — first push, set upstream
- [x] `git push` — subsequent pushes
- [x] `git pull` — fetch + merge in one step
- [x] `git fetch` — download without merging
- [x] SSH key setup (ed25519) and `ssh -T git@github.com` verification
- [x] `git branch -M main` — rename default branch
- [ ] `git clone <url>` — clone an existing repo
- [ ] Forking a repo on GitHub
- [ ] Adding an upstream remote after forking
- [ ] Syncing a fork with upstream
- [ ] Opening a pull request on GitHub
- [ ] Reviewing and merging a PR
- [ ] Branch protection basics

---

## 🔧 04 — Intermediate

- [ ] `git diff` — unstaged changes
- [ ] `git diff --staged` — staged vs last commit
- [ ] `git diff <commit1> <commit2>` — compare commits
- [ ] `git stash` — shelve uncommitted work
- [ ] `git stash pop` — restore stashed work
- [ ] `git stash list` — see all stashes
- [ ] Named stashes: `git stash push -m "name"`
- [ ] `git revert <commit>` — safe undo (creates new commit)
- [ ] `git reset --soft` — undo commit, keep changes staged
- [ ] `git reset --mixed` — undo commit, unstage changes
- [ ] `git reset --hard` — undo commit, discard changes ⚠️
- [ ] When to use revert vs reset
- [ ] `.gitignore` — basic patterns
- [ ] `.gitignore` — wildcards, directories, negation
- [ ] Global `.gitignore`
- [ ] Untracking a file already committed
- [ ] `git tag` — lightweight tags
- [ ] `git tag -a` — annotated tags
- [ ] `git push --tags` — push tags to remote

---

## ⚡ 05 — Advanced

- [ ] `git cherry-pick <commit>` — apply a specific commit
- [ ] `git rebase -i` — interactive rebase
- [ ] Squashing commits
- [ ] Fixup and reword in interactive rebase
- [ ] Git hooks — what they are
- [ ] `pre-commit` hook — run checks before committing
- [ ] `post-merge` hook
- [ ] `git submodule add` — add a nested repo
- [ ] `git submodule update --init` — initialise submodules after clone
- [ ] `git bisect start` / `git bisect good` / `git bisect bad`
- [ ] `git reflog` — see every HEAD movement
- [ ] Recovering a lost commit with `git reflog`

---

## 🤝 06 — Workflows

- [ ] Gitflow — feature/release/hotfix strategy
- [ ] Trunk-based development
- [ ] Short-lived feature branches
- [ ] Code owners file
- [ ] Branch protection rules on GitHub
- [ ] Review etiquette — what makes a good PR

---

## ⚙️ 07 — GitHub Actions

- [ ] YAML workflow syntax basics
- [ ] Trigger types: push, pull_request, schedule
- [ ] Jobs and steps
- [ ] Using community actions (`actions/checkout`)
- [ ] Running tests on push (CI)
- [ ] Build and publish artifacts
- [ ] Deploy on merge to main

---

## 📅 Last Session

```
Date        : August 2026
Completed   : Merge conflicts (hands-on) ✅
Current     : 03-remotes — forking and PRs
Next up     : git diff, git stash
Blockers    : none
Notes       : Module 4 graded assessment pending after all Module 3 topics done
```

> Update the block above after every session.
> Keep it honest — this is your source of truth when you come back after a break. 📌
