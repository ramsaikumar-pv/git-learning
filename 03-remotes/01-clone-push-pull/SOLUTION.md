# Solution

## `git remote -v` after adding origin
```
origin  git@github.com:ramsaikumar-pv/my-project.git (fetch)
origin  git@github.com:ramsaikumar-pv/my-project.git (push)
```

Two entries — one for fetch (download), one for push (upload). They're usually the same URL. You can have different fetch and push remotes (rare, but possible).

## `git push -u origin main`
```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (12/12), 1.23 KiB | 1.23 MiB/s, done.
Total 12 (delta 2), reused 0 (delta 0)
To git@github.com:ramsaikumar-pv/my-project.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

The last line confirms `--upstream` tracking is set. Future `git push` / `git pull` will know where to go.

## `git fetch origin` then `git log --oneline origin/main`
```
* f5d8e2a (origin/main) Edit via GitHub
* b7e1f3a (HEAD -> main) Add version comment to app
```

`origin/main` is ahead of your local `main` by one commit. `HEAD` hasn't moved — fetch doesn't change your local branches.

## `git pull`
```
Updating b7e1f3a..f5d8e2a
Fast-forward
 config.yaml | 1 +
 1 file changed, 1 insertion(+)
```

Fast-forward pull: no local commits diverged from origin, so Git just moved your `main` pointer forward.

## `git remote -v` in a cloned repo
```
origin  git@github.com:ramsaikumar-pv/my-project.git (fetch)
origin  git@github.com:ramsaikumar-pv/my-project.git (push)
```

`git clone` automatically sets up `origin` pointing back to the source. This is why you don't need `git remote add` after cloning.
