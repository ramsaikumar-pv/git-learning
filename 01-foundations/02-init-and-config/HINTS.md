# Hints

<details>
<summary>Hint 1 — git status says "No commits yet" — is that an error?</summary>

No. "On branch main / No commits yet / nothing to commit" is exactly what you expect from a fresh, empty repo. Git knows you're on the `main` branch but there's nothing to track yet. Add a file and the message will change.

</details>

<details>
<summary>Hint 2 — git config --list shows duplicate keys — which one wins?</summary>

Git reads config from three levels: system (`/etc/gitconfig`), global (`~/.gitconfig`), and local (`.git/config`). Each level overrides the one above. So if you set `user.email` both globally and locally, the local value wins for that repo. `--show-origin` tells you exactly which file each line comes from so you can spot conflicts.

</details>

<details>
<summary>Hint 3 — I already have config from a previous install — how do I change it?</summary>

Run `git config --global user.name "New Name"` — it overwrites the existing value. Or open `~/.gitconfig` in `vi` and edit it directly. The file is plain text. After saving, `git config --list` will show the updated value immediately.

</details>
