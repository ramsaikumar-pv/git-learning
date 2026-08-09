# Solution

## `git status` before .gitignore
```
On branch main
Untracked files:
        .env
        __pycache__/
        app.pyc
        debug.log
```

All four visible.

## `git status` after .gitignore
```
On branch main
Untracked files:
        .gitignore
```

The four files are gone from `git status`. Git is ignoring them. Only `.gitignore` itself shows — because it's a new untracked file you should stage.

## `git check-ignore -v .env`
```
.gitignore:1:.env   .env
```

Line 1 of `.gitignore` matched. The format: `file:line:pattern   matched-filename`.

## After committing credentials.txt and adding it to .gitignore:

`git status`:
```
On branch main
Changes not staged for commit:
        modified:   .gitignore
```

`.gitignore` shows as modified, but `credentials.txt` does NOT disappear from tracking. Git still watches tracked files, `.gitignore` only prevents UNTRACKED files from showing up.

## After `git rm --cached credentials.txt`:
```
On branch main
Changes to be committed:
        deleted:    credentials.txt
Changes not staged for commit:
        modified:   .gitignore
```

`git rm --cached` stages a deletion — removes from Git's index (so it stops being tracked) but leaves the file on disk. After committing, Git forgets about `credentials.txt` going forward.

## git rm vs git rm --cached

`git rm` = delete from both the index AND the local filesystem (file gone from disk)
`git rm --cached` = delete from the index only (file stays on disk, just untracked)

Use `--cached` whenever you want to stop tracking a file but keep it locally — which is almost always what you want when fixing `.gitignore` issues.
