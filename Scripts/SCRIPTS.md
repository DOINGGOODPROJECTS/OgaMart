# Script quick reference

Load the scripts in this order:

1. `scripts/ui/ogamart_ui.js`
2. `scripts/game/ogamart_data.js`
3. `scripts/game/ogamart_game.js`
4. `scripts/game/ogamart_bridge.js`

## gdjs.ogaBridge (use in GDevelop)

| Call | When |
|---|---|
| `startScene(runtimeScene, 'Shop')` | At the beginning of every scene (use the scene's name) |
| `update(runtimeScene)` | Every frame |
| `goTo('Upgrades')` | Change screen. It saves, then sets scene variable `GoToScene`; a normal event does the Change scene |
| `toast(tag, text, color)` | Show a toast (color: green, orange, blue, red, gold) |
| `fillList(prefix, items)` / `rowTapped(prefix)` | Fill repeated rows (missions, upgrades) and read which row was tapped |
| `buildOn(type, plotObject)` / `collectAt(buildingObject)` | Neighborhood: build on a plot, collect coins |
| `showRewardedAd(done)` | Replace with your AdMob call. Ads are always optional |

## gdjs.ogaGame (game logic)

| Area | Functions |
|---|---|
| Start and save | `newGame()`, `load()` (returns the offline report), `collectOffline(doubled)`, `save()`, `reset()` |
| Every frame | `tick(seconds)` |
| Listen | `on(event, fn)`. Events: `coins`, `xp`, `levelup`, `sale`, `stock`, `stock_low`, `out_of_stock`, `customer_enter/move/react/exit`, `indicator`, `ripple`, `toast`, `mission_done`, `achievement`, `relationship`, `story`, `event_start/end`, `vip_done`, `build`, `delivery`, `dialogue_done`, `new_day` |
| Shelves | `shelfInfo(i)`, `restock(i)`, `restockAll()`, `upgradeShelf(i)`, `addShelf(product)`, `changeProduct(i, id)`, `buyStorage(id, qty)` |
| Prices | `price(id)`, `setPrice(id, coins)`, `setStrategy('low' or 'competitive' or 'premium')`, `pricePreview(id, coins)` |
| Upgrades | `upgradeList()`, `buyUpgrade(id)`, `checkoutSpeed()`, `setManualCheckout(on)`, `manualScan()` |
| Staff | `candidates()`, `hire(id, role)`, `train(id)`, `promote(id, role)`, `assign(id, role)`, `fire(id)`, `wagesPerDay()` |
| Neighborhood | `buildingList()`, `build(type, plot)`, `upgradeBuilding(id)`, `collectBuilding(id)`, `collectAll()`, `freePlots(kind)` |
| Characters | `characterList()`, `relLevel(id)`, `availableDialogues()`, `dialogue(id)`, `choose(id, choiceIndex)`, `storyInfo(id)`, `characterRequest(id)` |
| Missions | `missions()`, `acceptMission(uid)`, `ignoreMission(uid)`, `claimMission(uid)`, `achievementList()` |
| Events | `eventInfo()`, `startEvent(id)`, `fulfillVip()`, `declineVip()` |
| Numbers | `dashboard()`, `xpInfo()`, `stage()`, `indicatorStatus(value)` |

## gdjs.ogaUI (motion)

See `ui-kit/GDEVELOP_SETUP.md`. The main functions are:

- `bindBar` / `setBar`, `countTo`
- `makeButton` / `clicked`
- `setNav`, `setSegment`, `setToggle`, `makeSlider`
- `toast`, `popIn` / `popOut`, `openSheet` / `closeSheet`
- `floatUp`, `coinFly`, `confetti`, `pulse`, `bob`, `spin`
- `startTimer`
