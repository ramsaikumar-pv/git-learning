# Solution

## `git show v0.1` (lightweight tag)
```
commit b7e1f3a4c2d8e9f0a1b3c4d5e6f7a8b9c0d1e2f3
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 15:00:00 2026 +0530

    Add version comment to app

diff --git a/app.py b/app.py
...
```

Goes straight to the commit. No tag metadata.

## `git show v1.0` (annotated tag)
```
tag v1.0
Tagger: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 16:00:00 2026 +0530

Release 1.0 — first stable version

commit b7e1f3a4c2d8e9f0a1b3c4d5e6f7a8b9c0d1e2f3
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 15:00:00 2026 +0530

    Add version comment to app

diff --git a/app.py b/app.py
...
```

Two sections: the tag object (tagger, date, message) then the commit it points to. This is why annotated tags are preferred — they have their own metadata, separate from the commit.

## `git tag` output
```
v0.0.1
v1.0
```

Alphabetical order. Git sorts tags alphabetically by default, not by creation date or commit date.

## Detached HEAD when checking out a tag

```
Note: switching to 'v1.0'.

You are in 'detached HEAD' state. You can look around, make experimental
commits, and can check out back to a branch by running

  git switch -

HEAD is not on any branch now. Your next commit will be lost unless you
create a new branch. Do it like this:

  git switch -c <new-branch-name>
```

"Detached" means HEAD points directly to a commit, not to a branch. Normally HEAD → branch → commit. In detached HEAD: HEAD → commit (no branch in between). Commits you make here aren't on any branch and will be orphaned if you switch away.

## `git push origin --tags` on GitHub

GitHub's Tags page shows your annotated tags. It lets you download tarballs, create releases with notes, and attach binaries. This is the standard release flow for open-source projects.
