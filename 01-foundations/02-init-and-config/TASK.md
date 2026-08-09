# Task: Initialise a Repo and Configure Git

## Steps

1. Create a new directory and initialise a Git repo:

```bash
mkdir ~/git-practice
cd ~/git-practice
git init
```

2. Check what Git created:

```bash
ls -la
```

Do you see `.git/`?

3. Check the current config (name/email might be empty):

```bash
git config --list
```

4. Set your name and email globally:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

5. Set the default editor to `vi` and default branch to `main`:

```bash
git config --global core.editor vi
git config --global init.defaultBranch main
```

6. Verify all settings:

```bash
git config --list --show-origin
```

7. Look at the raw config file:

```bash
cat ~/.gitconfig
```

8. Now check the status of your empty repo:

```bash
git status
```

---

## What do you see? What does it mean?

- What does `git status` say when there are no files?
- Where is your name/email stored — which file?
- What does `--show-origin` tell you that `--list` alone doesn't?

Record your answers in `notes.txt`.
