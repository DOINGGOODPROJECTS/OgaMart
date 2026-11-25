# Week 1: Supermarket gameplay

**Paste this into Claude Code to start week 1:**

> Read `CLAUDE.md`, `CLAUDE_CODE_PROMPT.md` (sections 1 to 5) and `weeks/WEEK1_TASKS.md`. Do the week 1 tasks in order. Stop at the end of each day, show me what you did and how to test it, and wait for my OK.

**Goal (design doc 14.2.4, week 1):** a playable supermarket where customers buy products and the player earns coins.

## Day 1: Project setup
- [ ] Check the folders (`docs/`, `screens/`, `assets/`, `ui-kit/`, `scripts/`, `tests/`) and list what you found. Tell me anything missing.
- [ ] Set up git with a `.gitignore` for `node_modules/` and GDevelop build output. Make the first commit.
- [ ] Ask me for the GDevelop sample project (CLAUDE_CODE_PROMPT.md section 2, step 1). Read the `game.json` I save and write down its exact structure in `tools/FORMAT_NOTES.md`.
- [ ] Create `tools/build-project.mjs` with its modules: `resources.mjs`, `objects.mjs`, `layout.mjs`, `events.mjs` and `scenes/`.
- [ ] Generate a project with the `Loading` scene and an empty `Shop` scene. It uses resolution 1170×2532 portrait, the fonts from `ui-kit/fonts`, and the `Base`, `Actors`, `UI` and `Popup` layers.
- [ ] Create the `Boot` external events with the 4 scripts inside `if (!gdjs.ogaBridge)`. Every scene must link it.
- [ ] Run `node tests/simulate.js 3`. It must pass.
- **Check:** I open `game/game.json` in GDevelop and it loads with no errors. Preview goes from Loading to Shop.

## Day 2: Shop scene and UI frame
- [ ] Build the `Shop` scene from `ui-kit/layout/OgaMart-1-Shop.json`: top bar, nav bar and the shelf action card, with every part at its exact position.
- [ ] Create the objects named in the bridge: `LevelText`, `StageText`, `CoinText`, `HappyText`, `XPTrack`, `XPFill`, `NavIcon`, `NavLabel` and `NavHit` (each with an `Index` variable), `NavActive`, the toast group, `RewardPop`, `RewardCoin` and `RewardText`.
- [ ] Build the store interior for stage 1 (Corner Shop) from `assets/store`: floor and wall tiles, the bakery, eggs and dairy units, the checkout counter, lights and the sign.
- [ ] Use the fonts and sizes from `ui-kit/TEXT_STYLES.md`.
- **Check:** a screenshot of the `Shop` scene next to `screens/OgaMart-1-Shop.png`. List the differences, then fix them.

## Day 3: Products and shelf inventory
- [ ] Create the `Shelf` Sprite with animations `<category>_<material>`, each with 5 frames (`stock_1` to `stock_5`). Add 3 instances with `Index` 0, 1 and 2, plus `ShelfLabel` and `ShelfAlert`.
- [ ] Create `ProductIcon`, with one animation per product, and `CardThumb`.
- [ ] Unlock five products: bread, milk and eggs at the start, then water and biscuits (or soda) at level 3. These come from `ogamart_data.js`.
- [ ] Wire up the shelves:
  - tapping a shelf selects it and fills the action card (name, stock, cost, price, profit)
  - **Restock** fills the shelf, charges coins, slides the stock bar and changes the shelf image
  - **Product** opens a small sheet to change the product
- **Check:** restocking costs the right amount (bread at 3 coins each). The shelf image changes from empty to full, and the red "!" shows when stock is low.

## Day 4: Customers and automatic checkout
- [ ] Create a Sprite object for each of the 3 starting customer types, `Cust_Regular`, `Cust_FamilyMom` and `Cust_Budget`, with their idle, walk, happy, angry and sad animations. Put the origin at the feet.
- [ ] Add invisible markers: `Door`, `Exit`, `ShelfSpot` (`Index`), `QueueSpot` (`Index` 0–7) and `CounterSpot` (`Index`).
- [ ] Customers come from the bridge's `customer_enter` and `customer_move` events. They walk door → shelves → queue → counter → exit, sorted by feet Y, and turn to face the way they walk.
- [ ] Add emotion bubbles (the `Bubble` Sprite) when a product is missing or too expensive.
- [ ] Automatic checkout: customers pay at the counter. "+coins" floats up and the coin number counts up.
- **Check:** for 5 minutes, customers walk naturally, nobody gets stuck, there are never more than 12 on screen, and the coins add up correctly.

## Day 5: Coins, upgrades and XP
- [ ] Build the `Upgrades` scene from `layout/OgaMart-7-Upgrades.json`, using the bridge's `fillList('Upgrade', ...)`.
- [ ] Basic upgrades:
  - shelf capacity (from the action card's **Upgrade** tile)
  - checkout speed
  - add a shelf
  - plants and decor
- [ ] XP and levels 1 to 5:
  - the XP bar slides
  - a Level Up pop-up appears with rays, confetti and the unlock list
  - unlocks are applied from `ogaData.levels`
- [ ] Nav switches between `Shop` and `Upgrades`, with the gold highlight sliding.
- **Check:** after a level up, the level badge, the stage text and the XP bar are all correct.

## Day 6–7: Tests and fixes
- [ ] Add `tests/logic.test.js`, using Node's built-in test runner and no packages. It must check:
  - restock cost and stock
  - a sale adds the right coins and the right XP
  - the sales XP cap works
  - level-up unlocks are applied
  - upgrades change capacity and speed
  - save and load keep the state
- [ ] Run `node --test tests/` and `node tests/simulate.js 3`. Both must pass.
- [ ] Fix every bug found this week. Update `PROGRESS.md` and commit: "Week 1: supermarket gameplay".

**Week 1 deliverable:** in GDevelop preview, I can restock 3 shelves, watch customers shop and pay, earn coins, buy upgrades and reach level 3 to 5.
