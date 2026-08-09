# What Is Git? 🌱

## 📖 In plain words

Git is a tool that **remembers every version of your files, forever** — so you can always go back.

Think about writing an essay in Word and hitting "Save" over and over. Each save *overwrites* the last one — the old version is gone. Git works differently: every time you save with Git (called a **commit**), it keeps *that* version too, alongside all the earlier ones. Nothing gets lost. You can jump back to any saved point, whenever you want.

That's it. That's the whole idea. Everything else in this course is just "cool things you can do because Git remembers everything."

---

## A quick example

Imagine you're managing a Kubernetes manifest. You make a change. It breaks prod. You want the old version back — but you saved over it. 😬

That's the exact problem Git solves. With Git, that old working version is still sitting in the history, one command away.

Git is what's called a **version control system**: software whose only job is to track changes to files over time, and let you move between those versions safely.

Think of Git like the audit trail in your platform — it records *what* changed, *when*, and *who did it*. The difference is: with Git, **you** decide when a new "entry" gets written (by making a commit) — it's not automatic.

---

## Git is NOT GitHub 🤔

This trips up a lot of beginners, so let's be very clear:

- **Git** = the tool installed on *your* laptop that tracks changes to files. It works completely offline.
- **GitHub** = a *website* that stores a copy of your Git history in the cloud, so you can back it up and share it with others.

You can use Git without ever touching GitHub — millions of people do. Git existed for years before GitHub was built on top of it. Think of Git as the diary, and GitHub as a website where you can optionally publish and share that diary.

---

## What does Git actually store?

Here's a common misconception: Git does **not** store a list of "changes" (like "line 5 changed from X to Y"). Instead, every time you commit, Git stores a **snapshot** — a full picture of what every file looked like at that exact moment. Like taking a photo of your whole desk, not just noting "the pen moved."

Each snapshot gets a unique ID, called a **hash** (something like `a1b2c3d`). No two snapshots ever share the same ID. You'll see these IDs constantly — they're simply how Git labels and refers to a specific saved moment in time.

---

## The three areas you need to know

Every file in a Git project lives in one of three "zones." You'll use these words constantly, so it's worth slowing down here:

```
Working Directory  →  Staging Area (Index)  →  Repository (.git/)
   (your files)         (what's queued)          (saved history)
```

- **Working Directory** — the actual folder on your computer. Where you open files and type. This is just normal editing, nothing Git-specific happens here yet.
- **Staging Area** — a waiting room. Before a commit is saved, you choose exactly which changes go into it. Nothing here is permanent yet.
- **Repository** — the permanent, saved history, stored inside a hidden `.git/` folder. Once something's here, it's part of your project's memory.

Don't worry about memorising this yet — you'll *use* these three zones hands-on in the very next module, and it'll click fast.

---

## Why Git beats "backup folders"

Before Git, people (maybe you too!) tried to solve this with folders full of files like `app_v1.py`, `app_v2_final.py`, `app_v2_final_REAL.py`. It kind of works for a day. Here's why it falls apart, and what Git gives you instead:

| Approach | Problem |
|---|---|
| `app_v1.py`, `app_v2_final.py` | Turns to chaos after a week — which one is "real"? |
| Google Drive version history | No way to work on an experiment separately, no way to combine two people's changes |
| Git | Full history, safe experiments (branches), combining work (merging), and easy collaboration |

---

## ✅ Quick recap

- Git = remembers every saved version of your files, forever.
- A **commit** = a saved snapshot, made on purpose by you.
- Git ≠ GitHub. Git is the tool; GitHub is a website that hosts a copy.
- Every project has three zones: Working Directory → Staging Area → Repository.

Next up: initialising a repo and configuring Git for the first time.
