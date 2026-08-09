# What Is Git?

Imagine you're managing a Kubernetes manifest. You make a change. It breaks prod. You want the old version back — but you saved over it.

That's the problem Git solves.

Git is a **version control system**. Every time you save a snapshot of your work (called a *commit*), Git stores it permanently. You can go back to any snapshot, anytime. You can work on experimental changes without touching the stable version. You can collaborate with teammates without overwriting each other's work.

Think of Git like the audit trail in your platform — it records *what* changed, *when*, and *who did it*. Except here, you control when an entry is written.

---

## Git is NOT GitHub

Git = the tool on your machine that tracks changes.
GitHub = a website that hosts your Git history in the cloud.

You can use Git without GitHub. Git existed for years before GitHub did.

---

## What does Git actually store?

Git doesn't store diffs. It stores **snapshots** — a complete picture of every file at the moment you committed.

Internally, Git is a content-addressable filesystem. Each snapshot gets a unique ID (a SHA-1 hash like `a1b2c3d`). You'll see these everywhere. They're how Git refers to specific moments in time.

---

## The three areas you need to know

```
Working Directory  →  Staging Area (Index)  →  Repository (.git/)
   (your files)         (what's queued)          (saved history)
```

- **Working Directory**: where you edit files normally.
- **Staging Area**: a holding area — you choose what goes into the next commit.
- **Repository**: the permanent record, stored in `.git/`.

You'll understand this deeply after the next two modules. For now, just know these three zones exist.

---

## Why Git beats "backup folders"

| Approach | Problem |
|---|---|
| `app_v1.py`, `app_v2_final.py` | Chaos after week 2 |
| Google Drive history | No branching, no merging, no diffs |
| Git | Full history, branching, merging, diffs, collaboration |

---

Next up: initialising a repo and configuring Git for the first time.
