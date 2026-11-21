"""龍門鎮民 Longmen townsfolk: the unnamed people of the Longmen Quest towns (until 2026-11-20 they were drawn inside
each game's tools/people.py), now gallery characters in the nes style, built with the nes2 kit like the cast.
TOWN lists them in the games' order; each has a portrait (person) and a field sprite (sp)."""
from nes2_kit import person
from nes2 import put  # noqa: F401
from nes2_cast_lq import SK, BLACK, C
from nes2_cast_sprites import sp, prop, beard_rows

TOWN = ['tf_man', 'tf_woman', 'tf_oldman', 'tf_oldwoman', 'tf_child', 'tf_guard', 'tf_merchant', 'tf_innkeeper',
        'tf_monk', 'tf_nun', 'tf_boatman', 'tf_bandit', 'tf_cultist', 'tf_scholar', 'tf_blacksmith', 'tf_fisherman',
        'tf_dancer', 'tf_beggar']
# the id each game uses in its maps (js/people_art.js PEOPLE keys)
GAME_ID = {t: t[3:] for t in TOWN}

BK = 0x0C
TAN = dict(S=0x27, s=0x17)
WOOD = dict(p=0x17, q=0x07)
GREY = dict(h=0x30, i=0x10, j=0x00)
WH = {'i': 'j', 'h': 'i', 'm': 'n'}

# ---------------------------------------------------------------- portraits
person('tf_man', dict(colours=C(SK, BLACK, a=0x28, b=0x18, d=0x08, e=0x37, f=0x27, z=0x0C),
       hair='topknot', eyes='calm', mouth='smile', collar='ea'))
person('tf_woman', dict(colours=C(SK, BLACK, m=0x16, n=0x06, a=0x2A, b=0x1A, d=0x0A, e=0x30, f=0x10, z=0x0C),
       hair='bun_f', eyes='cool', mouth='small', collar='ea', front=[('sidehair', {})]))
person('tf_oldman', dict(colours=C(SK, GREY, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, z=0x00, **WOOD),
       hair='topknot', eyes='shut', mouth='none', beard='long', beard_slot='h', beard_shade='i', hair_shade=WH,
       behind=[('staff', dict(x=43.5, y0=12))]))
person('tf_oldwoman', dict(colours=C(SK, GREY, m=0x10, n=0x00, a=0x00, b=0x2D, d=0x0C, e=0x10, f=0x00, z=0x00, **WOOD),
       hair='bun_f', eyes='shut', mouth='small', collar='ea', hair_shade=WH, behind=[('staff', dict(x=43.5, y0=20))]))
person('tf_child', dict(colours=C(SK, BLACK, a=0x36, b=0x26, d=0x16, e=0x30, f=0x10, t=0x25, z=0x0C),
       hair='topknot', face='kid', eyes='bright', mouth='beam', collar='ee', after=[(['tt'], 14, 26, True)], spr='t'))
person('tf_guard', dict(colours=C(SK, BLACK, m=0x16, n=0x06, y=0x28, a=0x26, b=0x16, d=0x06, e=0x26, f=0x16, g=0x06,
       w=0x30, v=0x10, r=0x28, z=0x06, **WOOD), hair='helmet', eyes='keen', mouth='firm', body='armour', collar='',
       behind=[('spear', dict(x=43.5, y0=2))]))
person('tf_merchant', dict(colours=C(SK, BLACK, m=0x16, n=0x06, y=0x28, a=0x38, b=0x28, d=0x18, e=0x16, f=0x06, z=0x06),
       hair='melon', face='fat', eyes='shut', mouth='beam', collar='ef', wide=2))
person('tf_innkeeper', dict(colours=C(SK, BLACK, m=0x30, n=0x10, a=0x30, b=0x10, d=0x00, e=0x17, f=0x07, z=0x0C),
       hair='kerchief', face='wide', eyes='calm', mouth='smile', collar='ef', sash=('f', 'f')))
person('tf_monk', dict(colours=C(SK, w=0x30, a=0x37, b=0x27, d=0x17, e=0x16, f=0x06, z=0x07),
       hair='bald', hair_slot='S', eyes='shut', mouth='small', collar='ee', hair_shade={'S': 's'}))
person('tf_nun', dict(colours=C(SK, BLACK, m=0x30, n=0x10, a=0x31, b=0x21, d=0x11, e=0x30, f=0x10, z=0x0C),
       hair='long', eyes='calm', mouth='small', collar='ea', behind=[('longhair', {})]))
person('tf_boatman', dict(colours=C(TAN, BLACK, m=0x38, n=0x28, a=0x18, b=0x08, d=0x0C, e=0x37, f=0x27, z=0x08),
       hair='straw', eyes='keen', mouth='smile', body='vest',
       post=[lambda c: [put(c, ['b'], x, y) for x in range(4, 44, 3) for y in range(46, 56, 3)
                        if c.tone[y][x] == 'a']]))
person('tf_bandit', dict(colours=C(SK, BLACK, m=0x10, n=0x00, a=0x10, b=0x00, d=0x0C, e=0x17, f=0x07, g=0x00, z=0x00),
       hair='kerchief', hair_slot='m', eyes='glare', mouth='none', mask='cloth', mask_slot='g', mask_slot2='g'))
person('tf_cultist', dict(colours=C(SK, m=0x14, n=0x04, a=0x14, b=0x04, d=0x0C, w=0x30, v=0x10, r=0x16, e=0x04, f=0x0C,
       z=0x04), hair='hood', hair_slot='m', eyes='glare', mouth='none', mask='ghost', collar='', neck='n',
       behind=[('hoodcape', {})]))
person('tf_scholar', dict(colours=C(SK, BLACK, a=0x21, b=0x11, d=0x02, e=0x30, f=0x10, p=0x16, q=0x06, w=0x30, z=0x0C),
       hair='topknot', eyes='calm', mouth='small', collar='ea', front=[('book', dict(x=37, y0=44))]))
person('tf_blacksmith', dict(colours=C(TAN, BLACK, a=0x06, b=0x07, d=0x08, e=0x17, f=0x07, w=0x30, v=0x10, z=0x06, **WOOD),
       hair='topknot', eyes='keen', mouth='grin', body='vest', wide=2, front=[('hammer', dict(x=41.5, y0=32))]))
person('tf_fisherman', dict(colours=C(TAN, BLACK, m=0x1C, n=0x0C, a=0x2C, b=0x1C, d=0x0C, e=0x37, f=0x27, z=0x0C,
       p=0x18, q=0x08), hair='band', eyes='calm', mouth='smile', behind=[('staff', dict(x=43.5, y0=6))]))
person('tf_dancer', dict(colours=C(SK, BLACK, m=0x25, n=0x15, a=0x35, b=0x25, d=0x15, e=0x30, f=0x10, t=0x25, z=0x0C),
       hair='twinbuns', eyes='cool', mouth='small', collar='ee', after=[(['tt'], 14, 27, True)], spr='t'))
person('tf_beggar', dict(colours=C(SK, BLACK, w=0x30, v=0x10, a=0x18, b=0x08, d=0x0C, e=0x27, f=0x17, p=0x08, q=0x0C, z=0x08),
       hair='wild', eyes='sly', mouth='smile', beard='stubble', collar='fe', inner2='S',
       front=[('cup', dict(x=38, y0=48))],
       post=[lambda c: [put(c, ['ee', 'ee'], x, y) for x, y in ((8, 48), (34, 51), (14, 53))]]))

# ---------------------------------------------------------------- field sprites (same colours as the portraits)
sp('tf_man', 'topknot', 0x28, 0x18, BK, 0x08, w='S')
sp('tf_woman', 'bun_f', 0x2A, 0x1A, BK, 0x16, body='gown', w='S')
sp('tf_oldman', 'topknot', 0x10, 0x00, 0x30, 0x17, w='h', props=prop('staff', 'b'), face=beard_rows('long', 'h'))
sp('tf_oldwoman', 'bun_f', 0x00, 0x0C, 0x10, 0x17, body='gown', w='h', props=prop('staff', 'b'))
sp('tf_child', 'topknot', 0x26, 0x16, BK, 0x30, body='boy', w='b', short=True)
sp('tf_guard', 'helmet', 0x16, 0x06, BK, 0x10, w='b', x='c', props=prop('spear', 'b'))
sp('tf_merchant', 'melon', 0x28, 0x18, BK, 0x16, w='b', hm={'b': 'b', 'x': 'h'})
sp('tf_innkeeper', 'cap', 0x30, 0x10, BK, 0x17, w='b', x='b', hm={'b': 'c'})
sp('tf_monk', 'bald', 0x27, 0x17, BK, 0x16, w='b')
sp('tf_nun', 'long', 0x31, 0x21, BK, 0x30, body='gown', w='b')
sp('tf_boatman', 'straw', 0x18, 0x08, BK, 0x38, S=0x27, w='S', x='d')
sp('tf_bandit', 'cap', 0x10, 0x00, BK, 0x00, w='d', x='k', face=beard_rows('cloth', 'b'))
sp('tf_cultist', 'hood', 0x14, 0x04, 0x30, 0x04, w='h', face=beard_rows('mask', 'h'))
sp('tf_scholar', 'topknot', 0x21, 0x11, BK, 0x16, w='S', props=prop('book', 'b'))
sp('tf_blacksmith', 'topknot', 0x06, 0x07, BK, 0x10, S=0x27, w='S', props=prop('club', 'b'))
sp('tf_fisherman', 'band', 0x2C, 0x1C, BK, 0x18, S=0x27, w='S', hm={'b': 'd'}, props=prop('staff', 'b'))
sp('tf_dancer', 'twinbuns', 0x35, 0x25, BK, 0x15, body='gown', w='S', x='b')
sp('tf_beggar', 'wild', 0x18, 0x08, BK, 0x27, w='S')
