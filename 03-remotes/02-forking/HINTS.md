# Hints

<details>
<summary>Hint 1 — git log HEAD..upstream/main shows nothing — does that mean my fork is current?</summary>

Yes. `HEAD..upstream/main` shows commits that are in `upstream/main` but NOT in your current branch (`HEAD`). If there's no output, your fork already has everything upstream has. Your fork is up to date.

If you want to see commits you have that upstream doesn't (the reverse):

```bash
git log upstream/main..HEAD
```

</details>

<details>
<summary>Hint 2 — git fetch upstream says "fatal: repository not found" or "Permission denied"</summary>

Check the upstream URL you added. Run `git remote -v` and verify the `upstream` URL matches the original repo exactly. A typo in the username or repo name will fail. Remove and re-add if needed:

```bash
git remote remove upstream
git remote add upstream git@github.com:CORRECT-OWNER/CORRECT-REPO.git
git fetch upstream
```

</details>

<details>
<summary>Hint 3 — I want to make changes to the forked repo — do I commit directly to main?</summary>

No. Always work on a feature branch, even in your fork:

```bash
git switch -c my-feature
# make changes
git add . && git commit -m "My change"
git push origin my-feature
```

Then open a pull request from `ramsaikumar-pv/repo:my-feature` to `original-owner/repo:main`. This keeps your `main` clean and always syncable with upstream. If you commit directly to your fork's `main`, syncing with upstream becomes messier (you'll get conflicts every time).

</details>
