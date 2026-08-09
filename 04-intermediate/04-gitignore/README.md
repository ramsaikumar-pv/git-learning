# .gitignore 🌱

## 📖 In plain words

Not everything in your project folder should be tracked by Git. Things like passwords, temporary build files, or your editor's auto-save files shouldn't be shared or saved in history — they're either sensitive, or just noise.

`.gitignore` is a plain text file where you list patterns for files Git should simply pretend don't exist. Once listed, those files stop showing up in `git status`, and `git add .` will skip right over them.

---

## Create a .gitignore

At the root of your repo:

```bash
vi .gitignore
```

Each line is a pattern. Git will ignore any file matching that pattern.

```
# Python
__pycache__/
*.pyc
*.pyo
.env

# Node
node_modules/

# Secrets
.env
*.key
secrets.yaml

# Editors
.vscode/
*.swp
*~

# OS
.DS_Store
Thumbs.db

# Build output
dist/
build/
*.egg-info/
```

---

## Pattern syntax

```
*.log           # any file ending in .log
logs/           # any directory named logs (trailing / means directory)
!important.log  # exception: don't ignore this specific file
/config.yaml    # only at repo root, not in subdirectories
debug[0-9].log  # debug0.log through debug9.log
```

---

## .gitignore only works on untracked files ⚠️

An important gotcha for beginners: `.gitignore` only stops Git from noticing files it *doesn't already know about*. If a file was already committed before you added it to `.gitignore`, Git keeps tracking it — the ignore rule has no effect retroactively. You need to explicitly tell Git to stop tracking it:

```bash
git rm --cached secrets.yaml    # remove from tracking, keep the local file
git add .gitignore
git commit -m "Stop tracking secrets.yaml"
```

The file itself stays right where it is on your disk — you just told Git to stop watching it. Best practice: add sensitive or generated files to `.gitignore` *before* you ever commit them, so you never have to clean this up. (And if a secret ever does get committed by mistake, untracking it isn't enough — it's still in old history. That needs a different, more careful fix.)

---

## Global .gitignore (applies to all repos)

For editor temp files and OS-specific cruft that you never want in any repo:

```bash
git config --global core.excludesfile ~/.gitignore_global
vi ~/.gitignore_global
```

Add `.DS_Store`, `*.swp`, `Thumbs.db`, etc. here. Every repo on your machine respects this file.

---

## Check if a file is ignored

```bash
git check-ignore -v secrets.yaml
```

```
.gitignore:5:*.yaml   secrets.yaml
```

Shows which line in which file caused it to be ignored.

---

## GitHub's gitignore templates

When creating a repo on GitHub, you can auto-generate a `.gitignore` for your language. Also: [github.com/github/gitignore](https://github.com/github/gitignore) — community-maintained templates for every stack.

---

## ✅ Quick recap

- `.gitignore` — a text file listing patterns Git should ignore.
- Only affects files not already tracked. Already-committed files need `git rm --cached`.
- `git config --global core.excludesfile` — a global ignore file for every repo on your machine.
- `git check-ignore -v <file>` — check why a file is being ignored.
