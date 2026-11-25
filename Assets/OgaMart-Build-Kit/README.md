# OgaMart Build Kit

This folder is set up so **Claude Code** can build the full OgaMart game in GDevelop 5. It holds the brief, the game-logic scripts and the tests. You add the art and the screens yourself (step 2).

## 1. What is inside

| File or folder | What it is |
|---|---|
| `CLAUDE_CODE_PROMPT.md` | The full prompt for Claude Code: approach, scenes, objects, motion, milestones and rules. |
| `weeks/` | The same work split into week 1, week 2 and week 3 task lists, with a day-by-day checklist and a paste-ready starting line for each week. |
| `CLAUDE.md` | The short rules Claude Code reads automatically in every session. |
| `scripts/game/ogamart_data.js` | All game data from the design document: products, prices, levels 1–25 and their unlocks, buildings, customers, staff, suppliers, rush events, missions, the 12 characters, dialogues, stories and achievements. |
| `scripts/game/ogamart_game.js` | The whole game logic: stock and restocking, customers who browse, buy or leave, checkout queues, coins, XP and levels, the 3 neighborhood indicators, ripple events, buildings and income, offline earnings (4-hour cap), daily missions, staff, suppliers and deliveries, pricing strategies, dialogue choices and stories, VIP and rush events, achievements, and saving. |
| `scripts/game/ogamart_bridge.js` | Connects the logic to GDevelop objects and the UI kit: top bar, nav, shelves, walking customers, toasts, pop-ups, dialogue screen, lists. |
| `scripts/ui/ogamart_ui.js` | The UI kit motion helpers: moving bars, counting numbers, button press, sliders, sheets, toasts, confetti and more. |
| `scripts/game/ogamart_audio.js` | Plays the OgaMart sounds and music from game events. |
| `tests/simulate.js` | A bot that plays the game logic and prints when each level is reached, for balancing. |
| `docs/OgaMart-Design-Document.txt` | Your design document. |
| `SCRIPTS.md` | Quick reference of the script functions. |

## 2. Everything is already in place

This complete kit already contains every file Claude Code needs:

| Folder | What it is |
|---|---|
| `assets/` | The art pack: 34 characters with all their animations, store objects, 59 products, buildings, vehicles, sky, tiles and effects |
| `ui-kit/` | The UI kit: 487 interface parts, the layout of all 42 screens, fonts and setup guide |
| `audio/` | 56 sound effects, jingles and music loops |
| `screens/` | The 42 UI/UX screens and the PDF |

## 3. Start Claude Code

```bash
cd OgaMart-Build-Kit
git init && git add . && git commit -m "OgaMart build kit"
claude
```

Then work week by week (this follows the 3-week plan in section 14.2.4 of the design doc). Paste the line at the top of each file:

- `weeks/WEEK1_TASKS.md`: supermarket gameplay
- `weeks/WEEK2_TASKS.md`: neighborhood development
- `weeks/WEEK3_TASKS.md`: characters, Ripple system, saving, Android prototype

Or, to let Claude Code run everything as milestones: `Read CLAUDE_CODE_PROMPT.md and follow it. Start with milestone M0.`

Claude Code will first ask you to make a tiny sample project in GDevelop, so it can learn the exact file format your GDevelop version uses. It stops after each milestone so you can open the project in GDevelop and check it.

## 4. Test the scripts yourself (optional)

You need Node.js installed. Run:

```bash
node tests/simulate.js 6
```

It plays 6 hours of game time in about a second and prints when each level is reached. With the current numbers:

- level 4 (coffee shop): about 4 minutes
- level 10: about 1 hour 15 minutes
- level 25: about 16 hours
