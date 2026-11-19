"""Foe busts, part 2: animals, bugs and spirits as head-and-forequarters close-ups. See foe_busts.py."""
from foe_busts import *  # noqa: F401,F403

FUR = Mat('a', 'b', 'd')
FURD = Mat('b', 'd', 'd')
LIGHT = Mat('a', 'a', 'b', hi=0.5)
WH = flat('w')
FURTUFT = '''
........
...d....
..d.d...
........
.......d
......d.
.d...d..
d.d.....
'''


# ================================================================ wolf: a snarling head close-up, ears up, a thick ruff
@bust('wolf')
def wolf(c):
    ruff = c.new_part()
    c.poly2([(24, 34), (10, 36), (2, 44), (0, 56), (24, 56)], FURD, ruff)
    c.reshade(ruff, 16, 40, 22, 16, FURD, dw=2, hi=0.9)
    ears = c.new_part()
    c.poly2([(9, 2), (7, 14), (19, 12)], FUR, ears)
    hd = c.new_part()
    c.ellipse(24, 22, 15.5, 13, FUR, hd)
    c.reshade(hd, 20, 18, 16, 14, FUR, dw=2, hi=0.85)
    cheek = c.new_part()
    c.poly2([(10, 22), (5, 30), (9, 31), (6, 36), (14, 35), (16, 30)], FUR, cheek)
    muzzle = c.new_part()
    c.ellipse(24, 33, 9, 7.5, LIGHT, muzzle)
    c.finish()
    c.pattern(ruff, FURTUFT, margin=1, only='b')
    put(c, '''
.kk
kddk
kdddk
.kddk
..kdk
''', 9, 5, mirror=True)
    # brows and slanted eyes
    put(c, '''
kkk......
.kkkk....
...kkkk..
..krrkk..
...kkk...
''', 13, 15, mirror=True)
    # nose and snarling mouth
    put(c, '''
.kkkkkk.
kkaakkkk
.kkkkkk.
...kk...
''', 20, 27)
    put(c, '''
kkkkkkkkkkkk
kwkkkkkkkkwk
kwwkkkkkkwwk
.kkkwkkwkkk.
..kkkkkkkk..
''', 18, 33)
    shade_rows(c, {'a': 'b'}, band=2, x0=24, y0=26, y1=40)
    return c


def wolf_scar(c):
    wolf(c)
    put(c, 'k\n.k\n..k\n...k\n....k\n.....k\n......k', 12, 13)
    put(c, 'w\nw', 19, 38)
    return c


def wolf_frost(c):
    wolf(c)
    for x, y in [(6, 40), (14, 44), (22, 42), (30, 46), (38, 41), (42, 49), (10, 50), (26, 52), (34, 53)]:
        put(c, '.w.\nwww\n.w.', x, y)
    return c


BUSTS['wolf_scar'] = dict(fn=wolf_scar, mirrored=True, open_slots='')
BUSTS['wolf_frost'] = dict(fn=wolf_frost, mirrored=True, open_slots='')


# ================================================================ boar: a broad head, bristling mane, a big snout and curved tusks
@bust('boar')
def boar(c):
    neck = c.new_part()
    c.poly2([(24, 30), (6, 32), (0, 42), (0, 56), (24, 56)], FURD, neck)
    c.reshade(neck, 16, 38, 22, 16, FURD, dw=2, hi=0.9)
    ears = c.new_part()
    c.poly2([(4, 8), (6, 18), (15, 14)], FUR, ears)
    mane = c.new_part()
    c.poly2([(24, 14), (13, 14), (14, 9), (16, 12), (17, 7), (19, 11), (21, 6), (23, 10), (24, 5)], Mat('d', 'd', 'd'), mane)
    hd = c.new_part()
    c.ellipse(24, 24, 15, 14, FUR, hd)
    c.reshade(hd, 20, 19, 16, 15, FUR, dw=2, hi=0.85)
    snout = c.new_part()
    c.ellipse(24, 36, 9.5, 7, LIGHT, snout)
    tusk = c.new_part()
    c.tube([(15, 38), (11, 36), (9, 31)], 1.5, WH, tusk, r1=0.8)
    c.tube([(33, 38), (37, 36), (39, 31)], 1.5, WH, tusk, r1=0.8)
    c.finish()
    put(c, '''
.kk
kddk
kdddk
.kkk
''', 6, 11, mirror=True)
    put(c, '''
kkkk....
..kkk...
.krrk...
..kk....
''', 13, 20, mirror=True)
    put(c, '''
..kk..kk..
.kkkk.kkkk
..kk..kk..
''', 19, 34)
    put(c, 'kkkkkkkk', 20, 41)
    c.pattern(neck, FURTUFT, margin=1, only='b')
    return c


def boar_iron(c):
    boar(c)
    for x in (12, 18, 24, 29, 35):
        for y in range(12, 20):
            if c.tone[y][x] not in '.k':
                c.paint(x, y, 'd')
        put(c, 'w', x + 1, 14)
    return c


BUSTS['boar_iron'] = dict(fn=boar_iron, mirrored=True, open_slots='')


# ================================================================ viper: a coiled snake rising, head to the viewer, tongue out
@bust('snake')
def snake(c):
    coil = c.new_part()
    c.ellipse(24, 50, 22, 8, FUR, coil)
    c.ellipse(24, 47, 15, 5, FURD, coil, clip=lambda x, y: y < 47)
    neck = c.new_part()
    c.tube([(24, 46), (30, 40), (30, 33), (24, 27)], 5.5, FUR, neck, r1=6)
    belly = c.new_part()
    c.tube([(25, 45), (29.5, 40), (29, 34)], 2.5, WH, belly)
    hd = c.new_part()
    c.ellipse(24, 18, 13, 10, FUR, hd)
    c.poly2([(24, 8), (14, 10), (11, 18), (16, 27), (24, 29)], FUR, hd)
    c.reshade(hd, 20, 14, 14, 12, FUR, dw=2, hi=0.85)
    c.finish()
    for y in range(44, 56, 2):
        for x in range(4, 44, 4):
            if c.tone[y][x] in 'ab' and c.part[y][x] == coil:
                c.paint(x + (y // 2) % 2 * 2, y, 'd')
    put(c, '''
kk.......
.kkkk....
..kyyk...
..kykk...
...kk....
''', 12, 13, mirror=True)
    put(c, 'k..k', 22, 23)
    put(c, '''
kkkkkkkk
.kkkkkk.
...rr...
...rr...
..r..r..
.r....r.
''', 20, 26)
    return c


# ================================================================ bat: face-on, wings spread across the panel, ears up, fangs
@bust('bat')
def bat(c):
    wing = c.new_part()
    c.poly2([(24, 22), (14, 14), (3, 6), (0, 12), (0, 40), (4, 36), (8, 42), (12, 37), (17, 42), (21, 34)], FURD, wing)
    body_ = c.new_part()
    c.ellipse(24, 40, 9, 12, FUR, body_)
    ears = c.new_part()
    c.poly2([(13, 3), (14, 16), (21, 13)], FUR, ears)
    hd = c.new_part()
    c.ellipse(24, 22, 11, 10, FUR, hd)
    c.reshade(hd, 21, 18, 12, 11, FUR, dw=2, hi=0.85)
    c.finish()
    for pts in [((20, 22), (4, 8)), ((19, 26), (2, 30)), ((19, 28), (9, 40))]:
        (x0, y0), (x1, y1) = pts
        n = max(abs(x1 - x0), abs(y1 - y0))
        for i in range(n + 1):
            x = round(x0 + (x1 - x0) * i / n)
            y = round(y0 + (y1 - y0) * i / n)
            if c.tone[y][x] in 'bd':
                c.tone[y][x] = 'k'
                c.tone[y][47 - x] = 'k'
    put(c, '''
.kk
kddk
kddk
.kdk
''', 14, 6, mirror=True)
    put(c, '''
kk.....
.kkkk..
.krrk..
..kk...
''', 15, 19, mirror=True)
    put(c, '''
.kk..kk.
..kkkk..
kkkkkkkk
.kwkkwk.
..w..w..
''', 20, 25)
    put(c, 'kk\nkk', 23, 50)
    return c


# ================================================================ crab: claws raised, eyes on stalks, a wide shell
@bust('crab')
def crab(c):
    arms = c.new_part()
    c.capsule2(9, 40, 7, 26, 2.6, FUR, arms)
    claws = c.new_part()
    c.ellipse2(7, 16, 7, 8.5, FUR, claws)
    shell = c.new_part()
    c.ellipse(24, 46, 20, 12, FUR, shell)
    c.reshade(shell, 20, 40, 20, 12, FUR, dw=2, hi=0.85)
    stalks = c.new_part()
    c.capsule2(19, 35, 18, 27, 1.5, FUR, stalks)
    eyes = c.new_part()
    c.ellipse2(18, 25, 3.5, 3.5, WH, eyes)
    c.cut([(5, 4), (9, 4), (7.5, 15), (6.5, 15)], m=True)
    c.finish()
    put(c, '''
kk
kk
''', 17, 24, mirror=True)
    put(c, '''
..kkkkkkkk..
.k.kk..kk.k.
''', 18, 44)
    for x in range(8, 40, 6):
        put(c, 'd\nd', x, 50 - abs(x - 23) // 6)
    return c


# ================================================================ monkey: a round face in a fur ring, big ears, a cheeky grin
@bust('monkey')
def monkey(c):
    sh = c.new_part()
    c.poly2([(24, 34), (10, 38), (2, 46), (0, 56), (24, 56)], FURD, sh)
    c.reshade(sh, 16, 42, 22, 16, FURD, dw=2, hi=0.9)
    ears = c.new_part()
    c.ellipse2(7, 22, 5, 6.5, FUR, ears)
    hd = c.new_part()
    c.ellipse(24, 22, 15, 15, FURD, hd)
    c.reshade(hd, 20, 16, 16, 16, FUR, dw=2, hi=0.8)
    mask = c.new_part()
    c.ellipse2(18.5, 19, 6, 6, LIGHT, mask)
    mouth = c.new_part()
    c.ellipse(24, 30, 9.5, 6.5, LIGHT, mouth)
    c.finish()
    put(c, '''
kk
kdk
kdk
kk
''', 6, 20, mirror=True)
    put(c, '''
kkkkk...
...kkkk.
..kwkk..
..kkk...
''', 14, 15, mirror=True)
    put(c, '''
.k..k.
''', 21, 26)
    put(c, '''
kkkkkkkkkk
kwwwwwwwwk
.kkkkkkkk.
''', 19, 29)
    put(c, '''
...k.k.k...
..k.k.k.k..
''', 13, 5)
    return c


# ================================================================ hornet: face-on, huge compound eyes, antennae, mandibles, a striped body, wings behind
@bust('hornet')
def hornet(c):
    wing = c.new_part()
    c.ellipse2(9, 30, 9, 13, Mat('w', 'w', 'a'), wing)
    body_ = c.new_part()
    c.ellipse(24, 47, 12, 10, FUR, body_)
    hd = c.new_part()
    c.ellipse(24, 24, 13, 12, FUR, hd)
    eyes = c.new_part()
    c.ellipse2(16, 21, 6, 9, Mat('b', 'd', 'd'), eyes)
    jaws = c.new_part()
    c.poly2([(23, 33), (17, 33), (16, 38), (20, 40), (22, 37)], Mat('d', 'd', 'd'), jaws)
    c.cut([(0, 24), (2, 24), (2, 36), (0, 36)], m=True)
    c.finish()
    put(c, '''
kk..
.kk.
..kk
...kk
....k
''', 13, 3, mirror=True)
    put(c, 'w\nw', 13, 16, mirror=True)
    for y in range(41, 56, 4):
        for x in range(12, 37):
            if c.part[y][x] == body_ and c.tone[y][x] != 'k':
                c.tone[y][x] = 'd'
                if y + 1 < 56 and c.tone[y + 1][x] != 'k':
                    c.tone[y + 1][x] = 'd'
    for y in range(20, 42, 4):
        for x in range(1, 17):
            if c.part[y][x] == wing and c.tone[y][x] == 'w' and (x + y) % 5 == 0:
                c.tone[y][x] = 'a'
                c.tone[y][47 - x] = 'a'
    return c


def hornet_ghost(c):
    hornet(c)
    put(c, '''
.ww.
wkkw
wwww
.ww.
''', 20, 44, mirror=False)
    put(c, '''
.ww.
wkkw
wwww
.ww.
''', 24, 44, mirror=False)
    return c


BUSTS['hornet_ghost'] = dict(fn=hornet_ghost, mirrored=True, open_slots='')


# ================================================================ centipede: a head with hooked fangs and long feelers, the body curling up behind
@bust('centipede')
def centipede(c):
    legs = c.new_part()
    for y in (33, 42, 51):
        c.capsule2(12, y - 1, 3, y + 4, 1.5, flat('y'), legs)
    for (y, rx) in [(53, 15), (44, 14), (35, 13)]:
        p = c.new_part()
        c.ellipse(24, y, rx, 5.5, FUR, p)
        c.reshade(p, 20, y - 2, rx, 6, FUR, dw=1, hi=0.85)
    ants = c.new_part()
    c.tube([(19, 16), (13, 8), (6, 5), (3, 9)], 1.1, FURD, ants)
    c.tube([(29, 16), (35, 8), (42, 5), (45, 9)], 1.1, FURD, ants)
    hd = c.new_part()
    c.ellipse(24, 22, 12.5, 9, FUR, hd)
    c.reshade(hd, 20, 19, 13, 10, FUR, dw=2, hi=0.85)
    fang = c.new_part()
    c.tube([(19, 28), (13, 30), (13, 35), (18, 38)], 1.8, flat('y'), fang, r1=1)
    c.tube([(29, 28), (35, 30), (35, 35), (30, 38)], 1.8, flat('y'), fang, r1=1)
    c.finish()
    put(c, '''
.kk.
kwkk
.kk.
''', 15, 19, mirror=True)
    put(c, 'kkkkkk', 21, 27)
    return c


# ================================================================ scorpion: claws raised, the tail arched over its back, the sting high above
@bust('scorpion', mirrored=False)
def scorpion(c):
    tail = c.new_part()
    c.tube([(24, 44), (24, 30), (25, 18), (30, 9), (37, 6), (41, 10)], 3.2, FUR, tail, r1=2.2)
    sting = c.new_part()
    c.poly([(40, 10), (45, 9), (43, 17)], flat('d'), sting)
    arms = c.new_part()
    c.capsule(10, 44, 7, 32, 2.6, FUR, arms)
    c.capsule(38, 44, 41, 32, 2.6, FUR, arms)
    claws = c.new_part()
    c.ellipse(6.5, 24, 6, 8, FUR, claws)
    c.ellipse(41.5, 24, 6, 8, FUR, claws)
    body_ = c.new_part()
    c.ellipse(24, 47, 15, 10, FUR, body_)
    c.reshade(body_, 20, 42, 16, 10, FUR, dw=2, hi=0.85)
    c.cut([(5, 15), (8, 15), (7, 23), (6, 23)])
    c.cut([(40, 15), (43, 15), (42, 23), (41, 23)])
    c.finish()
    for y in (20, 26, 32, 38):
        for x in range(19, 31):
            if c.part[y][x] == tail and c.tone[y][x] != 'k':
                c.tone[y][x] = 'k'
    put(c, '''
.kk.kk.
.krkrk.
''', 20, 43)
    return c


# ================================================================ wisp: a flame spirit's face, close up
@bust('wisp')
def wisp(c):
    fl = c.new_part()
    c.ellipse(24, 38, 17, 16, Mat('a', 'b', 'b'), fl)
    c.poly2([(24, 2), (19, 14), (12, 10), (11, 22), (5, 18), (7, 30), (24, 32)], Mat('a', 'b', 'b'), fl)
    core = c.new_part()
    c.ellipse(24, 40, 11, 11, flat('w'), core)
    c.finish()
    put(c, '''
kkk.
kkkk
kkkk
.kk.
''', 17, 34, mirror=True)
    put(c, '''
k....k
.kkkk.
''', 21, 45)
    return c


def wisp_nether(c):
    wisp(c)
    put(c, 'kk..\n.kkk\n..kk', 15, 30, mirror=True)
    return c


BUSTS['wisp_nether'] = dict(fn=wisp_nether, mirrored=True, open_slots='')


# ================================================================ paper effigy: a painted paper face, rouge cheeks, black paper hair, a paper robe
@bust('paperghost')
def paperghost(c):
    P = body(c, Mat('a', 'a', 'd'), Mat('a', 'a', 'd'), dots=None, robe=True, neck=(19, 28), finish=False, neck_slot='a')
    hair = c.new_part()
    c.ellipse(24, 16, 17, 15, flat('h'), hair)
    c.ellipse(24, 3, 7, 4, flat('h'), hair)
    fc = c.new_part()
    c.ellipse(24, 23, 12, 13, Mat('a', 'a', 'd', hi=0.6), fc)
    c.finish()
    for y in range(38, 56):
        for x in range(48):
            if c.part[y][x] == P['torso'] and c.tone[y][x] != 'k':
                u = abs(x - 23.5)
                if abs(u - (y - 38) * 0.9) < 1.2:
                    c.tone[y][x] = 'r'
    put(c, '''
.hhhh...
........
.kkkk...
..kk....
''', 16, 17, mirror=True)
    put(c, '''
.rr.
rrrr
.rr.
''', 14, 25, mirror=True)
    put(c, '''
.rrrr.
..rr..
''', 21, 31)
    return c


# ================================================================ tree sprite: a bark face under a leafy crown, hollow glowing eyes
@bust('treesprite')
def treesprite(c):
    trunk = c.new_part()
    c.poly2([(24, 18), (13, 18), (11, 40), (4, 50), (2, 56), (24, 56)], Mat('b', 'b', 'd'), trunk)
    br = c.new_part()
    c.capsule2(12, 36, 3, 28, 2.4, Mat('b', 'b', 'd'), br)
    crown = c.new_part()
    c.ellipse(24, 12, 22, 11, Mat('e', 'f', 'f'), crown)
    c.ellipse2(9, 17, 9, 7, Mat('e', 'f', 'f'), crown)
    c.finish()
    c.pattern(crown, '''
......
.kf...
......
....kf
''', margin=1)
    for x in (16, 21, 26, 31):
        for y in range(28, 56):
            if c.part[y][x] == trunk and c.tone[y][x] == 'b' and (y + x) % 9 < 6:
                c.tone[y][x] = 'd'
    put(c, '''
.kkkk.
kkyykk
kkyykk
.kkkk.
''', 15, 29, mirror=True)
    put(c, '''
..kkkk..
.kkkkkk.
.kkkkkk.
..kkkk..
''', 20, 40)
    return c


# ================================================================ toadstool: a big spotted cap, a face on the stem
@bust('mushroom')
def mushroom(c):
    stem = c.new_part()
    c.poly2([(24, 22), (14, 22), (12, 40), (8, 56), (24, 56)], Mat('e', 'e', 'f'), stem)
    cap = c.new_part()
    c.ellipse(24, 16, 23, 14, FUR, cap, clip=lambda x, y: y < 24)
    c.reshade(cap, 20, 10, 22, 14, FUR, dw=2, hi=0.85)
    gills = c.new_part()
    c.rect(4, 22, 43, 24, flat('d'), gills)
    c.finish()
    for x, y, s in [(10, 9, 3), (24, 5, 4), (36, 11, 3), (17, 15, 2), (31, 17, 2)]:
        put(c, '.yy.\nyyyy\nyyyy\n.yy.' if s > 2 else 'yy\nyy', x - s // 2, y)
    put(c, '''
kkk..
.kkkk
kkkk.
.kk..
''', 16, 30, mirror=True)
    put(c, '''
kkkkkk
.kkkk.
''', 21, 40)
    return c


# ================================================================ ink spirit: a dripping blob of ink with big round eyes
@bust('inkblot')
def inkblot(c):
    b = c.new_part()
    c.ellipse(24, 30, 19, 18, Mat('b', 'b', 'd'), b)
    c.ellipse2(9, 48, 4, 8, Mat('b', 'b', 'd'), b)
    c.ellipse2(18, 50, 3, 6, Mat('b', 'b', 'd'), b)
    c.ellipse(24, 10, 4, 5, Mat('b', 'b', 'd'), b)
    c.finish()
    put(c, '''
.kkkk.
kwwwwk
kwkkwk
kwkkwk
kwwwwk
.kkkk.
''', 13, 22, mirror=True)
    put(c, '''
k......k
.kkkkkk.
''', 20, 36)
    put(c, 'w', 13, 17)
    return c


# ================================================================ wind sprite: a whirl of wind with a face
@bust('windsprite', mirrored=False)
def windsprite(c):
    W_ = Mat('w', 'a', 'b')
    p = c.new_part()
    for i, (cx, cy, rx, ry) in enumerate([(24, 12, 20, 8), (24, 24, 16, 6), (25, 34, 11, 5), (26, 43, 7, 4), (27, 51, 4, 3)]):
        c.ellipse(cx, cy, rx, ry, W_, p)
    c.finish()
    for y in (16, 28, 38, 47):
        for x in range(48):
            if c.part[y][x] == p and c.tone[y][x] != 'k':
                c.tone[y][x] = 'b'
    put(c, '''
kk......kk
kk......kk
''', 19, 9)
    put(c, '''
k..k
.kk.
''', 22, 13)
    return c


# ================================================================ stone toad: a huge head, eyes on top, a wide mouth, warty stone skin
@bust('stonetoad')
def stonetoad(c):
    bd = c.new_part()
    c.ellipse(24, 42, 23, 15, FUR, bd)
    eyes = c.new_part()
    c.ellipse2(13, 19, 7, 7, FUR, eyes)
    hd = c.new_part()
    c.ellipse(24, 30, 21, 13, FUR, hd)
    c.reshade(hd, 20, 25, 22, 13, FUR, dw=2, hi=0.85)
    c.finish()
    put(c, '''
.kkkk.
kyyyyk
kykkyk
kykkyk
.kkkk.
''', 10, 15, mirror=True)
    put(c, 'kkkkkkkkkkkkkkkkkkkkkkkkkkk', 10, 36)
    put(c, '.k...............................k', 7, 35)
    for x, y in [(8, 28), (15, 26), (30, 26), (37, 29), (12, 44), (22, 46), (32, 45), (40, 48), (18, 51), (28, 52)]:
        put(c, 'dd\nd.', x, y)
    put(c, 'kk..kk', 21, 31)
    return c


# ================================================================ training dummy: a carved wooden head, painted eyes, peg arms
@bust('dummy')
def dummy(c):
    post = c.new_part()
    c.rect(14, 30, 33, 55, FUR, post)
    arms = c.new_part()
    c.capsule2(3, 36, 14, 40, 3, FUR, arms)
    c.capsule2(5, 50, 14, 48, 3, FUR, arms)
    hd = c.new_part()
    c.ellipse(24, 18, 12, 14, FUR, hd)
    c.reshade(hd, 20, 13, 13, 14, FUR, dw=2, hi=0.85)
    c.finish()
    for y in range(32, 56, 6):
        put(c, 'dddddddddddddddddd', 15, y)
    put(c, '''
.rrr..
rrrrr.
.rrr..
''', 15, 16, mirror=True)
    put(c, '''
kkkkkkkk
''', 20, 26)
    put(c, 'wwwwwwwwwwwwwwwwww', 15, 44)
    return c


def dummy_iron(c):
    dummy(c)
    for x, y in [(1, 34), (1, 48)]:
        put(c, 'kw\nkw', x, y, mirror=True)
    return c


BUSTS['dummy_iron'] = dict(fn=dummy_iron, mirrored=True, open_slots='')
