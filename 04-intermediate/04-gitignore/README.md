# .gitignore

Not everything in your project should go into Git. Build artifacts, secrets, virtual environments, log files, editor temp files — these should stay local. `.gitignore` tells Git to stop noticing them.

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

## .gitignore only works on untracked files

If a file is already committed, `.gitignore` does nothing. You need to untrack it first:

```bash
git rm --cached secrets.yaml    # remove from tracking, keep the local file
git add .gitignore
git commit -m "Stop tracking secrets.yaml"
```

The file stays on disk but disappears from Git's tracking. Add it to `.gitignore` BEFORE you ever commit it.

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
