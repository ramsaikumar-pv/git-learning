# Solution

## `git log` (verbose)
```
commit b7e1f3a4c2d8e9f0a1b3c4d5e6f7a8b9c0d1e2f3
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 15:00:00 2026 +0530

    Add version comment to app

commit a3f9d12b4e7c8f1d2e3a4b5c6d7e8f9a0b1c2d3e
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 14:30:00 2026 +0530

    Add app entrypoint and initial config
```

## `git log --oneline`
```
b7e1f3a Add version comment to app
a3f9d12 Add app entrypoint and initial config
```

## `git log --oneline --graph --all`
```
* b7e1f3a (HEAD -> main) Add version comment to app
* a3f9d12 Add app entrypoint and initial config
```

With only one branch, the graph is linear — just a vertical line of `*`s. The branching picture appears once you create feature branches (module 02).

## `git show a3f9d12`
```
commit a3f9d12b4e7c8f1d2e3a4b5c...
Author: Ram Sai Kumar <ram@example.com>
Date:   Mon Aug 5 14:30:00 2026 +0530

    Add app entrypoint and initial config

diff --git a/app.py b/app.py
new file mode 100644
index 0000000..3f8c1a2
--- /dev/null
+++ b/app.py
@@ -0,0 +1,8 @@
+def start_server(host="0.0.0.0", port=8080):
...
```

`git show` gives you the commit header AND the full diff — exactly what changed.

## Why 7-character hashes?

40 characters is the full SHA-1 hash. Git only needs enough characters to be unique in your repo. 7 characters gives 268 million possible values — more than enough for any project. Git shows the minimum needed; in huge repos (like the Linux kernel) it shows more.

## Why it works this way

The hash in `git log --oneline` is an abbreviation of the full commit SHA. You can use any unique prefix — `git show a3f9`, `git show a3f9d12`, or the full 40-char hash all refer to the same commit. Git resolves whichever prefix you give it.
