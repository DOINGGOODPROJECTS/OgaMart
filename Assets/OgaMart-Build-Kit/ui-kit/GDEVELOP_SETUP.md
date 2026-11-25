# Setting up the OgaMart UI in GDevelop

This guide uses the object names from the live demo (`scripts/demo/index.html`). You can use other names, but then change them in the code too.

## 1. Project settings

- **Game resolution:** 1170 x 2532, portrait. Set "Resize mode" to adapt the width so the layout stays the same on every phone.
- **Fonts:** add `fonts/Inter-*.otf` and `fonts/Poppins-*.ttf` as resources. Text objects then use them. Font sizes for each style are in `TEXT_STYLES.md` (already at 3x).
- **Layers:** use three layers. "Base" holds the store and street, "UI" holds the bars, cards and nav, and "Popup" holds the dim overlay, sheets, pop-ups and toasts. Keep the UI and Popup layer cameras still.

## 2. Load the script once

1. At the top of the scene's events, add a **JavaScript code** event with the condition "At the beginning of the scene".
2. Paste the whole of `scripts/ogamart_ui.js` into it, then add this line at the end:

```js
gdjs.ogaUI.init(runtimeScene);
```

3. Add a second **JavaScript code** event with no condition, so it runs every frame:

```js
gdjs.ogaUI.update(runtimeScene);
```

Every snippet below goes into a JavaScript code event: either the start-of-scene one, or one under a normal condition such as "Variable Coins changed".

## 3. Top bar

| Object name | Type | File |
|---|---|---|
| TopBar | Tiled Sprite | 01_topbar/topbar_bg.png |
| LevelBadge + LevelText | Sprite + Text (Poppins Bold 66, ink) | 01_topbar/level_badge.png |
| XPTrack | Panel Sprite (margins L12 R12 T0 B0) | 01_topbar/xp_bar_track.png |
| XPFill | Panel Sprite (margins L12 R12 T0 B0), same X and Y as XPTrack | 01_topbar/xp_bar_fill.png |
| CoinPill, HappyPill | Panel Sprite (margins 48) | 01_topbar/stat_pill.png |
| CoinIcon, HappyIcon | Sprite | icon_coin.png, icon_happiness.png |
| CoinText, HappyText | Text (Inter Bold 42, white) | – |
| SettingsBtn | Sprite with animations "Normal" and "Pressed" | settings_button.png, settings_button_pressed.png |

```js
// at scene start: connect the XP bar and show the saved values
const v = runtimeScene.getVariables();
gdjs.ogaUI.bindBar(runtimeScene, 'xp', 'XPTrack', 'XPFill', v.get('XP').getAsNumber() / v.get('XPNeeded').getAsNumber());
gdjs.ogaUI.setText(runtimeScene, 'CoinText', gdjs.ogaUI.fmt(v.get('Coins').getAsNumber()));
gdjs.ogaUI.makeButton(runtimeScene, 'SettingsBtn', [], 'Pressed');
```

```js
// when the player earns coins and XP (e.g. a sale)
const v = runtimeScene.getVariables();
const coins = v.get('Coins').getAsNumber();
gdjs.ogaUI.countTo(runtimeScene, 'CoinText', coins, coins + 5, 0.5);   // number rolls up
v.get('Coins').setNumber(coins + 5);
const xp = gdjs.ogaUI.addXP(runtimeScene, 'xp', v.get('XP').getAsNumber(), 10, v.get('XPNeeded').getAsNumber(), function (leftover) {
  // level up: runs when the bar reaches the end
  v.get('Level').add(1);
  gdjs.ogaUI.setText(runtimeScene, 'LevelText', v.get('Level').getAsNumber());
  gdjs.ogaUI.confetti(runtimeScene, 'Confetti', 60);
});
v.get('XP').setNumber(xp);
```

## 4. Bottom navigation

| Object name | Type | Notes |
|---|---|---|
| NavBg | Tiled Sprite | 02_nav/nav_bg.png |
| NavActive | Panel Sprite (margins 42) | 02_nav/nav_tab_active.png, the gold tile that slides |
| NavIcon | Sprite with animations "active" and "inactive" | 5 instances, instance variable **Index** = 0 to 4 (shop, neighborhood, missions, upgrades, profile) |
| NavLabel | Text (Inter Bold 30) | 5 instances, instance variable **Index** |
| NavHit | Sprite (any image, opacity 0) | 5 invisible tap areas, instance variable **Index** |
| NavBadge | Sprite + Text | 02_nav/nav_badge.png |

```js
// scene start (each screen sets its own tab: 0 shop, 1 neighborhood, 2 missions, 3 upgrades, 4 profile)
gdjs.ogaUI.makeButton(runtimeScene, 'NavHit');
gdjs.ogaUI.setNav(runtimeScene, 0, 0);
```

```js
// every frame: tapping a tab slides the highlight, then changes scene
if (gdjs.ogaUI.clicked('NavHit')) {
  const hit = runtimeScene.getObjects('NavHit').find(o => gdjs.ogaUI.cursorIn(runtimeScene, o));
  if (hit) {
    const i = hit.getVariables().get('Index').getAsNumber();
    gdjs.ogaUI.setNav(runtimeScene, i);
    runtimeScene.getVariables().get('GoToTab').setNumber(i);   // then use a normal event: "Change scene" after 0.25 s
  }
}
```

## 5. Buttons (every screen)

1. Make the button background a Panel Sprite. For example, use `04_buttons/button_primary.png` with margins of 48 px.
2. Put a Text on it for the label, and an icon Sprite if needed.
3. Register it once at scene start:

```js
gdjs.ogaUI.makeButton(runtimeScene, 'AcceptBtn', ['AcceptLabel']);   // the label moves down with the button
```

4. Then react to the tap every frame:

```js
if (gdjs.ogaUI.clicked('AcceptBtn')) { /* do the action */ }
```

You can also use a normal event condition: scene variable `UIClicked` = "AcceptBtn".

If you prefer a pressed *image* instead of the push-down, use a Sprite with two animations: "Normal" (`button_primary.png`) and "Pressed" (`button_primary_pressed.png`). Then pass `'Pressed'` as the last argument of `makeButton`.

| Button | File | Label colour |
|---|---|---|
| Main action (green) | button_primary | white |
| Money or reward (gold) | button_gold | ink |
| Secondary (cream) | button_ghost | ink |
| Locked or disabled | button_off | muted #5C4A38 |
| Dialogue choice | choice_primary / choice_white (large, 52pt) | white / ink |
| Close on dark background | button_outline_light | white |
| Danger | button_red | white |

## 6. Progress bars on cards (missions, stock, ripple, deliveries, achievements)

Use any `05_progress/barXX_track_*` plus `barXX_fill_*` pair. Both are Panel Sprites with margins of half the height on the left and right, and 0 on the top and bottom.

```js
gdjs.ogaUI.bindBar(runtimeScene, 'stock', 'StockTrack', 'StockFill', 12 / 30);   // scene start
gdjs.ogaUI.setBar('stock', 30 / 30, 0.8);   // later: slides to full in 0.8 s
```

- **Skill and relationship segments:** 5 Sprites with "on"/"off" animations and an **Index** variable from 0 to 4. Light them up with `gdjs.ogaUI.setSegments(runtimeScene, 'SkillSeg', 4)`.
- **Round timer:** one Sprite with 9 frames (`timer_ring_fill_0` to `_8`) on top of `timer_ring_track`. Start it with `gdjs.ogaUI.startTimer(runtimeScene, 'rush', 134, 'RushTimeText', 'RushRing', () => { /* rush over */ })`.

## 7. Chips, tabs and segmented controls

| Object name | Type | Notes |
|---|---|---|
| SegBg | Panel Sprite | 07_chips_pills/segmented_bg.png |
| SegHi | Panel Sprite | 07_chips_pills/segmented_active.png, the moving highlight |
| SegOpt | Sprite (opacity 0) | one per option, variable **Index** |
| SegLabel | Text | one per option, variable **Index** |

```js
gdjs.ogaUI.makeButton(runtimeScene, 'SegOpt');   // scene start
gdjs.ogaUI.setSegment(runtimeScene, 'SegHi', 'SegOpt', 1, 'SegLabel');
```

```js
// every frame
if (gdjs.ogaUI.clicked('SegOpt')) {
  const o = runtimeScene.getObjects('SegOpt').find(o => gdjs.ogaUI.cursorIn(runtimeScene, o));
  if (o) gdjs.ogaUI.setSegment(runtimeScene, 'SegHi', 'SegOpt', o.getVariables().get('Index').getAsNumber(), 'SegLabel');
}
```

Filter chips work the same way: use `chip_active` as the highlight and `chip_inactive` behind each option.

## 8. Settings controls

- **Switch or checkbox:** a Sprite with animations "on" (`toggle_on` / `checkbox_on`) and "off", plus an instance variable **On**. Register it with `makeButton(runtimeScene, 'MusicToggle')`, then call `if (gdjs.ogaUI.clicked('MusicToggle')) gdjs.ogaUI.flipToggle(runtimeScene, 'MusicToggle');`
- **Slider:** set it up with `gdjs.ogaUI.makeSlider(runtimeScene, 'music', 'MusicTrack', 'MusicFill', 'MusicKnob', 0, 100, 60, 'MusicVolume', 1);`. The value is saved in the scene variable `MusicVolume` while dragging. Use it with the "Set volume" action.

## 9. Pop-ups, sheets and toasts

Put all the parts of one pop-up on the Popup layer and hide them at the start. Then call these with the list of object names:

```js
// Welcome back / Level up card: bounces in over the dark overlay. Buttons behind it stop working until it closes
gdjs.ogaUI.popIn(runtimeScene, ['WelcomeCard', 'WelcomeRibbon', 'WelcomeTitle', 'CollectBtn', 'CollectLabel'], 'Dim');
gdjs.ogaUI.popOut(runtimeScene, ['WelcomeCard', 'WelcomeRibbon', 'WelcomeTitle', 'CollectBtn', 'CollectLabel'], 'Dim');

// Build something / shelf details: slides up from the bottom
gdjs.ogaUI.openSheet(runtimeScene, ['Sheet', 'SheetHandle', 'SheetTitle', 'SheetClose'], 'Dim');
gdjs.ogaUI.closeSheet(runtimeScene, ['Sheet', 'SheetHandle', 'SheetTitle', 'SheetClose'], 'Dim');

// Toast: "Happiness +3  Mama Biggie loved your discount"
gdjs.ogaUI.setText(runtimeScene, 'ToastTagText', 'Happiness +3');
gdjs.ogaUI.toast(runtimeScene, ['ToastCard', 'ToastTag', 'ToastTagText', 'ToastText'], 2.5, '"Mama Biggie loved your discount!"');
```

- **Dim** is a Tiled Sprite using `09_dialogue/dim_overlay.png`, stretched over the whole screen.
- The **dialogue** screen uses the same pop-in: name_plate, speech_bubble with speech_pointer, choice buttons and the character's portrait or full image.

## 10. Effects

```js
gdjs.ogaUI.floatUp(runtimeScene, ['RewardPop', 'RewardCoin', 'RewardText'], 150, 1.1);   // "+15" floats up and fades
gdjs.ogaUI.coinFly(runtimeScene, 'FlyCoin', x, y, 'CoinPill', 6, () => { /* coins arrived */ });   // FlyCoin = Sprite coin_big.png
gdjs.ogaUI.confetti(runtimeScene, 'Confetti', 60);   // Confetti = Sprite, animations c1..c6 = confetti_1..6.png
gdjs.ogaUI.pulse(runtimeScene, 'AlertDot', 0.15, 0.9);   // red "!" on a shelf
gdjs.ogaUI.pulse(runtimeScene, 'HighlightRing', 0.12, 0.8);   // tutorial ring
gdjs.ogaUI.bob(runtimeScene, 'TutorialArrow', 18, 0.8);   // tutorial arrow
gdjs.ogaUI.spin(runtimeScene, 'LevelRays', 12);   // level-up rays
```

## 11. Without JavaScript

Everything above can also be done with GDevelop's built-in **Tween** behavior:

- **Bar fill:** add the Tween behavior to the fill and use "Tween width" to (track width x value), over 0.5 s, easing easeOutCubic.
- **Button press:** on "Touch or left mouse button is down" and "cursor is on the object", move it down 6 px; on release, move it back and do the action.
- **Toast and sheets:** "Tween Y position" in, wait, then out.
- **Coins:** "Tween a number" on a scene variable, then set the text each frame.

The JavaScript file just saves you from building these events again for every screen.

## 12. Placing parts exactly as in the mockups

Open `layout/<screen>.json`. Every element has x, y, w and h in pixels for the 1170x2532 screen, plus:

- `kit_asset`: the file to use
- `text`, `font`, `size`, `weight`, `color`: for text

`layout/annotated/` shows the same thing visually. Characters are marked in pink; take them from the character pack.
