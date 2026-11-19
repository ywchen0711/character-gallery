"""喬許 Josh - big-hearted shield fighter who guards the others and draws the enemy's eye.
Amber skin, curly charcoal hair, full beard, leather vest, navy trousers, iron spear and a round shield."""
import sys
from pixlib import G, RLE, Layer, fliph
from variants import Variant

FACTION = 'west'
META = dict(
    id='josh',
    name={'zh': '喬許', 'en': 'Josh'},
    style_name={'zh': '盾手', 'en': 'Shieldbearer'},
    title={'zh': '熱心腸的盾牌', 'en': 'The big-hearted shield'},
    bio={
        'zh': '十歲的哥哥，勇敢又熱心。背著小木盾、拿著木棍，總是站在弟弟前面，'
              '大聲喊話把壞人引到自己身上。笑起來露出缺了一顆的門牙。',
        'en': 'The ten-year-old big brother, brave and warm-hearted. With his little wooden shield and stick he always '
              'stands in front of his brother, shouting to draw trouble onto himself. His grin shows a missing tooth.',
    },
    weapon={'zh': '小木盾與木棍', 'en': 'Little wooden shield and stick'},
)

# ---------------------------------------------------------------- GBA (Fire Emblem-like)
# Portrait: one 16-colour palette (15 + the panel colour), crisp line art, flat
# cel shading with hard shadow edges.
GP = dict(
    k='#3a1c10', S='#f0b878', s='#d08a50', d='#a05c30', D='#6e3a1c',
    W='#fff8e8', r='#9a2a2a', E='#1e1e2a',
    X='#74748a', x='#3c3c4e', z='#1e1e2a',
    L='#c07838', l='#7a4420', N='#3a4a8a', n='#232c5a', M='#c8ccd8',
)
PANEL = '#e8e0c8'

HEAD = RLE('''
14. 4k 2. 4k 16.
11. 3k 2X 2x 2k 2X 2x 4k 12.
9. 2k 3X 4x 3X 4x 2X 1x 2k 10.
8. 1k 2X 4x 1k 2X 4x 1k 2X 4x 1z 1k 9.
7. 1k 1X 4x 1k 2X 5x 2X 3x 1z 1k 1X 2x 1z 1k 7.
6. 1k 1X 3x 1k 2X 4x 1k 2X 4x 1z 1k 2X 2x 2z 1k 6.
5. 1k 1X 3x 1k 1X 4x 1z 1k 1X 5x 1z 1k 1X 5x 2z 1k 5.
5. 1k 3x 1k 1X 3x 2z 1k 1X 4x 2z 1k 1X 5x 4z 1k 4.
4. 1k 1X 2x 1z 1k 3x 2z 1k 1X 3x 3z 1k 4x 3z 1k 1x 1z 1k 5.
4. 1k 2x 2z 1k 2x 2z 1k 1X 2x 3z 1k 1X 3x 3z 1k 1X 1x 2z 1k 5.
4. 1k 1x 2z 1k 2x 2z 1k 1X 2x 2z 1k 1X 3x 3z 1k 1X 2x 3z 1k 5.
4. 1k 1z 4S 1k 1x 1k 4S 1k 2x 1k 3s 1k 1X 2x 5z 1k 6.
4. 1k 6S 1k 5S 3s 1k 2s 1d 1k 1X 2x 5z 1k 6.
4. 1k 12S 4s 2d 1k 1x 1X 1x 5z 1k 7.
4. 1k 11S 5s 2d 1k 2x 6z 1k 7.
4. 1k 1S 3z 2S 6z 2s 3d 1k 1x 7z 1k 8.
4. 1k 3d 1S 1s 1d 1d 4k 1s 5d 1k 1x 2z 1k 3z 1k 9.
4. 1k 1d 1k 1d 2S 1s 1d 1k 1E 1W 1k 1s 4d 1k 8z 1k 9.
4. 1k 2d 2S 1s 1d 1S 1d 2d 1S 2s 3d 1k 1x 6z 1k 10.
3. 1k 1S 1d 2S 1s 1d 5S 2s 4d 1k 1x 5z 1k 11.
3. 1k 1S 1d 2S 1s 1d 5S 3s 3d 1k 1x 4z 1k 12.
2. 1k 2S 1d 2S 1s 1d 4S 3s 3d 1k 2x 3z 1k 13.
1. 1k 3S 1d 1S 2s 1d 3S 4s 2d 1k 3x 3z 1k 13.
1. 1k 1d 2D 1d 3s 1d 2s 5s 1d 1k 4x 3z 1k 13.
2. 1k 1X 6x 2z 1k 2s 1d 1k 1X 4x 3z 1k 14.
2. 1k 2X 7x 1z 1k 1s 1k 1X 5x 3z 1k 14.
2. 1k 1X 1x 1k 6W 1k 1x 1k 1X 5x 4z 1k 14.
2. 1k 1X 1x 1k 1W 4r 1W 1k 2x 1X 5x 4z 1k 14.
2. 1k 1X 2x 1k 4k 1k 3x 1X 5x 3z 1k 15.
2. 1k 1X 9x 1X 6x 4z 1k 15.
3. 1k 1X 4x 1X 6x 1X 3x 3z 1k 16.
3. 1k 1X 2x 1X 5x 1X 4x 3z 1k 18.
4. 1k 1X 3x 1X 4x 1X 3x 3z 1k 18.
4. 1k 1X 1x 1X 4x 1X 3x 3z 1k 20.
5. 1k 1X 3x 1X 3x 1X 1x 3z 1k 20.
6. 1k 1X 2x 1X 3x 3z 1k 22.
7. 1k 1X 3x 1X 1x 2z 1k 23.
8. 1k 2x 1X 2z 1k 25.
9. 3k 28.
''', 40)

def curls(rows, y0, y1):
    """Curly texture on hand-drawn hair/beard: flat base tone, little highlight arcs
    on a staggered grid, a dark tuck under each curl."""
    r = [list(x) for x in rows]
    for y in range(y0, y1):
        for x in range(len(r[y])):
            if r[y][x] == 'X':
                r[y][x] = 'x'
    for cy in range(y0 + 1, y1, 3):
        for cx in range(1 + (cy // 3 % 2) * 2, len(r[0]) - 1, 4):
            pts = [(cx - 1, cy, 'X'), (cx, cy - 1, 'X'), (cx + 1, cy - 1, 'X'), (cx + 1, cy + 1, 'z')]
            if all(0 <= py < len(r) and r[py][px] in 'xz' for px, py, _ in pts):
                for px, py, c in pts:
                    if c == 'X' and r[py][px] == 'z':
                        continue
                    r[py][px] = c
    return [''.join(x) for x in r]


HEAD = curls(HEAD, 0, 11)
HEAD = curls(HEAD, 24, 38)

EAR = G('''
.kk.
kSdk
kSdk
ksdk
.kdk
..k.
''')


# ---- battle sprite (faces left, like a player unit), 48x48 cells
BHEAD = G("""
.....kkkk.kk...
...kkxXxkkXxk..
..kxXxxxXxxxzk.
..kXxxkxxxxxzzk
.kxxkSSkxxxzzzk
.kxkSSSSSkxzzzk
.kkSzzSSsdkzzk.
..kSkESSsdkSdk.
.kSSSSSsdddkdk.
kSSSSSsdddkzzk.
.kxxxxxxxxzzk..
.kxWWWkxxxzzk..
..kxxxxxxzzk...
...kxXxxzzk....
....kkkkkk.....
""")

BTORSO = G("""
....kkkkkkkkkk....
..kkLLLLLnnlllkk..
.kLLLLLLLNnllllllk
kLLLLLLLLNnllllllk
kLLLLLLLLNnllllllk
kLLLLLLLNNnllllllk
kLLLLLLLNnnllllllk
kLLLLLLLNnnlllllk.
kLLLLLLLNnnlllllk.
.kLLLLLLNnnlllllk.
.kkkkkkkkkkkkkkkk.
.kLLLLLLlllllllk..
.knnnnnnnnnnnnnk..
""")

LEGS = {
    'stand': G("""
.knnnnnnnnnnnk..
.knnnNNnnnnnnk..
.knnnNkknnnnnk..
.knnNk..knnnnk..
.knnNk..knnnk...
.knnNk..knnNk...
.knnNk..knnNk...
.knnNk..knnNk...
.knnNk..knnNk...
kzzzzk.kzzzzk...
kzzzzk.kzzzzk...
kkkkkk.kkkkkk...
"""),
    'apart': G("""
..knnnnnnnnnnnk.
..knnnnNNnnnnnk.
..knnnNk.knnnnk.
.knnnNk...knnnk.
.knnNk....knnnk.
knnNk......knnk.
knnNk......knnNk
knNk........knNk
knNk........knNk
kzzzk......kzzzzk
zzzzk......kzzzzk
kkkkk......kkkkkk
"""),
    'cross': G("""
.knnnnnnnnnnnk..
.knnnnnnnnnnnk..
..knnNnnnnnnk...
..knnNknnnnk....
...knnNknnk.....
...knnNknNk.....
...knnNkNNk.....
...knnNkNNk.....
...knnNkNNk.....
..kzzzzkzzk.....
..kzzzzkzzzk....
..kkkkkkkkkk....
"""),
}


def shield(L, cx, cy, r=10):
    for y in range(cy - r - 1, cy + r + 2):
        for x in range(cx - r - 1, cx + r + 2):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if d <= r + 0.5:
                if d > r - 1.5:
                    c = 'M' if (x - cx) + (y - cy) < 0 else 'X'
                elif d < 2.2:
                    c = 'M' if (x <= cx and y <= cy) else 'X'
                else:
                    c = 'L' if (x - cx) * 0.6 + (y - cy) < -2 else 'l'
                    if abs(x - cx) == 0 or abs(y - cy) == 0:
                        c = 'l' if c == 'L' else 'D'
                L.set(x, y, c)
    for y in range(cy - r - 2, cy + r + 3):
        for x in range(cx - r - 2, cx + r + 3):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if r + 0.5 < d <= r + 1.5 and L.get(x, y) in '.LlNnkSsdD':
                L.set(x, y, 'k')


def spear(L, x, top, bottom):
    for y in range(top, bottom):
        L.set(x - 1, y, 'k'); L.set(x, y, 'L'); L.set(x + 1, y, 'k')
    tip = ['..k..', '.kMk.', '.kMk.', 'kMMXk', 'kMXXk', 'kMXXk', '.kXk.', '.kXk.', 'kkkkk']
    for i, row in enumerate(tip):
        for j, c in enumerate(row):
            if c != '.':
                L.set(x - 2 + j, top - len(tip) + i + 1, c)


def battle_frame(legs='stand', bob=0, lean=0, guard=False):
    L = Layer(48, 48)
    spear(L, 32 + lean, 6 + bob, 46)
    L.stamp(LEGS[legs], 15, 34)
    L.stamp(BTORSO, 14 + lean, 21 + bob)
    L.stamp(G("""
.kk.
kssk
kSsk
.kk.
"""), 30 + lean, 30 + bob)                                   # spear hand
    L.stamp(BHEAD, 15 + lean, 7 + bob)
    shield(L, 14 + lean - (2 if guard else 0), 28 + bob - (5 if guard else 0))
    return L


class GBAVariant(Variant):
    style = 'gba'
    primary = True
    fps = {'idle': 3, 'walk': 8, 'guard': 6}
    loop = {'guard': False}
    anchor = (24, 45)
    notes = {'walk': 'faces left; mirror horizontally for right', 'guard': 'taunt: raises the shield and plants his feet'}

    def portrait(self):
        return gba_portrait()

    def frames(self):
        im = lambda L: L.image(GP)
        return {
            'idle': [im(battle_frame()), im(battle_frame(bob=1))],
            'walk': [im(battle_frame('apart')), im(battle_frame('cross', bob=-1)),
                     im(battle_frame('apart', lean=-1)), im(battle_frame('cross', bob=-1))],
            'guard': [im(battle_frame(bob=1)), im(battle_frame('apart', bob=2, guard=True)),
                      im(battle_frame('apart', bob=2, lean=-1, guard=True)), im(battle_frame('apart', bob=1)), im(battle_frame())],
        }


def gba_portrait():
    L = Layer(64, 64)
    # the round shield slung on his back, rim showing over the right shoulder
    for y in range(18, 64):
        for x in range(40, 64):
            d = ((x - 62) ** 2 + (y - 44) ** 2) ** 0.5
            if 17.5 <= d < 19:
                L.set(x, y, 'k')
            elif 15 <= d < 17.5:
                L.set(x, y, 'M' if y < 34 else 'X')
            elif d < 15:
                L.set(x, y, 'l')
    # broad shoulders: leather vest over a navy Han-cut shirt
    keys = [(42, 20, 46), (44, 10, 56), (46, 5, 60), (50, 2, 62), (56, 0, 63), (63, 0, 63)]
    for y in range(42, 64):
        for (y0, l0, r0), (y1, l1, r1) in zip(keys, keys[1:]):
            if y0 <= y <= y1:
                t = (y - y0) / max(1, y1 - y0)
                l, r = round(l0 + (l1 - l0) * t), round(r0 + (r1 - r0) * t)
                for x in range(l, r + 1):
                    u = (x - l) / max(1, r - l)
                    L.set(x, y, 'L' if u < 0.42 else 'l')
                if l > 0:
                    L.set(l - 1, y, 'k')
                if r < 63:
                    L.set(r + 1, y, 'k')
                break
    for x in range(20, 47):
        if L.get(x, 41) == '.':
            L.set(x, 41, 'k')
    # thick neck in shadow under the beard
    for y in range(32, 46):
        for x in range(23, 41):
            L.set(x, y, 'k' if x in (23, 40) else ('D' if y < 36 or x >= 34 else 'd'))
    # open vest: navy shirt in a V, crossed collar, vest edge stitching
    for y in range(44, 64):
        half = 4 + (y - 44) // 2
        for x in range(32 - half, 33 + half):
            if L.get(x, y) in 'Llsd':
                L.set(x, y, 'N' if x < 33 else 'n')
        L.set(32 - half - 1, y, 'k'); L.set(33 + half, y, 'k')
        if y % 3 == 0:
            L.set(32 - half - 3, y, 'l'); L.set(33 + half + 2, y, 'D')
    for i in range(14):
        L.set(37 - i, 44 + i, 'k')
    for y in range(52, 64):          # shoulder seams
        L.set(11 - (y - 52) // 4, y, 'l')
        L.set(53 + (y - 52) // 4, y, 'k')
    L.stamp(HEAD, 6, 0)
    L.stamp(EAR, 33, 17)
    from PIL import Image
    img = Image.new('RGBA', (64, 64), PANEL)
    img.alpha_composite(L.image(GP))
    return img


# ---------------------------------------------------------------- koei style (16-bit Three Kingdoms portrait + pixel-baseball chibi)
def koei_ns():
    from types import SimpleNamespace
    import portrait
    import faces
    ns = SimpleNamespace(FACTION=FACTION)
    ns.PAL = dict(
        k='#180c06', D='#5a2e16', d='#8a4c26', s='#b0703c', S='#cc9058', E='#120a06', B='#141218',
        u='#3a1408', r='#8a3a2a', W='#f0e6d0',
        P='#a8703c', p='#7c4c24', q='#563216', Q='#36200c',
        c='#24305e', C='#3a4a86', w='#2a3466',
        X='#5a5a6c', x='#2c2c38', z='#121218', M='#c0c4d0', m='#8a8e9a', n='#5a3418',
    )
    BEARD = G("""
...................kz.....
..................kxz.....
..................kxz.....
.................kxxz.....
.................kxxz.....
................kXxxz.....
........k.......kXxxz.....
...kXXXxxxk....kXxxzk.....
..kXXkWWWkXk..kXxxxzk.....
..kXk.uuu.kXxkXxxxzk......
..kXxxkkkxxXxXxxxxzk......
..kXXxxxxxxxXxxxxxzk......
..kXxxXxxxxxxxxxxzk.......
...kXxxxXxxxxxxxzzk.......
...kXXxxxxXxxxxzzk........
....kXxxXxxxxxzzk.........
.....kXxxxXxxzzk..........
......kkXxxzzkk...........
........kkkkk.............
""")
    CURLS = G("""
.......k.kk.k.kk.........
.....kkXkXxkXkXxkk.......
....kXxxXxxXxxXxxxk......
""")
    BROWS = G("""
..kBBB..BBBBBBB.
""")

    def BODY():
        L = portrait.body_layer(ramp='PpqQ')
        portrait.cross_collar(L, wide=2, inner='w', inner_hi='C', under='q', over='q', edge='p')
        return L

    def SHIELD(L):
        for y in range(18, 64):
            for x in range(36, 56):
                d = ((x - 56) ** 2 + (y - 44) ** 2) ** 0.5
                if 17.5 <= d < 19:
                    L.set(x, y, 'k')
                elif 15.5 <= d < 17.5:
                    L.set(x, y, 'M' if y < 36 else 'm')
                elif d < 15.5:
                    L.set(x, y, 'n')
    ns.BODY = BODY
    ns.BACK = [SHIELD]
    ns.FACE = [(faces.JAW_STRONG, 0, 22), (faces.MALE_HAIR, 0, -1), (CURLS, 0, -3), (BROWS, 0, 12), (BEARD, 0, 14)]
    ns.CPAL = dict(
        k='#180c06', S='#d49a60', s='#b0703c', d='#8a4c26', E='#120a06', B='#141218', r='#f0e6d0',
        X='#5a5a6c', x='#2c2c38', z='#121218',
        P='#a8703c', p='#7c4c24', q='#563216', C='#3a4a86', c='#24305e', W='#3a4a86', w='#24305e',
        Y='#5a3418', y='#3a200c', L='#3a4a86', l='#24305e', O='#1a1a20', o='#0e0e12',
        M='#c0c4d0', m='#8a8e9a', n='#7c4c24', F='#a8703c',
    )
    C_HAIR = G("""
......k.kk.k.kk.......
....kkXkXxkXkXxkk.....
...kXxxXxxXxxXxxxk....
..kXxXxxXxxXxxXxxzk...
.kXxxxXxxxXxxxxXxzzk..
.kxXxxxxXxxxxXxxxxzk..
kXxxXxxxxxxXxxxxXxzzk.
kxXkxXkxkxXkxkxXkxzzk.
kxk.kk.k.kk.kk.kk.kzk.
""")
    C_BEARD = G("""
kxk..........kxk
kxxk........kxxk
kxxxkxxxxxxkxxxk
kxXxxkrrrrkxxxzk
.kxXxxxxxxxxxzk.
..kxXxxxxXxxzk..
...kxxXxxxxzk...
....kkxxxxkk....
......kkkk......
""")

    def C_SHIELD(L, view, phase, bob, arm):
        cx, cy = 15, 48 + bob + arm[0]
        for y in range(cy - 9, cy + 10):
            for x in range(cx - 9, cx + 10):
                d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                if d <= 8.5:
                    if d > 6.8:
                        c = 'M' if (x - cx) + (y - cy) < 0 else 'm'
                    elif d < 1.5:
                        c = 'M'
                    else:
                        c = 'F' if (x - cx) + (y - cy) < 0 else 'n'
                    L.set(x, y, c)
                elif d <= 9.5:
                    L.set(x, y, 'k')
    ns.CHIBI = dict(costume='armor', face=[(C_HAIR, -1, -2), (C_BEARD, 2, 12)], prop_front=C_SHIELD)
    return ns


def variants():
    from variants import KoeiVariant
    from family_variant import FamilyVariant
    v = GBAVariant()
    v.primary = False
    from nes_variant import NESVariant
    fam = FamilyVariant('josh')
    fam.primary = False
    return [NESVariant('josh'), fam, v, KoeiVariant(koei_ns(), full=False)]
