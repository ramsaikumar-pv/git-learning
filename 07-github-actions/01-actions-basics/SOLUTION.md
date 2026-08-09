# Solution

## Workflow run output: "Say hello" step
```
Hello from GitHub Actions! Branch is main
```

## "Show repo info" step
```
Repo: ramsaikumar-pv/my-project
SHA: b7e1f3a4c2d8e9f0a1b3c4d5e6f7a8b9c0d1e2f3
Actor: ramsaikumar-pv
```

The `${{ }}` syntax is evaluated at runtime by the Actions runner, substituting real values from the trigger context.

## "List files" step
```
total 32
drwxr-xr-x 4 runner docker 4096 Aug  5 17:00 .
drwxr-xr-x 8 runner docker 4096 Aug  5 17:00 ..
drwxr-xr-x 3 runner docker 4096 Aug  5 17:00 .github
-rw-r--r-- 1 runner docker  234 Aug  5 17:00 app.py
-rw-r--r-- 1 runner docker  145 Aug  5 17:00 config.yaml
...
```

The runner has your repo files because `actions/checkout@v4` cloned them.

## How long does it take?

A simple workflow (checkout + echo) typically takes 10-20 seconds. Most of that is provisioning the runner VM. The actual steps run instantly.

## Workflow status in the Actions tab

Each run shows:
- Green checkmark ✅ = all jobs passed (exit code 0)
- Red X ❌ = a step failed (non-zero exit code)
- Yellow dot 🟡 = queued or in progress
- Grey circle = skipped

Click a run → click a job → click a step to see the full output.

## The yaml `|` multiline block

```yaml
- run: |
    VAR="hello"
    echo $VAR       # can access VAR from the line above
    ls -la
```

All lines share the same shell instance. This is different from running separate steps — in separate steps, environment variables don't carry over (unless you write to `$GITHUB_ENV`).
