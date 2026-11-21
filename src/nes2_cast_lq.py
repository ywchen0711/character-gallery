"""nes2 portraits for the rest of the Longmen Quest cast (Black Wind Fort, the Netherworld Sect, the Alliance's
officers, Liu Hanyan's pupil, the old fisherman, the masked ones), drawn with the nes2 kit (src/nes2_kit.py)."""
from nes2_kit import person, prop  # noqa: F401
from nes2 import put  # noqa: F401

SK = dict(S=0x37, s=0x27)
BLACK = dict(h=0x1C, i=0x0C)


def C(*ds, **kw):
    out = {}
    for d in ds:
        out.update(d)
    out.update(kw)
    return out


# 黑熊 Black Bear: wild hair, full black beard, bear hide over a grey shirt, spiked club
person('heixiong', dict(
    colours=C(SK, BLACK, a=0x17, b=0x07, d=0x08, e=0x10, f=0x00, p=0x17, q=0x07, w=0x30, v=0x10, z=0x08),
    hair='wild', face='wide', eyes='glare', mouth='none', beard='full', beard_slot='i', beard_shade='k', body='fur',
    collar='ef', inner2='e',
    behind=[('club', dict(x=6.5, y0=4, y1=50))],
    post=[lambda c: [put(c, ['w'], x, y) for x, y in ((4, 8), (9, 12), (4, 16), (9, 20), (5, 24))]],
    near={'w': 'v'}, backdrop=dict(solid_to=6, check_to=26, fade=10)))

# 刀疤 Scar: shaved temples and a topknot, a long scar across the face, a broad dao
person('daoba', dict(
    colours=C(SK, BLACK, a=0x16, b=0x06, d=0x07, e=0x17, f=0x07, w=0x30, v=0x10, y=0x28, p=0x07, q=0x08, r=0x16,
              z=0x0C),
    hair='shaved', hair_slot='S', eyes='glare', mouth='frown', body='vest', mask='scar',
    front=[('dao', dict(x=41.5, y0=10, y1=56))], near={'y': 'p'}))

# 瘦猴 Skinny Monkey: thin, buck-toothed grin, patched brown clothes, a short knife
person('shouhou', dict(
    colours=C(SK, BLACK, a=0x18, b=0x08, d=0x0C, e=0x27, f=0x17, w=0x30, v=0x10, y=0x28, p=0x07, q=0x08, z=0x0C),
    hair='spiky', face='thin', eyes='sly', mouth='buck', mouth_y=31, body='robe', collar='fe', inner2='S',
    front=[('dagger', dict(x=40.5, y0=40))],
    post=[lambda c: [put(c, ['ee', 'ee'], x, y) for x, y in ((8, 48), (34, 51))]]))

# 屠千秋 Tu Qianqiu: pale, long ink-black hair with one white lock, silver half-mask, violet robe, bone fan
person('tuqianqiu', dict(
    colours=C(S=0x36, s=0x10, h=0x1C, i=0x0C, a=0x24, b=0x14, d=0x04, e=0x30, f=0x10, w=0x30, v=0x10, p=0x10,
              q=0x00, r=0x16, z=0x04),
    hair='long', eyes='cool', mouth='smirk', body='robe', mask='half', collar='eb', inner2='e',
    behind=[('longhair', {})], front=[('sidehair', {}), ('fan', dict(x=37, y0=41))],
    post=[lambda c: [c.tone[y].__setitem__(x, 'w') for y in range(2, 30) for x in (13, 14)
                     if c.tone[y][x] in 'hi']],
    spr='', near={'r': 'v'}))

# 鐵無私 Tie Wusi: black official cap with side wings, heavy black moustache, charcoal robe, iron chain
person('tiewusi', dict(
    colours=C(SK, BLACK, m=0x00, n=0x2D, a=0x10, b=0x00, d=0x0C, e=0x30, f=0x10, w=0x30, v=0x10, y=0x28, z=0x0C),
    hair='official', eyes='glare', mouth='frown', beard='moustache', beard_slot='k', body='robe', collar='eaa',
    front=[('chain', dict(x=41.5, y0=36, y1=56))]))

# 錢萬里 Qian Wanli: round face, red melon-skin cap with a gold knob, maroon robe, gold-beaded abacus
person('qianwanli', dict(
    colours=C(SK, BLACK, m=0x16, n=0x06, y=0x28, a=0x16, b=0x06, d=0x07, e=0x28, f=0x18, q=0x07, w=0x38, t=0x25, z=0x06),
    hair='melon', face='fat', eyes='shut', mouth='beam', after=[(['tt'], 12, 27, True)], spr='t', body='robe', collar='ea', inner2='S', wide=2,
    front=[('abacus', dict(x=24, y0=48))],
    post=[lambda c: [put(c, ['w'], x, y) for x in range(16, 32, 2) for y in (49, 51, 53)]]))

# 溫如玉 Wen Ruyu: a green-wrapped bun, pale green gown with an ink spot on the collar, the ledger at his chest
person('wenruyu', dict(
    colours=C(SK, BLACK, a=0x3B, b=0x3A, d=0x2A, e=0x30, f=0x10, m=0x2A, n=0x1A, p=0x1A, q=0x0A, w=0x30, z=0x0C),
    hair='topknot', eyes='calm', mouth='small', body='robe', collar='ea',
    front=[('book', dict(x=37, y0=44))],
    after=[(['kkkk', 'mmmm', 'nnnn'], 20, 1, True), (['kk'], 17, 44, False)]))

# 小蓮 Xiaolian: two round buns with red ribbons, pink robe with a white collar
person('xiaolian', dict(
    colours=C(SK, BLACK, m=0x16, n=0x06, a=0x35, b=0x25, d=0x15, e=0x30, f=0x10, t=0x25, z=0x0C),
    hair='twinbuns', face='kid', eyes='bright', mouth='beam', body='robe', collar='ee', inner2='e',
    after=[(['tt'], 14, 26, True)], spr='t'))

# 厲寒山 Li Hanshan: long white hair tied back, gaunt, dark red robe, blood-red curved blade
person('lihanshan', dict(
    colours=C(SK, h=0x30, i=0x10, a=0x16, b=0x06, d=0x07, e=0x26, f=0x16, w=0x26, v=0x16, y=0x28, p=0x07, q=0x08,
              z=0x00),
    hair='long', eyes='glare', mouth='frown', body='robe', collar='ef', inner2='k',
    hair_shade={'h': 'i', 'i': 'i'},
    behind=[('longhair', {})], front=[('dao', dict(x=42.5, y0=8, y1=56))]))

# 獨臂漁翁 the One-Armed Fisherman: straw hat, long white beard, grey robe, fishing rod
person('yuweng', dict(
    colours=C(SK, BLACK, m=0x38, n=0x28, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, w=0x30, v=0x10, p=0x18, q=0x08,
              z=0x08),
    hair='straw', eyes='shut', mouth='none', beard='long', beard_slot='w', beard_shade='v', body='robe',
    collar='ea', behind=[('staff', dict(x=43.5, y0=6, y1=56))]))

# 鬼面護法 the Ghost-mask Warden: pointed blood-red hood and cloak, white fanged ghost mask, red eye light
person('guimian', dict(
    colours=C(SK, m=0x16, n=0x06, a=0x16, b=0x06, d=0x07, w=0x30, v=0x10, r=0x16, e=0x06, f=0x07, z=0x07),
    hair='hood', hair_slot='m', eyes='glare', mouth='none', mask='ghost', body='robe', collar='', neck='n',
    behind=[('hoodcape', {})], after=[(['k', 'm', 'k'], 23, 0, True)]))

# 蒙面人 the Masked Man: deep purple hood, black face cloth, purple robe edged in gold
person('masked', dict(
    colours=C(SK, m=0x04, n=0x0C, a=0x14, b=0x04, d=0x0C, e=0x28, f=0x18, g=0x0C, z=0x0C),
    hair='hood', hair_slot='m', eyes='keen', mouth='none', mask='cloth', mask_slot='g', mask_slot2='g',
    body='robe', collar='ea', neck='g', behind=[('hoodcape', {})]))
