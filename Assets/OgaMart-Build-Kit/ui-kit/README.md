# OgaMart UI Kit for GDevelop

Every interface part used in the 42 OgaMart UI/UX screens, cut into separate pieces so they can move, stretch and react in the game. The colours, corners, shadows and fonts come from the same code that drew the screens, so they match the mockups.

## 487 parts, in 14 groups

- **Top and bottom bars:** the top bar, level badge, XP bar, coin and happiness pills, settings button, and the bottom navigation with an active and inactive version of each tab icon.
- **Buttons:** every colour (green, gold, cream, white, red, disabled) has a normal and a pressed version. There are large dialogue choice buttons, outline buttons and round arrow buttons.
- **Progress bars:** each bar is two pieces, a back and a fill, in 8pt and 10pt sizes and six colours. Also skill segments, stage-path circles, level-roadmap markers and a 9-frame round timer.
- **Cards and labels:** cards, list rows, tiles, a coloured card and avatar circle for each of the 12 characters, filter chips, tag pills and segmented controls.
- **Settings controls:** switches, checkboxes, and sliders with a draggable knob.
- **Pop-ups and messages:** dialogue name plate and speech box, Welcome Back card and ribbon, bottom sheet, toasts, the "+15" reward, the red "!" alert and the rush timer banner.
- **Tutorial and layout editing:** highlight ring, tutorial arrow, placement frames, floor grid and move arrows.
- **Level up:** light rays, the big level circle, confetti and the coin effect.
- **Icons:** 40 icons, each in 7 colours.
- **Fonts:** Inter and Poppins, both free to use in a game.

## What moves (preview/ui_kit_in_action.gif shows this)

- Progress bars slide when their value changes. The XP bar fills to the end, resets, and triggers the level up with confetti.
- Coin and happiness numbers roll up and down.
- Buttons push down when tapped.
- The gold nav highlight slides to the tab you tap.
- Toasts slide in and out. Pop-ups bounce in and sheets slide up over a dark layer, and the buttons behind them stop working while they're open.
- Sliders can be dragged, switches flip, and segmented controls slide to the chosen option.
- Coins fly to the coin counter, "+15" floats up and fades, the alert dot and tutorial ring pulse, the tutorial arrow bobs, and the level-up rays spin.
- Timers count down.

## Using it in GDevelop

- `scripts/ogamart_ui.js`: paste it once into a JavaScript event at the start of a scene. GDEVELOP_SETUP.md gives the object names to create and a copy-paste snippet for each moving part. It also explains how to do the same with GDevelop's built-in Tween behavior if you'd rather not use code.
- `scripts/demo/index.html`: open it in Chrome to try every moving part. It's built only from the kit PNGs and the same script.

## Matching the UI/UX

- `layout/` has a file for each of the 42 screens. It lists every box, text, icon and character with its position, size, colour and font, and which kit part it is. All 3,041 elements are listed.
- `layout/annotated/` shows each screen with every kit part labelled.
- SCREENS.md lists the parts each screen uses, and TEXT_STYLES.md lists every text style.

Everything is made for a 1170x2532 portrait game, the same size as the screen PNGs. Characters, products and buildings come from the OgaMart asset pack (OgaMart-GDevelop-Assets-Full.zip).

## Two limits

- The text isn't drawn on the buttons and cards. You add it in GDevelop as Text objects, so labels can change and be translated.
- The font for the biggest titles, Poppins ExtraBold, isn't included. Poppins Bold is the closest match in the kit, or you can download ExtraBold free from Google Fonts.

## What is inside

| Folder | Files |
|---|---|
| `01_topbar` | 10 |
| `02_nav` | 13 |
| `03_header` | 4 |
| `04_buttons` | 28 |
| `05_progress` | 38 |
| `06_cards` | 48 |
| `07_chips_pills` | 19 |
| `08_inputs` | 9 |
| `09_dialogue` | 10 |
| `10_modals_sheets` | 9 |
| `11_toasts` | 10 |
| `12_tutorial_edit` | 12 |
| `13_levelup_rewards` | 11 |
| `14_icons` | 266 |
| **Total** | **487 PNGs** |

- `assets/`: all PNGs, at 3x (made for a 1170x2532 portrait game, the same size as the screen PNGs).
- `scripts/ogamart_ui.js`: the code that makes the parts move: progress bars that fill, counting coins, button press, nav slide, toasts, pop-ups, sheets, sliders, switches, timers, coin fly, confetti and pulsing hints.
- `scripts/demo/index.html`: a live demo built only from these PNGs and that script. Open it in Chrome to see everything move (`preview/ui_kit_in_action.gif` shows it).
- `GDEVELOP_SETUP.md`: step by step setup in GDevelop, with copy-paste code for each moving part.
- `layout/`: every element of every one of the 42 screens (position, size, colour, font, text) and which kit part it is. `layout/annotated/` shows each screen with labels on every part.
- `SCREENS.md`: list of the kit parts each screen uses.
- `TEXT_STYLES.md`: every text style (font, size, weight, colour) used in the screens.
- `ASSET_LIST.md` and `ui_kit_manifest.json`: every file, its GDevelop object type, size and 9-slice margins.
- `design_tokens.json`: colours, corner sizes and layout sizes.
- `fonts/`: Inter and Poppins (the two fonts used in the UI).
- `preview/`: labelled sheets of every part.

## The parts that move or stretch

- **Progress bars** (XP, missions, happiness, stock, delivery, ripple gauges): every bar is two pieces, a *track* and a *fill*. The script changes the fill width smoothly, so the bar slides when the value changes. They come in 8pt and 10pt sizes and six colours.
- **Round timers**: 9 frames (0% to 100%) for delivery and rush countdowns.
- **Buttons**: every colour has a normal and a *pressed* image. The script also pushes the button and its label down 2pt while the finger is on it.
- **Panels** (cards, buttons, pills, chips, sheets, pop-ups): 9-slice images (Panel Sprite in GDevelop). They stretch to any size and the corners stay round.
- **Nav bar**: a gold highlight slides to the tapped tab. Each tab icon has an active and an inactive image.
- **Chips and segmented controls**: the highlight slides to the chosen option.
- **Switches and checkboxes**: on and off images.
- **Sliders**: track, fill and a knob you can drag (music, sound, price).
- **Toasts**: slide down, wait, then slide away.
- **Pop-ups and bottom sheets**: bounce in or slide up over a dark overlay. Buttons behind them are blocked while they are open.
- **Effects**: the "+15" reward floats up, coins fly to the coin counter while the number counts up, confetti falls, the level-up rays spin, the alert dot and tutorial ring pulse, and the tutorial arrow bobs.

## Quick start

1. In GDevelop, set the game resolution to **1170 x 2532** (portrait).
2. Add the fonts from `fonts/` as resources.
3. Drag the PNGs you need from `assets/` into your scene. Use **Panel Sprite** for files with 9-slice margins (see `ASSET_LIST.md`), **Tiled Sprite** for bars and backgrounds marked TiledSprite, and **Sprite** for the rest.
4. Paste `scripts/ogamart_ui.js` into a JavaScript code event at the start of the scene, then follow `GDEVELOP_SETUP.md`.
5. Use `layout/<screen>.json` or the annotated images to place each part exactly as in the mockup.

Characters, products, buildings and other art come from the OgaMart asset pack (OgaMart-GDevelop-Assets-Full.zip).
