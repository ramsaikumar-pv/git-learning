# git bisect

A bug appeared in prod. You know it worked at commit `v1.0`. It's broken now. You have 200 commits in between. Which one introduced the bug?

`git bisect` binary-searches your commit history to find it. It takes O(log n) steps instead of O(n). 200 commits → about 8 checks.

---

## The concept

Binary search: git picks the midpoint commit. You test it. If it works → bug is in the second half. If broken → bug is in the first half. Repeat until the bad commit is isolated.

```
v1.0 (good)  |----100 commits----|  HEAD (bad)
                      ↑
              git bisect picks here
              → you test → broken
              
v1.0 (good)  |--50--|  midpoint (bad)
                  ↑
              git picks here
              → you test → works
              → bug is between this and midpoint
```

---

## Start a bisect session

```bash
git bisect start
git bisect bad                   # current HEAD is broken
git bisect good v1.0             # this tag/hash was working
```

Git checks out the midpoint commit. You test it.

---

## Mark each commit

```bash
git bisect good   # this commit doesn't have the bug
git bisect bad    # this commit has the bug
```

Repeat until Git says:

```
b7e1f3a is the first bad commit
commit b7e1f3a4c2d8...
Author: Someone <email>
Date:   ...

    Add cache layer

:100644 100644 ...  app.py  M
```

Found it. That commit introduced the bug.

---

## End bisect

```bash
git bisect reset   # returns HEAD to where you started
```

---

## Automate with a script

Instead of manually testing each commit, give bisect a script:

```bash
git bisect run python tests/test_health.py
```

If the script exits 0 → good commit. Non-zero → bad commit. Git bisects automatically until it finds the first bad commit.

For shell-based tests:
```bash
git bisect run sh -c "grep 'timeout = 30' config.yaml"
```

---

## Skip a commit

If a commit can't be tested (doesn't compile, CI is broken):

```bash
git bisect skip
```

Git moves to the nearest testable commit.
