# Challenge

## Challenge 1: Negation patterns

`.gitignore` supports negation with `!`:

```
logs/
!logs/important.log
```

This ignores everything in `logs/` EXCEPT `logs/important.log`.

1. Create a `logs/` directory with three files: `app.log`, `error.log`, `important.log`.
2. Set up `.gitignore` to ignore all logs but keep `important.log`.
3. Verify with `git status` — which file shows up?

Note: negation order matters. The `!` rule must come AFTER the ignore rule.

---

## Challenge 2: Per-directory .gitignore

`.gitignore` files can exist in any subdirectory and apply only to that directory and below:

```bash
mkdir subproject
echo "*.tmp" > subproject/.gitignore
```

The `*.tmp` pattern now only applies inside `subproject/`. Test it: create `test.tmp` in the repo root and `subproject/test.tmp`. Which one is ignored?

---

## Challenge 3: .gitignore and git add --force

Sometimes you NEED to add an ignored file intentionally:

```bash
git add --force some-file.log
```

When would you need this? Think of vendor dirs, compiled CSS that you intentionally commit, or a specific config file that's mostly ignored but one copy is needed.

Add an ignored file with `--force`, commit it, then verify it's tracked even though `.gitignore` would otherwise exclude it.

---

## Bonus: Global gitignore for editor files

Set up a global gitignore so you never accidentally commit Vim swap files:

```bash
git config --global core.excludesfile ~/.gitignore_global
echo "*.swp" >> ~/.gitignore_global
echo "*.swo" >> ~/.gitignore_global
echo ".DS_Store" >> ~/.gitignore_global
```

Now create a `.swp` file in any repo and run `git status`. It should not appear.
