# Challenge

## Challenge 1: Squash merge

Normally a merge brings in all commits from the feature branch. A squash merge collapses them into one:

```bash
git merge --squash feature/add-metrics
git commit -m "Add metrics endpoint (squashed)"
```

Compare `git log --oneline --graph --all` before and after. What happened to the individual commits from the feature branch? Is the feature branch still visible in the graph?

When would you prefer a squash merge over a regular merge?

---

## Challenge 2: Merge commit message best practices

When Git opens the editor for a merge commit, write a meaningful message:

```
Merge branch 'feature/add-metrics'

Adds /metrics endpoint returning request counters.
Required by the ops team for Prometheus scraping.
Closes #42.
```

Check it with `git log`. Does the full body show up? Does `git log --oneline` just show the subject?

---

## Challenge 3: Merge without switching branches

You don't have to switch to the target branch before merging. You can use `git merge` from wherever you are and specify the target branch explicitly... except Git requires you to be on the branch you're merging INTO.

Research and answer: is there a way to merge branch A into branch B while you're on branch C? (Hint: look at `git fetch` + merge, or just accept the answer is "switch first.")

---

## Bonus: What is an octopus merge?

Run `git merge branch1 branch2 branch3` — merging three branches at once. This is called an octopus merge. When would this be useful? What are the limitations? (Hint: conflicts.)
