# Daily Strategy Drill

10 minutes a day for logic, reasoning and strategy. Static site for GitHub Pages. Three modes, linked by tabs at the top:

- **Today's Drill** (`index.html`) shows the newest drill; `?d=YYYY-MM-DD` opens an older one. Drills live in `data/drills.json`. The daily routine adds one object per day (same fields as the existing entry) and commits.
- **Idea Forge** (`forge.html`) helps you think outside the box. Type an idea, draw 3 lens cards from different books plus a random twist (a constraint or mash-up), answer each, then combine the best answers. Results save to an idea vault in your browser and can be copied out. Cards and twists live in `data/cards.json`.
- **Quiz** (`quiz.html`) asks 10 random multiple-choice questions, each with a short explanation, and tracks your best score. Questions live in `data/quiz.json`.

The decks and questions draw on these books: Great Mental Models, $100M Offers, the Naval Almanack, The Art of Focus, How to Start Your Own Business Without Losing Your Shirt, From the Trash Man to the Cash Man, Lead Funnels, Brick & Mortar Funnels, The Copywriter's Handbook, The Greatest Salesman in the World, Getting Things Done and The 33 Strategies of War.

To add a card, add `{"deck": "<deck key>", "title": "...", "prompt": "..."}` to `cards`. To add a question, add `{"src", "q", "a", "w": [3 wrong answers], "why"}` to `quiz.json`.

Scores, the vault and deck choices are stored in the browser (localStorage), so they don't sync between devices.

Pages setting: Settings > Pages > Deploy from branch `wc-final.pdf`, folder `/ (root)`. This folder lives inside the `Worldcup` repo (next to `8ball/`), so the site is at `https://greenerhealthwny-crypto.github.io/Worldcup/daily-strategy-drill/`.
