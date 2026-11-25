import re
CHAR = {'MamaBiggie': 'Mama Biggie', 'Daniel': 'Daniel', 'MrsParker': 'Mrs. Parker', 'Sofia': 'Sofia', 'MrBrooks': 'Mr. Brooks', 'PapaKofi': 'Papa Kofi', 'Maya': 'Maya',
        'AuntiePepper': 'Auntie Pepper', 'UncleMoney': 'Uncle Money', 'MadamFashion': 'Madam Fashion', 'SpeedySam': 'Speedy Sam', 'GrandpaWisdom': 'Grandpa Wisdom',
        'Daniel_Cashier': 'Daniel (Cashier)', 'Daniel_Supervisor': 'Daniel (Supervisor)', 'Daniel_Manager': 'Daniel (Manager)',
        'Emp_Cashier': 'Cashier', 'Emp_StockClerk': 'Stock Clerk', 'Emp_Assistant': 'Store Assistant', 'Emp_InventoryMgr': 'Inventory Manager', 'Emp_Supervisor': 'Store Supervisor', 'Emp_Delivery': 'Delivery Assistant', 'Emp_Manager': 'Store Manager',
        'Cust_Regular': 'Regular Shopper', 'Cust_FamilyMom': 'Family Shopper (Mum)', 'Cust_FamilyChild': 'Family Shopper (Child)', 'Cust_Budget': 'Budget Shopper', 'Cust_BigSpender': 'Big Spender', 'Cust_VIP': 'VIP Customer', 'Cust_Tourist': 'Tourist', 'Cust_Loyal': 'Loyal Customer', 'Cust_Resident': 'Neighborhood Resident',
        'Ped_Student': 'Student', 'Ped_Worker': 'Worker', 'Ped_Tourist': 'Tourist (Pedestrian)'}
BLD = {'brooks_store': "Brooks Mart (rival)", 'sofia_snacks': "Sofia's Snacks", 'pepper_food_spot': "Auntie Pepper's Food Spot"}
FIX = {'eggs dairy': 'Eggs & Dairy', 'fruit veg': 'Fruit & Veg', 'ogamart': 'OgaMart', 'led': 'LED', 'xp': 'XP', 'vip': 'VIP', 'h': 'Horizontal', 'v': 'Vertical', 'exp': 'Experience', 'mgr': 'Manager', 'customer exp': 'Customer Experience', 'operations m': 'Operations', 'auto': 'Automatic'}
def nice(stem):
    if stem.startswith('nametag_'): return 'Name tag – ' + CHAR.get(stem[8:], stem[8:])
    if stem.startswith('buildingtag_'): return 'Building tag – ' + nice(stem[12:])
    s = stem
    for k, v in BLD.items():
        if s == k or s.startswith(k + '_'): s = v.replace(' ', '§') + s[len(k):]
    for p in ('product_', 'icon_nav_', 'icon_action_', 'icon_building_', 'icon_upgrade_', 'icon_mission_', 'icon_cosmetic_', 'icon_indicator_', 'icon_misc_', 'glyph_', 'tiled_', 'vehicle_', 'rel_', 'bubble_', 'panel_', 'button_', 'sign_', 'overlay_', 'sky_'):
        if s.startswith(p): s = s[len(p):]; break
    m = re.search(r'_stock_(\d)$', s); stock = ''
    if m: stock = f' – Stock {m.group(1)}/5' + (' (empty)' if m.group(1) == '1' else ' (full)' if m.group(1) == '5' else ''); s = s[:m.start()]
    s = s.replace('_', ' ')
    for k, v in FIX.items(): s = re.sub(rf'\b{k}\b', v, s)
    s = re.sub(r'\b(c8412e|3b7dd8|f4f1ea|4f6b3a|e8b62c)\b', lambda m: {'c8412e': 'red', '3b7dd8': 'blue', 'f4f1ea': 'white', '4f6b3a': 'green', 'e8b62c': 'gold'}[m.group(1)], s)
    s = ' '.join(w if w[:1].isupper() else w.capitalize() for w in s.split())
    s = s.replace('§', ' ')
    return s + stock
def anim_label(stem, char):
    a = stem[len(char) + 1:]; m = re.match(r'(.*)_(\d+)$', a)
    if a.startswith('portrait_'): return 'Portrait – ' + a[9:].capitalize()
    return (m.group(1).replace('_', ' ').capitalize() + f' – frame {m.group(2)}') if m else a
