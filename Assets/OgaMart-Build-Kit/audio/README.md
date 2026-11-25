# OgaMart Audio

56 original sounds made for OgaMart, each in **OGG** (best for GDevelop and Android) and **MP3**:

- 49 sound effects
- 3 jingles
- 4 music loops: shop, neighborhood, menu and rush

The music uses African pop styles: an afrobeat-style shop loop, a highlife-style neighborhood loop with guitar picking, marimba and shakers.

## Licence

These sounds were synthesized from scratch for this project, with no samples or recordings from anyone else. You can use them in OgaMart, including commercial releases, with no credit required.

## Files

| File | Length | When to play it |
|---|---|---|
| `sfx/ui_tap.ogg` | 0.05s | any button tap |
| `sfx/ui_tap_soft.ogg` | 0.05s | chips, list rows |
| `sfx/ui_back.ogg` | 0.08s | back button |
| `sfx/ui_toggle_on.ogg` | 0.11s | switch/checkbox on |
| `sfx/ui_toggle_off.ogg` | 0.11s | switch/checkbox off |
| `sfx/ui_error.ogg` | 0.29s | not enough coins, locked item |
| `sfx/ui_whoosh_open.ogg` | 0.3s | bottom sheet opens |
| `sfx/ui_whoosh_close.ogg` | 0.25s | sheet/pop-up closes |
| `sfx/ui_popup.ogg` | 0.48s | pop-up card bounces in |
| `sfx/ui_slider_tick.ogg` | 0.02s | slider moves (every step) |
| `sfx/toast.ogg` | 0.69s | toast slides in |
| `sfx/notification.ogg` | 0.62s | character notification bubble |
| `sfx/coin.ogg` | 0.36s | single coin / +coins float |
| `sfx/coins_many.ogg` | 0.69s | coin fly, collect offline earnings |
| `sfx/cash_register.ogg` | 0.9s | big sale, VIP paid |
| `sfx/sale.ogg` | 0.44s | customer pays at checkout |
| `sfx/scan_beep.ogg` | 0.09s | manual checkout scan |
| `sfx/restock.ogg` | 0.75s | shelf restocked |
| `sfx/shelf_upgrade.ogg` | 0.59s | shelf upgraded |
| `sfx/upgrade.ogg` | 0.88s | any store upgrade bought |
| `sfx/level_up.ogg` | 1.95s | level up pop-up |
| `sfx/mission_complete.ogg` | 1.0s | mission done / claimed |
| `sfx/achievement.ogg` | 1.26s | achievement unlocked |
| `sfx/confetti_pop.ogg` | 0.53s | confetti burst |
| `sfx/build_start.ogg` | 0.64s | construction starts |
| `sfx/build_complete.ogg` | 1.35s | building finished |
| `sfx/collect.ogg` | 0.33s | collect building coins |
| `sfx/door_chime.ogg` | 1.45s | customer enters (play sometimes) |
| `sfx/customer_happy.ogg` | 0.24s | happy customer bubble |
| `sfx/customer_angry.ogg` | 0.35s | angry customer bubble |
| `sfx/customer_sad.ogg` | 0.4s | sad customer bubble |
| `sfx/out_of_stock.ogg` | 0.3s | shelf empty |
| `sfx/footstep.ogg` | 0.05s | optional footsteps |
| `sfx/rush_start.ogg` | 0.62s | rush event starts |
| `sfx/timer_tick.ogg` | 0.03s | last 10 seconds of a timer |
| `sfx/timer_end.ogg` | 0.85s | timer ends |
| `sfx/vip_arrive.ogg` | 1.18s | VIP order card |
| `sfx/dialogue_open.ogg` | 0.43s | dialogue screen opens |
| `sfx/dialogue_blip.ogg` | 0.04s | text typing blip |
| `sfx/choice_select.ogg` | 0.36s | dialogue choice tapped |
| `sfx/relationship_up.ogg` | 1.0s | friendship level up |
| `sfx/relationship_down.ogg` | 0.52s | friendship drops |
| `sfx/delivery_arrive.ogg` | 0.6s | delivery arrives |
| `sfx/car_horn.ogg` | 0.25s | random car horn on the street |
| `sfx/tutorial_hint.ogg` | 0.8s | tutorial tip appears |
| `sfx/ad_reward.ogg` | 0.46s | rewarded ad bonus given |
| `sfx/purchase.ogg` | 1.46s | cosmetic purchase done |
| `sfx/mama_laugh.ogg` | 0.63s | Mama Biggie laughs / dances |
| `sfx/mama_huh.ogg` | 0.4s | Mama Biggie complains |
| `jingles/jingle_level_up.ogg` | 2.0s | longer level-up fanfare (Level Up screen) |
| `jingles/jingle_welcome_back.ogg` | 2.1s | Welcome Back pop-up |
| `jingles/jingle_grand_opening.ogg` | 1.05s | new business opens |
| `music/music_shop_loop.ogg` | 34.3s | Shop scene music (loop, 112 bpm afrobeat feel) |
| `music/music_neighborhood_loop.ogg` | 38.4s | Neighborhood music (loop, 100 bpm highlife feel) |
| `music/music_menu_loop.ogg` | 42.7s | Loading / menus / Settings (loop, 90 bpm) |
| `music/music_rush_loop.ogg` | 30.0s | during rush events (loop, 128 bpm) |

## Using them in GDevelop

1. Copy the `sfx`, `jingles` and `music` folders into your project, for example `game/assets/audio/`.
2. **Music:** use the action "Play the music" with the loop on, at volume 40–60. Switch tracks per scene. During a rush event, switch to `music_rush_loop`, then back afterwards.
3. **Sound effects:** use the action "Play a sound" at volume 70–90. Change the pitch a little (0.95–1.05) for repeated sounds like `coin` and `sale` so they don't sound robotic.
4. `scripts/game/ogamart_audio.js` plays all of these automatically from the game events. Load it after `ogamart_bridge.js`.
5. The Settings sliders set the volumes: scene variables `MusicVolume` and `SfxVolume` (0–100).

Open `preview.html` in Chrome to listen to every sound.
