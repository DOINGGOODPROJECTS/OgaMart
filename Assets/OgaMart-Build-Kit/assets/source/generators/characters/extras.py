import sys; sys.path.insert(0, '/home/claude/rig2')
from rig2 import Char, P, rel, HEAD, CX
import copy
from cast2 import C
G, GOLD = '#24503B', '#E8B62C'
def var(base, **k):
    c = copy.deepcopy(base); c.__dict__.update(k)
    from rig2 import _dark, _light
    for key, src in (('top', 'top'), ('bot', 'bot'), ('shoes', 'shoes')):
        if key in k and key + '_d' not in k: setattr(c, key + '_d', _dark(getattr(c, src)))
    if 'top' in k: c.top_h = _light(c.top)
    return c
D = C['Daniel']
CAREER = {  # Daniel evolves (doc 6.8) - unemployed is base
 'Daniel_Cashier': var(D, name='Daniel_Cashier', top=G, top_kind='polo', nametag=GOLD, apron=None, bot='#2B2B2B', hairstyle='short'),
 'Daniel_Supervisor': var(D, name='Daniel_Supervisor', top='#F4F1EA', top_kind='shirt', sleeve='long', vest=G, tie=GOLD, nametag=G, bot='#2B3A55', hairstyle='short', shoe='dress_shoe', shoes='#3B2A20', prop='clipboard'),
 'Daniel_Manager': var(D, name='Daniel_Manager', top='#24364F', top_kind='suit', sleeve='long', tie=GOLD, bot='#24364F', hairstyle='fade', shoe='dress_shoe', shoes='#111111', watch=True, prop='tablet'),
}
EMP = {
 'Emp_Cashier': Char(name='Emp_Cashier', sex='f', skin='#8A5431', skin_d='#6A3D21', hairstyle='bun', top=G, top_kind='polo', nametag=GOLD, bot='#2B2B2B', bust=0.5, hip=1.15, shoe='flat', shoes='#2B2118', earrings='small'),
 'Emp_StockClerk': Char(name='Emp_StockClerk', sex='m', skin='#5E3A22', skin_d='#462A17', hairstyle='short', top=G, top_kind='tshirt', apron='#7A5230', nametag=GOLD, bot='#3D4F5E', shoe='boot', shoes='#4A3626', headwear='cap', head_col=G, prop='box', girth=1.05),
 'Emp_Assistant': Char(name='Emp_Assistant', sex='f', skin='#A0683E', skin_d='#7E4E2C', hairstyle='puffs', top=G, top_kind='polo', nametag=GOLD, bottom='skirt', bot='#2B2B2B', bust=0.5, hip=1.1, shoe='flat', shoes='#2B2118'),
 'Emp_InventoryMgr': Char(name='Emp_InventoryMgr', sex='m', skin='#7A4A2C', skin_d='#5E3820', hairstyle='fade', eyewear='round', eye_col='#2B2118', top='#F4F1EA', top_kind='shirt', sleeve='long', vest=G, nametag=GOLD, bot='#3D4F5E', prop='clipboard', shoe='dress_shoe', shoes='#3B2A20'),
 'Emp_Supervisor': Char(name='Emp_Supervisor', sex='f', skin='#6E4227', skin_d='#53301B', hairstyle='updo', top='#F4F1EA', top_kind='blouse', sleeve='long', vest=G, nametag=GOLD, bot='#2B3A55', bust=0.6, hip=1.2, prop='tablet', shoe='flat', shoes='#2B2118', earrings='hoop'),
 'Emp_Delivery': Char(name='Emp_Delivery', sex='m', skin='#5A3720', skin_d='#432716', hairstyle='short', headwear='cap', head_col=GOLD, top=G, top_kind='delivery', jacket=G, sleeve='long', bot='#2B2B2B', shoe='sneaker', shoes='#C9C1B4', prop='box'),
 'Emp_Manager': Char(name='Emp_Manager', sex='f', skin='#8E5732', skin_d='#6E4024', hairstyle='long_braids', top=G, top_kind='suit', sleeve='long', bot=G, bust=0.6, hip=1.2, shoe='heel', shoes='#2B2118', earrings='small', prop='tablet'),
}
CUST = {
 'Cust_Regular': Char(name='Cust_Regular', sex='m', skin='#704428', skin_d='#553219', hairstyle='short', top='#C8412E', top_kind='tshirt', bot='#3D5A80', shoe='sneaker', shoes='#F4F1EA', shoes_d='#C9C1B4', prop='shopping_bag'),
 'Cust_FamilyMom': Char(name='Cust_FamilyMom', sex='f', skin='#8A5431', skin_d='#6A3D21', hairstyle='bun', headwear='headband', head_col='#E8B62C', outfit='dress', outfit_col='#3D7A6F', pattern='ankara', trim='#E8B62C', bust=0.8, hip=1.3, rear=0.5, shoe='sandal', shoes='#8B5A3C', prop='basket', sleeve='short'),
 'Cust_FamilyChild': Char(name='Cust_FamilyChild', sex='m', age='child', skin='#7A4A2C', skin_d='#5E3820', hairstyle='short', top='#F5C542', top_kind='tshirt', bot='#3B7DD8', shoe='sneaker', shoes='#E2435E', height=0.6, girth=0.85),
 'Cust_Budget': Char(name='Cust_Budget', sex='m', skin='#5E3A22', skin_d='#462A17', age='mid', hairstyle='short', hair='#4A4A4A', top='#8E8476', top_kind='shirt', bot='#4F5B66', shoe='sandal', shoes='#5B4030', prop='phone', eyewear='round', eye_col='#2B2118'),
 'Cust_BigSpender': Char(name='Cust_BigSpender', sex='f', skin='#6E4227', skin_d='#53301B', hairstyle='bouffant', outfit='dress', outfit_col='#7B3AA8', trim='#E8B62C', bust=1.0, hip=1.4, rear=0.8, earrings='big', chain=True, handbag='#E8B62C', shoe='heel', shoes='#E8B62C', eyewear='sunglasses', sleeve='short'),
 'Cust_VIP': Char(name='Cust_VIP', sex='m', skin='#4E2F1C', skin_d='#3A2214', hairstyle='fade', top='#111111', top_kind='suit', sleeve='long', bot='#111111', tie='#7B3AA8', eyewear='sunglasses', watch=True, shoe='dress_shoe', shoes='#111111', height=1.05),
 'Cust_Tourist': Char(name='Cust_Tourist', sex='f', skin='#E2B48C', skin_d='#C4936A', skin_h='#F0C9A4', lip='#B5655A', hair='#C9963E', hair_h='#E2B45E', hairstyle='long_braids', headwear='straw_hat', top='#6FB3D9', top_kind='tshirt', bot='#E8D9B5', bottom='pants', backpack='#E07A3F', shoe='sneaker', shoes='#F4F1EA', shoes_d='#C9C1B4', prop='camera', bust=0.5, hip=1.1),
 'Cust_Loyal': Char(name='Cust_Loyal', sex='f', skin='#80502F', skin_d='#623A1F', age='mid', hairstyle='short', headwear='gele', head_col='#1E6B45', outfit='dress', outfit_col='#E07A3F', trim='#1E6B45', bust=0.9, hip=1.3, rear=0.5, shoe='sandal', shoes='#1E6B45', handbag='#1E6B45', sleeve='short'),
 'Cust_Resident': Char(name='Cust_Resident', sex='m', skin='#6B4226', skin_d='#51301A', hairstyle='short', headwear='kufi', head_col='#F4F1EA', outfit='robe', outfit_col='#F4F1EA', trim='#3D6FA8', shoe='sandal', shoes='#5B4030', facial='stubble', sleeve='long'),
}
PED = {
 'Ped_Student': Char(name='Ped_Student', sex='f', skin='#8E5732', skin_d='#6E4024', hairstyle='puffs', top='#F4F1EA', top_kind='shirt', bottom='skirt', bot='#3B4C8C', backpack='#C8412E', shoe='flat', shoes='#2B2118', bust=0.2, hip=1.0, height=0.92),
 'Ped_Worker': Char(name='Ped_Worker', sex='m', skin='#5E3A22', skin_d='#462A17', hairstyle='short', headwear='cap', head_col='#F28C28', top='#F28C28', top_kind='tshirt', vest='#D7F02E', bot='#3D4F5E', shoe='boot', shoes='#4A3626', girth=1.1, shoulder=1.1),
 'Ped_Tourist': Char(name='Ped_Tourist', sex='m', skin='#D9A47A', skin_d='#B9835A', skin_h='#E8BC96', lip='#A85A50', hair='#6B4A2E', hairstyle='short', headwear='cap', head_col='#3D7A6F', top='#F5E9C8', top_kind='shirt', bot='#C9B48A', backpack='#3D7A6F', eyewear='sunglasses', shoe='sneaker', shoes='#8E8476', prop='camera'),
}
# work / shopping poses
WORK = {
 'scan_1': P(la=rel(-1, 40, -70), lh='grip', ra=rel(1, 50, -50), rh='open', expr='smile'), 'scan_2': P(la=rel(-1, 50, -50), lh='grip', ra=rel(1, 40, -70), rh='open', expr='talk'),
 'restock_1': P(la=('ik', (CX - 24, 120)), lh='grip', ra=('ik', (CX + 24, 120)), rh='grip', expr='neutral', prop='box', prop_at=(CX, 116)),
 'restock_2': P(la=rel(-1, 150, 10), lh='grip', ra=rel(1, 150, 10), rh='grip', expr='smile', prop='box', prop_at=(CX, -16)),
 'carry_1': P(la=('ik', (CX - 24, 124)), lh='grip', ra=('ik', (CX + 24, 124)), rh='grip', expr='smile', prop='box', prop_at=(CX, 120)),
 'check_1': P(la=rel(-1, 40, -95), lh='grip', ra=rel(1, 30, -80), rh='point', expr='neutral', prop='clipboard', prop_at=(CX - 30, 118)),
 'pick_item_1': P(la=rel(-1, 8, 6), ra=rel(1, 100, 10), rh='open', expr='smile'), 'pick_item_2': P(la=rel(-1, 8, 6), ra=rel(1, 60, -60), rh='fist', expr='happy'),
 'pay_1': P(la=rel(-1, 8, 6), ra=rel(1, 60, -10), rh='palmup', expr='smile', prop='phone', prop_at=(CX + 74, 120)),
 'impatient_1': P(la=('ik', (CX - 40, 166)), lh='fist', ra=rel(1, 30, -100), rh='fist', expr='angry', lift_r=8), 'impatient_2': P(la=('ik', (CX - 40, 166)), lh='fist', ra=rel(1, 30, -100), rh='fist', expr='neutral'),
}
