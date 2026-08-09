# Deploy Workflow

CI tests your code. CD (Continuous Deployment/Delivery) ships it. A deploy workflow runs after a merge to `main` and pushes the new version to wherever it needs to go.

For a platform engineer: this is your GitOps pipeline. Code merge → automated deploy → running in cluster. The same pattern you know from ArgoCD, but triggered by GitHub Actions instead of watching a repo.

---

## The pattern

```yaml
on:
  push:
    branches: [main]    # trigger: merge to main

jobs:
  test:
    ...                 # CI must pass first

  deploy:
    needs: test         # only run if test job passes
    runs-on: ubuntu-latest
    environment: production   # uses GitHub environments for approvals
    steps:
      - ...             # deploy steps
```

The `needs: test` dependency ensures CI passes before deploying. If tests fail, deploy never runs.

---

## GitHub Environments

Environments add deployment controls on top of workflows:
- **Required reviewers**: a human must approve before deploy runs
- **Wait timer**: delay deployment (e.g., wait 10 minutes after merge)
- **Environment secrets**: separate secrets per environment (e.g., different AWS keys for staging vs prod)

Set up: Settings → Environments → New environment → `production`

---

## Example: Deploy to a server via SSH

```yaml
  deploy:
    needs: test
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.DEPLOY_HOST }}
          username: deploy
          key: ${{ secrets.DEPLOY_SSH_KEY }}
          script: |
            cd /app
            git pull origin main
            systemctl restart my-service
```

---

## Example: Build and push Docker image

```yaml
      - name: Log in to registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

## Example: Update a Kubernetes manifest (GitOps)

```yaml
      - name: Update image tag in manifest
        run: |
          sed -i "s|image: my-app:.*|image: my-app:${{ github.sha }}|" \
            k8s/deployment.yaml
          git config user.email "ci@github.com"
          git config user.name "GitHub Actions"
          git commit -am "ci: update image to ${{ github.sha }}"
          git push
```

This is the GitOps pattern: the workflow commits the new image tag back to the repo. ArgoCD picks up the change and deploys it. Fully automated, fully auditable.

---

## Staging before production

```yaml
jobs:
  deploy-staging:
    needs: test
    environment: staging
    ...

  deploy-production:
    needs: deploy-staging   # prod only after staging succeeds
    environment: production
    ...
```

A three-stage pipeline: test → deploy-staging → deploy-production. Each step is gated.
