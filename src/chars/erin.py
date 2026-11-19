"""艾琳 Erin - navigator and healer: reads stars, weather, wounds and the sea.
Ginger braid, sky-blue long tunic with navy trim, leather belt, tan trousers, brown boots, bamboo staff."""
import sys
from pixlib import G, Layer, fliph, strands
from variants import Variant

FACTION = 'west'
META = dict(
    id='erin',
    name={'zh': '艾琳', 'en': 'Erin'},
    style_name={'zh': '領航員', 'en': 'Navigator'},
    title={'zh': '觀星的醫者', 'en': 'The star-reading healer'},
    bio={
        'zh': '船上的領航員，也是醫者。看星象、讀天氣、包紮傷口，樣樣在行。'
              '船難後她把紅髮編成一條長辮，用江東的竹杖代替遺失的六分儀，照樣能說出明天會不會下雨。',
        'en': 'The ship\'s navigator and its healer: stars, weather and wounds are all hers to read. After the wreck she '
              'wears her red hair in one long braid and carries a Jiangdong bamboo staff in place of her lost sextant, '
              'and she can still tell you whether it will rain tomorrow.',
    },
    weapon={'zh': '竹杖', 'en': 'Bamboo staff'},
)

# ---------------------------------------------------------------- SNES (FF6-like)
SN = dict(
    k='#2a1c1c', E='#2c3450',
    S='#fcdcc0', s='#eab094', d='#c07c64',
    H='#f8a058', h='#d86a30', j='#963c1c',
    B='#a8d4f8', b='#70a8e0', n='#2c4c8c', N='#1c3060',
    L='#946038', l='#5e3a20', T='#e0c088', t='#ae8c58', W='#f8f8f0',
)

F_DOWN = G('''
.....kkkkk......
....kHHHHHkk....
...kHHHHHHHhk...
..kHHHhHHHhhhk..
..kHhSSSSSShhk..
..khSSSSSSSShk..
..khSESSSSEShk..
..khsSSSSSSshk..
..kjhsSssSshjk..
...kjksSSskhhk..
....knBBBBnkhk..
...kbBBnnBBbkhk.
..kbkBBBBBBkbjk.
..kbkBBBBBBkbjk.
..kskLLLLLLkskk.
...kkBBBBBBkk...
...kbBBBBBBbk...
...kbBBBBBBbk...
...knnnnnnnnk...
....kTTkkTtk....
....kTtk.kTtk...
....kTtk.kTtk...
....kLLk.kLlk...
....kkkk.kkkk...
''')

F_UP = G('''
.....kkkkk......
....kHHHHHkk....
...kHHHHHHHhk...
..kHHHHHHHhhhk..
..kHHHHHHhhhhk..
..kHHHHhhhhhhk..
..khHHhhhhhhhk..
..khhhhhhhhjhk..
..kjhhhhhhhjjk..
...kjjhhhhjjk...
....knBhhBnk....
...kbBBhhBBbk...
..kbkBBjhBBkbk..
..kbkBBhhBBkbk..
..kskLLjjLLksk..
...kkBBhhBBkk...
...kbBBjjBBbk...
...kbBBBBBBbk...
...knnnnnnnnk...
....kTTkkTtk....
....kTtk.kTtk...
....kTtk.kTtk...
....kLLk.kLlk...
....kkkk.kkkk...
''')

F_LEFT = G('''
......kkkkk.....
....kkHHHHHk....
...kHHHHHHHhk...
..kHHHHHHhhhhk..
..kSSHHHHhhhhk..
.kSSSSHHhhhhhk..
.kSESSSHhhhhk...
..ksSSSShhhjk...
...ksSSShhjkhk..
...kkssskkkhhk..
....knBBBnkkhk..
....kbBBBbkjk...
....kBkbBBbk....
....kBksBBbk....
....kLLLLLLk....
....kBBBBBbk....
....kBBBBBbk....
....kBBBBBbk....
....knnnnnnk....
.....kTTTtk.....
.....kTTtk......
.....kTTtk......
.....kLLLk......
....kkkkkk......
''')


STEP = ['....kTTkkTtk....', '....kTtk.kTtk...', '....kTtk.kLlk...', '....kLLk.kkkk...', '....kkkk........']


def legs_step(rows, which):
    """Front/back walk pose: one leg forward (a row longer), the other back."""
    feet = STEP if which == 0 else fliph(STEP)
    return list(rows[:19]) + feet


def side_step(rows, phase):
    """Side walk: legs apart (phase 1) or crossing (phase 2), hand-drawn feet."""
    r = [list(x) for x in rows[:19]]
    feet = {
        1: ['....kTTkkTtk....', '...kTtk..kTtk...', '..kTtk....kTtk..', '..kLLk....kLlk..', '.kkkk.....kkkk..'],
        2: ['.....kTTTtk.....', '.....kTkTtk.....', '....kTtkTtk.....', '....kLlkLLk.....', '...kkkkkkkk.....'],
    }[phase]
    return [''.join(x) for x in r] + feet


class SNESVariant(Variant):
    style = 'snes'
    primary = True
    fps = {'idle': 3, 'walk_down': 6, 'walk_up': 6, 'walk_left': 6, 'walk_right': 6}
    anchor = (8, 23)
    notes = {'walk_right': 'mirror of walk_left'}

    def frames(self):
        def im(rows):
            L = Layer(16, 24)
            L.stamp(rows)
            return L.image(SN)
        blink = list(F_DOWN)
        blink[6] = '..khSdSSSSdShk..'
        down = [im(F_DOWN), im(legs_step(F_DOWN, 0)), im(F_DOWN), im(legs_step(F_DOWN, 1))]
        up = [im(F_UP), im(legs_step(F_UP, 0)), im(F_UP), im(legs_step(F_UP, 1))]
        left = [im(F_LEFT), im(side_step(F_LEFT, 1)), im(F_LEFT), im(side_step(F_LEFT, 2))]
        right = [im(fliph(F_LEFT)), im(fliph(side_step(F_LEFT, 1))), im(fliph(F_LEFT)), im(fliph(side_step(F_LEFT, 2)))]
        return {'idle': [im(F_DOWN), im(F_DOWN), im(F_DOWN), im(blink)], 'walk_down': down, 'walk_up': up,
                'walk_left': left, 'walk_right': right}

    def portrait(self):
        return snes_portrait()


# portrait palette: soft, warm shadows, dark-brown line art
SP = dict(
    k='#3a2220', D='#b8705c', d='#dc9a80', s='#f4c4a4', S='#fde2cc', r='#c8605a', R='#e8908a', p='#f4b0a0',
    E='#30406c', e='#f6f2ee', W='#ffffff',
    Y='#ffc890', H='#f49a52', h='#d46a30', j='#a44a20', J='#6e2c14',
    B='#b4dcfa', b='#7cb0e4', n='#3a5ca0', N='#203a70', C='#f8d878', c='#b88a30',
)

HEAD = G("""
..........kkkkkkkk........
.......kkkSSSSSSsssdkk....
......kSSSSSSSSSssssddk...
.....kSSSSSSSSSSsssssddk..
....kSSSSSSSSSSssssssdddk.
....kSSSSSSSSSssssssssddk.
...kSSSSSSSSSSsssssssssddk
...kSSSSSSSSSssssssssssddk
...kSSSSSSSSsssssssssssddk
...kSSSSSSSSsssssssssssdDk
...kSSSSSSSssssssssssssdDk
...kSSSSSSSssssssssssssdDk
...kSSSSSSSsSSSSssssssddDk
...kSShhSSSShhhhhsssssddDk
...kSkkSSsskkkkkkkssddkkDk
...kkEkSSskeEEWekssssdkSdk
...kSESSSssseEEesssssdkSdk
...kSSSSSssSdddSssssddksDk
...kSSSSSsSSSSSsssssddkdDk
...kSSSSdsSSpppssssddkdk..
...kSSSSddsSppsssssdDDkk..
....kSSdsssssssssdddk.....
....kSSssssssssssddDk.....
....kSssrrrsssssssddk.....
....kSssRRssssssddDDk.....
.....kSsssssssssdDDk......
.....kSSssssssssdDk.......
......kSSsssssddDk........
.......kksssddDkk.........
.........kkkkkk...........
""")

HAIR = G("""
.........kkkkkkkkkk.............
......kkkYYYYHHHHHhhkk..........
.....kYYYYHHHHHHHHHhhhhk........
....kYYYHHHHHHHHHHHhhhhhhk......
...kYYYHHHHHHHHHHHhhhhhhhhk.....
...kYYHHHHHHHHHHHhhhhhhhjhhk....
..kYYHHHHHHHHHHhhhhhhhhhjjhk....
..kYHHHHHHHHHHhhhhhhhhhhjjhhk...
..kHHHHHHHHHhhhhhhhhhhhjjjhhk...
..kHHHHHHHhhhhhhhhhhhhjjjjhhk...
..kHHHHHHhhhhhhhhhhhhjjjjjhhk...
..kHHHHHhhhhhkhhhhhhhjjjjhhhk...
..kHHHHhhhhhk.khhhhhjjjjjhhhk...
..kHHHhhhhk....khhhjjjjjjhhk....
..kHHhhhkk......khhjjjjjhhhk....
..kHhhkk.........khjjjjjhhhk....
...kkk...........khjjjjjhhhk....
.................kjjjjjjhhk.....
.................kjjjjjjhhk.....
..................kjjjjjhhk.....
..................kjjjjhhk......
...................kjjhhhk......
""")


HAIR = strands(HAIR, base='h', hi='j', period=7, drift=-0.9, phase=3)


def braid(L, x, y0, y1):
    """Three-strand plait hanging from (x, y0) down to y1: alternating lobes."""
    y, side = y0, 0
    while y < y1:
        lobe = ['.kHHhk.', 'kHHhhjk', 'kHhhjjk', '.kjjJk.'] if side == 0 else \
               ['.khHHk.', 'kjhhHHk', 'kjjhhHk', '.kJjjk.']
        for i, row in enumerate(lobe):
            for j, c in enumerate(row):
                if c != '.' and y + i < 48:
                    L.set(x - 3 + j + (1 if side else 0), y + i, c)
        y += 3
        side ^= 1


def snes_portrait():
    from PIL import Image
    L = Layer(48, 48)
    # shoulders and the sky-blue tunic with a navy crossed collar (Han cut)
    keys = [(38, 15, 30), (39, 10, 35), (40, 7, 38), (42, 4, 41), (44, 2, 43), (47, 1, 45)]
    for y in range(38, 48):
        for (y0, l0, r0), (y1, l1, r1) in zip(keys, keys[1:]):
            if y0 <= y <= y1:
                t = (y - y0) / max(1, y1 - y0)
                l, r = round(l0 + (l1 - l0) * t), round(r0 + (r1 - r0) * t)
                for x in range(l, r + 1):
                    u = (x - l) / max(1, r - l)
                    L.set(x, y, 'B' if u < 0.3 else 'b' if u < 0.8 else 'n')
                L.set(l - 1, y, 'k'); L.set(r + 1, y, 'k')
                break
    for x in range(15, 31):
        L.set(x, 37, 'k')
    for i in range(10):                     # navy collar bands, right over left
        y = 38 + i
        for dx in range(3):
            L.set(26 - i + dx, y, 'n' if dx else 'N')
        if i < 5:
            for dx in range(3):
                L.set(17 + i + dx, y, 'n' if dx else 'N')
    L.set(20, 44, 'k'); L.set(21, 44, 'C'); L.set(22, 44, 'c'); L.set(21, 45, 'c'); L.set(20, 45, 'k')
    for y in range(40, 44):                 # compass cord
        L.set(21 if y % 2 else 22, y, 'c')
    # neck
    for y in range(33, 38):
        for x in range(17, 25):
            L.set(x, y, 'k' if x in (17, 24) else ('d' if x > 21 else 's'))
    L.stamp(HEAD, 9, 8)
    L.stamp(HAIR, 7, 5)
    braid(L, 35, 26, 48)
    # FF6 menu window: blue gradient and a bevelled grey frame
    img = Image.new('RGBA', (56, 56))
    P = img.load()
    for y in range(56):
        t = round(y / 55 * 5) / 5
        c = (round(0x40 + (0x10 - 0x40) * t), round(0x60 + (0x18 - 0x60) * t), round(0xc8 + (0x60 - 0xc8) * t), 255)
        for x in range(56):
            P[x, y] = c
    frame = ['#202020', '#d8d8d8', '#ffffff', '#909090']
    from pixlib import hex2rgba
    for i, col in enumerate(frame):
        cc = hex2rgba(col)
        for k in range(i, 56 - i):
            for (x, y) in ((k, i), (k, 55 - i), (i, k), (55 - i, k)):
                P[x, y] = cc
    img.alpha_composite(L.image(SP), (4, 4))
    return img


# ---------------------------------------------------------------- koei style (16-bit Three Kingdoms portrait + pixel-baseball chibi)
def koei_ns():
    from types import SimpleNamespace
    import portrait
    import faces
    ns = SimpleNamespace(FACTION=FACTION, HEAD=faces.FEMALE)
    ns.PAL = dict(
        k='#1e1010', D='#a06450', d='#c88870', s='#e8b090', S='#f8d4b8', E='#1a1820', B='#8a3a1a',
        u='#7a3030', r='#b85a54', R='#d88078',
        P='#9cc4e4', p='#6c98c8', q='#44689c', Q='#284470',
        c='#203a6a', C='#3a5a96', w='#d8d0c4', W='#f2ece0',
        Y='#f4b070', H='#e08840', h='#b85a24', j='#843a14', J='#521e0a',
    )
    BROWS = G("""
...kSBBSSSBBBBBSs.
""")

    def BODY():
        L = portrait.body_layer(keys=portrait.SHOULDERS_F, ramp='PpqQ')
        portrait.cross_collar(L, wide=2)
        return L

    def BRAID(L):
        braid(L, 40, 31, 64)
    ns.BODY = BODY
    ns.FACE = [(BROWS, 0, 12), (HAIR, -2, -3)]
    ns.FRONT = [BRAID]
    ns.CPAL = dict(
        k='#1e1010', S='#fbd8bc', s='#e8b090', d='#c08068', E='#1a1820', B='#8a3a1a', r='#c86058',
        X='#f09a50', x='#c8642a', z='#843a14', R='#284c8c',
        P='#a8d0f0', p='#78a8dc', q='#4c74b0', C='#284c8c', c='#1c3466', W='#f2ece0', w='#d0c8bc',
        Y='#8a5a30', y='#5e3a1c', O='#6a4428', o='#462a16', L='#d8bc88', l='#a88a58',
    )
    C_HAIR = G("""
.......kkkkkkk........
.....kkXXXXxxxkk......
...kkXXXXXxxxxxxkk....
..kXXXXXxxxxxxxxxzk...
.kXXXXXxxxxxxxxxxzzk..
.kXXXXxxxxxxxxxxxzzk..
kXXXXxxxxkxxxxxxxxzzk.
kXXXxxxk.kxxxxxxxxzzk.
kXXxxkk...kkxxxxxxzzk.
kXxkk.......kkxxxxzzk.
kXk...........kxxxzk..
kk.............kxxzk..
................kxzk..
""")
    C_BRAID = G("""
.kxk.
kXxzk
kxzzk
.kXk.
kXxzk
kxzzk
.kXk.
kXxzk
kxzzk
.kXk.
.kRk.
..k..
""")
    ns.CHIBI = dict(costume='dress', face=[(C_HAIR, -1, -2)], torso_over=[(C_BRAID, 15, -2)])
    return ns


def variants():
    from variants import KoeiVariant
    return [SNESVariant(), KoeiVariant(koei_ns(), full=False)]
