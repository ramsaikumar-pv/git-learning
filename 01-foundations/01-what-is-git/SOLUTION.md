# Solution

## What you should see

### `ls -la` inside the module directory
```
-rw-r--r--  README.md
-rw-r--r--  TASK.md
-rw-r--r--  HINTS.md
-rw-r--r--  SOLUTION.md
-rw-r--r--  CHALLENGE.md
-rw-r--r--  notes.txt
```

### `ls .git/`
```
HEAD        config      description hooks/
info/       objects/    refs/
```

- `HEAD` — pointer to your current position in history
- `config` — repo-level Git settings (author name, remotes, etc.)
- `hooks/` — scripts that fire on Git events (more in module 05-03)
- `objects/` — the actual content database: every commit, file, tree stored as compressed blobs
- `refs/` — human-readable names (branch names, tag names) that point to commits

### `cat .git/HEAD`
```
ref: refs/heads/main
```

This means: "I'm on the `main` branch." When you make a commit, `main` will advance to point at it.

### `git log --oneline -5`
```
a3f9d12 Add initial project scaffold
b1c4e78 Add README for foundations
...
```

Each line is one commit: `<hash> <message>`. The hash is Git's unique ID for that snapshot. The message is what the author wrote to describe the change.

---

## Why it works this way

Git's `.git/` directory *is* the repository. The files you see in your working directory are just a checked-out copy of whatever commit HEAD points to. Delete `.git/` and Git history is gone — your files remain, but all history is lost. This is why you never `.gitignore` the `.git/` folder (Git itself manages it).
