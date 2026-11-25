import sys; sys.path.insert(0, '/home/claude/rig2')
from rig2 import Char, P, rel, HEAD, STD, CX
H = HEAD
# 12 recurring characters from doc 6.3
C = {}
C['MamaBiggie'] = Char(name='MamaBiggie', sex='f', skin='#7A4A2C', skin_d='#5E3820', skin_h='#93603C', age='mid', hairstyle='bun', headwear='gele', head_col='#7B3AA8',
    eyewear='oversized', eye_col='#C8412E', outfit='dress', outfit_col='#E8B62C', pattern='ankara', trim='#7B3AA8', bust=1.0, hip=1.55, rear=1.0, belly=0.5, girth=1.25,
    handbag='#D63A2A', earrings='big', shoes='#7B3AA8', shoe='sandal', sleeve='puff')
C['Daniel'] = Char(name='Daniel', sex='m', skin='#6B4226', skin_d='#51301A', skin_h='#85553A', hairstyle='messy', height=1.08, girth=0.88, top='#9DB8D9', top_kind='oversized',
    bot='#5A6B7E', shoes='#C9C1B4', shoes_d='#8E8476', shoe='sneaker', sleeve='short')
C['MrsParker'] = Char(name='MrsParker', sex='f', skin='#A0673E', skin_d='#7E4E2C', age='old', hair='#DADADA', hair_h='#FFFFFF', hairstyle='silver_bun', eyewear='stylish', eye_col='#5B2A86',
    top='#3D7A6F', top_kind='blouse', sleeve='long', bottom='long_skirt', bot='#2F4858', handbag='#8B5A3C', earrings='small', bust=0.4, hip=1.1, shoe='flat', shoes='#5B3A28', chain=True)
C['Sofia'] = Char(name='Sofia', sex='f', skin='#8E5732', skin_d='#6E4024', hairstyle='puffs', top='#F28C28', top_kind='blouse', bottom='pants', bot='#2E6DA4', earrings='hoop',
    bust=0.85, hip=1.3, rear=0.6, shoe='sneaker', shoes='#FFFFFF', shoes_d='#C9C1B4', prop=None)
C['MrBrooks'] = Char(name='MrBrooks', sex='m', skin='#B57A50', skin_d='#94603A', hair='#2B1D14', hairstyle='bald', facial='mustache', facial_col='#2B1D14', height=0.86, girth=1.35, belly=1.0,
    top='#2B3A55', top_kind='suit', sleeve='long', bot='#2B3A55', tie='#C8412E', shoes='#111111', shoe='dress_shoe', watch=False)
C['PapaKofi'] = Char(name='PapaKofi', sex='m', skin='#5E3A22', skin_d='#462A17', age='old', hair='#C9C9CE', hairstyle='short', headwear='straw_hat', facial='beard_thick', facial_col='#D8D4CC',
    top='#B9873F', top_kind='shirt', vest='overalls', bot='#4F6B3A', girth=1.12, shoulder=1.12, shoes='#5B4030', shoe='boot', sleeve='short', prop='basket')
C['Maya'] = Char(name='Maya', sex='f', skin='#9A5E36', skin_d='#7A4526', hairstyle='long_braids', hair='#2A1A10', eyewear='colorful', eye_col='#E2435E',
    top='#4CC38A', top_kind='tshirt', bottom='skirt', bot='#3D6FA8', shoe='sneaker', shoes='#F5C542', shoes_d='#C9971A', bust=0.55, hip=1.15, prop='tablet', earrings='small')
C['AuntiePepper'] = Char(name='AuntiePepper', sex='f', skin='#80502F', skin_d='#623A1F', age='mid', hairstyle='bouffant', hair='#1B110B', height=0.9, girth=1.12,
    outfit='dress', outfit_col='#D62828', trim='#F5C542', earrings='big', bust=1.0, hip=1.35, rear=0.6, belly=0.3, shoe='sandal', shoes='#F5C542', sleeve='short', prop='pot')
C['UncleMoney'] = Char(name='UncleMoney', sex='m', skin='#5A3720', skin_d='#432716', hairstyle='fade', headwear='fila', head_col='#E8B62C', eyewear='sunglasses', facial='stubble',
    outfit='agbada', outfit_col='#F2E2B6', trim='#C9A23A', top='#F2E2B6', bot='#F2E2B6', girth=1.42, belly=1.0, watch=True, chain=True, shoes='#C9A23A', shoe='dress_shoe', sleeve='long')
C['MadamFashion'] = Char(name='MadamFashion', sex='f', skin='#6E4227', skin_d='#53301B', hairstyle='updo', height=1.1, girth=0.95, outfit='dress', outfit_col='#E2435E', trim='#E8B62C',
    earrings='big', bust=0.9, hip=1.05, rear=0.2, shoe='heel', shoes='#E8B62C', handbag=None, prop='clutch', eyewear=None, sleeve='short', chain=True)
C['SpeedySam'] = Char(name='SpeedySam', sex='m', skin='#704428', skin_d='#553219', hairstyle='short', headwear='helmet', girth=0.82, top='#F28C28', top_kind='delivery', jacket='#F28C28',
    sleeve='long', bot='#2B3A55', shoe='sneaker', shoes='#E2435E', backpack='#3B7DD8')
C['GrandpaWisdom'] = Char(name='GrandpaWisdom', sex='m', skin='#5E3A22', skin_d='#462A17', age='old', hair='#F4F1EA', hairstyle='bald', headwear='kufi', head_col='#1E6B45',
    eyewear='round', eye_col='#8B6A4A', facial='beard_long', facial_col='#F4F1EA', outfit='robe', outfit_col='#1E6B45', pattern='kente', trim='#E8B62C', stick=True, shoe='sandal', shoes='#6B4A32', sleeve='long', girth=0.95)
WALKSTYLE = {'MamaBiggie': 'sway', 'SpeedySam': 'run', 'GrandpaWisdom': 'old', 'MadamFashion': 'strut', 'MrBrooks': 'brisk', 'UncleMoney': 'confident', 'AuntiePepper': 'brisk', 'PapaKofi': 'normal', 'MrsParker': 'old'}
# signature animations (doc 6.5 + personalities)
GL = lambda s: ('ik', H(s * 12, 40))
SIG = {
 'MamaBiggie': {
   'adjust_glasses_1': P(la=rel(-1, 8, 6), ra=('ik', H(20, 38)), rh='point', expr='neutral'), 'adjust_glasses_2': P(la=rel(-1, 8, 6), ra=('ik', H(19, 32)), rh='point', expr='confused'),
   'hands_hips_1': P(la=('ik', (CX - 44, 168)), lh='fist', ra=('ik', (CX + 44, 168)), rh='fist', expr='angry', bag='none'),
   'wave_bag_1': P(la=rel(-1, 30, -60), lh='palmup', ra=rel(1, 150, 20), rh='fist', bag='wave', bag_ang=-20, expr='angry'),
   'wave_bag_2': P(la=rel(-1, 30, -60), lh='palmup', ra=rel(1, 120, 40), rh='fist', bag='wave', bag_ang=15, expr='talk'),
   'wave_bag_3': P(la=rel(-1, 30, -60), lh='palmup', ra=rel(1, 160, 0), rh='fist', bag='wave', bag_ang=-35, expr='angry'),
   'hip_dance_1': P(la=rel(-1, 60, 60), lh='open', ra=('ik', (CX + 44, 168)), rh='fist', tilt=-5, sway=10, expr='laugh', bag='none'),
   'hip_dance_2': P(la=rel(-1, 40, 80), lh='open', ra=('ik', (CX + 44, 168)), rh='fist', tilt=4, sway=-10, expr='happy', bag='none'),
   'hip_dance_3': P(la=rel(-1, 60, 60), lh='open', ra=('ik', (CX + 44, 168)), rh='fist', tilt=-5, sway=10, expr='grin', bag='none', jump=4),
   'hip_dance_4': P(la=rel(-1, 40, 80), lh='open', ra=('ik', (CX + 44, 168)), rh='fist', tilt=4, sway=-10, expr='laugh', bag='none'),
   'laugh_1': P(la=('ik', (CX - 20, 150)), lh='open', ra=rel(1, 20, -90), rh='open', expr='laugh', head_tilt=-6), 'laugh_2': P(la=('ik', (CX - 20, 146)), lh='open', ra=rel(1, 26, -100), rh='open', expr='laugh', head_tilt=4, jump=3)},
 'Daniel': {
   'scratch_head_1': P(la=rel(-1, 8, 6), ra=('ik', H(16, 4)), rh='fist', expr='confused', head_tilt=5), 'scratch_head_2': P(la=rel(-1, 8, 6), ra=('ik', H(10, 2)), rh='fist', expr='confused', head_tilt=7),
   'jump_1': P(la=rel(-1, 20, -60), lh='fist', ra=rel(1, 20, -60), rh='fist', expr='grin', jump=-4, slump=True), 'jump_2': P(la=rel(-1, 160, 10), lh='fist', ra=rel(1, 160, 10), rh='fist', expr='laugh', jump=34, lift_l=14, lift_r=14), 'jump_3': P(la=rel(-1, 140, 30), lh='fist', ra=rel(1, 140, 30), rh='fist', expr='happy', jump=8),
   'dance_1': P(la=rel(-1, 110, 60), lh='fist', ra=rel(1, 40, -80), rh='fist', tilt=-5, expr='happy', lift_r=14), 'dance_2': P(la=rel(-1, 40, -80), lh='fist', ra=rel(1, 110, 60), rh='fist', tilt=5, expr='laugh', lift_l=14),
   'dance_3': P(la=rel(-1, 150, 15), lh='point', ra=rel(1, 20, -20), rh='fist', tilt=-3, expr='grin'), 'dance_4': P(la=rel(-1, 20, -20), lh='fist', ra=rel(1, 150, 15), rh='point', tilt=3, expr='happy')},
 'Sofia': {
   'dance_1': P(la=rel(-1, 120, 40), lh='open', ra=('ik', (CX + 40, 170)), rh='fist', tilt=-4, expr='grin'), 'dance_2': P(la=('ik', (CX - 40, 170)), lh='fist', ra=rel(1, 120, 40), rh='open', tilt=4, expr='happy'),
   'dance_3': P(la=rel(-1, 90, 80), lh='point', ra=rel(1, 90, 80), rh='point', expr='laugh', jump=5), 'dance_4': P(la=rel(-1, 40, -60), lh='fist', ra=rel(1, 40, -60), rh='fist', expr='grin'),
   'pose_1': P(la=('ik', (CX - 42, 166)), lh='fist', ra=rel(1, 150, 30), rh='point', tilt=-3, expr='proud'),
   'surprise_1': P(la=('ik', H(-16, 50)), lh='open', ra=('ik', H(16, 50)), rh='open', expr='surprised', jump=10)},
 'MrBrooks': {
   'adjust_mustache_1': P(la=('ik', (CX - 30, 160)), lh='fist', ra=('ik', H(12, 50)), rh='point', expr='proud'), 'adjust_mustache_2': P(la=('ik', (CX - 30, 160)), lh='fist', ra=('ik', H(18, 48)), rh='point', expr='neutral'),
   'stomp_1': P(la=rel(-1, 40, -105), lh='fist', ra=rel(1, 40, -105), rh='fist', expr='angry', lift_r=26), 'stomp_2': P(la=rel(-1, 30, -95), lh='fist', ra=rel(1, 30, -95), rh='fist', expr='angry', jump=-3),
   'victory_dance_1': P(la=rel(-1, 160, 10), lh='fist', ra=rel(1, 60, -40), rh='fist', tilt=-6, expr='laugh', lift_l=12), 'victory_dance_2': P(la=rel(-1, 60, -40), lh='fist', ra=rel(1, 160, 10), rh='fist', tilt=6, expr='happy', lift_r=12),
   'victory_dance_3': P(la=rel(-1, 160, 10), lh='fist', ra=rel(1, 160, 10), rh='fist', expr='laugh', jump=12), 'victory_dance_4': P(la=rel(-1, 60, -40), lh='fist', ra=rel(1, 60, -40), rh='fist', expr='grin'),
   'ignore_1': P(la=('ik', (CX + 20, 140)), lh='rest', ra=('ik', (CX - 20, 142)), rh='rest', expr='proud', head_tilt=-10)},
 'PapaKofi': {
   'laugh_hat_1': P(la=('ik', (CX - 20, 150)), lh='open', ra=('ik', H(24, 10)), rh='fist', expr='laugh'), 'laugh_hat_2': P(la=('ik', (CX - 20, 146)), lh='open', ra=('ik', H(20, 6)), rh='fist', expr='laugh', jump=3, head_tilt=-4),
   'show_produce_1': P(la=rel(-1, 70, -30), lh='palmup', ra=rel(1, 70, -30), rh='palmup', expr='proud', prop='basket', prop_at=(CX, 104)),
   'trad_dance_1': P(la=rel(-1, 60, 50), lh='open', ra=rel(1, 30, -60), rh='open', tilt=-4, expr='happy', lift_l=16, prop='none'), 'trad_dance_2': P(la=rel(-1, 30, -60), lh='open', ra=rel(1, 60, 50), rh='open', tilt=4, expr='laugh', lift_r=16, prop='none'),
   'trad_dance_3': P(la=rel(-1, 90, 0), lh='open', ra=rel(1, 90, 0), rh='open', expr='grin', jump=6, prop='none'), 'trad_dance_4': P(la=rel(-1, 30, -60), lh='open', ra=rel(1, 30, -60), rh='open', expr='happy', prop='none'),
   'drama_react_1': P(la=('ik', H(-14, 46)), lh='open', ra=rel(1, 140, 30), rh='open', expr='sad', head_tilt=-8, tilt=-5, prop='none')},
 'Maya': {
   'wave_big_1': P(la=rel(-1, 30, -60), lh='fist', ra=rel(1, 160, 30), rh='open', expr='grin', jump=4), 'wave_big_2': P(la=rel(-1, 30, -60), lh='fist', ra=rel(1, 130, 60), rh='open', expr='laugh'),
   'confetti_1': P(la=rel(-1, 150, 15), lh='open', ra=rel(1, 150, 15), rh='open', expr='laugh', jump=10, confetti=True, prop='none'), 'confetti_2': P(la=rel(-1, 130, 30), lh='open', ra=rel(1, 130, 30), rh='open', expr='happy', confetti=True, prop='none'),
   'explain_1': P(la=rel(-1, 30, -80), lh='palmup', ra=rel(1, 80, 0), rh='point', expr='talk'), 'explain_2': P(la=rel(-1, 40, -70), lh='palmup', ra=rel(1, 30, -90), rh='palmup', expr='smile'), 'explain_3': P(la=rel(-1, 90, 10), lh='open', ra=rel(1, 30, -80), rh='palmup', expr='talk')},
 'MrsParker': {'check_price_1': P(la=('ik', H(-12, 40)), lh='point', ra=rel(1, 30, -90), rh='palmup', expr='neutral'), 'approve_1': P(la=rel(-1, 8, 6), ra=rel(1, 22, -100), rh='thumb', expr='proud')},
 'AuntiePepper': {'impatient_1': P(la=('ik', (CX - 42, 168)), lh='fist', ra=('ik', (CX + 42, 168)), rh='fist', expr='angry', lift_r=10, prop='none'), 'impatient_2': P(la=('ik', (CX - 42, 168)), lh='fist', ra=('ik', (CX + 42, 168)), rh='fist', expr='talk', prop='none'),
                  'taste_1': P(la=rel(-1, 60, -40), lh='palmup', ra=('ik', H(6, 58)), rh='fist', expr='happy', prop='pot', prop_at=(CX - 46, 150))},
 'UncleMoney': {'show_watch_1': P(la=rel(-1, 8, 6), ra=rel(1, 60, -70), rh='fist', expr='proud'), 'make_it_rain_1': P(la=rel(-1, 150, 20), lh='open', ra=rel(1, 150, 20), rh='open', expr='laugh', confetti=True)},
 'MadamFashion': {'pose_1': P(la=('ik', (CX - 40, 166)), lh='fist', ra=('ik', H(18, 0)), rh='open', tilt=-4, expr='proud', prop='none'), 'pose_2': P(la=rel(-1, 140, 40), lh='open', ra=('ik', (CX + 40, 166)), rh='fist', tilt=4, expr='smile', prop='none')},
 'SpeedySam': {'check_phone_1': P(la=rel(-1, 30, -100), lh='grip', ra=rel(1, 8, 6), expr='talk', prop='phone', prop_at=(CX - 30, 120))},
 'GrandpaWisdom': {'advise_1': P(la=rel(-1, 140, 20), lh='point', expr='talk'), 'stroke_beard_1': P(la=('ik', H(-4, 80)), lh='rest', expr='proud')},
}
# role-specific extras for tutorial/talk etc. inherit STD
