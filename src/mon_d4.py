"""Monster designs, part 4: the nine big beasts (怪物與野獸), 56x56 to 64x56, all facing the viewer."""
import math

from mondraw import Mat, flat
from mon_designs import design, BODY, BODY2, DARKB, WHITE

DD = flat('d')
KK = flat('k')


def arc(cx, cy, rx, ry, a0, a1, n=14):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n))
            for i in range(n + 1)]


# ================================================================ white ape 白猿 (hunched, knuckles down)
APEFACE = Mat('d', 'd', 'd')
APEFUR = Mat('a', 'a', 'b', hi=0.5)


@design('ape', 56, 56, mirrored=True)
def ape(c):
    lg = c.new_part()
    c.capsule2(21, 41, 19, 49, 4.6, APEFUR, lg)
    c.ellipse2(18.5, 51, 5.5, 2.8, APEFACE, lg)
    body = c.new_part()
    c.ellipse(28, 34, 13.5, 13, APEFUR, body)
    c.ellipse2(17, 23, 8, 7, APEFUR, body)
    c.reshade(body, 24, 27, 17, 17, APEFUR, dw=2)
    arm = c.new_part()
    c.capsule2(15, 24, 9, 37, 4.4, APEFUR, arm)
    c.capsule2(9, 37, 9, 46, 4.0, APEFUR, arm)
    fist = c.new_part()
    c.ellipse2(9, 48.5, 5, 3.8, APEFACE, fist)
    tuft = c.new_part()
    c.poly2([(20, 12), (16, 4), (24, 8), (28, 2), (28, 12)], APEFUR, tuft)
    head = c.new_part()
    c.ellipse(28, 15, 10.5, 9.5, APEFUR, head)
    c.reshade(head, 25, 12, 12, 11, APEFUR, dw=1)
    face = c.new_part()
    c.ellipse(28, 18, 7, 6.5, APEFACE, face)
    c.reshade(face, 26, 16, 8, 8, APEFACE, dw=1)
    c.finish()
    c.stamp(21, 14, "kkkkk", mirror=True)
    c.stamp(23, 16, "kr", mirror=True)
    c.stamp(26, 20, "k", mirror=True)
    c.stamp(24, 22, "kkkk", mirror=True)
    c.stamp(24, 23, "kw", mirror=True)
    # a red peach in the right fist
    c.stamp(41, 44, """
...kk
..kgk
.kkkkk
krrrrrk
krrrrrk
krrrrrk
.krrrk
..kkk
""")
    return c


# ================================================================ white-browed tiger 白額虎 (sitting)
TIGER = Mat('b', 'b', 'd')
TW = Mat('w', 'w', 'b')


@design('tiger', 56, 56, mirrored=True)
def tiger(c):
    tail = c.new_part()
    c.tube([(40, 51), (47, 50), (51, 45), (51, 38), (48, 34)], 2.6, TIGER, tail, r1=2.0)
    body = c.new_part()
    c.ellipse(28, 42, 14, 11.5, TIGER, body)
    c.reshade(body, 25, 38, 15, 13, TIGER, dw=2)
    chest = c.new_part(sep=False)
    c.ellipse(28, 37, 5, 5, TW, chest)
    lg = c.new_part(sep=False)
    c.capsule2(21.5, 38, 21, 49, 3.8, TIGER, lg)
    paw = c.new_part()
    c.ellipse2(20.5, 51, 5, 2.8, TW, paw)
    ear = c.new_part()
    c.ellipse2(16.5, 9.5, 4.8, 4.8, TIGER, ear)
    c.ellipse2(16.8, 10, 2.2, 2.4, KK, ear)
    ruff = c.new_part()
    c.poly2([(18, 18), (11, 24), (13, 26.5), (10.5, 31), (17, 30), (22, 33)], TIGER, ruff)
    head = c.new_part()
    c.ellipse(28, 20, 14, 12, TIGER, head)
    c.reshade(head, 24, 16, 15, 13, TIGER, dw=1)
    muz = c.new_part(sep=False)
    c.ellipse2(24.5, 27, 4.5, 3.6, TW, muz)
    c.ellipse(28, 31, 3.5, 2.2, TW, muz)
    c.finish()
    # brows, eyes, nose, stripes
    c.stamp(19, 17, "wwww", mirror=True)
    c.stamp(19, 19, "kkkk", mirror=True)
    c.stamp(19, 20, "kyyk", mirror=True)
    c.stamp(20, 21, "kk", mirror=True)
    c.stamp(25, 25, "pp", mirror=True)
    c.stamp(26, 26, "p", mirror=True)
    c.stamp(27, 27, "k", mirror=True)
    c.stamp(24, 29, "kkk", mirror=True)
    c.stamp(25, 10, "kk", mirror=True)
    c.stamp(24, 12, "kkkkkkkk")
    c.stamp(27, 11, "kk")
    c.stamp(26, 14, "kkkk")
    for (x, y) in ((14, 18), (14, 22), (15, 26)):
        c.stamp(x, y, "kkk", mirror=True)
    for (x, y) in ((15, 38), (15, 42), (16, 46)):
        c.stamp(x, y, "kk", mirror=True)
    c.stamp(45, 49, "k")
    c.stamp(49, 42, "kk")
    c.stamp(48, 37, "kk")
    return c


# ================================================================ stone guardian lion 石獅 (on its plinth)
STONE = Mat('a', 'b', 'd')


@design('lion', 56, 56, mirrored=True)
def lion(c):
    plinth = c.new_part()
    c.rect(7, 47, 48, 54, Mat('b', 'd', 'd'), plinth)
    lg = c.new_part()
    c.capsule2(19.5, 36, 19, 44, 4.2, STONE, lg)
    c.ellipse2(18.5, 45, 5.5, 2.8, STONE, lg)
    chest = c.new_part()
    c.ellipse(28, 39, 11, 8.5, STONE, chest)
    for i in range(14):
        a = math.pi * 2 * i / 14 + math.pi / 14
        c.ellipse(28 + 15 * math.cos(a), 20 + 14 * math.sin(a), 4.6, 4.6, STONE)
    mane = c.new_part()
    c.ellipse(28, 20, 15, 14, STONE, mane)
    head = c.new_part()
    c.ellipse(28, 21, 10.5, 9.5, STONE, head)
    c.reshade(head, 25, 18, 12, 11, STONE, dw=1)
    mouth = c.new_part()
    c.ellipse(28, 27, 6, 3.4, KK, mouth)
    ball = c.new_part()
    c.ellipse(28, 28, 3, 2.6, STONE, ball)
    c.finish()
    c.stamp(19, 15, "kkkkkk", mirror=True)
    c.stamp(20, 16, "kwwwk", mirror=True)
    c.stamp(20, 17, "kwrrk", mirror=True)
    c.stamp(20, 18, "kwrrk", mirror=True)
    c.stamp(21, 19, "kkk", mirror=True)
    c.stamp(25, 21, "kk", mirror=True)
    c.stamp(25, 22, "kd", mirror=True)
    c.stamp(23, 25, "w.w", mirror=True)
    c.stamp(26, 28, "aa", mirror=True)
    c.stamp(25, 29, "aaa", mirror=True)
    for (x, y) in ((10, 49), (11, 52), (40, 51), (26, 50)):
        c.stamp(x, y, "mmm")
    return c


# ================================================================ jiangshi 殭屍 (the old hopping corpse)
JROBE = Mat('b', 'b', 'd')
JSKIN = flat('S')


@design('jiangshi', 56, 56, mirrored=True)
def jiangshi(c):
    lg = c.new_part()
    c.capsule2(24.5, 44, 24.5, 50, 3.0, Mat('d', 'd', 'd'), lg)
    c.ellipse2(23.5, 52, 4.5, 2.2, Mat('d', 'd', 'd'), lg)
    robe = c.new_part()
    c.poly2([(28, 21), (17, 22), (14, 46), (28, 46)], JROBE, robe)
    c.reshade(robe, 23, 28, 12, 20, JROBE, dw=1, hi=2)
    sleeve = c.new_part()
    c.capsule2(17, 24, 6, 25, 4.0, JROBE, sleeve)
    hand = c.new_part()
    c.poly2([(1.5, 22), (5.5, 22), (5, 29), (2, 29)], JSKIN, hand)
    badge = c.new_part()
    c.rect(22, 30, 33, 39, flat('y'), badge, shade='flat')
    head = c.new_part()
    c.ellipse(28, 15, 8, 7.5, JSKIN, head)
    brim = c.new_part()
    c.ellipse(28, 9, 14, 3.2, DD, brim)
    hat = c.new_part()
    c.ellipse(28, 6, 8, 4.2, JROBE, hat)
    c.finish()
    c.stamp(25, 10, """
kkkkkk
kyyyyk
kyrryk
kyyyyk
kyrryk
kyyyyk
kyrryk
kyyyyk
kkkkkk
""")
    c.stamp(27, 1, "kk")
    c.stamp(26, 2, "krrk")
    c.stamp(21, 14, "kkk", mirror=True)
    c.stamp(21, 15, "kek", mirror=True)
    c.stamp(25, 19, "kk", mirror=True)
    c.stamp(24, 32, "dddddddd")
    c.stamp(24, 34, "dd....dd")
    c.stamp(24, 36, "dddddddd")
    c.stamp(1, 29, "kSkSk", mirror=True)
    c.stamp(1, 30, "kSkSk", mirror=True)
    c.stamp(1, 31, ".k.k.", mirror=True)
    return c


# ================================================================ mountain spirit 山魈 (a mandrill-faced demon)
FUR = Mat('g', 'o', 'd')


@design('shanxiao', 56, 56, mirrored=True)
def shanxiao(c):
    lg = c.new_part()
    c.capsule(28, 44, 28, 50, 5.0, FUR, lg)
    c.ellipse(28, 52, 9, 2.8, DD, lg)
    arm = c.new_part()
    c.capsule2(15, 26, 8, 38, 4.0, FUR, arm)
    c.capsule2(8, 38, 9, 46, 3.4, FUR, arm)
    claw = c.new_part()
    c.ellipse2(9, 48, 4, 3, DD, claw)
    body = c.new_part()
    c.ellipse(28, 36, 13, 12, FUR, body)
    c.reshade(body, 24, 31, 15, 15, FUR, dw=2)
    mane = c.new_part()
    for i in range(12):
        a = math.pi * 2 * i / 12
        c.poly([(28 + 12 * math.cos(a - 0.3), 19 + 12 * math.sin(a - 0.3)),
                (28 + 19 * math.cos(a), 19 + 18 * math.sin(a)),
                (28 + 12 * math.cos(a + 0.3), 19 + 12 * math.sin(a + 0.3))], FUR, mane)
    c.ellipse(28, 19, 14, 13.5, FUR, mane)
    c.reshade(mane, 24, 15, 17, 17, FUR, dw=2)
    face = c.new_part()
    c.ellipse(28, 20, 9, 10, DD, face)
    c.finish()
    # the mandrill face: blue ridged cheeks, a long red nose, small gold eyes (sprite layer)
    c.stamp(21, 15, "kkkkkk", mirror=True)
    c.stamp(22, 16, "kyk", mirror=True)
    c.stamp(21, 18, "BBB", mirror=True)
    c.stamp(20, 19, "BkBB", mirror=True)
    c.stamp(20, 20, "BBkB", mirror=True)
    c.stamp(20, 21, "BkBB", mirror=True)
    c.stamp(20, 22, "BBkB", mirror=True)
    c.stamp(21, 23, "BBB", mirror=True)
    c.stamp(26, 15, "rr", mirror=True)
    for y in range(16, 24):
        c.stamp(26, y, "rr", mirror=True)
    c.stamp(26, 24, "kr", mirror=True)
    c.stamp(23, 26, "kkkkk", mirror=True)
    c.stamp(24, 27, "y", mirror=True)
    return c


# ================================================================ nine-tailed fox 九尾狐 (tails fanned behind)
FOX = Mat('w', 'b', 'd')
FOXW = Mat('w', 'w', 'b')


@design('fox', 56, 56, mirrored=True)
def fox(c):
    for i in (0, 8, 1, 7, 2, 6, 3, 5, 4):
        a = math.radians(196 + 148 * i / 8)
        tip = (28 + 24 * math.cos(a), 44 + 33 * math.sin(a))
        mid = (28 + 14 * math.cos(a), 45 + 18 * math.sin(a))
        t = c.new_part()
        c.tube([(28, 44), mid, tip], 2.6, FOX, t, r1=3.0)
        c.ellipse(tip[0], tip[1], 3.2, 3.2, FOXW, t)
    body = c.new_part()
    c.ellipse(28, 41, 9, 11, FOX, body)
    chest = c.new_part(sep=False)
    c.ellipse(28, 39, 5, 8, FOXW, chest)
    lg = c.new_part()
    c.capsule2(24.5, 42, 24.5, 50, 2.2, FOX, lg)
    c.ellipse2(24, 51.5, 3.2, 2.0, FOXW, lg)
    ear = c.new_part()
    c.poly2([(21, 16), (19, 4.5), (26.5, 12)], FOX, ear)
    c.poly2([(21.5, 14), (20.3, 8), (24, 12.5)], flat('p'), ear)
    ruff = c.new_part()
    c.poly2([(21, 20), (16.5, 27), (21, 26), (24, 29)], FOXW, ruff)
    head = c.new_part()
    c.ellipse(28, 20, 8.5, 7.5, FOX, head)
    c.reshade(head, 26, 17, 10, 9, FOX, dw=1, hi=0.97)
    snout = c.new_part(sep=False)
    c.ellipse(28, 25, 4, 3.2, FOXW, snout)
    c.finish()
    c.stamp(22, 18, "kk", mirror=True)
    c.stamp(23, 19, "rrk", mirror=True)
    c.stamp(27, 24, "kk")
    c.stamp(26, 27, "k", mirror=True)
    return c


# ================================================================ river dragon 蛟 (rising from the waves)
SCALE = Mat('a', 'b', 'd')
BELLY = Mat('e', 'e', 'b')
WATER = Mat('h', 'i', 'i')


@design('jiao', 64, 56, mirrored=True)
def jiao(c):
    for side in (0, 1):
        pts = arc(14, 47.5, 8, 13, math.pi, 2 * math.pi)
        if side:
            pts = [(64 - x, y) for x, y in pts]
        c.tube(pts, 3.4, SCALE, r1=2.4)
        fin = c.new_part()
        for k in (4, 7, 10):
            x, y = pts[k]
            c.poly([(x - 2, y - 2), (x + (1 if side else -1) * 1, y - 7), (x + 2, y - 2)], DARKB, fin)
    neck = c.new_part()
    c.capsule(32, 46, 32, 24, 6.5, SCALE, neck, r1=5.5)
    belly = c.new_part(sep=False)
    c.rect(29, 26, 34, 47, BELLY, belly, shade='flat')
    horn = c.new_part()
    c.tube([(26, 10), (21, 5.5), (19, 2.6)], 1.8, Mat('e', 'e', 'b'), horn, r1=1.2)
    c.tube([(38, 10), (43, 5.5), (45, 2.6)], 1.8, Mat('e', 'e', 'b'), horn, r1=1.2)
    crest = c.new_part()
    c.poly2([(23, 12), (14, 9), (17, 14), (13, 17), (22, 18)], DARKB, crest)
    head = c.new_part()
    c.ellipse(32, 14, 9.5, 7.5, SCALE, head)
    c.ellipse(32, 21, 8, 5, SCALE, head)
    c.reshade(head, 29, 13, 11, 10, SCALE, dw=1)
    water = c.new_part()
    c.rect(1, 49, 62, 54, WATER, water)
    c.finish()
    c.stamp(25, 13, "kkkk", mirror=True)
    c.stamp(26, 14, "krr", mirror=True)
    c.stamp(27, 15, "kk", mirror=True)
    c.stamp(29, 20, "k", mirror=True)
    c.stamp(26, 23, "kkkkk", mirror=True)
    c.stamp(27, 24, "e.e", mirror=True)
    c.stamp(25, 21, "kk", mirror=True)
    c.stamp(22, 22, "kkk", mirror=True)
    c.stamp(19, 23, "kkk", mirror=True)
    c.stamp(17, 24, "kk", mirror=True)
    for y in (30, 34, 38, 42, 46):
        c.stamp(29, y, "bbbbbb")
    for x in range(2, 62, 8):
        c.stamp(x, 50, "www")
        c.stamp(x + 1, 49, "w")
        if x + 5 < 62:
            c.stamp(x + 4, 52, "hh")
    return c


# ================================================================ fire crow 火鴉 (wings spread, tail aflame)
FEATHER = Mat('o', 'r', 'd')
FLAME = Mat('o', 'r', 'd')


@design('crow', 64, 56, mirrored=True)
def crow(c):
    tail = c.new_part()
    c.poly2([(32, 38), (25, 40), (21, 54), (26, 49), (28, 55), (31, 48), (32, 52)], FLAME, tail)
    c.reshade(tail, 30, 44, 8, 12, FLAME, dw=1, hi=0.5)
    wing = c.new_part()
    c.poly2([(27, 19), (20, 10), (11, 5), (2, 7), (1.5, 15), (5, 19), (3.5, 25), (9, 27), (8.5, 33), (14, 32),
             (15, 38), (20, 35), (27, 36)], FEATHER, wing)
    c.reshade(wing, 16, 14, 20, 18, FEATHER, dw=1)
    feet = c.new_part()
    c.capsule2(29, 38, 28, 44, 1.2, flat('e'), feet)
    c.capsule(32, 39, 32, 45, 1.2, flat('e'), feet)
    body = c.new_part()
    c.ellipse(32, 29, 8, 10.5, FEATHER, body)
    c.reshade(body, 30, 26, 9, 11, FEATHER, dw=1)
    head = c.new_part()
    c.ellipse(32, 15, 6.5, 6, FEATHER, head)
    c.poly2([(29, 9), (26, 2), (31, 7)], FEATHER, head)
    beak = c.new_part()
    c.poly2([(32, 16), (29.5, 17), (32, 23.5)], Mat('e', 'e', 'e'), beak)
    c.finish()
    for (a, b) in (((22, 14), (6, 9)), ((21, 18), (4, 20)), ((21, 22), (8, 29)), ((22, 27), (13, 33))):
        for t in range(1, 12):
            x = round(a[0] + (b[0] - a[0]) * t / 12)
            y = round(a[1] + (b[1] - a[1]) * t / 12)
            if c.tone[y][x] not in '.k':
                c.paint(x, y, 'd')
                c.paint(63 - x, y, 'd')
    c.stamp(28, 13, "kk", mirror=True)
    c.stamp(28, 14, "kW", mirror=True)
    for (x, y) in ((28, 52), (31, 47), (24, 47)):
        if c.tone[y][x] not in '.k':
            c.stamp(x, y, "e", mirror=True)
    return c


# ================================================================ giant toad 大蟾蜍 (warty, throat swelling)
TOAD = Mat('a', 'b', 'd')
THROAT = Mat('a', 'a', 'b')


@design('toad', 64, 48, mirrored=True)
def toad(c):
    hind = c.new_part()
    c.ellipse2(11, 35, 9, 7.5, TOAD, hind)
    c.ellipse2(9, 44, 8, 2.5, TOAD, hind)
    body = c.new_part()
    c.ellipse(32, 29, 22, 14, TOAD, body)
    c.reshade(body, 27, 22, 23, 16, TOAD, dw=2)
    throat = c.new_part(sep=False)
    c.ellipse(32, 36, 11, 7, THROAT, throat)
    fl = c.new_part()
    c.capsule2(22, 36, 20, 42, 3.0, TOAD, fl)
    c.ellipse2(19, 44, 5, 2.4, TOAD, fl)
    eye = c.new_part()
    c.ellipse2(20.5, 13, 6.5, 6, TOAD, eye)
    c.finish()
    c.stamp(17, 9, """
..kkkk
.kooook
kooooook
kkkkkkkk
kooooook
.kooook
..kkkk
""", mirror=True)

    c.stamp(11, 26, "kk", mirror=True)
    c.stamp(13, 27, "kk", mirror=True)
    c.stamp(15, 28, "kkkkkkkkkkkkkkkkk", mirror=True)
    for (x, y) in ((14, 21), (20, 23), (26, 20), (10, 30), (44, 21), (49, 25), (38, 19), (53, 31), (30, 17)):
        c.stamp(x, y, "aa")
        c.stamp(x, y + 1, "bb")
    return c
