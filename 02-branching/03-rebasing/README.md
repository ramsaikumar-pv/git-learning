# Rebasing

Rebase is the alternative to merge. Both integrate changes from one branch into another. The difference is in the history they produce.

Infrastructure analogy: rebase is like replaying your config changes on top of a newer base image. Your changes are the same — they're just applied on top of something more recent.

---

## The problem rebase solves

You branched off `main` three days ago. Since then, teammates have merged six things into `main`. Your branch is behind.

With **merge**, you'd create a merge commit that has two parents — your work + main's updates. The graph gets bushy.

With **rebase**, Git replays your commits on top of the latest `main`. The graph stays linear.

---

## How rebase works

```
Before:
  main:          A → B → C → D
  feature/login: A → B → E → F

git switch feature/login
git rebase main

After:
  main:          A → B → C → D
  feature/login: A → B → C → D → E' → F'
```

E and F become E' and F' — new commits with new hashes, but the same changes. Git replayed them on top of D.

---

## The commands

```bash
git switch feature/login
git rebase main
```

If there are no conflicts:
```
Successfully rebased and updated refs/heads/feature/login.
```

If there are conflicts, Git pauses:
```
CONFLICT (content): Merge conflict in app.py
error: could not apply e3f2a1b... Add login handler
hint: Resolve all conflicts manually, then run "git rebase --continue"
```

Resolve the conflict, `git add` the file, then:
```bash
git rebase --continue
```

To abort and go back to before you started:
```bash
git rebase --abort
```

---

## Rebase vs merge: when to use which

| Situation | Use |
|-----------|-----|
| Integrating a finished feature into `main` | Merge (preserves history, shows feature as a unit) |
| Updating your feature branch with latest `main` | Rebase (keeps your branch up to date cleanly) |
| Cleaning up messy commits before a PR | Interactive rebase (module 05-02) |
| Shared branches (pushed to GitHub) | **Never rebase** — rewrites history others rely on |

---

## The golden rule of rebasing

**Never rebase commits that have been pushed to a shared remote branch.**

Rebase rewrites commit hashes. If you rebase and push (force), anyone who pulled the old commits will have a broken history. On your local, private branch: rebase freely. Once pushed: merge only.
