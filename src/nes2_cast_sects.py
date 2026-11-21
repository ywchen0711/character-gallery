"""nes2 portraits for the 龍門江湖志 (Sects of Longmen) people and the Longmen Tactics jobs (nes2 kit).
Carts, engines, ships and mounted troops keep their old field sprite (the vehicle); their portrait is the crew."""
from nes2_kit import person
from nes2 import put  # noqa: F401
from nes2_cast_lq import SK, BLACK, C

TAN = dict(S=0x27, s=0x17)
WHITEHAIR = dict(h=0x30, i=0x10, j=0x00)
METAL = dict(w=0x30, v=0x10)
WOOD = dict(p=0x17, q=0x07)
WH = {'i': 'j', 'h': 'i', 'm': 'n'}

P = person

P('sx_grandmaster', dict(colours=C(SK, WHITEHAIR, a=0x21, b=0x11, d=0x02, e=0x30, f=0x10, p=0x07, q=0x08, y=0x28, z=0x00),
  hair='topknot', eyes='shut', mouth='none', beard='long', beard_slot='h', beard_shade='i', hair_shade=WH,
  behind=[('bell', dict(x=43.5, y0=2, y1=56))]))
P('sx_smith', dict(colours=C(TAN, BLACK, m=0x0C, n=0x0F, a=0x17, b=0x07, d=0x08, e=0x27, f=0x17, p=0x07, q=0x08, z=0x0C, **METAL),
  hair='kerchief', eyes='keen', mouth='grin', body='vest', wide=2, front=[('hammer', dict(x=41.5, y0=30, y1=56))]))
P('sx_founder', dict(colours=C(SK, BLACK, a=0x27, b=0x17, d=0x07, e=0x30, f=0x10, p=0x2A, q=0x1A, w=0x30, v=0x10, z=0x0C),
  hair='topknot', eyes='bright', mouth='smile', behind=[('ball', dict(x=7.5, y0=26)), ('staff', dict(x=43.5, y0=8))]))
P('sx_scout', dict(colours=C(SK, BLACK, m=0x38, n=0x28, a=0x2A, b=0x1A, d=0x0A, e=0x30, f=0x10, y=0x28, z=0x08, **METAL, **WOOD),
  hair='straw', eyes='calm', mouth='firm', front=[('dagger', dict(x=41.5, y0=40))]))
P('sx_disciple', dict(colours=C(SK, BLACK, m=0x30, n=0x10, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, z=0x0C, **WOOD),
  hair='band', eyes='keen', mouth='firm', behind=[('staff', dict(x=43.5, y0=8))]))
P('sx_archer', dict(colours=C(SK, BLACK, m=0x16, n=0x06, a=0x1A, b=0x0A, d=0x0C, e=0x30, f=0x10, z=0x0C, **WOOD),
  hair='band', eyes='keen', mouth='firm', behind=[('bow', dict(x=6.5, y0=8, y1=54))]))
P('sx_saber', dict(colours=C(SK, BLACK, a=0x17, b=0x07, d=0x08, e=0x27, f=0x17, y=0x28, z=0x0C, **METAL, **WOOD),
  hair='topknot', eyes='glare', mouth='firm', front=[('dao', dict(x=42.5, y0=10))]))
P('sx_sword', dict(colours=C(SK, BLACK, m=0x30, n=0x10, a=0x31, b=0x21, d=0x11, e=0x30, f=0x10, y=0x28, z=0x0C, **METAL, **WOOD),
  hair='band', eyes='keen', mouth='firm', front=[('jian', dict(x=42.5, y0=10))]))
P('sx_hidden', dict(colours=C(SK, m=0x10, n=0x00, a=0x13, b=0x03, d=0x0C, e=0x10, f=0x00, y=0x28, z=0x00, **METAL, **WOOD),
  hair='hood', hair_slot='m', eyes='glare', mouth='firm', neck='n', behind=[('hoodcape', {})],
  front=[('dagger', dict(x=41.5, y0=40))]))
P('sx_spear', dict(colours=C(SK, BLACK, m=0x10, n=0x00, y=0x16, a=0x26, b=0x16, d=0x06, e=0x26, f=0x16, g=0x06, r=0x16, z=0x00, **METAL, **WOOD),
  hair='helmet', eyes='keen', mouth='firm', body='armour', collar='', behind=[('spear', dict(x=43.5, y0=2))]))
P('sx_inner', dict(colours=C(SK, BLACK, a=0x30, b=0x10, d=0x00, e=0x21, f=0x11, z=0x0C),
  hair='long', eyes='calm', mouth='small', behind=[('longhair', {})], collar='ef'))
P('sx_swordform', dict(colours=C(SK, BLACK, m=0x10, n=0x00, y=0x30, a=0x21, b=0x11, d=0x02, e=0x21, f=0x11, g=0x02, z=0x00, **WOOD, w=0x30, v=0x10),
  hair='helmet', eyes='glare', mouth='firm', body='armour', collar='', front=[('jian', dict(x=42.5, y0=6))], near={'y': 'm'}))
P('sx_crossbow', dict(colours=C(SK, BLACK, m=0x0C, n=0x0F, a=0x2C, b=0x1C, d=0x0C, e=0x2C, f=0x1C, g=0x0C, z=0x0C, **WOOD),
  hair='kerchief', eyes='keen', mouth='firm', body='armour', collar='', behind=[('bow', dict(x=6.5, y0=20, y1=54))]))
P('sx_master', dict(colours=C(SK, WHITEHAIR, a=0x00, b=0x2D, d=0x0C, e=0x28, f=0x18, y=0x28, z=0x0C, **METAL, **WOOD),
  hair='topknot', eyes='shut', mouth='firm', hair_shade=WH, collar='ef', behind=[('jian', dict(x=5.5, y0=8, y1=50))]))
P('sx_starbow', dict(colours=C(SK, BLACK, m=0x28, n=0x18, y=0x16, a=0x26, b=0x16, d=0x06, e=0x26, f=0x16, g=0x06, p=0x28, q=0x18, z=0x06),
  hair='helmet', eyes='keen', mouth='firm', body='armour', collar='', behind=[('bow', dict(x=6.5, y0=6, y1=54))]))
P('sx_rider', dict(colours=C(SK, BLACK, m=0x17, n=0x07, y=0x16, a=0x26, b=0x16, d=0x06, e=0x17, f=0x07, g=0x08, z=0x08),
  hair='helmet', eyes='keen', mouth='firm', body='armour', collar=''))
P('sx_ironcav', dict(colours=C(SK, BLACK, m=0x10, n=0x00, y=0x30, a=0x21, b=0x11, d=0x02, e=0x10, f=0x00, g=0x2D, z=0x00),
  hair='helmet', eyes='glare', mouth='firm', body='armour', collar='', near={'y': 'm'}))
P('sx_caravan', dict(colours=C(SK, BLACK, m=0x16, n=0x06, a=0x27, b=0x17, d=0x07, e=0x30, f=0x10, r=0x16, z=0x0C, **WOOD),
  hair='band', eyes='keen', mouth='smile', behind=[('banner', dict(x=44.5, y0=4))]))
P('sx_ram', dict(colours=C(TAN, w=0x30, v=0x10, p=0x17, q=0x07, a=0x17, b=0x07, d=0x08, e=0x27, f=0x17, z=0x08),
  front=[('log', {})],
  hair='bald', hair_slot='S', face='wide', eyes='glare', mouth='grit', body='vest', wide=3, hair_shade={'S': 's'}))
P('sx_catapult', dict(colours=C(SK, BLACK, m=0x17, n=0x07, a=0x1A, b=0x0A, d=0x0C, e=0x30, f=0x10, z=0x0C),
  hair='kerchief', eyes='calm', mouth='firm'))
P('sx_thunder', dict(colours=C(SK, BLACK, m=0x0C, n=0x0F, a=0x16, b=0x06, d=0x07, e=0x28, f=0x18, w=0x00, v=0x0C, r=0x28, z=0x06),
  hair='kerchief', eyes='round', mouth='grin', front=[('ball', dict(x=40.5, y0=38))]))
P('sx_boat', dict(colours=C(SK, BLACK, m=0x38, n=0x28, a=0x21, b=0x11, d=0x02, e=0x30, f=0x10, z=0x08, **WOOD),
  hair='straw', eyes='calm', mouth='smile', behind=[('staff', dict(x=43.5, y0=12))]))
P('sx_warship', dict(colours=C(SK, BLACK, m=0x10, n=0x00, y=0x28, a=0x21, b=0x11, d=0x02, e=0x21, f=0x11, g=0x02, r=0x28, z=0x00, **WOOD),
  hair='helmet', eyes='glare', mouth='frown', beard='thin', body='armour', collar='', behind=[('banner', dict(x=44.5, y0=4))]))
P('sx_lm_saber', dict(colours=C(SK, BLACK, m=0x21, n=0x11, a=0x12, b=0x02, d=0x0C, e=0x30, f=0x10, y=0x28, z=0x0C, **METAL, p=0x07, q=0x17),
  hair='band', eyes='keen', mouth='firm', behind=[('dao', dict(x=5.5, y0=12))]))
P('sx_hj_sword', dict(colours=C(SK, BLACK, m=0x10, n=0x00, a=0x31, b=0x21, d=0x11, e=0x30, f=0x10, y=0x28, z=0x0C, **METAL, **WOOD),
  hair='bun_f', eyes='cool', mouth='small', front=[('sidehair', {}), ('jian', dict(x=42.5, y0=10))]))
P('sx_qf_monk', dict(colours=C(SK, w=0x30, a=0x38, b=0x28, d=0x18, e=0x16, f=0x06, y=0x28, p=0x28, q=0x18, z=0x08),
  hair='bald', hair_slot='S', eyes='glare', mouth='frown', collar='ee', hair_shade={'S': 's'},
  behind=[('bell', dict(x=43.5, y0=2))],
  post=[lambda c: [put(c, ['q'], x, y) for x, y in ((15, 43), (17, 45), (19, 47), (28, 47), (30, 45), (32, 43))]]))
P('sx_bl_palm', dict(colours=C(TAN, BLACK, a=0x27, b=0x17, d=0x07, e=0x28, f=0x18, w=0x30, z=0x06),
  hair='spiky', eyes='glare', mouth='fang', body='vest', collar='', wide=2,
  post=[lambda c: [put(c, ['ee', 'ff'], x, 50) for x in (3, 43)]]))
P('sx_ym_assassin', dict(colours=C(SK, m=0x14, n=0x04, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00, w=0x30, v=0x10, r=0x16, z=0x04),
  hair='hood', hair_slot='m', eyes='glare', mouth='none', mask='half', neck='n', behind=[('hoodcape', {})]))
P('sx_yy_tiger', dict(colours=C(SK, BLACK, m=0x2A, n=0x1A, a=0x1A, b=0x0A, d=0x0C, e=0x30, f=0x10, z=0x0C),
  hair='tiger', hair_slot='m', eyes='calm', mouth='small'))
P('sx_qj_escort', dict(colours=C(SK, BLACK, m=0x16, n=0x06, y=0x28, a=0x38, b=0x28, d=0x18, e=0x16, f=0x06, r=0x16, z=0x06, **WOOD),
  hair='melon', eyes='keen', mouth='smile', behind=[('banner', dict(x=44.5, y0=4))]))
P('sx_hf_club', dict(colours=C(TAN, BLACK, a=0x17, b=0x07, d=0x08, e=0x27, f=0x17, w=0x30, z=0x08, **WOOD),
  hair='wild', eyes='glare', mouth='none', beard='full', body='vest', behind=[('club', dict(x=42.5, y0=4, y1=52))],
  post=[lambda c: [put(c, ['w'], x, y) for x, y in ((40, 8), (45, 12), (40, 16), (45, 20))]]))
P('sx_xd_blood', dict(colours=C(SK, BLACK, a=0x16, b=0x06, d=0x07, e=0x26, f=0x16, w=0x26, v=0x16, y=0x28, z=0x06, **WOOD),
  hair='topknot', eyes='glare', mouth='frown', front=[('dao', dict(x=42.5, y0=10))]))
P('sx_zf_chain', dict(colours=C(SK, BLACK, m=0x00, n=0x2D, a=0x10, b=0x00, d=0x0C, e=0x30, f=0x10, z=0x0C, **METAL),
  hair='official', eyes='glare', mouth='frown', beard='moustache', beard_slot='k',
  front=[('chain', dict(x=41.5, y0=36, y1=56))]))
P('sx_cy_nun', dict(colours=C(SK, m=0x30, n=0x10, a=0x35, b=0x25, d=0x15, e=0x30, f=0x10, y=0x28, r=0x16, z=0x00, **METAL, **WOOD),
  hair='hood', hair_slot='m', eyes='calm', mouth='small', neck='m', behind=[('hoodcape', {})],
  front=[('jian', dict(x=42.5, y0=12))]))
P('sx_physician', dict(colours=C(SK, BLACK, a=0x2A, b=0x1A, d=0x0A, e=0x30, f=0x10, p=0x27, q=0x17, r=0x16, z=0x0C),
  hair='topknot', eyes='calm', mouth='smile', front=[('gourd', dict(x=39.5, y0=42))]))
P('sx_physician_f', dict(colours=C(SK, BLACK, m=0x2C, n=0x1C, a=0x2C, b=0x1C, d=0x0C, e=0x30, f=0x10, p=0x27, q=0x17, r=0x16, z=0x0C),
  hair='bun_f', eyes='cool', mouth='small', front=[('sidehair', {}), ('gourd', dict(x=39.5, y0=42))]))
P('sx_thief', dict(colours=C(TAN, BLACK, m=0x16, n=0x06, a=0x00, b=0x2D, d=0x0C, e=0x16, f=0x06, y=0x28, z=0x0C, **METAL, **WOOD),
  hair='band', eyes='sly', mouth='smile', collar='ef', front=[('dagger', dict(x=41.5, y0=40))]))
P('sx_daoist', dict(colours=C(SK, BLACK, y=0x28, a=0x38, b=0x28, d=0x18, e=0x16, f=0x06, w=0x37, v=0x27, p=0x07, q=0x08, z=0x08),
  hair='crown', eyes='calm', mouth='firm', collar='ef', front=[('jian', dict(x=42.5, y0=10))],
  after=[(['kkk', 'kyk', 'kyk', 'kyk', 'kkk'], 37, 30, False)], near={'y': 'b'}))
P('sx_qin', dict(colours=C(SK, BLACK, a=0x21, b=0x11, d=0x02, e=0x30, f=0x10, p=0x17, q=0x07, z=0x0C),
  hair='long', eyes='calm', mouth='small', behind=[('longhair', {})], front=[('qin', {})]))
P('sx_qin_f', dict(colours=C(SK, BLACK, m=0x28, n=0x16, a=0x35, b=0x25, d=0x15, e=0x30, f=0x10, p=0x17, q=0x07, z=0x0C),
  hair='bun_f', eyes='cool', mouth='small', front=[('sidehair', {}), ('qin', {})]))
P('sx_poison', dict(colours=C(SK, m=0x14, n=0x04, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00, w=0x30, p=0x1A, q=0x0A, r=0x16, z=0x04),
  hair='hood', hair_slot='m', eyes='sly', mouth='buck', neck='n', behind=[('hoodcape', {})],
  front=[('gourd', dict(x=39.5, y0=42))]))
P('sx_strategist', dict(colours=C(SK, BLACK, m=0x0C, n=0x0F, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, w=0x30, v=0x10, p=0x07, q=0x08, z=0x0C),
  hair='kerchief', eyes='calm', mouth='firm', beard='goatee', beard_slot='k', front=[('feather', dict(x=40.5, y0=30))]))
P('sx_teller', dict(colours=C(SK, BLACK, m=0x00, n=0x2D, a=0x17, b=0x07, d=0x08, e=0x27, f=0x17, w=0x16, v=0x06, p=0x07, q=0x08, z=0x08),
  hair='scholar', eyes='shut', mouth='smile', beard='goatee', beard_slot='k', front=[('fan', dict(x=40, y0=36))]))
P('sx_scholar', dict(colours=C(SK, BLACK, m=0x30, n=0x10, a=0x2C, b=0x1C, d=0x0C, e=0x30, f=0x10, p=0x07, q=0x08, z=0x0C),
  hair='band', eyes='calm', mouth='small', front=[('brush', dict(x=41.5, y0=8))]))
P('sx_phantom', dict(colours=C(SK, m=0x00, n=0x2D, a=0x10, b=0x00, d=0x0C, e=0x10, f=0x00, g=0x0C, z=0x00),
  hair='hood', hair_slot='m', eyes='glare', mouth='none', mask='cloth', mask_slot='g', mask_slot2='g', neck='g',
  behind=[('hoodcape', {})]))
