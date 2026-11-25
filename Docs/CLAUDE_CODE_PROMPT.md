# Build OgaMart in GDevelop: full prompt for Claude Code

You are building **OgaMart**, a mobile supermarket and neighborhood management game, as a **GDevelop 5** project that exports to Android. Everything you need is in this folder: the design document, all the art, a UI kit, the 42 UI/UX screens, and working game-logic scripts. Your job is to turn them into a real, playable GDevelop project that looks exactly like the screens and plays like the design document.

Read this whole prompt before you start. Then read `CLAUDE.md`, which has the short version of the rules you must keep following.

---

## 1. What is in this folder

Before doing anything, check that these are present. If something is missing, stop and tell me which one.

| Folder | What it is |
|---|---|
| `docs/OgaMart-Design-Document.txt` | The game design document. **It is the source of truth for game rules.** |
| `screens/` | The 42 UI/UX screens, `OgaMart-1-Shop.png` … `OgaMart-42-...png` (1170×2532), plus `OgaMart-Game-Interface.pdf`. **They are the source of truth for how every screen looks.** |
| `assets/` | Unzipped `OgaMart-GDevelop-Assets-Full.zip`: characters (34, all animations and portraits), store objects, 59 products, neighborhood buildings (3 levels each), vehicles, sky, tiles, effects, name tags. Each subfolder has PNGs plus `manifest.json` and `asset_names.csv`. |
| `ui-kit/` | Unzipped `OgaMart-UI-Kit.zip`: 487 UI parts, `ui_kit_manifest.json` (object type and 9-slice margins for every file), `layout/<screen>.json` (every element of every screen with x, y, w, h, text, font, colour and `kit_asset`), `layout/annotated/`, `TEXT_STYLES.md`, `design_tokens.json`, `fonts/`, `GDEVELOP_SETUP.md`, `scripts/ogamart_ui.js` and `scripts/demo/`. |
| `scripts/game/ogamart_data.js` | All game data: products, prices, levels 1–25, unlocks, buildings, customers, staff, suppliers, events, missions, characters, dialogues, stories, achievements. |
| `scripts/game/ogamart_game.js` | The game logic (economy, customers, checkout, stock, XP and levels, indicators, ripple, buildings, offline earnings, missions, staff, dialogues, events, save/load). It contains no GDevelop calls, and it already runs and is balance-tested in node. |
| `scripts/game/ogamart_bridge.js` | Connects the logic to GDevelop objects and to the UI kit: top bar, nav, shelves, walking customers, toasts, pop-ups, dialogue, lists. |
| `scripts/ui/ogamart_ui.js` | The UI kit motion helpers: bars, count-up numbers, button press, nav slide, toasts, sheets, sliders, timers, coin fly, confetti. |
| `tests/simulate.js` | A bot that plays the logic headlessly and prints when each level is reached (`node tests/simulate.js 6`). |

## 2. The approach (important)

A GDevelop project is a JSON file (`game.json`) plus resource files. You cannot click around the GDevelop editor, so you will **generate the project with code**:

1. **Learn the exact file format first.** Ask me to do this once, and wait until I confirm:
   > "Open GDevelop 5 (latest version), create an empty project called OgaMart in `game/`, resolution 1170×2532 portrait. Add one Sprite object with 2 animations, one Panel Sprite, one Tiled Sprite, one Text object, one BBText object, an object group, an External events sheet, a scene with a 'JavaScript code' event and a normal event using the Tween behavior, then save."

   Then read `game/game.json` carefully and copy its exact structure, property names and version numbers. Never invent fields. If you are unsure about a field, look at what GDevelop wrote.
2. **Write a generator**: `tools/build-project.mjs` (Node, no extra framework). It reads the manifests, the layout JSONs and the scripts, copies the needed PNGs into `game/assets/...`, and writes `game/game.json`. Running it twice must give the same result. **Never hand-edit `game.json`**: change the generator and run it again.
3. **Keep the generator split in small modules** under `tools/`:
   - `resources.mjs`: registers images and fonts.
   - `objects.mjs`: builds Sprite, Panel Sprite and Tiled Sprite objects from the manifests.
   - `layout.mjs`: turns `ui-kit/layout/<screen>.json` into instances.
   - `scenes/*.mjs`: one per scene.
   - `events.mjs`: builds normal and JavaScript events.
4. **Validate after every run.** Check that the JSON parses, every resource file exists, every object referenced in an event exists, and every instance's object exists. If the npm package `gdcore-tools` works on this machine, use it to load the project headlessly and export an HTML5 build. Then open that build with Playwright and screenshot each scene. If it doesn't work, build a browser preview harness instead: reuse `ui-kit/scripts/demo/fake_gdjs.js` and the same scripts so logic and layout can still be checked.
5. **Ask me to open the project in GDevelop** at the end of each milestone. I will report any errors or screenshots back to you.

## 3. Project settings

- **Resolution:** 1170×2532 portrait. Resize mode: adapt width. Pixel-perfect off, smoothing on. Orientation: portrait.
- **Fonts:** load every file in `ui-kit/fonts/` as font resources. Text styles come from `ui-kit/TEXT_STYLES.md`; sizes are already in px for 1170×2532.
- **Layers in every main scene:**
  - `Base`: store or street art
  - `Actors`: characters, z-sorted by feet Y
  - `UI`: top bar, cards, nav
  - `Popup`: dim overlay, sheets, modals, toasts
- **Global variables:** `Dialogue` (string), `MusicVolume`, `SfxVolume`, `Language`.
- **Scene variables:** `GoToScene` (string), `UIClicked` (string), `ActorScale` (number, default 0.5), `OpenProductPicker` (number).
- **Android:** package `com.ogamart.game`, name "OgaMart". Generate the icons from `assets/ui` or `assets/store/signage`.

## 4. Loading the scripts

GDevelop JavaScript events cannot import files, so the generator puts the code into the project:

1. Create an **External events sheet called `Boot`**. Its first event is a JavaScript code event with the condition "At the beginning of the scene". Paste the full contents of these files into it, in this order, inside `if (!gdjs.ogaBridge) { ... }` so they only load once per game:
   1. `scripts/ui/ogamart_ui.js`
   2. `scripts/game/ogamart_data.js`
   3. `scripts/game/ogamart_game.js`
   4. `scripts/game/ogamart_bridge.js`
2. Every scene links `Boot` at the top. It then has:
   - one JavaScript event at the beginning of the scene: `gdjs.ogaBridge.startScene(runtimeScene, '<SceneName>');`
   - one JavaScript event every frame: `gdjs.ogaBridge.update(runtimeScene);`
   - one normal event: if scene variable `GoToScene` is not "", then **Change scene** to that value and clear it.
3. Every time you edit a file in `scripts/`, rerun the generator so the project picks up the change.

**Keep the scripts as the single source of truth for game rules.**

- **Balance:** change numbers in `ogamart_data.js`, then run `node tests/simulate.js 20`. The targets are: level 4 within 5 minutes, first business by about 10 minutes (design doc section 3.10), level 10 in 1–3 hours, and level 25 in 12–25 hours of active play.
- **Logic changes:** add or adjust them in `ogamart_game.js`, and add a check to `tests/` for each one.
- **Screen and object wiring:** goes in `ogamart_bridge.js`, or in normal GDevelop events when that is simpler.

## 5. Building objects from the assets

Read the manifests. Do not guess sizes.

**Characters** (`assets/characters/<group>/<Name>/`):
- One Sprite object per character, named exactly like the folder (for example `MamaBiggie`, `Cust_Regular`, `Emp_Cashier`).
- Animations come from the file names `<Name>_<anim>_<n>.png`:
  - `idle`, `walk` (8 frames, loop, 0.08 s)
  - `talk`, `happy`, `angry`, `surprised`, `sad`, `wave`, `point`, `think`, `shrug`, `thumbs`, `celebrate`
  - signature animations: `hip_dance`, `wave_bag`, `adjust_glasses`, `scratch_head`, `jump`, `dance`, `stomp`, `victory_dance`, `trad_dance`, `show_produce`, `confetti`, `explain`, and the rest
  - work poses: `scan`, `restock`, `carry`, `check`, `pick_item`, `pay`, `impatient`
  - `run` for Speedy Sam, Daniel and Emp_Delivery
- Origin point and center point at the feet: bottom center of the 640×920 frame. Walk frames face right; flip for left.
- Portraits (`<Name>_portrait_<expression>.png`) go in a separate Sprite object `<Name>Portrait` with one animation per expression.

**Shelves:**
- One Sprite object `Shelf`. It has one animation per `<category>_<material>` (`wood`, `metal`, `premium`), and each animation has 5 frames: `stock_1` to `stock_5`.
- Other equipment stock levels work the same way: fridges, the chest freezer, the produce stand and the bakery case.

**Products:**
- One Sprite object `ProductIcon`, with one animation per product id.
- The id is the file name without `product_`. It must match the ids in `ogamart_data.js`.

**Buildings:**
- One Sprite object per building type, named like the data id (`coffee_shop`, `bakery`, ...).
- Each has animations `basic`, `established` and `premium`.
- The OgaMart exteriors are one Sprite object `OgaMartExterior`, with one animation per store style.

**UI parts:**
- Use the `gdevelop_object` field in `ui_kit_manifest.json`.
- Panel Sprites take their margins from `nine_slice_px`. Files starting with `tiled_` become Tiled Sprites.
- Button states become Sprite animations (`Normal` and `Pressed`) when a button needs an image swap.
- List buttons whose colour changes become a Sprite with animations `primary`, `gold`, `ghost` and `off`.
- Toast tags become a Sprite with animations `green`, `orange`, `blue`, `red` and `gold`.

**Vehicles, sky, overlays and effects:** use them in the Neighborhood and stage street scenes, the level-up screen and the effects.

**Naming:** keep object names exactly as listed in `ui-kit/GDEVELOP_SETUP.md` and in the comments at the top of each section of `ogamart_bridge.js` (for example `CoinText`, `XPFill`, `NavIcon` with an `Index` variable, `ShelfSpot` with `Index`). If you need a different name, change the bridge too.

## 6. Scenes to build (each must match its screen PNG)

Place every element using `ui-kit/layout/<screen>.json`: x, y, w and h are the exact pixel box. Use `kit_asset` for the image, and the `text`, `font`, `size`, `weight` and `color` fields for Text objects. Elements whose `kind` is `character` use the character Sprites. Big `art` regions, such as the store interior and the street, are built from the store and neighborhood assets rather than screenshots.

| Scene | Screen(s) | Notes |
|---|---|---|
| `Loading` | – | OgaMart logo, progress bar, then `Shop` |
| `Shop` | 1, 27, 23, 28, 33, 35, 37, 39, 41 | The main game: store interior for the current stage, shelves, checkout counters, walking customers, action card, toasts, rush banner, VIP card, tutorial tips, Welcome Back and Level Up pop-ups. The store look changes by stage: Corner Shop, Mini Market, Supermarket, Superstore, Mega Market (screens 33–41). |
| `Neighborhood` | 2, 17, 34, 36, 38, 40, 42 | Street with plots, buildings (3 levels), pedestrians, vehicles, day/night sky, the Build sheet, build preview with Place / Rotate / Cancel, and coin bubbles to collect |
| `Dialogue` | 3 | Character big image, name plate, relationship tag, speech bubble, choice buttons. Driven by `ogaData.dialogues` |
| `Missions` | 6 | Chips, mission cards with progress bars and Accept / Ignore / Claim |
| `Upgrades` | 7 | Chips by category; cards with Lv and cost, locked cards |
| `Profile` | 8 | Level path, stats, achievements preview, links |
| `Ripple` | 9 | Three gauges and the "What happened" list |
| `Performance` | 10 | KPIs and units sold |
| `CharacterProfile` | 11 | Story chapters, relationship bar, actions |
| `HireStaff` | 12 | Candidate card with skills and wage; other candidates |
| `PricingSuppliers` | 13, 29 | Price slider, Low / Competitive / Premium segmented control, preview tiles, suppliers, deliveries with timers |
| `StyleShop` | 14 | Cosmetics only (doc section 10.5); purchases are stubbed |
| `Settings` | 15 | Sliders, checkboxes, links |
| `RippleReport` | 16 | Daily report |
| `BusinessManage` | 18 | Building management: collect, upgrade, I manage it / Staff runs it |
| `Inventory` | 19 | Stock per product and storage, Restock all |
| `Employees` | 20 | Staff list: assign, train, details, promotion |
| `LayoutEdit` | 21 | Move shelves on a grid; valid/invalid frames; keep customer paths clear |
| `FoodFestival` | 22 | Event screen with optional offers |
| `Characters` | 5, 24 | Collection grid: met, stories, not met |
| `LevelUp` | 25 | Can also be a pop-up inside `Shop` |
| `Rewards` | 26 | Optional rewarded ads (stub `ogaBridge.showRewardedAd`) |
| `ManualCheckout` | 28 | Scan item / Take payment calls `ogaGame.manualScan()` |
| `Achievements` | 30 | Uses `ogaGame.achievementList()` |
| `Levels` | 31, 32 | Roadmap 1–25 from `ogaData.levels` |

Lists with more rows than fit on screen must scroll: drag the content layer, clamped. For repeated rows, create one set of row objects with an `Index` variable, as `ogaBridge.fillList` expects.

## 7. How things must move (no static UI)

Use the helpers in `ogamart_ui.js` through the bridge:

- **Bars:** XP, stock, missions, gauges and delivery bars slide to their new value.
- **Numbers:** coins and happiness count up and down.
- **Buttons:** push down when pressed; nothing reacts to taps behind an open pop-up.
- **Nav:** the gold highlight slides between tabs.
- **Messages and pop-ups:** toasts slide in and out; pop-ups bounce in over the dim overlay; sheets slide up.
- **Effects:** "+coins" floats up at the counter; coins fly to the coin pill; the level up shows rays, confetti and a toast; the alert dot and tutorial ring pulse; the tutorial arrow bobs.
- **Characters:** walk between door, shelves, queue, counter and exit. They play happy, angry or sad reactions with emotion bubbles; characters with a dialogue ready show a "!" and open `Dialogue` when tapped.
- **Timers:** rush events and deliveries count down.
- **Neighborhood life:** cars and the danfo drive along the road; pedestrians walk; the sky changes between day, sunset and night with the night tint and lamp glow.

The live demo `ui-kit/scripts/demo/index.html` shows the expected feel.

## 8. Milestones (stop after each one, show me, and wait for my OK)

**M0 – Setup**
- Folder check, the GDevelop format sample from me, the generator skeleton, a project that opens in GDevelop with the `Loading` and an empty `Shop` scene.
- Tests pass: `node tests/simulate.js 3`.

**M1 – Playable prototype (design doc section 14.2)**
- `Shop` scene fully working: 3 shelves (bread, milk, eggs), restocking, 3 customer types walking and buying, automatic checkout, coins and XP, levels 1–5, shelf and checkout upgrades.
- Customer Happiness, Mama Biggie walking in with her eggs dialogue, 3–5 missions, the Coffee Shop and Bakery in `Neighborhood`, saving and loading, offline earnings with Welcome Back, and the first-10-minutes hints from section 3.10.
- Acceptance: I can play 15 minutes, reach level 5, build the coffee shop, close and reopen the game and get Welcome Back.

**M2 – All screens**
- Every scene in the table above, laid out from the layout JSONs.
- Acceptance: side-by-side screenshots of each scene next to its reference PNG, with differences listed and fixed.

**M3 – Full content**
- Levels 1–25 with all unlocks, the five store stages with their looks, every building with 3 levels, every character and dialogue/story in the data, staff hiring, training and promotion, suppliers and deliveries, pricing strategies, rush and VIP events, the Neighborhood Trust and Business Growth indicators, the ripple report, and achievements.

**M4 – Polish and Android**
- Sound effects and music hooks (volume from Settings), a performance pass (object pooling for customers, at most 12 actors), an Android export guide, an optional AdMob rewarded ad hook (never required to progress, doc section 10.3), and a localization-ready text table.

After each milestone, update `PROGRESS.md` with what's done, how to test it in GDevelop, and the known issues. Then commit with a clear message.

## 9. Rules

- **Follow the design document.** Player freedom, optional tutorials, no forced orders, ads always optional, offline earnings capped at 4 hours, and 25 levels with play continuing after level 25.
- **Use the provided art only.** Do not redraw, recolour or restyle anything. If an asset is truly missing, list it in `PROGRESS.md` and use the closest existing one.
- **Match the screens.** Layout, colours, fonts and text come from `ui-kit/layout`. Wording on the screens can come from the data (for example real prices and real levels).
- **Keep the code readable.** Use small files and short comments written in plain language. Use no frameworks inside the game: only GDevelop and the given scripts.
- **Keep the tests green.** Never break `tests/simulate.js`. Add tests when you change logic.
- **Ask before deleting anything**, and before changing any decision listed here.
- **Ask me** whenever the design document and a screen disagree. Until I answer, follow the screen for looks and the document for rules.

Start with M0. Begin by listing what you found in each folder and asking me for the GDevelop format sample.
