# Solution

## Step 2: `git diff` (unstaged)
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

`---` = old file, `+++` = new file. `+` lines were added. `-` lines were removed. Context lines (no prefix) show unchanged surrounding code.

## Step 4 (after staging app.py):

`git diff` → **nothing** (app.py is staged; no unstaged changes)
`git diff --staged` → shows the app.py changes

After also editing config.yaml:

`git diff` → shows config.yaml changes only (unstaged)
`git diff --staged` → shows app.py changes only (staged)

This is the power of the three-zone model: you can see exactly what's in each zone independently.

## Step 8: `git diff HEAD~1 HEAD --stat`
```
 app.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

## Step 9: `git diff HEAD~1 HEAD -- app.py`
Shows only changes in `app.py` between the two commits. The `--` separator tells Git "everything after this is a filename, not a commit reference."

## Why staged vs unstaged matters

Without the staging area, every `git diff` would just show all changes at once. The separation lets you:
1. Review staged: "is this exactly what I want to commit?"
2. Review unstaged: "what have I changed that's not going in yet?"

It's the photographer's staging area — arrange the shot (`git add`), then check it (`git diff --staged`), then click the shutter (`git commit`).
