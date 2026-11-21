"""nes2 portraits for the Longmen Quest II cast, the Tactics story people and the Mercy Cloud abbess (nes2 kit)."""
from nes2_kit import person, HAIR
from nes2 import put  # noqa: F401
from nes2_cast_lq import SK, BLACK, C

TAN = dict(S=0x27, s=0x17)

# 胡半仙 Hu Banxian: flat grey hat, round black glasses, thin moustache, grey robe, his fortune banner
person('hubanxian', dict(
    colours=C(SK, BLACK, m=0x10, n=0x00, a=0x10, b=0x00, d=0x0C, e=0x1C, f=0x0C, g=0x0C, p=0x07, q=0x08, r=0x30,
              w=0x30, z=0x0C),
    hair='flat', eyes='calm', mouth='smirk', beard='thin', mask='glasses', mask_slot2='g', body='robe', collar='ef',
    behind=[('banner', dict(x=44.5, y0=4, y1=56))],
    post=[lambda c: [put(c, ['k'], 39, y) for y in (7, 10, 13)]]))

# 賈八方 Jia Bafang: red round cap, a wide grin, an orange vest, his great pack
person('jiabafang', dict(
    colours=C(SK, BLACK, m=0x16, n=0x06, a=0x27, b=0x17, d=0x07, e=0x37, f=0x27, p=0x18, q=0x08, z=0x06),
    hair='kerchief', eyes='shut', mouth='beam', body='vest', behind=[('pack', {})]))

# 吳大膽 Wu Dadan: big, tanned, bearded, red cap, wide-eyed and timid, iron-shod staff
person('wudadan', dict(
    colours=C(TAN, BLACK, m=0x16, n=0x06, a=0x16, b=0x06, d=0x07, e=0x27, f=0x17, p=0x10, q=0x00, z=0x06),
    hair='kerchief', face='wide', eyes='round', mouth='none', beard='full', body='vest', wide=2,
    behind=[('staff', dict(x=43.5, y0=4, y1=56))]))

# 溫對仗 Wen Duizhang: flat scholar's hat, sky-blue gown, his rafter-sized brush
person('wenduizhang', dict(
    colours=C(SK, BLACK, m=0x10, n=0x00, a=0x31, b=0x21, d=0x11, e=0x30, f=0x10, p=0x07, q=0x08, z=0x0C),
    hair='flat', eyes='calm', mouth='firm', body='robe', collar='ea',
    front=[('brush', dict(x=41.5, y0=14, y1=56))]))

# 蘇小婉 Su Xiaowan: a ghost who does not know it: pale blue skin, bun with a green ribbon, green gown, a cup
person('suxiaowan', dict(
    colours=C(S=0x31, s=0x21, h=0x1C, i=0x0C, m=0x2A, n=0x1A, a=0x2A, b=0x1A, d=0x0A, e=0x30, f=0x10, t=0x25,
              w=0x30, v=0x10, p=0x10, q=0x00, z=0x0C),
    hair='bun_f', eyes='calm', mouth='small', body='robe', collar='ea',
    front=[('sidehair', {}), ('cup', dict(x=38, y0=46))], after=[(['tt'], 14, 27, True)], spr='t'))

# 楚天闊 Chu Tiankuo: white headband, teal robe, the sword on his back, a cocky smirk
person('chutiankuo', dict(
    colours=C(SK, BLACK, m=0x30, n=0x10, a=0x2C, b=0x1C, d=0x0C, e=0x30, f=0x10, w=0x30, v=0x10, y=0x28, p=0x07,
              q=0x08, z=0x0C),
    hair='band', eyes='keen', mouth='smirk', body='robe', collar='ea',
    behind=[('jian', dict(x=5.5, y0=10, y1=52))]))

# 牛包包 Niu Baobao: bald and round, beaming, orange robe over a white apron, a meat bun in hand
person('niubaobao', dict(
    colours=C(SK, a=0x27, b=0x17, d=0x07, e=0x30, f=0x10, w=0x30, v=0x10, z=0x07),
    hair='bald', hair_slot='S', face='fat', eyes='shut', mouth='beam', body='robe', collar='ee', inner2='e', wide=2,
    front=[('ball', dict(x=40.5, y0=40))], hair_shade={'S': 's'}))

# 莫記得 Mo Jide: grey cap, round glasses, thin goatee, green robe, medicine box
person('mojide', dict(
    colours=C(SK, BLACK, m=0x10, n=0x00, a=0x2A, b=0x1A, d=0x0A, e=0x30, f=0x10, p=0x17, q=0x07, w=0x38, z=0x0C),
    hair='kerchief', eyes='calm', mouth='firm', beard='goatee', beard_slot='k', mask='roundglasses', body='robe',
    collar='ea', front=[('book', dict(x=39, y0=42))]))

# 霍天下 Huo Tianxia: gold headband, a boastful grin, red pauldrons
person('huotianxia', dict(
    colours=C(SK, BLACK, m=0x28, n=0x18, a=0x27, b=0x17, d=0x07, e=0x26, f=0x16, g=0x06, y=0x16, z=0x06),
    hair='band', eyes='proud', mouth='beam', body='armour', collar='', behind=[('redcape', {})],
    after=[(['.kk', 'kyk', 'kyk', '.k.'], 22, 9, False)]))

# 莫無涯 Mo Wuya: dark hair, pale, violet robe, the Bell of Ten Thousand Beasts on his staff
person('mowuya', dict(
    colours=C(S=0x36, s=0x26, h=0x02, i=0x0C, a=0x13, b=0x03, d=0x0C, e=0x30, f=0x10, p=0x18, q=0x08, y=0x28,
              z=0x0C),
    hair='topknot', eyes='cool', mouth='firm', body='robe', collar='ea',
    behind=[('bell', dict(x=43.5, y0=4, y1=56))]))

# 阿蠻 A-Man: a Miao girl raised among wolves: silver headdress with white feathers, tanned, grey fur over blue
person('aman', dict(
    colours=C(TAN, BLACK, m=0x10, n=0x00, w=0x30, v=0x30, a=0x12, b=0x02, d=0x0C, e=0x10, f=0x00, g=0x2D, z=0x0C),
    hair=[r.replace('w', 'm') for r in HAIR['feather'].strip().split(chr(10))], face='kid', eyes='bright', mouth='small', body='armour', collar='',
    # two tall white feathers curving out of the silver headdress, as in her old portrait
    after=[(['kk......', 'kvk.....', 'kvvk....', '.kvvk...', '..kvvk..', '...kvvk.', '....kvk.'], 3, 0, True)]))

# 靜慈師太 Abbess Jingci: white hood with a red band, grey robe, red prayer beads, horsetail whisk
person('jingci', dict(
    colours=C(SK, m=0x30, n=0x10, r=0x16, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, w=0x30, v=0x10, p=0x07, q=0x08,
              z=0x00),
    hair='hood', hair_slot='m', eyes='calm', mouth='small', body='robe', collar='ea', neck='m',
    behind=[('hoodcape', {})], front=[('whisk', dict(x=41.5, y0=26, y1=56))],
    after=[(['rrrrrrrrrrrrrrrr'], 8, 11, True)],
    post=[lambda c: [put(c, ['r'], x, y) for x, y in ((15, 44), (17, 46), (19, 48), (28, 48), (30, 46), (32, 44))]]))

# 奕長風 Yi Changfeng: grey topknot, long grey beard, deep blue robe, ring-pommel sabre
person('yichangfeng', dict(
    colours=C(SK, h=0x30, i=0x10, j=0x00, a=0x12, b=0x02, d=0x0C, e=0x30, f=0x10, w=0x30, v=0x10, y=0x28, p=0x07,
              q=0x17, z=0x0C),
    hair='topknot', eyes='glare', mouth='none', beard='long', beard_slot='i', beard_shade='j', body='robe',
    collar='eaa', hair_shade={'i': 'j', 'h': 'i'},
    behind=[('dao', dict(x=5.5, y0=12, y1=56))]))

# 蕭無影 Xiao Wuying: black gauze cap with wings, deep violet official robe, darts up his sleeve
person('xiaowuying', dict(
    colours=C(SK, BLACK, m=0x00, n=0x2D, a=0x14, b=0x04, d=0x0C, e=0x28, f=0x18, w=0x30, v=0x10, y=0x28, p=0x07,
              q=0x08, z=0x04),
    hair='official', eyes='sly', mouth='firm', body='robe', collar='ea',
    front=[('dagger', dict(x=41.5, y0=40))]))
