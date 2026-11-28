# Daily Strategy Drill

10 minutes a day for logic, reasoning and strategy. Static site for GitHub Pages.

- `index.html` shows the newest drill; `?d=YYYY-MM-DD` opens an older one.
- `data/drills.json` holds every drill. The daily routine adds one object per day (same fields as the existing entry) and commits.
- Pages setting: Settings > Pages > Deploy from branch `main`, folder `/ (root)`. This folder lives inside the `Worldcup` repo (next to `8ball/`), so the game is served at `https://<user>.github.io/Worldcup/daily-strategy-drill/`.
