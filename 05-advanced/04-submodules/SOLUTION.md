# Solution

## After `git submodule add`

```
Cloning into '/home/ram/project/libs/shared'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
```

## `cat .gitmodules`
```
[submodule "libs/shared"]
    path = libs/shared
    url = git@github.com:ramsaikumar-pv/my-shared-lib.git
```

## `git status` after adding submodule
```
On branch main
Changes to be committed:
        new file:   .gitmodules
        new file:   libs/shared
```

Note: `libs/shared` is a single entry in the index — a gitlink, not a directory of files.

## `git submodule status`
```
 a3f9d12abc (HEAD)
```

The hash after the space is the commit in the submodule repo that your parent repo is pinned to.

## After cloning elsewhere: `ls libs/shared/`
```
(empty)
```

Cloning pulls the parent repo's history but not the submodule's content. The `.gitmodules` file is there, but the actual submodule content isn't downloaded yet.

## After `git submodule update --init`: `ls libs/shared/`
```
util.py
```

Now the submodule content is populated.

## After updating submodule: `git diff --staged`
```
diff --git a/libs/shared b/libs/shared
index a3f9d12..b7e1f3a 160000
--- a/libs/shared
+++ b/libs/shared
@@ -1 +1 @@
-Subproject commit a3f9d12abc...
+Subproject commit b7e1f3abc...
```

This diff IS the version bump. The parent repo stores a gitlink (the submodule commit hash), and changing it = updating the pinned version.
