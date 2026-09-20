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
- [ ] Module 3 graded assessment (`03-remotes/04-assessment`) — complete after all topics above

---

## 🔧 04 — Intermediate

- [x] `git diff` — unstaged changes
- [x] `git diff --staged` — staged vs last commit
- [x] `git diff <commit1> <commit2>` — compare commits
- [x] `git stash` — shelve uncommitted work
- [x] `git stash pop` — restore stashed work
- [x] `git stash list` — see all stashes
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
Date        : 2026-09-20
Completed   : git stash (stash/pop/apply/drop, branch-scoping, stash-caused conflicts) ✅
Current     : Module 3 wrap-up (04-intermediate topics interleaved)
Next up     : git revert / git reset  →  .gitignore  →  forking & PRs
Guidance    : HIGH
Blockers    : none
Notes       : Ram wants fewer basics re-covered and trickier probing questions
              once a mechanic is shown solid (see CLAUDE.md "How Ram Learns").
```

> Update the block above after every session, then add a dated entry to the
> session log below. Keep it honest — this is the source of truth when you
> come back after a break. 📌

---

## 📓 Session Log (newest first)

### 2026-09-20 (resume, later same day)
- On resume, found an uncommitted change in `dummy.html` on `test-branch`
  left over from the prior `stash apply` demo (apply had left the change in
  the working dir but the stash list was already empty — nothing to
  pop/drop). Confirmed with Ram it was leftover practice, not new work.
- Ram committed it himself: `738b9cb "this is a demonstration for the git
  stash related changes"` on `test-branch`. Tree clean, on `main`.
- Guidance level: HIGH.
- Housekeeping: moved all progress tracking out of `CLAUDE.md` into this
  file. `CLAUDE.md` now only holds the stable mentor guide + a mandatory
  pointer here.
- Paused before starting `git revert` / `git reset` — still the next topic.

### 2026-09-20 — `git stash`
- All hands-on in `~/githubrtesting` on `main` and `test-branch`.
- Discovered (didn't just recall) why `git switch`/`checkout` refuses when
  uncommitted changes conflict with the target branch's committed version
  ("would be overwritten by checkout"); ran `git stash` to see it clear the
  working dir.
- Proved stashes are **not branch-scoped** by popping a main-based stash
  onto `test-branch`, triggering a real merge conflict, then resolved it
  solo (add/commit).
- Isolated `pop` vs `apply` vs `drop` experimentally: clean pop auto-drops,
  conflicted pop keeps the entry, apply never removes it, drop discards
  without applying. Stated the distinction correctly unprompted. Solid.
- Correction logged: a prior "Ram's Own Analogies" table in `CLAUDE.md` had
  fabricated attribution — those were Claude-generated suggestions never
  validated with Ram. Fixed; Ram called this out directly. Don't repeat.
- Not yet done: named stashes (`git stash push -m`) — quick, fold into a
  later session.

### 2026-09-19 — refresher + `git diff`
- Long break → full refresher: VCS basics, staging vs `.gitignore`, 3-stage
  workflow, `git log`/`--oneline`, branching, `git switch -c`. Then a fresh
  merge conflict created and resolved end-to-end; `git log --graph` read
  back correctly on second pass.
- `git diff` dedicated session: unstaged vs `--staged` vs last commit,
  arbitrary commits (`HEAD~1`, two hashes). Independently discovered that
  argument order controls diff direction (`+`/`-` flip). Solid.
- Learning-style request: stop revisiting demonstrated basics; ask trickier
  "what happens if…" questions instead. Calibrate up incrementally.
- All practice commits pushed to `origin/main`.

### August 2026 — merge conflicts
- Merge conflicts hands-on: created conflict, resolved in `vi`, staged and
  committed the resolution, visualised with `git log --graph` 🎉
- All module READMEs rewritten for beginner clarity.
- Module 3 graded assessment added (`03-remotes/04-assessment`) — complete
  after forking + PRs, before starting `04-intermediate` proper.

### Earlier
- Foundations, branching, remotes basics, SSH setup — see checkboxes above.
- Ram spotted commit hashes unprompted in `git log`; loved `git log --graph`
  ("it's beautiful!").
