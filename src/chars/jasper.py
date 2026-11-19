"""賈斯珀 Jasper - the youngest traveller: scout and archer, quick and light-fingered.
Blonde cowlick, green laced tunic, scarf, brown trousers and boots, short bow and quiver."""
import sys
from pixlib import G, Layer, fliph
from variants import Variant

FACTION = 'west'
META = dict(
    id='jasper',
    name={'zh': '賈斯珀', 'en': 'Jasper'},
    style_name={'zh': '斥候', 'en': 'Scout'},
    title={'zh': '眼尖的斥候', 'en': 'The sharp-eyed scout'},
    bio={
        'zh': '八歲的弟弟，一家人裡最小也最快。眼尖手巧，背著小布包、拿著彈弓，'
              '地圖上的祕密總是他先發現；頭上兩個小髻是媽媽每天早上替他綁的。',
        'en': 'The eight-year-old little brother, smallest and quickest of the family. Sharp eyes, quick hands, a '
              'satchel and a slingshot: he finds the map\'s secrets first. Mum ties his two little hair buns every '
              'morning.',
    },
    weapon={'zh': '彈弓', 'en': 'Slingshot'},
)

# ---------------------------------------------------------------- NES (Dragon Quest-like)
# Sprites follow NES hardware rules: a 16x16 character is four 8x8 sprites; the
# top pair (head) and the bottom pair (body) each use one 3-colour palette + transparency.
# The portrait follows NES background rules: black shared, at most 4 colours in
# every 16x16 attribute block (checked by nes_check()).
NES = dict(k='#000000', W='#fcfcfc', p='#fcd8a8', Y='#f8b800', g='#00a800', b='#ac7c00')
TOP = {'k', 'p', 'Y'}         # head sprites: black, skin, blonde
BOT = {'k', 'g', 'b'}         # body sprites: black, green tunic, brown scarf/gloves/boots

DOWN = G("""
......kk.k......
.....kYYkYk.....
...kkYYYYYYkk...
..kYYYYYYYYYYk..
..kYYpYYYYpYYk..
..kYppppppppYk..
..kYpkppppkpYk..
...kppppppppk...
....kbbbbbbkbb..
...kbbbbbbbbkb..
..kbkgkgkggkbk..
..kbkggkgggkbk..
...kkgggggggk...
....kbbkkbbk....
....kkkk.kkkk...
.........kkkk...
""")

UP = G("""
......kk.k......
.....kYYkYk.....
...kkYYYYYYkk...
..kYYYYYYYYYYk..
..kYYYYYYYYYYk..
..kYYYYkYYYYYk..
..kpYYYYYkYYpk..
...kYYYYYYYYk...
....kbbbbbbkb...
...kbbbbbbbbkbk.
..kbkggbgbgkbk..
..kbkgggbbgkbk..
...kkgggggbgk...
....kbbkkbbk....
....kkkk.kkkk...
.........kkkk...
""")

LEFT_A = G("""
.......kk.k.....
.....kkYYkYk....
....kYYYYYYYk...
...kYYYYYYYYYk..
..kpYpYYYYkYYk..
.kppppppkpYYYk..
..kkpppppkYYk...
...kpppppppk....
....kkbbbbkkbb..
....kbbbbbbkbbk.
....kgkbbkgkbk..
....kgkbbkgkk...
....kkggggkk....
.....kbbbbbk....
.....kkk.kkk....
....kkkk.kkkk...
""")

LEFT_B = G("""
.......kk.k.....
.....kkYYkYk....
....kYYYYYYYk...
...kYYYYYYYYYk..
..kpYpYYYYkYYk..
.kppppppkpYYYk..
..kkpppppkYYk...
...kpppppppk....
....kkbbbbkkbb..
....kbbbbbbkbbk.
....kggkbbgkbk..
....kggkbbgkk...
....kkggggkk....
....kbbkkbbk....
...kkkk..kkkk...
...kkk....kkk...
""")


def sprite_check(rows, name):
    for y, r in enumerate(rows):
        allowed = TOP if y < 8 else BOT
        bad = {c for c in r if c != '.' and c not in allowed}
        assert not bad, (name, y, bad)


for _n, _r in (('down', DOWN), ('up', UP), ('left_a', LEFT_A), ('left_b', LEFT_B)):
    sprite_check(_r, _n)


class NESVariant(Variant):
    style = 'nes'
    primary = True
    fps = {'idle': 2, 'walk_down': 4, 'walk_up': 4, 'walk_left': 4, 'walk_right': 4}
    anchor = (8, 15)
    notes = {'idle': 'Dragon Quest-style: characters always mark time',
             'walk_right': 'mirror of walk_left'}

    def frames(self):
        def im(rows):
            L = Layer(16, 16)
            L.stamp(rows)
            return L.image(NES)
        return {
            'idle': [im(DOWN), im(fliph(DOWN))],
            'walk_down': [im(DOWN), im(fliph(DOWN))],
            'walk_up': [im(UP), im(fliph(UP))],
            'walk_left': [im(LEFT_A), im(LEFT_B)],
            'walk_right': [im(fliph(LEFT_A)), im(fliph(LEFT_B))],
        }

    def portrait(self):
        L = Layer(48, 48, 'k')
        L.stamp(NES_FACE)
        # Dragon Quest window: white frame inset by one pixel, rounded corners
        for i in range(2, 46):
            for (x, y) in ((i, 1), (i, 46), (1, i), (46, i)):
                L.set(x, y, 'W')
        for (x, y) in ((2, 2), (45, 2), (2, 45), (45, 45)):
            L.set(x, y, 'W')
        nes_check(L)
        return L.image(NES)


def nes_check(L):
    for by in range(0, 48, 16):
        for bx in range(0, 48, 16):
            cols = {L.get(x, y) for y in range(by, by + 16) for x in range(bx, bx + 16)}
            assert len(cols) <= 4, ('attribute block', bx, by, sorted(cols))


# left half of the face (mirrored), then the asymmetric details
_HALF = G("""
........................
........................
........................
........................
........................
..................kkkkkk
...............kkkYYYYYY
.............kkYYYYYYYYY
............kYYYYYYYYYYY
...........kYYYYYYYYYYYY
..........kYYYYYYYYYYYYY
..........kYYYYYYYYYYYYY
.........kYYYYYYYYYYYYYY
.........kYYYYYYYkYYYYYk
.........kYYYYYYkpkYYYkp
.........kYYYYYkppkYYkpp
.........kYYYYkpppkkkppp
.........kYYYkpppppppppp
.........kYYkpkkpppppppp
........kkYkppppkkkkpppp
.......kpkkppppppppppppp
.......kppkppppWkkpppppp
.......kppkpppppkkkppppp
........kpkppppppppppppp
.........kkppppppppppppp
..........kppppppppppppp
..........kppppppppppppp
...........kpppppppppppp
...........kppppppppkkkk
............kppppppppppp
.............kkppppppppp
...............kkkkkkkkk
..........kkkkkbbbbbbbbb
........kkbbbbbbbbbbbbbb
......kkggkbbbbbbbbbbbbb
.....kgggggkkbbbbbbbbbbb
....kggggggggkkkkkkkkbbb
....kggggggggggggggggkbk
...kgggggggggggggggggggk
...kgggggggggggggggggggg
...kgggggggggggggggggggg
...kgggggggggggggggggggg
...kgggggggggggggggggggg
...kgggggggggggggggggggg
...kgggggggggggggggggggg
........................
........................
........................
""")


def _face():
    rows = [list(r + r[::-1]) for r in _HALF]

    def put(x, y, c):
        rows[y][x] = c
    for (x, y) in ((26, 3), (27, 3), (25, 4), (28, 4), (24, 5), (27, 5)):   # cowlick
        put(x, y, 'k')
    for (x, y) in ((26, 4), (27, 4), (25, 5), (26, 5)):
        put(x, y, 'Y')
    put(24, 25, 'k'); put(25, 24, 'k')                       # nose shadow
    for x in range(24, 30):                                  # lopsided grin
        put(x, 28, 'k' if x < 29 else 'p')
    put(29, 27, 'k'); put(30, 27, 'k')
    for y in range(37, 45):                                  # tunic lacing
        put(23, y, 'k' if y % 2 else 'g'); put(24, y, 'g' if y % 2 else 'k')
    for i in range(10):                                      # quiver strap across the chest
        x, y = 13 + i * 2, 35 + i
        if y < 45 and rows[y][x] == 'g':
            put(x, y, 'b'); put(x + 1, y, 'b')
    for (x, y) in ((33, 32), (34, 33), (35, 33), (36, 34), (35, 35), (36, 35), (37, 36)):   # scarf tail
        put(x, y, 'b')
    for y in range(32, 45):                                  # bow limb over the shoulder
        x = 41 - abs(y - 38) // 3
        if rows[y][x] in '.g':
            put(x, y, 'b')
        if rows[y][x + 1] == '.':
            put(x + 1, y, 'k')
    return [''.join(r) for r in rows]


NES_FACE = _face()


# ---------------------------------------------------------------- koei style (16-bit Three Kingdoms portrait + pixel-baseball chibi)
def koei_ns():
    from types import SimpleNamespace
    import portrait
    import faces
    from pixlib import stroke
    ns = SimpleNamespace(FACTION=FACTION)
    ns.PAL = dict(
        k='#1a120a', D='#8a5038', d='#b47658', s='#dca07c', S='#f4c8a2', E='#1a1410', B='#8a6420',
        u='#6a3024', r='#b06050',
        P='#5aa04a', p='#3a7c34', q='#245a24', Q='#143a16',
        c='#8a5a24', C='#b47c38', w='#6a4418', W='#c8944a',
        J='#f6d478', j='#d8a840', i='#9a6c1c', T='#7a4a1c', t='#4a2a10', F='#d8c8a0',
    )
    COWLICK = G("""
.........kk.k....
........kJJkJk...
.......kJjjJjk...
""")
    BROWS = G("""
..kBB...BBBBBBB.
""")

    def BODY():
        L = portrait.body_layer(ramp='PpqQ')
        portrait.cross_collar(L, wide=4, under='C', over='C', edge='W', inner='w', inner_hi='c')
        for i in range(18):                       # quiver strap across the chest
            x, y = 12 + i * 2, 63 - i
            for dx in (0, 1):
                if L.get(x + dx, y) in 'PpqQ':
                    L.set(x + dx, y, 't' if i % 3 else 'T')
        return L

    def BOW(L):
        def tone(t, side):
            return 'T' if side < 0.2 else 't'
        stroke(L, (46, 18), (57, 40), (47, 63), width=lambda t: 1.0, tone=tone)
        for y in range(19, 63):
            x = round(46 + (47 - 46) * (y - 18) / 45)
            if L.get(x, y) == '.':
                L.set(x, y, 'F')
    ns.BODY = BODY
    ns.BACK = [BOW]
    ns.FACE = [(faces.YOUNG, 0, 22), (faces.MALE_HAIR, 0, -1, {'X': 'J', 'x': 'j', 'z': 'i'}), (COWLICK, 4, -3),
               (BROWS, 0, 12)]
    ns.CPAL = dict(
        k='#1a120a', S='#f8d0aa', s='#dca07c', d='#b47658', E='#1a1410', B='#8a6420', r='#b06050',
        X='#fae088', x='#e0b048', z='#a87420',
        P='#62aa52', p='#3e8236', q='#26602a', C='#b47c38', c='#8a5a24', W='#c8944a', w='#8a5a24',
        Y='#7a4a1c', y='#4a2a10', L='#8a5a30', l='#5e3a1c', O='#5a3418', o='#3a200c', T='#7a4a1c', t='#4a2a10',
    )
    C_HAIR = G("""
..........kk.k........
.....kkkkkXXkXkk......
...kkXXXXXXXXXxxkk....
..kXXXXXXXXXxxxxxzk...
.kXXXXXXXXxxxxxxxzzk..
.kXXXXxXXxxxxxxxxzzk..
kXXXXxXXxxxxxxxxxxzzk.
kXXkXXkXxkxxkxxkxxzzk.
kXk.kk.kk.kk.kk.kxkzk.
kk................kk..
""")
    C_BOW = G("""
....kk..
...kTk..
..kTtk..
..kTk...
.kTtk...
.kTk....
.kTk....
.kTk....
.kTtk...
..kTk...
..kTtk..
...kTk..
....kk..
""")
    ns.CHIBI = dict(costume='armor', face=[(C_HAIR, -1, -2)], back=[(C_BOW, 16, 8)])
    return ns


def variants():
    from variants import KoeiVariant
    from family_variant import FamilyVariant
    v = NESVariant()
    v.primary = False
    return [FamilyVariant('jasper'), v, KoeiVariant(koei_ns(), full=False)]
