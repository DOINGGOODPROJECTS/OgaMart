# Week 2: Neighborhood development

**Paste this into Claude Code to start week 2:**

> Read `CLAUDE.md`, `CLAUDE_CODE_PROMPT.md` (sections 5 to 7) and `weeks/WEEK2_TASKS.md`. Week 1 is done (see `PROGRESS.md`). Do the week 2 tasks in order. Stop at the end of each day, show me what you did and how to test it, and wait for my OK.

**Goal (design doc 14.2.4, week 2):** a playable neighborhood connected to the supermarket.

## Day 1: Neighborhood scene
- [ ] Build the `Neighborhood` scene from `ui-kit/layout/OgaMart-2-Neighborhood.json` and `layout/OgaMart-34-Stage1-Corner-Shop-Neighborhood.json`. Use the same top bar and nav as the Shop scene.
- [ ] Build the street from `assets/neighborhood`:
  - sky (day)
  - road and sidewalk tiles
  - the OgaMart exterior for the current store style (`OgaMartExterior` animations)
  - trees, streetlights and benches
- [ ] Add the 2 starting houses (`residential_basic`) on residential plots.
- [ ] The camera can be dragged left and right to explore the street, within limits. The UI layer stays still.
- **Check:** a screenshot next to `screens/OgaMart-2-Neighborhood.png` and `OgaMart-34`. List the differences, then fix them.

## Day 2: Construction plots and building
- [ ] Add `Plot` objects with an `Index` variable and a `Kind` variable (commercial or residential), using the "for sale" plot art from `assets/neighborhood/construction`.
- [ ] Build the **Build Something** bottom sheet (screen 2):
  - category chips
  - building cards with cost, lock and level
  - it slides up with `openSheet`
- [ ] Add build preview (screen 17): the building appears on the chosen plot with **Place**, **Rotate** and **Cancel**.
- [ ] **Place** calls `gdjs.ogaBridge.buildOn(type, plot)`. Show the construction stages (`construction_1` to `_3`) for a few seconds with the dust effect, then the building.
- **Check:** I can't build without enough coins or on a taken plot. Coins drop by the right amount.

## Day 3: Two business types and income
- [ ] Add the Coffee Shop (level 4) and the Bakery (level 6), each a Sprite with animations `basic`, `established` and `premium`.
- [ ] Income piles up in each building (`ogaGame.tick`). A coin bubble shows above a building when coins are ready, and tapping it calls `collectAt()`. Coins then fly to the coin pill.
- [ ] Building income also counts while the game is closed, through the offline report. Welcome Back is added in week 3.
- **Check:** in 5 minutes of play, the coffee shop earns about 20 coins (240 coins an hour). This must match `ogaGame.buildingIncome()`.

## Day 4: Building upgrades and management
- [ ] Build the `BusinessManage` scene from `layout/OgaMart-18-Coffee-Shop-Management.json`:
  - collect
  - upgrade
  - the "I manage it / Staff runs it" segmented control
  - stats
- [ ] Building upgrades go Basic → Established → Premium, with the image changing on the street. This uses `upgradeBuilding()`.
- [ ] Tapping a built building opens `BusinessManage`. Tapping the OgaMart exterior goes back to `Shop`.
- **Check:** after an upgrade, both the building image and its income change.

## Day 5: Pedestrians, vehicles and navigation
- [ ] Pedestrians walk along the sidewalk in both directions, at random intervals. Use `Ped_*` and the unlocked customer and character Sprites with their walk animations. Never have more than 6 at once.
- [ ] Cars, the taxi and the danfo drive along the road with simple looping.
- [ ] Scene navigation: all 5 nav tabs work (Shop, Neighborhood, Missions, Upgrades, Profile). Use simple placeholder Missions and Profile scenes if they aren't built yet.
- [ ] Coins, XP and stock carry over between scenes. The `gdjs.ogaGame` state persists, with nothing reset when changing scenes.
- **Check:** going back and forth 20 times doesn't duplicate customers or listeners, and doesn't leak objects.

## Day 6–7: Connect finances, tests and fixes
- [ ] Supermarket and neighborhood share one coin balance. The more buildings and homes there are, the more customers come into the shop (`traffic` and `houses` in the data).
- [ ] Add tests:
  - building cost and income per hour
  - upgrade cost and multiplier
  - free plots
  - traffic goes up after building
  - offline income is capped at 4 hours
- [ ] Run `node --test tests/` and `node tests/simulate.js 6`. Both must pass. Update `PROGRESS.md` and commit: "Week 2: neighborhood development".

**Week 2 deliverable:** I reach level 4, open the neighborhood, build the coffee shop, collect its coins, upgrade it, and see more customers in the shop.
