# Challenge

## Challenge 1: Add a production environment with approval

1. Create a `production` environment in GitHub settings.
2. Add yourself as a required reviewer.
3. Extend the workflow:

```yaml
  deploy-production:
    needs: deploy-staging
    environment: production
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deployed to production! SHA=${{ github.sha }}"
```

Push to main. The staging deploy runs automatically. The production deploy waits for your approval in the GitHub UI (Actions tab → review pending deployments). Approve it.

---

## Challenge 2: Build a Docker image

Update the deploy job to build a Docker image:

```yaml
      - name: Build Docker image
        run: |
          docker build -t my-app:${{ github.sha }} .
          docker images my-app
```

Create a `Dockerfile` in your repo:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

Does the build succeed? Push the image to GitHub Container Registry (ghcr.io) using `docker/build-push-action`.

---

## Challenge 3: GitOps manifest update

Simulate the GitOps pattern:

```yaml
      - name: Update manifest with new image tag
        run: |
          sed -i "s/image: my-app:.*/image: my-app:${{ github.sha }}/" k8s/deployment.yaml
          git config user.email "actions@github.com"
          git config user.name "GitHub Actions"
          git diff
          git add k8s/deployment.yaml
          git commit -m "ci: deploy sha ${{ github.sha }}"
          git push
```

Create a `k8s/deployment.yaml` with a placeholder image tag. After the workflow runs, check: does the file in GitHub show the new SHA? This is exactly how teams like Weaveworks do GitOps — the pipeline writes to the infra repo and the CD controller (ArgoCD/Flux) does the actual deploy.

---

## Bonus: Reusable workflows

GitHub Actions supports calling one workflow from another (like a function call):

```yaml
# In caller workflow:
jobs:
  deploy:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
    secrets: inherit
```

Research: when would you extract a workflow into a reusable workflow? How is this similar to Helm chart templates — abstracting deployment logic so multiple repos can use the same pipeline?
