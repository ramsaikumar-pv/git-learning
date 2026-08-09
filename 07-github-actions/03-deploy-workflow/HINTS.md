# Hints

<details>
<summary>Hint 1 — The deploy job runs on PRs even though I added an `if` condition — why?</summary>

Check your `if` condition carefully:

```yaml
if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

This should only be true when:
- The ref is `refs/heads/main` (not a PR branch)
- The event is `push` (not `pull_request`)

On a PR, `github.event_name` is `pull_request` and `github.ref` is the PR's ref (like `refs/pull/1/merge`). Both conditions are false, so the job should be skipped.

If the job still runs, check if you accidentally removed the `if:` or have a typo. The job should show as "Skipped" (not green, not red) in the Actions UI when the condition is false.

</details>

<details>
<summary>Hint 2 — The deploy job shows "Skipped" even on a push to main — why?</summary>

Check `needs: test`. If the `test` job is skipped (e.g., no test files found), `needs: test` considers it "not succeeded" and skips the deploy job too.

Also check: the `if:` condition evaluates BEFORE the job runs. If it evaluates to false, the job is skipped. Double-check your `github.ref` — in some contexts it might be `main` not `refs/heads/main`.

Try: `if: github.ref_name == 'main'` — this uses the short branch name which is simpler to compare.

</details>

<details>
<summary>Hint 3 — What is $GITHUB_STEP_SUMMARY and where do I see it?</summary>

`$GITHUB_STEP_SUMMARY` is a special file that GitHub Actions renders as a Markdown summary on the workflow run's page. When your step writes to it:

```bash
echo "### Deployment Complete 🚀" >> $GITHUB_STEP_SUMMARY
```

GitHub renders the Markdown in a "Summary" panel at the bottom of the workflow run page. It's visible without clicking into individual step logs. Useful for showing key deployment info at a glance: what was deployed, to where, at what time.

Go to: Actions tab → your workflow run → scroll down to see the "Summary" section.

</details>
