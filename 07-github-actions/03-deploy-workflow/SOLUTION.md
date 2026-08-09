# Solution

## On push to main: both jobs run

```
Jobs:
  ✅ Test       (1m 12s)
  ✅ Deploy to Staging  (45s, ran after Test)
```

`needs: test` means Deploy only starts after Test completes successfully.

## On a PR: only test runs

```
Jobs:
  ✅ Test       (1m 12s)
  ⊘ Deploy to Staging  (skipped)
```

The `if:` condition evaluated to false because `github.event_name` is `pull_request` and `github.ref_name` is not `main`. Deploy is skipped — shown as a grey ⊘ circle, not a failure.

## The artifact in the Actions UI

After deploy runs, go to the run page → scroll down → "Artifacts" section:

```
release-b7e1f3a4c2d8e9f0a... (12 KB)
```

Download it and unzip. You'll find `app.py`, `config.yaml`, and `build.info`:

```
BUILD_SHA=b7e1f3a4c2d8e9f0a1b3c4d5e6f7a8b9c0d1e2f3
BUILD_TIME=2026-08-05T17:30:00Z
```

This is a build artifact — a versioned, reproducible snapshot of what was deployed. The `retention-days: 7` setting means GitHub keeps it for 7 days then deletes it.

## The $GITHUB_STEP_SUMMARY

On the workflow run page, scroll to the bottom:

```markdown
### Deployment Complete 🚀
- **SHA**: `b7e1f3a`
- **Branch**: `main`
- **Time**: Mon Aug  5 17:30:00 UTC 2026
```

Rendered as a formatted summary. Visible at a glance without clicking through step logs.

## Why this pattern matters for GitOps

In a real GitOps setup, replace the "Upload artifact" step with:
- Pushing a Docker image to a registry
- Updating a Kubernetes manifest with the new image tag
- Pushing the manifest change to an infra repo that ArgoCD watches

ArgoCD detects the manifest change and deploys automatically. The GitHub Actions workflow is the trigger; ArgoCD is the executor. CI + GitOps = fully automated, fully auditable deployments.
