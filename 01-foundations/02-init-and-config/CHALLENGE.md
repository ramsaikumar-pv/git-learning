# Challenge

## Challenge 1: Per-repo identity

Create a second repo and give it a different email address — simulate switching between a personal project and a work project:

```bash
mkdir ~/work-project && cd ~/work-project
git init
git config user.email "ram@workplace.com"
git config --list --show-origin
```

Which email appears for this repo? Which file is it stored in? Run the same check in `~/git-practice` — does it still show your global email?

---

## Challenge 2: Create a repo without leaving your current directory

You initialised `~/git-practice` by `cd`-ing into it first. Can you initialise a repo in a new directory *without changing directories*?

Hint: `git init` accepts a path argument.

---

## Challenge 3: Set a useful alias

Git supports command aliases. Add this to your global config:

```bash
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

Now run `git st` and `git lg`. What do you see?

Aliases live in `~/.gitconfig` under `[alias]`. Open the file and see how they look. This is the Git equivalent of a shell alias — same concept you already know.

---

## Bonus: What happens if you `git init` inside an existing Git repo?

Try it. What does Git say? Is it dangerous? Why or why not?
