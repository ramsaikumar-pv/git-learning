# Task: The "Metrics Service" Scenario

Work through these checkpoints in order, in a fresh practice folder (not one of the course example repos). Do each step for real before reading ahead.

---

## Checkpoint 1 — Start the project

1. Create a new folder called `metrics-service` and turn it into a Git repo.
2. Confirm your name/email are configured (either globally already, or set them for this repo).
3. Create a file `app.py` with any simple content (a few lines is fine).
4. Stage it and make your first commit with a clear message.
5. Confirm it's saved using `git log --oneline`.

**Checkpoint question:** at each step, which of the three zones (Working Directory / Staging / Repository) was `app.py` sitting in?

---

## Checkpoint 2 — Branch and build a feature

1. Create a branch called `feature/add-metrics` and switch to it.
2. Add a new file `metrics.py` with a couple of lines of content, commit it.
3. Modify `app.py` slightly (add a comment or a line), commit that too.
4. Switch back to `main` and confirm `metrics.py` is *not* there.
5. Switch back to `feature/add-metrics` and confirm it *is* there.

**Checkpoint question:** why did `metrics.py` disappear and reappear? What actually happened to your working directory?

---

## Checkpoint 3 — Merge it in

1. On `main`, make one small unrelated commit (e.g., add a `README.md` with one line).
2. Now merge `feature/add-metrics` into `main`.
3. Look at `git log --oneline --graph --all` — did you get a fast-forward or a 3-way merge? How can you tell?
4. Delete the now-merged `feature/add-metrics` branch.

**Checkpoint question:** what determined whether Git did a fast-forward vs. a 3-way merge here?

---

## Checkpoint 4 — Cause and resolve a conflict

1. Create a branch `feature/change-port`, and in `app.py`, change (or add) a line like `port = 8080`. Commit it.
2. Switch back to `main`, and on `main` directly, change that same line to `port = 9090`. Commit it.
3. Merge `feature/change-port` into `main`. You should get a conflict.
4. Resolve it — pick one value, remove the markers, stage, and commit the merge.

**Checkpoint question:** why did Git flag this as a conflict instead of merging it automatically?

---

## Checkpoint 5 — Connect to GitHub

1. Create an empty repo on GitHub (don't initialize it with a README).
2. Link your local `metrics-service` repo to it as `origin`, using the SSH URL.
3. Push `main` for the first time, setting the upstream.
4. Make one more small commit locally and push it again — notice you don't need `-u` this time.

**Checkpoint question:** what does `-u` actually set up, and why don't you need it on the second push?

---

## Checkpoint 6 — Simulate a fork workflow (optional, if you have a second GitHub account or a public repo to practice on)

1. Fork any small public repo on GitHub.
2. Clone your fork locally.
3. Add the original repo as a remote named `upstream`.
4. Run `git remote -v` and confirm you see both `origin` (your fork) and `upstream` (the original).

**Checkpoint question:** if you commit locally and run `git push`, which remote does it go to by default — and why does that matter?

---

When you've worked through all checkpoints (and can answer the questions without peeking), check `SOLUTION.md` to compare.
