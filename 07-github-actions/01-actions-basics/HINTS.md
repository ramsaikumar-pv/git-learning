# Hints

<details>
<summary>Hint 1 — The workflow isn't appearing in the Actions tab</summary>

Check:
1. The file is in `.github/workflows/` (correct path, correct directory name)
2. The file has a `.yml` or `.yaml` extension
3. The YAML syntax is valid — YAML is indentation-sensitive. Use consistent spaces (not tabs)
4. The `on:` trigger matches what you did (e.g., `on: push` with a branch filter that includes your branch)

Validate your YAML locally:
```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/hello.yml'))"
```

If Python isn't available: paste the YAML into yamllint.com

</details>

<details>
<summary>Hint 2 — What's `${{ github.ref_name }}` — where do these variables come from?</summary>

These are GitHub Actions context variables — metadata GitHub injects into every workflow run:

- `github.ref_name` — branch or tag name that triggered the run
- `github.sha` — full commit hash
- `github.repository` — `owner/repo-name`
- `github.actor` — who triggered the run (username)
- `github.event_name` — what triggered it (`push`, `pull_request`, etc.)

Full list: search "GitHub Actions contexts" in GitHub docs. You access them with `${{ context.property }}` syntax in YAML.

</details>

<details>
<summary>Hint 3 — What's the difference between `run: echo` and `run: |`?</summary>

`run: echo "..."` — single-line command. Only one line.

`run: |` — multi-line command block. The `|` is YAML literal block scalar syntax. Everything indented below it is one multi-line shell script:

```yaml
- run: |
    echo "Line 1"
    echo "Line 2"
    ls -la
    python --version
```

Each line runs in the same shell instance, so environment variables set on line 2 are visible on line 3. Use `|` for any step with more than one command.

</details>
