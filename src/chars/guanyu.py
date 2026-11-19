"""關羽 Guan Yu - red face, phoenix eyes, silkworm brows, long beard, green headscarf,
green robe over gold armour, the Green Dragon Crescent Blade behind his shoulder."""
from pixlib import G, strands, stroke, rot90, fliph
import portrait

FACTION = 'shu'
META = dict(
    id='guanyu',
    name={'zh': '關羽', 'en': 'Guan Yu'},
    style_name={'zh': '雲長', 'en': 'Yunchang'},
    title={'zh': '美髯公', 'en': 'Lord of the Beautiful Beard'},
    bio={
        'zh': '河東解良人，與劉備、張飛結為兄弟。赤面長髯，綠巾綠袍，手持青龍偃月刀。'
              '重義守信，千里尋兄的故事流傳至今。',
        'en': 'A man of Xieliang in Hedong, sworn brother of Liu Bei and Zhang Fei. Red-faced and long-bearded, '
              'in a green headscarf and robe, he carries the Green Dragon Crescent Blade. His loyalty '
              'is remembered in the tale of riding a thousand li to rejoin his brother.',
    },
    weapon={'zh': '青龍偃月刀', 'en': 'Green Dragon Crescent Blade'},
)
GREEN = dict(P='#5aa462', p='#33804a', q='#1f5c36', Q='#123c24')
GOLD = dict(C='#f2d27a', c='#c89a40')
PAL = dict(
    k='#160c0a', E='#160c0a', B='#160c0a',
    D='#5e2018', d='#8e3426', s='#b84a34', S='#d8704e', u='#3a1410', r='#7a2a22',
    w='#a8a6a6', W='#e6dece', R='#c83a2a',
    X='#4c5466', x='#1c1e26', z='#0a0b10',
    F='#eef2f6', f='#a8a6a6',
    **GREEN, **GOLD,
    G=GREEN['P'], g=GREEN['p'], h=GREEN['q'], H=GREEN['Q'],
    Y=GOLD['C'], y=GOLD['c'],
    M=GOLD['c'], m='#94682c', n='#5a3e18', N='#2c1e0c', T='#5a3e18',
)

HAT = G('''
...........kkkkkk............
.........kkGGGGggkk..........
.......kkGGGGGGggghkk........
......kGGGGGGGgggggghk..kk...
.....kGGGGGGGggggggghhkkghk..
....kGGGGGGhgggggggghhhkghhk.
....kGGGGGhggggggggghhhhkhhk.
...kGGGGGhgggggggggghhhhHkHk.
...kGGGGhggggggggggghhhhHHk..
...kGGGhgggggggggggghhhhHHk..
..kGGGGhgggggggggggghhhhHHHk.
..kGGGhggggggggggggghhhhHHHk.
..kGGkkkkgggggggggghhhhhHHHk.
..kGkYYYykgggggggghhhhhHHHHk.
.kGGkYRYykgggggggghhhhHHHHkhk
.kgGkYyyykggggggghhhhhHHHHkhhk
.kggGkkkkGGGgggghhhhhHHHHkkhhk
..kkgggggggggghhhhhhHHHHk.khHk
....kkkkkkkkkkkkkhhhHHHk...khHk
................kkkkkkk.....khk
............................khk
............................kHk
.............................kk
''')

# a second cloth fold toward the back of the headscarf
_rows = [list(r) for r in HAT]
for x, y in [(20, 4), (20, 5), (19, 6), (19, 7), (18, 8), (18, 9), (17, 10), (17, 11), (16, 12)]:
    if _rows[y][x] in 'Ggh':
        _rows[y][x] = 'H'
        if _rows[y][x - 1] in 'gh':
            _rows[y][x - 1] = 'g' if _rows[y][x - 1] == 'h' else 'G'
HAT = [''.join(r) for r in _rows]

BEARD = G('''
...................kz.....
...................xz.....
..................kxz.....
..................xxz.....
..................xxz.....
.................kxxz.....
.................Xxxz.....
........k.......kXxxz.....
...kXXXxxxk....kXxxzk.....
..kXXkuuukXk..kXxxxzk.....
..kXk.rrr.kXxkXxxxzk......
..kXxxkkkxxxXxxxxxzk......
..kXXxxxxxxXxxxxxxzk......
..kXxXxxxxXxxxxxxzzk......
...kXxXxxxXxxxxxzzk.......
...kXxxXxxxXxxxxzzk.......
...kXxxXxxxXxxxzzk........
....kXxxXxxxXxxzzk........
....kXxxXxxxXxxzk.........
....kxXxxXxxxXzzk.........
....kxXxxXxxxXzk..........
.....kXxxXxxxzzk..........
.....kxXxxXxxzk...........
.....kxXxxXxzzk...........
......kXxxXxzk............
......kxXxxXzk............
......kxxkxxzk............
.....kxxk.kxzk............
.....kxk..kxk.............
......k....k..............
''')

# phoenix eyes (long, outer corner raised, a tiny catchlight) under silkworm brows
BROWS = G('''
..kBBBSSBBBBBBB...
..kSSSSSsSdddDkkE.
..kdEdSSsdkEWEk...
...kddSSssSsssd...
''')

# the Green Dragon Crescent Blade rising behind the near shoulder
BLADE = G('''
..kk..........
.kFFk.........
.kFFFk........
..kFFFk.......
..kFFFFk......
..kfFFFFk.....
..kfFFFFFk....
..kffFFFFFk...
.kkffFFFFFFk..
kfkffFFFFFFFk.
.kkffFFFFFFFk.
..kffFFFFFFFFk
..kffFFFFFFFFk
..kfffFFFFFFFk
..kfffFFFFFFk.
..kfffFFFFFk..
..kkffFFFFk...
.kYYkfFFkk....
kYYYykkk......
kRYyyk........
kRRYyk........
.kRRk.........
..kk..........
''')


def POLEARM(L):
    for y in range(21, 64):
        L.set(42, y, 'k'); L.set(43, y, 'T'); L.set(44, y, 'k')
    L.stamp(BLADE, 41, 0)


def BODY():
    L = portrait.body_layer(ramp='PpqQ')
    # gold lamellar armour shows on the far side of the chest, under the green robe
    arm = portrait.body_layer(ramp='PpqQ')
    portrait.lamellar(arm, top=43)
    for y in range(43, 64):
        edge = 31 - (y - 42) - 1
        for x in range(2, max(2, edge)):
            if arm.get(x, y) in 'MmnN':
                L.set(x, y, arm.get(x, y))
    portrait.cross_collar(L, wide=3)
    # drape folds on the near side of the robe
    dn = {'P': 'p', 'p': 'q', 'q': 'Q', 'Q': 'Q'}
    for (x0, y0), (x1, y1) in (((36, 50), (39, 63)), ((47, 47), (50, 63)), ((31, 56), (32, 63))):
        for y in range(y0, y1 + 1):
            x = round(x0 + (x1 - x0) * (y - y0) / (y1 - y0))
            c = L.get(x, y)
            if c in dn:
                L.set(x, y, dn[dn[c]] if c == 'p' else dn[c])
    return L


BACK = [POLEARM]
FACE = [(BROWS, 0, 13), (BEARD, 0, 14)]
FRONT = [(HAT, 14, 4)]


# ---------------- chibi ----------------
import chibi

CPAL = dict(
    k='#1a0e0a', S='#e07a58', s='#c0503a', d='#8e3426', E='#140806', B='#140c0a', r='#6a1e18',
    X='#4a5268', x='#20232e', z='#0e0f16',
    G='#62ac68', g='#3a8a50', h='#24663c', H='#14442a', Y='#f0c858', y='#a87a28', R='#d03c2c',
    P='#58a060', p='#367c48', q='#205a36', C='#f0c858', c='#c89a40', W='#f0e8d8', w='#b8b0a0',
    L='#2e4a34', l='#1e3424', O='#4a3424', o='#2a1c12',
    F='#eef2f6', f='#94a2b4', T='#963c24', t='#5a2414',
)

C_HAT = G('''
........kkkkkk........
.....kkkGGGGggkkk.....
....kGGGGGGGggggghk...
...kGGGGGGGGgggghhhk..
..kGGGGGGGGgggggghhhk.
..kGGGGGGGgggggghhhhk.
.kGGGGGGGGggggghhhhhHk
.kGGGGGGGgggggghhhhhHk
.kGGGGGGkkkkggghhhhhHk
.kGGGGGkYYRykgghhhhHHk
.kgGGGGkYyyykgghhhhHHk
.kggggGGkkkkGgghhhHHk.
..kkhhhhhhhhhhhhhHHkk.
''')

C_TAILS = G('''
.kk.
khhk
khHk
.khHk
.khHk
..kHk
..khk
..kHk
...k.
''')

C_BROWS = G('''
..BBBB......BBBB..
''')

C_BEARD = G('''
kxk..........kxk
kxxk.kxxxxk.kxxk
kxxxkxk..kxkxxxk
kxXxxxxkkxxxxxzk
.kxXxxxxxxxxxxzk
.kxxXxxxxxxxxzk.
..kxXxxxxxxxxzk.
..kxxXxxxxxxzk..
...kxXxxxxxzk...
...kxxXxxxxzk...
....kxXxxxzk....
....kxxXxxzk....
.....kxXxzk.....
.....kxxXzk.....
......kxzk......
.......kk.......
''')
C_BEARD = C_BEARD[:3] + strands(C_BEARD[3:], period=3, drift=-0.34, keep_hi=False)

C_BLADE = G('''
...kk.......
..kFFk......
.kFFFk......
.kFFfk......
kFFFfk......
kFFFffk.....
kFFFFfk.....
kFFFFffk....
kFFFFfffk...
kFFFFffffkk.
kFFFFFfffkYk
.kFFFFfffkYk
.kFFFFffkYYk
..kFFFfkkYyk
...kFFkRRYyk
....kkRRRkk.
.....kRRk...
......kk....
''')


def C_PROP(L, view, phase, bob, arm):
    if view == 'front':
        chibi.polearm(L, 16, 47 + bob + arm[0], C_BLADE, -10, -9, length_up=31, length_down=13)


def _swoosh(p0, p1, p2):
    def draw(L):
        stroke(L, p0, p1, p2, width=lambda t: 0.4 + 1.8 * t, tone=lambda t, side: 'W' if side < 0.2 else 'w', outline=None)
    return draw


def C_ACTION():
    base = dict(CHIBI)

    class V:      # a view of this module with a swapped prop
        CPAL_ = CPAL

    def with_prop(prop, back=None):
        V.CHIBI = dict(base, prop=prop, prop_back=back)
        return V

    def ready(L, view, phase, bob, arm):
        chibi.polearm(L, 39, 47 + bob, fliph(C_BLADE), -1, -9, length_up=31, length_down=13)

    blade_l = rot90(C_BLADE, cw=False)

    def sweep(L, view, phase, bob, arm):
        chibi.hshaft(L, 47 + bob, 15, 51)
        L.stamp(blade_l, 2, 46 + bob)

    def strike(L, view, phase, bob, arm):
        chibi.hshaft(L, 48 + bob, 12, 46)
        L.stamp(blade_l, -1, 47 + bob)

    sw1 = _swoosh((50, 44), (30, 18), (6, 40))
    sw2 = _swoosh((52, 40), (44, 62), (8, 56))
    return [chibi.front(with_prop(ready), 0, 1, (0, -2)),
            chibi.front(with_prop(sweep, lambda L, *a: sw1(L)), 0, 0, (0, 0)),
            chibi.front(with_prop(strike, lambda L, *a: sw2(L)), 2, 1, (1, 1)),
            chibi.front(sys.modules[__name__], 0, 0)]


C_HAT_SIDE = G('''
........kkkkkk........
.....kkkGGGGGGkk......
...kkGGGGGGGGGGGkk....
..kgGGGGGGGGGGGGGGk...
.kggGGGGGGGGGGGGGGGk..
.kggGGGGGGGGGGGGGGGk..
khggGGGGGGGGGGGGGGGGk.
khgggGGGGGGGGGGkkkkGk.
khhgggGGGGGGGGkYYRykk.
khhgggGGGGGGGGkYyyyk..
kHhhgggGGGGGGGGkkkkk..
kHhhhggggGGGGGGGGGk...
.kHhhhhhhhhhhhhhhhk...
''')

C_TAILS_SIDE = G('''
.kk..
khhk.
khHk.
khHk.
.khHk
.khHk
.kHk.
.khk.
..k..
''')

C_BEARD_SIDE = G('''
kxk...........
kxxk.....kk...
kxxxk...kxxk..
kxxxxkkkxxk...
.kxxxxxxxxxk..
.kxXxxxxxxxk..
..kxXxxxxxxk..
..kxxXxxxxk...
...kxXxxxxk...
...kxxXxxk....
....kxXxxk....
....kxxXk.....
.....kxxk.....
.....kxk......
......k.......
''')
C_BEARD_SIDE = C_BEARD_SIDE[:4] + strands(C_BEARD_SIDE[4:], period=3, drift=-0.34, keep_hi=False)

C_BROW_SIDE = G('''
...........BBBBB
''')


def C_SIDE_PROP(L, step, bob):
    chibi.polearm(L, 38, 46 + bob, fliph(C_BLADE), -1, -9, length_up=31, length_down=13)


def C_SIDE():
    return chibi.side_walk(sys.modules[__name__])


import sys
CHIBI = dict(costume='robe', action=C_ACTION, side=C_SIDE, side_prop=C_SIDE_PROP,
             side_back=[(C_TAILS_SIDE, -2, 3)],
             side_face=[(C_BROW_SIDE, 1, 8), (C_HAT_SIDE, -1, -7), (C_BEARD_SIDE, 8, 11)], back=[(C_TAILS, 18, 2)],
             face=[(C_BROWS, 1, 8), (C_HAT, -1, -7), (C_BEARD, 2, 12)], prop=C_PROP)


def variants():
    from variants import KoeiVariant
    from nes_variant import NESVariant
    return [NESVariant('guanyu'), KoeiVariant(sys.modules[__name__])]
