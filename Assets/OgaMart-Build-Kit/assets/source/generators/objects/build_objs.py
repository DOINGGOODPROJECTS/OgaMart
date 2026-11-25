import sys, os, json, subprocess; sys.path.insert(0, '/home/claude/obj')
from concurrent.futures import ThreadPoolExecutor
import common as C, products as P, store as S, hood as Hd, env as E, ui_kit as U
ROOT = '/home/claude/pack2/OgaMart-GDevelop-Assets'; TMP = '/home/claude/tmp_svg2'; os.makedirs(TMP, exist_ok=True)
jobs = []; man = {}; srcs = []
def add(folder, name, body_vb, scale=None, height=None, width=None, src=False, section=''):
    b, vb = body_vb; x0, y0, w, h = map(float, vb.split()); d = f'{ROOT}/{folder}'; os.makedirs(d, exist_ok=True)
    if height: px_h = height; px_w = round(w * height / h)
    elif width: px_w = width; px_h = round(h * width / w)
    else: px_w, px_h = round(w * scale), round(h * scale)
    s = C.svg(b, vb, px_w, px_h); jobs.append((s, f'{d}/{name}.png', px_w, px_h))
    man.setdefault(folder, []).append(dict(file=f'{name}.png', size=f'{px_w}x{px_h}', doc=section))
    if src:
        sd = f'{ROOT}/source/{folder}'; os.makedirs(sd, exist_ok=True); open(f'{sd}/{name}.svg', 'w').write(s)
K = 1.3  # px per unit, matches characters
# products
for k, f in P.CATALOG.items(): add('products', f'product_{k}', (f(), '0 0 100 100'), height=256, src=True, section='4.2 products')
# store
for cat in ['bakery', 'eggs_dairy', 'drinks', 'snacks', 'fruit_veg', 'household', 'frozen', 'premium', 'local_specialty', 'pantry']:
    for mat in ('wood', 'metal', 'premium'):
        for st in range(5): add(f'store/shelves/{cat}', f'shelf_{cat}_{mat}_stock_{st+1}', S.shelf_unit(cat, st, mat), K, src=(st == 4), section='4.2/4.6 shelves, stock levels')
for st in range(5):
    add('store/equipment', f'fridge_drinks_stock_{st+1}', S.fridge(st, 'drinks'), K, section='4.6 equipment'); add('store/equipment', f'fridge_dairy_stock_{st+1}', S.fridge(st, 'dairy'), K)
    add('store/equipment', f'chest_freezer_stock_{st+1}', S.chest_freezer(st), K); add('store/equipment', f'produce_stand_stock_{st+1}', S.produce_stand(st), K); add('store/equipment', f'bakery_case_stock_{st+1}', S.bakery_case(st), K)
for k in ('manual', 'automatic', 'express', 'self_service'): add('store/checkout', f'checkout_{k}', S.checkout(k), K, src=True, section='4.4 checkout')
add('store/checkout', 'queue_barrier', S.queue_barrier(), K)
for full in (True, False): add('store/storage', f'storage_rack_{"full" if full else "empty"}', S.storage_rack(full), K, section='4.5 storage'); add('store/storage', f'pallet_{"loaded" if full else "empty"}', S.pallet(full), K)
for k in ('mangoes', 'oranges', 'chin_chin', 'bread_loaf'): add('store/displays', f'display_table_{k}', S.display_table(k), K, section='4.6 displays')
add('store/displays', 'promo_stand', S.promo_stand(), K); add('store/displays', 'end_cap_sofia_snacks', S.end_cap('chin_chin'), K); add('store/displays', 'end_cap_hot_deal', S.end_cap('biscuits'), K)
for k in ('pendant', 'led_panel', 'chandelier', 'spot'):
    for on in (True, False): add('store/lighting', f'lamp_{k}_{"on" if on else "off"}', S.lamp(k, on), K, section='8.5 lighting')
for st in ('corner_shop', 'traditional', 'modern_mini', 'neighborhood', 'premium', 'superstore', 'mega_market'): add('store/signage', f'sign_ogamart_{st}', S.sign(st), width=700, src=True, section='8.5 store styles')
for cat in ['bakery', 'eggs_dairy', 'drinks', 'snacks', 'fruit_veg', 'household', 'frozen', 'premium', 'local_specialty', 'pantry']: add('store/signage', f'aisle_sign_{cat}', S.aisle_sign(cat), K)
add('store/signage', 'price_tag', S.price_tag(), K); add('store/signage', 'price_tag_sale', S.price_tag('₦350', True), K)
for i, stt in enumerate(('closed', 'half', 'open')): add('store/entrance', f'doors_auto_{i+1}', S.doors(stt), K, section='entrance (anim: doors_auto_1-3)')
for full in (False, True): add('store/carts', f'cart_{"full" if full else "empty"}', S.cart(full), K); add('store/carts', f'basket_{"full" if full else "empty"}', S.basket(full), K)
add('store/decor', 'plant_palm', S.plant('palm'), K); add('store/decor', 'plant_bush', S.plant('bush'), K); add('store/decor', 'wall_art', S.wall_art(), K)
add('store/decor', 'banner_grand_opening', S.banner(), K); add('store/decor', 'banner_sale', S.banner('BIG SALE', '#1E8C4E'), K); add('store/decor', 'balloons', S.balloons(), K); add('store/decor', 'string_lights', S.string_lights(), K)
for th in S.THEMES:
    add('store/floors_walls', f'tiled_floor_{th}', S.floor(th), height=256, section='8.5 floors/walls + cosmetic themes'); add('store/floors_walls', f'tiled_wall_{th}', S.wall(th), height=256)
# neighborhood
for k in Hd.SPEC:
    for lv, nm in enumerate(('basic', 'established', 'premium')): add(f'neighborhood/buildings/{k}', f'{k}_{nm}', Hd.building(k, lv), 1.6, src=(lv == 1), section='5.2 buildings, 3 levels')
for lv, nm in enumerate(('basic', 'established', 'premium')): add('neighborhood/buildings/farm', f'farm_{nm}', Hd.farm(lv), 1.6); add('neighborhood/buildings/park', f'park_{nm}', Hd.park(lv), 1.6)
for st in ('corner_shop', 'traditional', 'modern_mini', 'neighborhood', 'premium', 'superstore', 'mega_market'): add('neighborhood/ogamart_exterior', f'ogamart_{st}', Hd.ogamart(st), 1.6, src=True, section='8.5 store styles exterior')
for i in range(3): add('neighborhood/construction', f'construction_{i+1}', Hd.construction(i), 1.6, section='5.3 construction stages')
for k in ('commercial', 'residential', 'locked'): add('neighborhood/construction', f'plot_{k}', Hd.plot(k), 1.6)
for k in ('h', 'v', 'cross', 'crosswalk', 'sidewalk', 'path', 'grass', 'parking', 'dirt'): add('neighborhood/ground', f'tiled_{"road_"+k if k in ("h","v","cross","crosswalk") else k}', E.road(k), height=256, section='infrastructure')
for k in ('mango', 'palm', 'round', 'flame'):
    add('neighborhood/nature', f'tree_{k}', E.tree(k), 1.6, src=True, section='decorations')
add('neighborhood/nature', 'bush', E.tree('bush'), 1.6); add('neighborhood/nature', 'flowerbed', E.flowerbed(), 1.6); add('neighborhood/nature', 'hedge', E.hedge(), 1.6)
add('neighborhood/street', 'bench', E.bench(), 1.6); add('neighborhood/street', 'streetlight_on', E.streetlight(True), 1.6); add('neighborhood/street', 'streetlight_off', E.streetlight(False), 1.6); add('neighborhood/street', 'fountain', E.fountain(), 1.6); add('neighborhood/street', 'trash_bin', E.trashbin(), 1.6)
for k, col in [('car', '#C8412E'), ('car', '#3B7DD8'), ('car', '#F4F1EA'), ('taxi', ''), ('danfo', ''), ('truck', ''), ('pickup', '#4F6B3A'), ('tractor', ''), ('motorbike', ''), ('keke', '')]:
    nm = f'{k}_{col.strip("#").lower()}' if col else k; add('neighborhood/vehicles', f'vehicle_{nm}', E.vehicle(k, col or '#C8412E'), 1.6, section='vehicles')
for k in ('day', 'dawn', 'sunset', 'night'): add('neighborhood/sky', f'sky_{k}', E.sky(k), width=1920, section='day/night cycle')
for k in ('night_tint', 'sunset_tint', 'lamp_glow', 'rain', 'cloud'): add('neighborhood/sky', f'overlay_{k}', E.overlay(k), height=512)
add('neighborhood/events', 'market_stall_red', E.market_stall(), 1.6, section='events'); add('neighborhood/events', 'market_stall_green', E.market_stall('#1E8C4E', ('plantain', 'yam', 'garri', 'palm_oil')), 1.6)
add('neighborhood/events', 'festival_arch', E.festival_arch(), 1.6); add('neighborhood/events', 'ribbon_grand_opening', E.ribbon(), 1.6); add('neighborhood/events', 'bunting', E.flag_bunting(), 1.6); add('neighborhood/events', 'holiday_tree', E.xmas_tree(), 1.6)
for c in ('#C8412E', '#E8B62C'): add('neighborhood/events', f'lantern_{c[1:].lower()}', E.lantern(c), 1.6)
# UI
GROUPS = {'nav': ['home', 'store', 'map', 'people', 'missions', 'shop', 'settings', 'profile'],
 'action': ['restock', 'change_product', 'move', 'upgrade', 'details', 'assign', 'train', 'manage', 'enter', 'collect', 'customize', 'interact', 'profile', 'request', 'talk', 'hire', 'skills', 'story', 'negotiate', 'partner', 'discount', 'build', 'rotate', 'preview', 'cancel', 'expand', 'performance'],
 'building': ['commercial', 'residential', 'food', 'entertainment', 'community', 'infrastructure', 'decoration'],
 'upgrade': ['inventory', 'checkout', 'employees', 'equipment', 'store_size', 'customer_exp', 'operations'],
 'mission': ['operations_m', 'service', 'business', 'employees', 'neighborhood', 'character'],
 'cosmetic': ['theme', 'outfit', 'floor', 'wall', 'signage', 'lighting', 'celebration'],
 'indicator': ['happiness', 'trust', 'growth'], 'misc': ['lock', 'check', 'ad', 'coin', 'cart', 'gem', 'xp']}
for g, names in GROUPS.items():
    for n in names: add(f'ui/icons/{g}', f'icon_{g}_{n}', U.badge(n, U.ICONCOL[g], 'square' if g in ('nav',) else 'circle'), height=128, section='9.x UI icons')
for n in U.GLYPH: add('ui/icons/glyphs_white', f'glyph_{n}', (U.glyph(n), '0 0 100 100'), height=128)
for col, nm in [('#24503B', 'green'), ('#E8B62C', 'gold'), ('#C8412E', 'red'), ('#3B7DD8', 'blue')]:
    for st in ('normal', 'pressed', 'disabled'): add('ui/buttons', f'button_{nm}_{st}', U.button(col, st), height=100, section='UI buttons (Panel Sprite, margins 36)')
for k in ('card', 'dialog', 'speech', 'topbar', 'progress_frame', 'progress_fill', 'toast'): add('ui/panels', f'panel_{k}', U.panel(k), 2, section='Panel Sprite 9-slice')
for i in range(6): add('ui/effects', f'coin_spin_{i+1}', U.coin(i), height=96, section='coin fly effect')
add('ui/effects', 'xp_star', U.xp_star(), height=96); add('ui/effects', 'gem', U.gem(), height=96); add('ui/effects', 'level_up', U.levelup(), height=400)
for i in range(6): add('ui/effects', f'confetti_{i+1}', U.confetti_piece(i), height=40); add('ui/effects', f'burst_{i+1}', U.burst(i), height=256); add('ui/effects', f'payment_{i+1}', U.payment(i), height=120) if i < 5 else None
for i in range(4): add('ui/effects', f'dust_{i+1}', U.dust(i), height=200); add('ui/effects', f'tutorial_arrow_{i+1}', U.arrow(i), height=120); add('ui/effects', f'highlight_ring_{i+1}', U.ring(i), height=160)
for k in ('happy', 'angry', 'sad', 'love', 'question', 'exclaim', 'money', 'zzz', 'idea', 'shopping', 'time'): add('ui/emotion_bubbles', f'bubble_{k}', U.bubble(k), height=128, section='6.x emotion bubbles')
for nm, col, n in U.REL: add('ui/relationship', f'rel_{nm}', U.rel_badge(nm, col, n), height=128, section='6.7 relationship levels')
def run(j):
    s, out, w, h = j; t = f'{TMP}/{abs(hash(out))}.svg'; open(t, 'w').write(s)
    subprocess.run(['rsvg-convert', '-w', str(w), '-h', str(h), t, '-o', out], check=True); os.remove(t)
with ThreadPoolExecutor(16) as ex: list(ex.map(run, jobs))
json.dump(man, open('/home/claude/pack2/obj_manifest.json', 'w'), indent=1); print(len(jobs))
