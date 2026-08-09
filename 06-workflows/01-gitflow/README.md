# Gitflow 🌱

## 📖 In plain words

Gitflow is simply an agreed-upon *set of rules* for what branches to create and when — nothing new about Git itself, just a shared convention a team follows. It was invented by Vincent Driessen in 2010 to answer a common question: "when we have features, releases, and emergency fixes all happening at once, which branch does what?"

Think of it like a formal promotion pipeline: feature → develop → release → main, with hotfix lanes for prod emergencies.

---

## The branches

| Branch | Purpose | Merges from | Merges into |
|--------|---------|-------------|-------------|
| `main` | Production code. Tagged with release versions. | `release/*`, `hotfix/*` | — |
| `develop` | Integration branch. All features land here first. | `feature/*` | `release/*` |
| `feature/*` | One branch per feature. Created from develop. | `develop` | `develop` |
| `release/*` | Stabilisation branch. Bug fixes only, no new features. | `develop` | `main` + `develop` |
| `hotfix/*` | Emergency fix to production. | `main` | `main` + `develop` |

---

## The lifecycle

```
main ──────────────────────────────────── v1.1 ──
       ↑                                    ↑
develop ──── feature/A ──── feature/B ──── release/1.1 ──
                                                     ↓
                                               hotfix/1.0.1 ──
```

1. Branch `feature/login` from `develop`
2. Work on feature, merge back to `develop`
3. When develop is ready to ship, cut `release/1.2` from `develop`
4. Bug-fix only on `release/1.2`
5. Merge `release/1.2` into `main` (tag `v1.2`) AND back into `develop`
6. If prod breaks: branch `hotfix/1.2.1` from `main`, merge into `main` AND `develop`

---

## Commands

```bash
# Start a feature
git switch develop
git switch -c feature/my-feature

# Finish a feature
git switch develop
git merge --no-ff feature/my-feature
git branch -d feature/my-feature

# Start a release
git switch -c release/1.2 develop

# Finish a release
git switch main
git merge --no-ff release/1.2
git tag -a v1.2 -m "Release 1.2"
git switch develop
git merge --no-ff release/1.2
git branch -d release/1.2
```

---

## When to use Gitflow

- Projects with scheduled release cycles
- Multiple versions in production simultaneously (must support v1.x and v2.x)
- Regulated environments where release sign-off is required

---

## When NOT to use Gitflow

- Web apps deploying multiple times a day (trunk-based is better)
- Small teams with fast iteration cycles
- SaaS where you only support the current version

Gitflow was designed for software shipped on a release schedule (CDs, binaries, desktop apps). For continuous delivery, see module 06-02.

---

## ✅ Quick recap

- Gitflow = a set of team conventions for branch names and merge rules, not a Git feature.
- Branches: `main` (prod), `develop` (integration), `feature/*`, `release/*`, `hotfix/*`.
- Good fit for scheduled releases and multiple supported versions.
- Poor fit for fast-shipping web apps — see trunk-based development next.
