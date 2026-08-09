# Init and Config 🌱

## 📖 In plain words

Before Git can start tracking your files, two things need to happen: you need to tell a folder "hey, start watching me" (that's `git init`), and you need to tell Git who you are (that's `git config`), so it knows whose name to attach to your saved snapshots.

That's the whole module in one sentence. Let's do both, one step at a time.

---

## Step 1: Create a repository

Think of `git init` like laying the foundation for a new house — it creates a hidden `.git/` folder that becomes Git's private database for this project. You won't normally open this folder yourself; Git manages it for you.

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

That `.git/` folder is everything — it's where all your history will live. No `.git/` folder = this isn't a Git project yet. And notice: nothing here touched the internet. `git init` is 100% local, on your own machine.

---

## Step 2: Tell Git who you are

Every commit gets a name and email stamped on it, so later you (or a teammate) can see who made which change. Git needs you to set this once.

```bash
git config --global user.name "Ram Sai Kumar"
git config --global user.email "ram@example.com"
```

The `--global` flag means "apply this everywhere" — it writes to a file called `~/.gitconfig`, and every Git project on your machine will use it. If you ever need one project to use a different email (say, a personal project vs. a work one), you can set it just for that folder by dropping `--global`:

```bash
git config user.email "work@company.com"   # applies only to this one repo
```

---

## Config is just a file

Nothing magic is happening — `git config` is simply writing to a plain text file. You can see it for yourself:

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

## ✅ Quick recap

- `git init` — turns a folder into a Git project (creates the hidden `.git/` folder). Purely local.
- `git config --global user.name/user.email` — tells Git who you are, once, for every project.
- `~/.gitconfig` — just a plain text file. `git config` edits it for you.

Next: adding files and making your first commit.
