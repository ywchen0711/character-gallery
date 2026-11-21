"""The 龍門武林 heroes in the `nes2` style (round 1: 奕叡, 奕碩, 柳寒煙, 白先生, 苦禪, 冷笑天).

Portraits: 48x56 busts built with src/nes2.py (mondraw shapes for the robe, shoulders, cape and props; hand-typed
mirrored heads; tiny dark eyes without whites; right-side contour shading), fitted to the Famicom rules.
Field sprites: src/nes2_longmen_sprites.py.

    BUSTS[cid] = dict(fn, colours, spr)     build(cid) -> finished Canvas      portrait(cid) -> nes.Pic
"""
from nes2 import Canvas, Mat, flat, put, half, shade_right, shade_under, recolour, fit, T  # noqa: F401

BUSTS = {}


def bust(cid, colours, spr='', backdrop=None, near=None):
    def deco(fn):
        BUSTS[cid] = dict(fn=fn, colours=colours, spr=spr, backdrop=backdrop, near=near)
        return fn
    return deco


def build(cid):
    c = Canvas(48, 56)
    BUSTS[cid]['fn'](c)
    return c


def portrait(cid):
    b = BUSTS[cid]
    c = build(cid)
    bd = b['backdrop'](c) if b['backdrop'] else None
    return fit(c.rows(), b['colours'], b['spr'], name=cid + '/nes2', backdrop_rows=bd, near=b['near'])


def raw(cid):
    from nes2 import raw_image
    b = BUSTS[cid]
    c = build(cid)
    rows = c.rows()
    if b['backdrop']:
        rows = [''.join(q if p == '.' else p for p, q in zip(r, br)) for r, br in zip(rows, b['backdrop'](c))]
    return raw_image(rows, b['colours'])


SKIN = Mat('S', 'S', 's', hi=2)


def robe(c, mat, top=38, wide=0, part=None):
    """Sloped shoulders of a robe, from the neck down to the panel edge, shaded as one form."""
    p = c.new_part() if part is None else part
    c.poly2([(24, top), (17, top), (9 - wide, top + 3), (3 - wide, top + 7), (0, top + 12), (0, 56), (24, 56)], mat, p)
    c.reshade(p, 14, top + 6, 18, 14, mat, dw=2, hi=0.88)
    return p


def neck(c, x0=20, x1=27, y0=30, y1=41):
    """The neck: lit on the left, in shadow on the right."""
    p = c.new_part()
    c.rect(x0, y0, x1, y1, Mat('S', 'S', 's'), p, shade='flat')
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            c.tone[y][x] = 's' if x >= x1 - 2 or y <= 35 else 'S'
    return p


def cross_collar(c, part, light, dark, y0=39, slope=0.95, w=1.7, inner=None):
    """A crossed collar (the wearer's right over left) as a band on the robe, with an under-collar V of `inner`."""
    for y in range(y0, c.h):
        for x in range(c.w):
            if c.part[y][x] != part or c.tone[y][x] == 'k':
                continue
            u = x + 0.5 - 24
            d = (y - y0) * slope
            if abs(u + d) < w and u < 4:          # left lapel (goes over)
                c.tone[y][x] = light
            elif abs(u - d) < w and u > -4:
                c.tone[y][x] = dark
            elif inner and abs(u) < d - w and y < y0 + 9:
                c.tone[y][x] = inner


def jaw_shadow(c, y0=27, y1=38):
    """Skin right above the jaw line falls into shadow; so does the right cheek (light from the top-left)."""
    shade_under(c, {'S': 's'}, band=1, y0=y0, y1=y1)
    shade_right(c, {'S': 's'}, band=3, y0=10, y1=y1)


# ---------------------------------------------------------------- the shared face (left half, rows y=16..35)
# '#' marks the temple / sideburn pixels each character fills with its hair slot.
FACE = T("""
........kk#kSSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
........kkkkSSSSSSSSSSSS
........kSSkSSSSSSSSSSSS
........kSskSSSSSSSSSSSS
........kSskSSSSSSSSSSSS
.........kSkSSSSSSSSSSSS
..........kkSSSSSSSSSSSS
...........kSSSSSSSSSSSS
............kSSSSSSSSSSS
............kSSSSSSSSSSS
.............kSSSSSSSSSS
..............kSSSSSSSSS
...............kSSSSSSSS
................kSSSSSSS
.................kkSSSSS
...................kkkkk
""")

# brows and eyes (left half, x from 0, rows from y=19): tiny dark eyes, no whites
EYES = {
    'keen': T("""
.............kkkk.......
...............kkkkk....
........................
...............kkk......
................kk......
................kk......
"""),
    'glare': T("""
.............kk.........
..............kkkkk.....
................kkk.....
..............kkkk......
...............kkk......
................k.......
"""),
    'sly': T("""
..............kkkk......
........................
........................
..............kkkkk.....
...............kkk......
........................
"""),
    'calm': T("""
..............kkkk......
........................
........................
...............kkk......
...............kkk......
........................
"""),
    'round': T("""
..............kkkk......
........................
........................
...............kk.......
..............kkkk......
...............kk.......
"""),
    'bright': T("""
...............kkk......
..............k...k.....
........................
................kk......
................kk......
................kk......
"""),
    'cool': T("""
..............kkkkk.....
........................
........................
.............kkkkk......
................kk......
................kk......
"""),
    'shut': T("""
.............kkkk.......
.................kk.....
........................
...............kkk......
..............k...k.....
........................
"""),
    'proud': T("""
.............kk.........
..............kkkk......
................kkk.....
.............kkkkkk.....
...............kkk......
................k.......
"""),
}


FACE_KID = T("""
........kk#kSSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
........kkkkSSSSSSSSSSSS
........kSSkSSSSSSSSSSSS
........kSskSSSSSSSSSSSS
........kSskSSSSSSSSSSSS
.........kSkSSSSSSSSSSSS
..........kkSSSSSSSSSSSS
...........kSSSSSSSSSSSS
...........kSSSSSSSSSSSS
...........kSSSSSSSSSSSS
............kSSSSSSSSSSS
.............kSSSSSSSSSS
..............kkSSSSSSSS
................kkkSSSSS
...................kkkkk
""")

# wide, fleshy face (the treasurer, the fat monk, big brawlers): cheeks reach further and the jaw is heavy
FACE_WIDE = T("""
........k##kSSSSSSSSSSSS
........k#kSSSSSSSSSSSSS
.......kk#kSSSSSSSSSSSSS
......kkkkSSSSSSSSSSSSSS
......kSSkSSSSSSSSSSSSSS
......kSskSSSSSSSSSSSSSS
......kSskSSSSSSSSSSSSSS
.......kSkSSSSSSSSSSSSSS
.......kkSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
.........kSSSSSSSSSSSSSS
..........kkSSSSSSSSSSSS
............kkkSSSSSSSSS
...............kkkkkkkkk
""")

# a thin, long face (the skinny lackey): narrow cheeks and a pointed chin
FACE_THIN = T("""
........kkk#kSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
.........k#kSSSSSSSSSSSS
.........kkkSSSSSSSSSSSS
.........kSkSSSSSSSSSSSS
.........kSkSSSSSSSSSSSS
.........kkSSSSSSSSSSSSS
..........kSSSSSSSSSSSSS
..........kSSSSSSSSSSSSS
...........kSSSSSSSSSSSS
...........kSSSSSSSSSSSS
............kSSSSSSSSSSS
.............kSSSSSSSSSS
..............kSSSSSSSSS
...............kSSSSSSSS
................kkSSSSSS
..................kkSSSS
....................kkkk
""")

# a round, fat face (the treasurer, the bun-loving camp master): full cheeks and a double chin
FACE_FAT = T("""
........kk#kSSSSSSSSSSSS
.......kk#kSSSSSSSSSSSSS
......kk#kSSSSSSSSSSSSSS
.....kkkkSSSSSSSSSSSSSSS
.....kSSkSSSSSSSSSSSSSSS
.....kSskSSSSSSSSSSSSSSS
.....kSskSSSSSSSSSSSSSSS
.....kSSkSSSSSSSSSSSSSSS
.....kkkSSSSSSSSSSSSSSSS
......kSSSSSSSSSSSSSSSSS
......kSSSSSSSSSSSSSSSSS
......kSSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
.........kkSSSSSSSSSSSSS
...........kkkssssssssss
..............kkkkkkkkkk
""")

MOUTHS = {'flat': 'kkkkkk', 'smile': 'k....k|.kkkk.', 'grin': 'kkkkkk|kwwwwk|.kkkk.', 'firm': '.kkkk.',
          'smirk': '...kkk|kkk...', 'beam': 'k......k|.kkkkkk.', 'frown': '.kkkk.|k....k', 'small': '..kk..',
          'fang': 'kkkkkk|.w..w.', 'open': '.kkkk.|kkkkkk|.kkkk.', 'grit': 'kkkkkk|kwkwwk|kkkkkk', 'none': '', 'buck': 'kkkkkk|.kwwk.|..kk..'}


def face(c, hair='i', eyes='keen', nose=True, mouth='flat', top=None, shape='adult', mouth_y=30, eyes_dy=0):
    """The shared face. The nose is only a soft skin-shadow side stroke (no dark nostril pixels)."""
    base = {'adult': FACE, 'kid': FACE_KID, 'wide': FACE_WIDE, 'thin': FACE_THIN, 'fat': FACE_FAT}[shape]
    rows = [r.replace('#', hair) for r in base]
    if top:
        rows = top + rows[len(top):]
    half(c, chr(10).join(rows), 16)
    put(c, EYES[eyes], 0, 19 + eyes_dy, mirror=True)
    if nose:
        put(c, ['s', 's'], 24, 25 + (1 if shape in ('adult', 'thin') else 0))
    m = MOUTHS[mouth]
    if m:
        rows_m = m.split('|')
        put(c, rows_m, 24 - len(rows_m[0]) // 2, mouth_y)


def skin_shade(c, y0=16, y1=40):
    """Right cheek and jaw in shadow (light from the top-left): a 2-px band inside the right outline and one
    pixel above the jaw line."""
    for y in range(y0, min(y1, 34)):
        xs = [x for x in range(24, 40) if c.tone[y][x] in 'Ss']
        if not xs:
            continue
        e = max(xs)
        for x in (e, e - 1):
            if c.tone[y][x] == 'S':
                c.tone[y][x] = 's'
    shade_under(c, {'S': 's'}, band=1, x0=14, x1=34, y0=29, y1=34)


def backdrop_sky(z='z', solid_to=0, check_to=24, fade=10, moon=None, Z='Z'):
    """The panel motif, in a colour the figure already uses near the top (so it costs no palette room):
    solid z down to solid_to, a 50% checker down to check_to, then sparse 25% dots for `fade` rows.
    moon=(cx, cy, r): an optional disc of Z behind the figure."""
    def fn(c):
        rows = []
        for y in range(c.h):
            r = []
            for x in range(c.w):
                ch = '.'
                if y < solid_to:
                    ch = z
                elif y < check_to:
                    ch = z if (x + y) % 2 == 0 else '.'
                elif y < check_to + fade:
                    ch = z if (x % 2 == 0 and y % 2 == 0) and ((x // 2 + y // 2) % 2 == 0) else '.'
                if moon:
                    cx, cy, rr = moon
                    if (x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2 <= rr * rr:
                        ch = Z
                r.append(ch)
            rows.append(''.join(r))
        return rows
    return fn


# ================================================================ 奕叡 Yi Rui
# topknot through a silver ring, blue headband with flying ties, indigo robe over a white under-collar,
# the ring-pommel saber over his shoulder
YIRUI_HAIR = """
.....................kkk
...................kkhii
..................khhiii
..................khiiii
..................kkkkkk
..................kwwwww
.............kkkkkvvvvvv
...........kkiiiikkkkkkk
..........kiiihiikiiiiii
.........kiihiiikiiiiiii
........kiihiiikiiiiiiii
........kihiiikiiiiiiiii
.......kkkkkkkkkkkkkkkkk
.......kmmmmmmmmmmmmmmmm
.......knnnnnnnnnnnnnnnn
.......kkkkkkkkkkkkkkkkk
"""


@bust('yirui', dict(S=0x37, s=0x27, h=0x1C, i=0x0C, a=0x12, b=0x02, d=0x0C, e=0x30, f=0x10, m=0x21, n=0x11,
                    v=0x10, w=0x30, p=0x07, q=0x17, y=0x28, r=0x16, z=0x0C), spr='',
     near={'h': 'i', 'q': 'p', 'y': 'q', 'e': 'f', 'm': 'n'}, backdrop=backdrop_sky(solid_to=6, check_to=26, fade=10))
def yirui(c):
    # the saber on his back: the wrapped grip rises over his right shoulder (our left), ring pommel on top
    grip = c.new_part()
    c.capsule(10.5, 44, 5.5, 22, 1.7, Mat('q', 'q', 'p'), grip)
    ring = c.new_part()
    c.ellipse(4.5, 17.5, 3.4, 3.4, Mat('w', 'v', 'v'), ring)
    guard = c.new_part()
    c.ellipse(10, 38.5, 4.5, 1.8, Mat('y', 'y', 'q'), guard)
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'd'), top=39)
    c.finish()
    put(c, ['kk', 'kk'], 4, 17)
    for y in range(23, 37, 3):           # wrap pattern on the grip
        for x in range(0, 14):
            if c.tone[y][x] == 'q':
                c.tone[y][x] = 'p'
    robe_folds(c, body)
    collar(c, body, top=39, band='eaa', inner='S', inner2='f')
    half(c, YIRUI_HAIR)
    face(c, 'i', 'keen', mouth='firm')
    # headband ties flying to our right, knot at his temple
    put(c, """
kkk......
mmmkkk...
nnmmmmkk.
knnnnnnmk
.kkkknnnk
.....kkk.
""", 37, 12)
    skin_shade(c)
    shade_right(c, {'i': 'k', 'h': 'i', 'm': 'n'}, band=2, x0=24, y0=0, y1=16)
    return c


def collar(c, part, top=39, x_over=27.5, x_under=20.0, slope=0.8, band='eaa', inner='S', inner2=None, skin_rows=6):
    """A crossed collar (右衽: the wearer's left panel over the right). The over-lapel edge runs from the neck at
    x_over down to our left; the under-lapel edge from x_under down to our right until it meets it. Each edge is a
    black line, then the band slots from the opening outward (white under-collar, then the robe's collar band),
    then a black line. Inside the opening: skin for skin_rows rows, then inner2 (an under-robe) if given."""
    nb = len(band)
    for y in range(top, c.h):
        x1 = x_over - (y - top) * slope
        x2 = x_under + (y - top) * slope
        for x in range(c.w):
            if c.part[y][x] != part or c.tone[y][x] == 'k':
                continue
            px = x + 0.5
            t = None
            d1 = px - x1                     # >0: right of the over edge (on the over panel)
            if 0 <= d1 < nb + 1:
                t = 'k' if d1 < 0.0 + 1 and d1 >= nb else None
                k = int(d1)
                t = band[k] if k < nb else 'k'
            elif -1 <= d1 < 0:
                t = 'k'
            elif d1 < -1 and x2 < x1 - 1:
                d2 = x2 - px                 # >0: left of the under edge (on the under panel)
                if 0 <= d2 < nb + 1:
                    k = int(d2)
                    t = band[k] if k < nb else 'k'
                elif -1 <= d2 < 0:
                    t = 'k'
                elif d2 < -1:
                    t = inner if (y - top) < skin_rows or not inner2 else inner2
            if t:
                c.tone[y][x] = t


def robe_folds(c, part, light='a', dark='d', mid='b'):
    """Sleeve seams and a highlight along the top of each shoulder, so a plain robe reads as cloth."""
    for y in range(c.h):
        for x in range(c.w):
            if c.part[y][x] != part or c.tone[y][x] == 'k':
                continue
            up = c.tone[y - 1][x] if y else 'k'
            up2 = c.tone[y - 2][x] if y > 1 else 'k'
            if (up == 'k' or up2 == 'k') and c.tone[y][x] == mid and x < 24:
                c.tone[y][x] = light
    for x0, sgn in ((7, 1), (40, -1)):
        for y in range(46, 56):
            x = x0 + sgn * (y - 46) // 4
            if c.part[y][x] == part and c.tone[y][x] != 'k':
                c.tone[y][x] = 'k'
                xx = x + sgn
                if c.part[y][xx] == part and c.tone[y][xx] != 'k':
                    c.tone[y][xx] = light if sgn > 0 else dark


import nes2_longmen_more  # noqa: E402,F401  (registers the other five)
