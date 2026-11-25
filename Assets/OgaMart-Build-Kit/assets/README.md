# OgaMart – GDevelop Asset Pack (realistic 2D)

Everything in the OgaMart design document that can be drawn, as transparent PNGs ready for GDevelop, plus editable Inkscape SVG sources.

## Counts
- Characters: 1436 PNGs (34 characters: 12 recurring, 3 Daniel career looks, 7 staff, 9 customers incl. a child, 3 pedestrians)
- Store interior: 248 PNGs
- Products: 59 PNGs
- Neighborhood: 127 PNGs
- UI kit: 215 PNGs
- Name labels:
  - `preview/` has labeled sheets: every character and object with its name and file name under it.
  - `preview/characters/` has one labeled page per character showing every animation frame.
  - `asset_names.csv` lists every PNG with its readable name and folder.
  - `ui/name_tags/` has name-tag sprites for all 34 characters and every building type, ready to show in game.

## Import into GDevelop
1. Copy the folders into your GDevelop project folder (e.g. `assets/`).
2. Characters: create a **Sprite** object per character. Add one animation per name (idle, walk, talk, happy...). For each, click "+" and select all frames of that name together, e.g. `MamaBiggie_walk_1.png` … `MamaBiggie_walk_8.png`. GDevelop orders them by number.
3. Set the **origin point at the feet** (bottom centre of the frame). Every frame of every character uses the same 640×920 canvas, so poses don't jump when switching animations.
4. Walk/run frames face right. To walk left, use the action "Flip horizontally".
5. Suggested speeds: walk 0.08 s per frame (looping), idle 0.6 s, talk 0.18 s, dances and celebrations 0.15 s.
6. Files starting with `tiled_` (floors, walls, roads, grass) are seamless. Use them with a **Tiled Sprite** object.
7. `ui/buttons` and `ui/panels`: use a **Panel Sprite** (9-slice) with 36 px margins so they stretch without blurring.
8. Shelves, fridges, freezers and stands have 5 stock levels (`_stock_1` = empty … `_stock_5` = full). Put them in one Sprite as animation frames and change the frame to match stock.
9. Doors (`doors_auto_1-3`), coins (`coin_spin_1-6`), bursts, dust, payment pop, arrow and highlight ring are all short frame animations.

## Scale
- Characters and store interior share one scale: 270 px = 1 m (a person is about 460 px tall). Drop them into the same scene without resizing.
- Buildings and vehicles are drawn for the neighborhood map view (a smaller scale). Use them in the neighborhood scene.

## Characters and animations
Every character has these front-view animations: idle, talk, happy, angry, surprised, sad, wave, point, think, shrug, thumbs, celebrate. Every character also has an 8-frame side walk and 8 dialogue portraits (smile, talk, happy, laugh, angry, surprised, sad, neutral).

Signature animations from section 6.5:
- Mama Biggie: adjust glasses, hands on hips, waving handbag, hip-shake dance, laugh. Walks with a hip sway.
- Daniel: scratches head, jumps, dances, run. His career looks are Daniel_Cashier, Daniel_Supervisor and Daniel_Manager, who walks confidently.
- Sofia: dance, dramatic pose, surprise.
- Mr. Brooks: adjusts mustache, stomps, victory dance, "ignore" pose.
- Papa Kofi: laughs while adjusting his hat, shows produce, traditional dance, dramatic reaction.
- Maya: big wave, confetti, explaining gestures.
- Also: Speedy Sam runs, Grandpa Wisdom walks with his stick, Madam Fashion struts and poses, Uncle Money shows off his watch, Auntie Pepper is impatient, Mrs. Parker checks prices.
- Staff have work poses: scan, restock, carry, check.
- Customers have shopping poses: pick item, pay, impatient.

- `MamaBiggie` (recurring, walk: sway): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, adjust_glasses ×2, hands_hips ×1, wave_bag ×3, hip_dance ×4, laugh ×2, walk ×8, portrait ×8
- `Daniel` (recurring, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scratch_head ×2, jump ×3, dance ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, run ×8, portrait ×8
- `MrsParker` (recurring, walk: old): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, check_price ×1, approve ×1, walk ×8, portrait ×8
- `Sofia` (recurring, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, dance ×4, pose ×1, surprise ×1, walk ×8, portrait ×8
- `MrBrooks` (recurring, walk: brisk): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, adjust_mustache ×2, stomp ×2, victory_dance ×4, ignore ×1, walk ×8, portrait ×8
- `PapaKofi` (recurring, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, laugh_hat ×2, show_produce ×1, trad_dance ×4, drama_react ×1, walk ×8, portrait ×8
- `Maya` (recurring, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, wave_big ×2, confetti ×2, explain ×3, walk ×8, portrait ×8
- `AuntiePepper` (recurring, walk: brisk): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, impatient ×2, taste ×1, walk ×8, portrait ×8
- `UncleMoney` (recurring, walk: confident): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, show_watch ×1, make_it_rain ×1, walk ×8, portrait ×8
- `MadamFashion` (recurring, walk: strut): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pose ×2, walk ×8, portrait ×8
- `SpeedySam` (recurring, walk: run): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, check_phone ×1, walk ×8, run ×8, portrait ×8
- `GrandpaWisdom` (recurring, walk: old): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, advise ×1, stroke_beard ×1, walk ×8, portrait ×8
- `Daniel_Cashier` (daniel_career, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Daniel_Supervisor` (daniel_career, walk: confident): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Daniel_Manager` (daniel_career, walk: confident): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_Cashier` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_StockClerk` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_Assistant` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_InventoryMgr` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_Supervisor` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Emp_Delivery` (employees, walk: brisk): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, run ×8, portrait ×8
- `Emp_Manager` (employees, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, scan ×2, restock ×2, carry ×1, check ×1, walk ×8, portrait ×8
- `Cust_Regular` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_FamilyMom` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_FamilyChild` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_Budget` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_BigSpender` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_VIP` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_Tourist` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_Loyal` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Cust_Resident` (customers, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Ped_Student` (pedestrians, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Ped_Worker` (pedestrians, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8
- `Ped_Tourist` (pedestrians, walk: normal): idle ×2, talk ×2, happy ×2, angry ×2, surprised ×1, sad ×1, wave ×2, point ×1, think ×1, shrug ×1, thumbs ×1, celebrate ×4, pick_item ×2, pay ×1, impatient ×2, walk ×8, portrait ×8

## How it maps to the document
- 4.2–4.6 Products and stock: about 59 products, shelves for 10 categories × 3 materials (wood, metal, premium) × 5 stock levels, fridges, chest freezer, produce stand, bakery case, storage racks, pallets, displays, promo stand.
- 4.3 Customers: all 8 customer types. 4.7 Staff: all 7 employee roles.
- 4.4 Checkout: manual, automatic, express and self-service checkouts, plus queue barrier.
- 5.2 Buildings: all 19 building types, plus Brooks Mart, Sofia's Snacks and Auntie Pepper's food spot. Each comes in basic, established and premium versions. Also included: farm, park, construction stages, plots, roads, vehicles (car, taxi, danfo, keke, delivery truck, farm pickup, tractor, Speedy Sam's motorbike), trees, sky for day, dawn, sunset and night, and rain and night overlays.
- 6.3–6.7 Characters: all 12 recurring characters with their described looks, the 6.5 animations, emotion bubbles and the 5 relationship badges (Stranger → Close Ally).
- 7.2 Indicators: Customer Happiness, Neighborhood Trust and Business Growth icons.
- 8.5 Store styles: 7 OgaMart exteriors and signs (Corner Shop → Mega Market), plus floors and walls for the themes (standard, modern, tropical, luxury, African market, holiday...). Also lighting, decorations, festival and grand-opening items.
- UI: navigation, action, building, upgrade, mission, cosmetic and indicator icons. Also buttons (normal, pressed, disabled), panels, toasts, progress bar, coin/XP/gem, level-up, confetti, tutorial arrow, highlight ring, lock, check and ad icons.

## Editing in Inkscape
- `source/` holds SVGs that open in Inkscape. Characters have body parts on labelled layers (head, torso, arm_left, arm_right, legs, props).
- To re-export one file: `inkscape file.svg --export-type=png --export-height=600 --export-background-opacity=0`
- To rebuild the whole pack after changing colours or outfits: edit `source/generators/characters/cast2.py` (or extras.py) and run `python3 build_chars.py`. Object generators are in `source/generators/objects/` (run `python3 build_objs.py`). These scripts need Python 3 and `librsvg2-bin` (`sudo apt install librsvg2-bin`), and the folder paths at the top of each script must be changed to yours.

## Name tags in game
- Add `nametag_<Character>.png` (for example `nametag_MamaBiggie.png`) as its own Sprite.
- Each frame, set its position to the character's X and the character's Y minus about 480 px, so it floats above the head.
- `buildingtag_<type>.png` works the same way above buildings on the neighborhood map.
- The names are not drawn on the character or object sprites themselves, so you can show or hide a tag whenever you want.
