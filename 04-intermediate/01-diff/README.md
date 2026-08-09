# git diff 🌱

## 📖 In plain words

`git diff` answers one question: "what exactly changed?" It shows you a before/after comparison — line by line — between any two versions of your files: your unsaved edits vs. the last commit, what's staged vs. the last commit, or even between two totally different commits.

Think of it like Word's "Track Changes" view, but for any two snapshots you choose.

---

## Unstaged changes (working directory vs last commit)

```bash
git diff
```

Running `git diff` with no options shows what you've edited but haven't staged yet. If you've already staged everything with `git add`, this command shows nothing — because there's no *unstaged* difference left to show.

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

How to read this: lines starting with `+` (usually shown in green) were added. Lines starting with `-` (usually red) were removed. Unmarked lines are just there for context, so you can see where the change sits. The `@@` line is a location marker telling you which line numbers were affected — you can safely ignore the exact numbers at first and just focus on the `+`/`-` lines.

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

---

## ✅ Quick recap

- `git diff` — unstaged changes vs. last commit.
- `git diff --staged` — staged changes vs. last commit (use this right before committing).
- `git diff <commit1> <commit2>` — compare any two commits or branches.
- Lines with `+` were added, lines with `-` were removed.
