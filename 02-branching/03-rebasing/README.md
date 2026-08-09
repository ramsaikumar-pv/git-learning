# Rebasing 🌱

## 📖 In plain words

Rebase is a second way (besides merge) to bring one branch's changes into another. Both end with your work joined into `main`. The difference is purely about what the *history* looks like afterward — messy and branching (merge), or clean and straight-line (rebase).

Infrastructure analogy: rebase is like replaying your config changes on top of a newer base image. Your changes are the same — they're just reapplied on top of something more recent, as if you'd started from there in the first place.

---

## The problem rebase solves

Picture this: you branched off `main` three days ago. Since then, teammates have merged six other things into `main`. Your branch is now "behind" — it doesn't have those updates.

With **merge**, catching up would create a merge commit with two parents — your work plus main's updates tangled together. Do this often and the history graph gets messy and hard to follow.

With **rebase**, Git instead picks up your commits, sets them aside for a moment, and replays them one by one on top of the newest `main` — as if you'd started your branch today instead of three days ago. The result: a single, clean, straight line of history.

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

Notice E and F become E' and F' — brand new commits with brand new hashes, even though the actual code changes are identical. This matters: because the hash changed, Git now sees these as completely different commits from the originals. Keep this in mind — it's the whole reason for the golden rule below.

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

## The golden rule of rebasing ⚠️

**Never rebase commits that have already been pushed to a shared remote branch (one others are pulling from).**

Why: as you just saw, rebase gives every replayed commit a brand-new hash. If you rebase commits that a teammate already has, and then force-push, their copy of history and yours no longer match — Git will call this a broken history, and untangling it is painful. Simple rule to remember: on your own private, unpushed branch — rebase as freely as you like. The moment it's pushed and shared: merge only.

---

## ✅ Quick recap

- Rebase = replay your commits on top of the latest `main`. Result: clean, linear history.
- Merge = combine two branches as-is. Result: a merge commit, branching history.
- Rebased commits get new hashes — treat them as "different" from the originals.
- Golden rule: never rebase commits others have already pulled.
