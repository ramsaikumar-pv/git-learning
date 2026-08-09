# Solution

## Expected output: `git init`
```
Initialized empty Git repository in /home/ram/git-practice/.git/
```

## Expected output: `git status` (empty repo)
```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Git already knows you're on `main` because of the `init.defaultBranch main` setting. Without that setting you'd see `master` instead.

## Expected output: `git config --list --show-origin`
```
file:/home/ram/.gitconfig    user.name=Ram Sai Kumar
file:/home/ram/.gitconfig    user.email=ram@example.com
file:/home/ram/.gitconfig    core.editor=vi
file:/home/ram/.gitconfig    init.defaultbranch=main
file:/home/ram/git-practice/.git/config  core.repositoryformatversion=0
file:/home/ram/git-practice/.git/config  core.filemode=true
file:/home/ram/git-practice/.git/config  core.bare=false
```

## Expected: `cat ~/.gitconfig`
```ini
[user]
    name = Ram Sai Kumar
    email = ram@example.com
[core]
    editor = vi
[init]
    defaultBranch = main
```

## Why it works this way

Git's config is layered: system → global → local. Global config lives in your home directory and applies everywhere. Local config (inside `.git/config`) only applies to that one repo. This is the same pattern as `/etc/` vs `~/.config/` vs a per-project config file — you already know this model from Kubernetes config files.
