"""傑夫 Jeff - shipwright and engineer, the party's strategist who builds fire rafts.
Messy chestnut hair, stubble, round glasses, brown frock coat over a Han-cut linen shirt, charcoal trousers, boots, wrench."""
import math
import sys
from pixlib import G, Layer, fliph, hex2rgba
from variants import Variant
import faces
from paint import Soft

FACTION = 'west'
META = dict(
    id='jeff',
    name={'zh': '傑夫', 'en': 'Jeff'},
    style_name={'zh': '船匠', 'en': 'Shipwright'},
    title={'zh': '造火船的軍師', 'en': 'The strategist who builds fire rafts'},
    bio={
        'zh': '船匠兼工程師，四人之中的軍師。眼鏡在船難裡裂了一角，扳手卻一直插在腰間。'
              '他看得懂江東的船，也看得懂風向，第一個想到把整條船變成火龍衝進敵陣。',
        'en': 'Shipwright, engineer and the strategist of the four. His glasses cracked in the wreck, but the wrench '
              'never left his belt. He reads Jiangdong hulls as well as the wind, and was the first to think of turning '
              'a whole boat into a fire dragon and sailing it into the enemy line.',
    },
    weapon={'zh': '扳手與火龍船', 'en': 'Wrench and fire rafts'},
)

# ---------------------------------------------------------------- HD-2D (Octopath-like)
RAMPS = {
    'skin': ['#4e2a20', '#74402e', '#9a5c44', '#c07c5e', '#dc9c7a', '#eebc98', '#f9d8bc'],
    'hair': ['#22110a', '#3c1e10', '#5c2f18', '#7e4422', '#9e5a2e', '#bc7840', '#d89a5c'],
    'coat': ['#1a120c', '#2e2016', '#463220', '#5e442c', '#78583a', '#94704a', '#b08c62'],
    'shirt': ['#5e5a52', '#7e786c', '#9e9686', '#bcb4a2', '#d6cfbd', '#e9e3d4', '#f7f3ea'],
    'neck': ['#4e2a20', '#74402e', '#9a5c44', '#c07c5e', '#dc9c7a', '#eebc98', '#f9d8bc'],
    'line': ['#2a160e'],
}


def hair_mask(x, y):
    spans = {4: (30, 36), 5: (27, 40), 6: (24, 46), 7: (22, 50), 8: (20, 54), 9: (19, 57), 10: (18, 59),
             11: (17, 61), 12: (16, 62)}
    if y in spans:
        l, r = spans[y]
    elif 13 <= y <= 20:
        l, r = 15, 64
    elif 21 <= y <= 26:
        l, r = 15, 66
    elif 27 <= y <= 31:
        l, r = 16, 67
    else:
        l, r = 99, -1
    if l <= x <= r:
        return True
    # fringe locks hanging over the forehead
    for (tx, ty, w) in ((21, 37, 3), (26, 35, 2), (31, 36, 3), (37, 34, 2), (42, 33, 2), (47, 35, 3)):
        if 31 < y <= ty and abs(x - tx) <= w * (ty - y) / (ty - 31):
            return True
    if 32 <= y <= 40 and 44 <= x <= 67:          # temple and side hair
        return True
    if 40 < y <= 47 and 53 <= x <= 56:           # sideburn
        return True
    # messy tufts on the crown
    for (tx, ty) in ((24, 5), (35, 2), (46, 3), (57, 7), (63, 11)):
        if abs(x - tx) <= (8 - (y - ty)) // 3 and ty <= y <= ty + 6:
            return True
    return False


def hair_tone(x, y):
    t = 5.2 - (x - 15) / 52 * 3.4 - (y - 4) / 30 * 1.0
    a = math.atan2(y - 6, x - 44)
    r = math.hypot(x - 44, y - 6)
    if math.sin(a * 17 + r * 0.22) > 0.62:
        t -= 1.4
    if 13 <= r <= 16 and x < 46:
        t += 1.0
    return max(0.0, min(6.0, t))


def hd2d_portrait():
    W, H = 80, 104
    S = Soft(W, H, RAMPS)
    # coat: shoulders, lit from the left, with wide frock lapels; linen Han shirt crossed under it
    keys = [(77, 30, 54), (79, 20, 64), (81, 13, 70), (85, 7, 75), (91, 3, 78), (103, 0, 79)]
    for y in range(77, H):
        for (y0, l0, r0), (y1, l1, r1) in zip(keys, keys[1:]):
            if y0 <= y <= y1:
                t = (y - y0) / max(1, y1 - y0)
                l, r = round(l0 + (l1 - l0) * t), round(r0 + (r1 - r0) * t)
                for x in range(l, r + 1):
                    u = (x - l) / max(1, r - l)
                    S.put(x, y, 'coat', 5.5 - u * 4.5)
                break
    for y in range(76, H):                        # shirt V with crossed collar
        half = 3 + (y - 76) * 0.55
        for x in range(int(41 - half), int(43 + half)):
            if S.get(x, y) == 'coat':
                S.put(x, y, 'shirt', 4.2 if x < 42 else 2.6)
        for x in (int(41 - half) - 1, int(41 - half) - 2, int(43 + half), int(43 + half) + 1):   # lapels, lit edge
            if S.get(x, y) == 'coat':
                S.put(x, y, 'coat', 6 if x < 42 else 1)
    for i in range(16):                           # shirt crossing (right over left)
        S.put(46 - i, 77 + i, 'shirt', 1.2)
    for y in range(60, 82):                       # neck in shadow
        for x in range(33, 52):
            S.put(x, y, 'neck', 2.6 if x < 40 else 1.2)
    # head: the hand-drawn 3/4 male head at 2x
    key = {'k': ('skin', 0.4), 'D': ('skin', 1), 'd': ('skin', 2.2), 's': ('skin', 4), 'S': ('skin', 5.3),
           'E': ('skin', 2.2), 'B': ('skin', 3), 'r': ('skin', 3)}
    S.stamp(faces.MALE, 14, 12, key, scale=2)
    # silhouette line stays dark; inner template lines become soft skin creases
    for y in range(H):
        for x in range(W):
            if S.get(x, y) == 'skin' and S.t[y][x] < 0.5:
                edge = any(S.get(x + dx, y + dy) is None for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                S.t[y][x] = 0 if edge else 1.6
    for y in range(H):
        for x in range(W):
            if hair_mask(x, y) and not (57 <= x <= 66 and 41 <= y <= 56):
                S.put(x, y, 'hair', hair_tone(x, y))
    S.soften(passes=2)
    # stubble on the jaw and upper lip
    import random
    rnd = random.Random(7)
    for y in range(55, 74):
        for x in range(20, 58):
            if S.get(x, y) != 'skin' or (27 <= x <= 37 and 58 <= y <= 62):
                continue
            jaw = (y >= 62) or (x >= 44 and y >= 52) or (y in (56, 57) and 25 <= x <= 38)
            if jaw and rnd.random() < 0.38:
                S.t[y][x] = max(0, S.t[y][x] - 1.3)
    # nose: lit ridge, shadowed side, nostril and the shadow under it
    for y in range(44, 53):
        S.t[y][30 - (y - 44) // 4] = min(6, S.t[y][30 - (y - 44) // 4] + 1.0)
        S.t[y][32 - (y - 44) // 5] = max(0, S.t[y][32 - (y - 44) // 5] - 1.2)
    for x in range(20, 31):
        S.t[55][x] = max(0, S.t[55][x] - 1.4)
    S.t[54][24] = 0.6; S.t[54][25] = 1
    feats = HD_FEATURES
    for y, r in enumerate(feats):
        for x, c in enumerate(r):
            if c != '.':
                S.paint(18 + x, 38 + y, FEAT_PAL[c])
    # round glasses: thin dark-gold wire rims and a cool glint
    def ring(cx, cy, rx, ry, col):
        for k in range(120):
            a = k / 120 * 2 * math.pi
            S.paint(round(cx + rx * math.cos(a)), round(cy + ry * math.sin(a)), col)
    ring(39.5, 45.5, 5, 5, '#3a2a1a')
    ring(25, 45.5, 3, 5, '#3a2a1a')
    for x in range(29, 35):
        S.paint(x, 43, '#3a2a1a')
    for x in range(45, 57):
        S.paint(x, 44 + (x - 45) // 6, '#3a2a1a')
    for (x, y) in ((37, 42), (36, 43), (24, 42)):
        S.paint(x, y, '#e8f4ff')
    S.paint(42, 49, '#7a8a9a'); S.paint(43, 48, '#7a8a9a')       # the crack

    def bg(x, y):
        t = y / H
        r0, g0, b0 = 40 + 60 * t, 52 + 44 * t, 66 + 10 * t
        for (cx, cy, rr, col) in ((10, 20, 9, (230, 170, 90)), (70, 14, 7, (240, 200, 120)),
                                  (64, 60, 10, (200, 120, 70)), (8, 66, 6, (250, 210, 140))):
            d = math.hypot(x - cx, y - cy)
            if d < rr:
                k = 0.45 * (1 - (d / rr) ** 2)
                r0, g0, b0 = r0 + (col[0] - r0) * k, g0 + (col[1] - g0) * k, b0 + (col[2] - b0) * k
        q = 6
        return (int(r0) // q * q, int(g0) // q * q, int(b0) // q * q, 255)
    return S.image(bg)


FEAT_PAL = {'k': '#24140e', 'e': '#3a2418', 'w': '#f4ece4', 'b': '#3c1e10', 'B': '#5c2f18', 'm': '#7a3a2c', 'l': '#b06a58'}

# eyes, brows and mouth, hand-placed after softening (origin 18,38)
HD_FEATURES = G('''
....BB.........BBBBBb......
...Bb.........BBBbbbbb.....
...............b......b....
...........................
....ke.........kkkkkk......
....ek........kewkeek......
...............eeee........
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
...........kmmmmmmk........
............llll...........
''')


# ---- HD-2D sprite: about three heads tall, soft ramps, tiny dark eyes
SPR_RAMPS = dict(RAMPS)
SPR_RAMPS.update({
    'pants': ['#1a1a20', '#26262e', '#34343e', '#44444f', '#565662', '#6a6a76', '#80808c'],
    'boot': ['#140c08', '#22140c', '#301e12', '#40281a', '#523424', '#664330', '#7a543e'],
    'belt': ['#2a1a0c', '#4a3018', '#6a4624', '#8a6032', '#a87a44', '#c49456', '#dcae6c'],
    'metal': ['#30343c', '#4a505a', '#666e7a', '#868e9a', '#a4acb8', '#c4ccd6', '#e2e8f0'],
})
SKEY = {
    'k': ('line', 0), 'H': ('hair', 5), 'h': ('hair', 3.2), 'j': ('hair', 1.5),
    'S': ('skin', 5.4), 's': ('skin', 4.2), 'd': ('skin', 2.6), 'r': ('skin', 2.2),
    'C': ('coat', 5), 'c': ('coat', 3.4), 'v': ('coat', 1.8), 'W': ('shirt', 5.4), 'w': ('shirt', 3.6),
    'T': ('pants', 4), 't': ('pants', 2.2), 'B': ('boot', 4), 'b': ('boot', 1.8),
    'm': ('belt', 3.5), 'M': ('metal', 5), 'n': ('metal', 2.5),
}
FIXED = {'g': '#6a4a2c', 'E': '#1a120e', 'i': '#dfefff'}

S_HEAD = G("""
.......kk.k.........
.....kkHHkHk.k......
....kHHHHHHHkHk.....
...kHHHHHHHHhhhk....
..kHHHHHHHHhhhhhk...
..kHHHHhHHhhhhhhjk..
..kHHHhHHhhhhhjhjk..
..kHhHSHHShhhhhjjk..
..kHSSSSSSSShhhjjk..
..kHSSSSSSSSShhjjk..
..khSSgSSSgSshjk....
..kSSgEgSgEgsssdk...
..kSSSSSSSSsssddk...
...kSSSSssssssdk....
...kSdSSsrrssddk....
....kdddssdddkk.....
.....kkkkkkkk.......
""")

S_BODY = G("""
......kddddk........
...kkCCwWWwcckk.....
..kCCCCwWWwcccvk....
.kCCCCCCwwcccccvk...
.kCCkCCCCwcccckcvk..
.kCCkCCCCWcccckcvk..
.kCCkCCCCWcccckcvk..
.kCCkCCCCwcccckcvk..
.kCCkmmmmmmmmmkcvk..
.kCCkCCCCCcccckcvk..
.kSSkCCCCCccccksdk..
.kSskCCCCkccccknnk..
..kkkCCCCkcccckMnk..
....kCCCCkccccvkk...
....kCCCCkccccvk....
....kCCCkk.kcccvk...
....kkkkk...kkkkk...
""")

def _taller(rows, top):
    return [top] * 3 + list(rows)


S_LEGS = {
    0: G("""
.....kTTk.kttk......
.....kTTk.kttk......
.....kTtk.kttk......
.....kTtk.kttk......
.....kTtk.kttk......
....kBBBk.kbbbk.....
....kBbbk.kbbbk.....
....kkkkk.kkkkk.....
"""),
    1: G("""
.....kTTk.kttk......
.....kTTk.kttk......
.....kTtk.kttk......
.....kTtk.kbbbk.....
....kBBBk.kbbbk.....
....kBbbk.kkkkk.....
....kkkkk...........
....................
"""),
    2: G("""
.....kTTk.kttk......
.....kTTk.kttk......
.....kTtk.kttk......
....kBBBk.kttk......
....kBbbk.kttk......
....kkkkk.kbbbk.....
..........kbbbk.....
..........kkkkk.....
"""),
}

# side view (facing right)
SD_HEAD = G("""
.......kk.k.........
.....kkHHkHkk.......
....kHHHHHHHHk......
...kHHHHHHHHHhk.....
..kjHHHHHHHHHHhk....
..kjhHHHHHHHHHHk....
..kjhhHHHHHSHHhk....
..kjhhhHHHSSSSSk....
..kjjhhhHSSSSSSk....
..kjjhkhSSSSSSSk....
..kjjkSkSSgSSSSSk...
..kjhkSskgEgSSSSSk..
..kjjhksSSSSSSSSk...
...kjhdssSSSSSSk....
....khdssssdsrk.....
.....kdddsdddk......
......kkkkkkk.......
""")

SD_BODY = G("""
.......kddk.........
.....kkcCCWWkk......
....kvcCCCCWWk......
....kvcCCCCCWk......
....kvccCCCCCk......
....kvcckCCCCk......
....kvcckCCCCk......
....kvcckCCCCk......
....kvmmkmmmmk......
....kvcckSSSCk......
....kvcckSsSCk......
....kvcckCCCCk......
....kvcccCCCCk......
....kvccccCCCk......
....kvccccCCCCk.....
....kvcccccCCCk.....
....kkkkkkkkkkk.....
""")

SD_LEGS = {
    'a': G("""
.....kttkTTk........
....kttk.kTTk.......
...kttk...kTTk......
..kttk.....kTTk.....
..ktk.......kTtk....
.kbbbk......kBBBBk..
.kbbbk......kBbbbk..
.kkkkk......kkkkkk..
"""),
    'p': G("""
......kttTTk........
......kttTTk........
......kttTTk........
......kttTtk........
......kttTtk........
......kbBBBBk.......
......kbBbbbk.......
......kkkkkkk.......
"""),
    'b': G("""
.....kTTkttk........
....kTTk.kttk.......
...kTTk...kttk......
..kTTk.....kttk.....
..kTtk......kttk....
.kBBBk......kbbbbk..
.kBbbk......kbbbbk..
.kkkkk......kkkkkk..
"""),
}


def sprite(head, body, legs, bob=0, ox=10):
    S = Soft(40, 56, SPR_RAMPS)
    fx = {}

    def put(rows, x0, y0):
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                if c == '.':
                    continue
                if c in FIXED:
                    fx[(x0 + x, y0 + y)] = FIXED[c]
                    S.put(x0 + x, y0 + y, 'skin', 4)
                else:
                    mat, tone = SKEY[c]
                    S.put(x0 + x, y0 + y, mat, tone)
    put(legs, ox, 38)
    put(body, ox, 22 + bob)
    put(head, ox, 6 + bob)
    S.soften(passes=1, weight=3.0)
    for (x, y), c in fx.items():
        S.paint(x, y, c)
    # soft ground shadow
    im = S.image()
    from PIL import Image
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    P = sh.load()
    for x in range(40):
        for y in range(47, 54):
            if ((x - 20) / 11) ** 2 + ((y - 50.5) / 2.2) ** 2 <= 1:
                P[x, y] = (20, 16, 24, 90)
    sh.alpha_composite(im)
    return sh


class HD2DVariant(Variant):
    style = 'hd2d'
    primary = True
    fps = {'idle': 3, 'walk_down': 7, 'walk_side': 7}
    anchor = (20, 50)
    notes = {'walk_side': 'faces right; mirror horizontally for left'}

    def portrait(self):
        return hd2d_portrait()

    def frames(self):
        return {
            'idle': [sprite(S_HEAD, S_BODY, S_LEGS[0]), sprite(S_HEAD, S_BODY, S_LEGS[0]),
                     sprite(S_HEAD, S_BODY, S_LEGS[0], bob=1), sprite(S_HEAD, S_BODY, S_LEGS[0], bob=1)],
            'walk_down': [sprite(S_HEAD, S_BODY, S_LEGS[1]), sprite(S_HEAD, S_BODY, S_LEGS[0], bob=-1),
                          sprite(S_HEAD, S_BODY, S_LEGS[2]), sprite(S_HEAD, S_BODY, S_LEGS[0], bob=-1)],
            'walk_side': [sprite(SD_HEAD, SD_BODY, SD_LEGS['a']), sprite(SD_HEAD, SD_BODY, SD_LEGS['p'], bob=-1),
                          sprite(SD_HEAD, SD_BODY, SD_LEGS['b']), sprite(SD_HEAD, SD_BODY, SD_LEGS['p'], bob=-1)],
        }


# ---------------------------------------------------------------- 霸王の大陸 × pixel baseball
def koei_ns():
    from types import SimpleNamespace
    import portrait
    import chibi
    ns = SimpleNamespace(FACTION=FACTION)
    ns.PAL = dict(
        k='#1a100c', D='#7a4632', d='#a86c50', s='#d49a76', S='#eec29c', E='#160e0a', B='#2a160c',
        u='#5a2a20', r='#a65a48',
        P='#8a6440', p='#644628', q='#46301a', Q='#2a1c10',
        c='#3a2616', C='#5a3c22', w='#c8c0ae', W='#ece6d6',
        J='#a8642e', j='#723c18', i='#3c1c0a', g='#4a3420',
    )
    TUFTS = G("""
.......k...k.k.......
......kJk.kJkjk..k...
.....kJJjkJjjjjkkjk..
""")
    LOCKS = G("""
..kjk.kjk.kj....
..kjk..kj..k....
...k....k.......
""")
    GLASSES = G("""
.ggg...ggggg.........
g...g.g.....g........
g...ggg.....gggggggg.
g...g.g.....g........
.ggg...ggggg.........
""")
    import random
    rnd = random.Random(3)
    stub = []
    for y in range(9):
        row = ''
        for x in range(22):
            jaw = y >= 3 or x >= 14
            row += ('d' if rnd.random() < 0.3 else '.') if jaw and 3 <= x <= 20 else '.'
        stub.append(row)
    BROWS = G("""
..kBB...BBBBBB..
""")

    def BODY():
        L = portrait.body_layer(ramp='PpqQ')
        portrait.cross_collar(L, wide=3, under='C', over='C', edge='P')
        return L
    ns.BODY = BODY
    ns.FACE = [(faces.MALE_HAIR, 0, -1, {'X': 'J', 'x': 'j', 'z': 'i'}), (TUFTS, 1, -4), (LOCKS, 1, 9),
               (BROWS, 0, 12), (stub, 2, 21, None, set('sSdD')), (GLASSES, 1, 13)]
    # chibi
    ns.CPAL = dict(
        k='#1a100c', S='#f0c49c', s='#d49a76', d='#a86c50', E='#160e0a', B='#2a160c', r='#a65a48',
        X='#c07a3e', x='#8a4c22', z='#56280e', g='#6a4a2c',
        P='#8a6440', p='#644628', q='#46301a', C='#3a2616', c='#2a1a0e', W='#ece6d6', w='#c8c0ae',
        Y='#a07a40', y='#6a4e24', L='#3c3c48', l='#26262e', O='#2a1a10', o='#160e08', M='#b8c0cc', m='#7a828e',
    )
    C_HAIR = G("""
.......k..k.k.........
.....kkXkkXkXkkk......
...kkXXXxXXxxxxxkk....
..kXXXXXxXxxxxxxxzk...
.kXXXXxXXxxxxxxxxzzk..
.kXXXxXXxxxxxxxxxzzk..
kXXXXXXxxxxxxxxxxxzzk.
kXXkXXkxkxxkxxkxxkzzk.
kXk.kk.k.kk.kk.kk.kzk.
kk..................k.
""")
    C_GLASSES = G("""
...ggg.....ggg....
...g.ggggggg.g....
...ggg.....ggg....
""")
    C_STUB = G("""
..d.d.......d.d...
...d..d..d.d..d...
.....d.....d......
""")
    WRENCH = G("""
.kk.
kMMk
kmmk
.km.
.km.
.kk.
""")
    ns.CHIBI = dict(costume='armor', face=[(C_HAIR, -1, -2), (C_GLASSES, 1, 9), (C_STUB, 1, 13)],
                    torso_over=[(WRENCH, 19, 10)])
    return ns


def variants():
    from variants import KoeiVariant
    return [HD2DVariant(), KoeiVariant(koei_ns(), full=False)]

S_LEGS = {k: _taller(v, '.....kTTkkttk.......') for k, v in S_LEGS.items()}
SD_LEGS = {k: _taller(v, '......kttTTk........') for k, v in SD_LEGS.items()}
