# Init and Config

Before Git can track anything, you need two things: a repository and an identity.

---

## Step 1: Create a repository

Think of `git init` like laying the foundation for a new project — it creates the invisible `.git/` folder that becomes Git's database.

```bash
git init my-project
cd my-project
```

Or if you're already inside a folder:

```bash
cd existing-folder
git init
```

Git responds:
```
Initialized empty Git repository in /home/ram/my-project/.git/
```

That `.git/` folder is everything. No `.git/` = no Git. It's local — nothing has touched the internet yet.

---

## Step 2: Tell Git who you are

Git attaches your name and email to every commit. Without this, every commit is anonymous and your team will hate you.

```bash
git config --global user.name "Ram Sai Kumar"
git config --global user.email "ram@example.com"
```

The `--global` flag writes this to `~/.gitconfig` — it applies to every repo on your machine. You can override it per-repo by dropping `--global`:

```bash
git config user.email "work@company.com"   # only this repo
```

---

## Config is just a file

```bash
cat ~/.gitconfig
```

```
[user]
    name = Ram Sai Kumar
    email = ram@example.com
[core]
    editor = vi
```

You can edit this file directly with any text editor. `git config` is just a structured way to write to it.

---

## Useful config to set early

```bash
git config --global core.editor vi          # default editor
git config --global init.defaultBranch main # new repos start on 'main' not 'master'
git config --global color.ui auto           # coloured output in terminal
```

---

## See all your config

```bash
git config --list
git config --list --show-origin   # shows which file each setting comes from
```

---

Next: adding files and making your first commit.
