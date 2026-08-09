# Solution & Answer Key

Compare your work against this after attempting `TASK.md` yourself — not before. 🙂

---

## Checkpoint 1

```bash
mkdir metrics-service && cd metrics-service
git init
git config user.name "Ram Sai Kumar"       # skip if already set globally
git config user.email "ram@example.com"
echo "def start(): pass" > app.py
git add app.py
git commit -m "Add initial app entrypoint"
git log --oneline
```

**Answer:** Before `git add`, `app.py` was in the Working Directory. After `git add`, it moved to the Staging Area. After `git commit`, it moved into the Repository, permanently.

---

## Checkpoint 2

```bash
git switch -c feature/add-metrics
echo "def record(): pass" > metrics.py
git add metrics.py
git commit -m "Add metrics module"
echo "# v2" >> app.py
git add app.py
git commit -m "Add version comment to app"
git switch main
ls            # metrics.py is gone
git switch feature/add-metrics
ls            # metrics.py is back
```

**Answer:** `metrics.py` only exists as a committed file on `feature/add-metrics`. Switching branches makes Git rewrite your actual working directory to match whichever branch's last commit you're on — files unique to one branch appear and disappear accordingly. This is expected, not a bug.

---

## Checkpoint 3

```bash
git switch main
echo "# Metrics Service" > README.md
git add README.md
git commit -m "Add README"
git merge feature/add-metrics
git log --oneline --graph --all
git branch -d feature/add-metrics
```

**Answer:** Because `main` moved forward (the README commit) after the branch was created, Git could not just slide the pointer — it created a 3-way merge commit with two parents. If you hadn't made that README commit on `main`, it would have been a fast-forward instead.

---

## Checkpoint 4

```bash
git switch -c feature/change-port
echo "port = 8080" >> app.py
git add app.py
git commit -m "Set port to 8080"
git switch main
echo "port = 9090" >> app.py
git add app.py
git commit -m "Set port to 9090"
git merge feature/change-port
# CONFLICT appears
vi app.py    # resolve, remove markers, keep one value
git add app.py
git commit
```

**Answer:** Both branches changed the exact same line differently after diverging from a common ancestor. Git has no reliable way to guess which value is "correct," so it stops and asks a human to decide.

---

## Checkpoint 5

```bash
git remote add origin git@github.com:ramsaikumar-pv/metrics-service.git
git push -u origin main
# ... make another commit ...
git push
```

**Answer:** `-u` links your local `main` to `origin/main` so Git remembers where this branch's "home" is. Once that link exists, plain `git push` (and `git pull`) know where to go automatically — no need to repeat the full remote and branch name every time.

---

## Checkpoint 6

```bash
# after forking on GitHub's website:
git clone git@github.com:ramsaikumar-pv/some-repo.git
cd some-repo
git remote add upstream git@github.com:original-owner/some-repo.git
git remote -v
```

**Answer:** `git push` defaults to `origin`, which is your fork — not the original repo. This matters because you never have write access to `upstream` directly; the only way your changes reach the original project is by opening a pull request from your fork.

---

## ✅ If you got through all six checkpoints and could answer the questions unaided

You're solid on Modules 1–3. Update `PROGRESS.md` at the repo root, mark this assessment complete, and move on to `04-intermediate/01-diff`. 🎉
