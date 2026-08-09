# git diff

`git diff` shows you what changed. It's your before/after view of the working directory, staging area, or between any two commits.

---

## Unstaged changes (working directory vs last commit)

```bash
git diff
```

Shows what you've changed but haven't staged yet. If everything is staged, this shows nothing.

```
diff --git a/app.py b/app.py
index 3f8c1a2..7b4d2e1 100644
--- a/app.py
+++ b/app.py
@@ -1,4 +1,5 @@
+# version 2
 def start_server(host="0.0.0.0", port=8080):
-    print(f"Starting server on {host}:{port}")
+    print(f"[INFO] Starting server on {host}:{port}")
     return True
```

Lines starting with `+` were added. Lines starting with `-` were removed. The `@@` line shows which line numbers were affected.

---

## Staged changes (staging area vs last commit)

```bash
git diff --staged
```

Shows what's in the staging area that will go into the next commit. Use this before committing to review what you're about to save.

Also works as:
```bash
git diff --cached   # older alias, same thing
```

---

## Between two commits

```bash
git diff a3f9d12 b7e1f3a         # between two specific commits
git diff HEAD~1 HEAD              # last commit vs the one before
git diff main feature/my-branch  # between two branches
```

---

## Diff for a specific file only

```bash
git diff app.py                   # unstaged changes in app.py only
git diff HEAD~2 HEAD -- app.py    # last 2 commits for app.py only
```

---

## Word-level diff

```bash
git diff --word-diff
```

Instead of whole-line diffs, shows exactly which words changed within a line. Useful for prose or config changes where most of the line is the same.

---

## Stat summary (no line detail)

```bash
git diff --stat HEAD~1 HEAD
```

```
 app.py     | 3 ++-
 config.yaml | 1 +
 2 files changed, 3 insertions(+), 1 deletion(-)
```

Just the count of changes per file. Good for a quick overview before diving into details.
