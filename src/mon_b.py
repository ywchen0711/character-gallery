"""Monster designs (second version), part 4: the nine big beasts (怪物與野獸), 64x64 / 64x56, finished by hand.

The shapes are the first version's, drawn bigger through mondraw.Scaled; every face, texture and detail is new."""
import math

from mondraw import Mat, flat, Scaled
from mon_designs import design, BODY, BODY2, DARKB, WHITE

DD = flat('d')
KK = flat('k')


def arc(cx, cy, rx, ry, a0, a1, n=14):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n))
            for i in range(n + 1)]


# ================================================================ white ape 白猿 (hunched, knuckles down)
APEFACE = Mat('d', 'd', 'd')
APEFUR = Mat('a', 'a', 'b', hi=0.5)


@design('ape', 64, 64, mirrored=True)
def ape(c):
    g = Scaled(c, 1.1429, 56, 56)
    lg = g.new_part()
    g.capsule2(21, 41, 19, 49, 4.6, APEFUR, lg)
    g.ellipse2(18.5, 51, 5.5, 2.8, APEFACE, lg)
    body = g.new_part()
    g.ellipse(28, 34, 13.5, 13, APEFUR, body)
    g.ellipse2(17, 23, 8, 7, APEFUR, body)
    g.reshade(body, 24, 27, 17, 17, APEFUR, dw=2)
    arm = g.new_part()
    g.capsule2(15, 24, 9, 37, 4.4, APEFUR, arm)
    g.capsule2(9, 37, 9, 46, 4.0, APEFUR, arm)
    fist = g.new_part()
    g.ellipse2(9, 48.5, 5, 3.8, APEFACE, fist)
    tuft = g.new_part()
    g.poly2([(20, 12), (16, 4), (24, 8), (28, 2), (28, 12)], APEFUR, tuft)
    head = g.new_part()
    g.ellipse(28, 15, 10.5, 9.5, APEFUR, head)
    g.reshade(head, 25, 12, 12, 11, APEFUR, dw=1)
    face = g.new_part()
    g.ellipse(28, 18, 7, 6.5, APEFACE, face)
    g.reshade(face, 26, 16, 8, 8, APEFACE, dw=1)
    c.finish()
    finish_ape(c, g)
    return c


# ================================================================ white-browed tiger 白額虎 (sitting)
TIGER = Mat('b', 'b', 'd')
TW = Mat('w', 'w', 'b')


@design('tiger', 64, 64, mirrored=True)
def tiger(c):
    g = Scaled(c, 1.1429, 56, 56)
    tail = g.new_part()
    g.tube([(40, 51), (47, 50), (51, 45), (51, 38), (48, 34)], 2.6, TIGER, tail, r1=2.0)
    body = g.new_part()
    g.ellipse(28, 42, 14, 11.5, TIGER, body)
    g.reshade(body, 25, 38, 15, 13, TIGER, dw=2)
    chest = g.new_part(sep=False)
    g.ellipse(28, 37, 5, 5, TW, chest)
    lg = g.new_part(sep=False)
    g.capsule2(21.5, 38, 21, 49, 3.8, TIGER, lg)
    paw = g.new_part()
    g.ellipse2(20.5, 51, 5, 2.8, TW, paw)
    ear = g.new_part()
    g.ellipse2(16.5, 9.5, 4.8, 4.8, TIGER, ear)
    g.ellipse2(16.8, 10, 2.2, 2.4, KK, ear)
    ruff = g.new_part()
    g.poly2([(18, 18), (11, 24), (13, 26.5), (10.5, 31), (17, 30), (22, 33)], TIGER, ruff)
    head = g.new_part()
    g.ellipse(28, 20, 14, 12, TIGER, head)
    g.reshade(head, 24, 16, 15, 13, TIGER, dw=1)
    muz = g.new_part(sep=False)
    g.ellipse2(24.5, 27, 4.5, 3.6, TW, muz)
    g.ellipse(28, 31, 3.5, 2.2, TW, muz)
    c.finish()
    finish_tiger(c, g)
    return c


# ================================================================ stone guardian lion 石獅 (on its plinth)
STONE = Mat('a', 'b', 'd')


@design('lion', 64, 64, mirrored=True)
def lion(c):
    g = Scaled(c, 1.1429, 56, 56)
    plinth = g.new_part()
    g.rect(7, 47, 48, 54, Mat('b', 'd', 'd'), plinth)
    lg = g.new_part()
    g.capsule2(19.5, 36, 19, 44, 4.2, STONE, lg)
    g.ellipse2(18.5, 45, 5.5, 2.8, STONE, lg)
    chest = g.new_part()
    g.ellipse(28, 39, 11, 8.5, STONE, chest)
    for i in range(14):
        a = math.pi * 2 * i / 14 + math.pi / 14
        g.ellipse(28 + 15 * math.cos(a), 20 + 14 * math.sin(a), 4.6, 4.6, STONE)
    mane = g.new_part()
    g.ellipse(28, 20, 15, 14, STONE, mane)
    head = g.new_part()
    g.ellipse(28, 21, 10.5, 9.5, STONE, head)
    g.reshade(head, 25, 18, 12, 11, STONE, dw=1)
    mouth = g.new_part()
    g.ellipse(28, 27, 6, 3.4, KK, mouth)
    ball = g.new_part()
    g.ellipse(28, 28, 3, 2.6, STONE, ball)
    c.finish()
    finish_lion(c, g)
    return c


# ================================================================ jiangshi 殭屍 (the old hopping corpse)
JROBE = Mat('b', 'b', 'd')
JSKIN = flat('S')


@design('jiangshi', 64, 64, mirrored=True)
def jiangshi(c):
    g = Scaled(c, 1.1429, 56, 56)
    lg = g.new_part()
    g.capsule2(24.5, 44, 24.5, 50, 3.0, Mat('d', 'd', 'd'), lg)
    g.ellipse2(23.5, 52, 4.5, 2.2, Mat('d', 'd', 'd'), lg)
    robe = g.new_part()
    g.poly2([(28, 21), (17, 22), (14, 46), (28, 46)], JROBE, robe)
    g.reshade(robe, 23, 28, 12, 20, JROBE, dw=1, hi=2)
    sleeve = g.new_part()
    g.capsule2(17, 24, 6, 25, 4.0, JROBE, sleeve)
    hand = g.new_part()
    g.poly2([(1.5, 22), (5.5, 22), (5, 29), (2, 29)], JSKIN, hand)
    badge = g.new_part()
    g.rect(22, 30, 33, 39, flat('y'), badge, shade='flat')
    head = g.new_part()
    g.ellipse(28, 15, 8, 7.5, JSKIN, head)
    brim = g.new_part()
    g.ellipse(28, 9, 14, 3.2, DD, brim)
    hat = g.new_part()
    g.ellipse(28, 6, 8, 4.2, JROBE, hat)
    c.finish()
    finish_jiangshi(c, g)
    return c


# ================================================================ mountain spirit 山魈 (a mandrill-faced demon)
FUR = Mat('g', 'o', 'd')


@design('shanxiao', 64, 64, mirrored=True)
def shanxiao(c):
    g = Scaled(c, 1.1429, 56, 56)
    lg = g.new_part()
    g.capsule(28, 44, 28, 50, 5.0, FUR, lg)
    g.ellipse(28, 52, 9, 2.8, DD, lg)
    arm = g.new_part()
    g.capsule2(15, 26, 8, 38, 4.0, FUR, arm)
    g.capsule2(8, 38, 9, 46, 3.4, FUR, arm)
    claw = g.new_part()
    g.ellipse2(9, 48, 4, 3, DD, claw)
    body = g.new_part()
    g.ellipse(28, 36, 13, 12, FUR, body)
    g.reshade(body, 24, 31, 15, 15, FUR, dw=2)
    mane = g.new_part()
    for i in range(12):
        a = math.pi * 2 * i / 12
        g.poly([(28 + 12 * math.cos(a - 0.3), 19 + 12 * math.sin(a - 0.3)),
                (28 + 19 * math.cos(a), 19 + 18 * math.sin(a)),
                (28 + 12 * math.cos(a + 0.3), 19 + 12 * math.sin(a + 0.3))], FUR, mane)
    g.ellipse(28, 19, 14, 13.5, FUR, mane)
    g.reshade(mane, 24, 15, 17, 17, FUR, dw=2)
    face = g.new_part()
    g.ellipse(28, 20, 9, 10, DD, face)
    c.finish()
    finish_shanxiao(c, g)
    return c


# ================================================================ nine-tailed fox 九尾狐 (tails fanned behind)
FOX = Mat('w', 'b', 'd')
FOXW = Mat('w', 'w', 'b')


@design('fox', 64, 64, mirrored=True)
def fox(c):
    g = Scaled(c, 1.1429, 56, 56)
    for i in (0, 8, 1, 7, 2, 6, 3, 5, 4):
        a = math.radians(196 + 148 * i / 8)
        tip = (28 + 24 * math.cos(a), 44 + 33 * math.sin(a))
        mid = (28 + 14 * math.cos(a), 45 + 18 * math.sin(a))
        t = g.new_part()
        g.tube([(28, 44), mid, tip], 2.6, FOX, t, r1=3.0)
        g.ellipse(tip[0], tip[1], 3.2, 3.2, FOXW, t)
    body = g.new_part()
    g.ellipse(28, 41, 9, 11, FOX, body)
    chest = g.new_part(sep=False)
    g.ellipse(28, 39, 5, 8, FOXW, chest)
    lg = g.new_part()
    g.capsule2(24.5, 42, 24.5, 50, 2.2, FOX, lg)
    g.ellipse2(24, 51.5, 3.2, 2.0, FOXW, lg)
    ear = g.new_part()
    g.poly2([(21, 16), (19, 4.5), (26.5, 12)], FOX, ear)
    g.poly2([(21.5, 14), (20.3, 8), (24, 12.5)], flat('p'), ear)
    ruff = g.new_part()
    g.poly2([(21, 20), (16.5, 27), (21, 26), (24, 29)], FOXW, ruff)
    head = g.new_part()
    g.ellipse(28, 20, 8.5, 7.5, FOX, head)
    g.reshade(head, 26, 17, 10, 9, FOX, dw=1, hi=0.97)
    snout = g.new_part(sep=False)
    g.ellipse(28, 25, 4, 3.2, FOXW, snout)
    c.finish()
    finish_fox(c, g)
    return c


# ================================================================ river dragon 蛟 (rising from the waves)
SCALE = Mat('a', 'b', 'd')
BELLY = Mat('e', 'e', 'b')
WATER = Mat('h', 'i', 'i')


@design('jiao', 64, 56, mirrored=True)
def jiao(c):
    g = Scaled(c, 1.0000, 64, 56)
    for side in (0, 1):
        pts = arc(14, 47.5, 8, 13, math.pi, 2 * math.pi)
        if side:
            pts = [(64 - x, y) for x, y in pts]
        g.tube(pts, 3.4, SCALE, r1=2.4)
        fin = g.new_part()
        for k in (4, 7, 10):
            x, y = pts[k]
            g.poly([(x - 2, y - 2), (x + (1 if side else -1) * 1, y - 7), (x + 2, y - 2)], DARKB, fin)
    neck = g.new_part()
    g.capsule(32, 46, 32, 24, 6.5, SCALE, neck, r1=5.5)
    belly = g.new_part(sep=False)
    g.rect(29, 26, 34, 47, BELLY, belly, shade='flat')
    horn = g.new_part()
    g.tube([(26, 10), (21, 5.5), (19, 2.6)], 1.8, Mat('e', 'e', 'b'), horn, r1=1.2)
    g.tube([(38, 10), (43, 5.5), (45, 2.6)], 1.8, Mat('e', 'e', 'b'), horn, r1=1.2)
    crest = g.new_part()
    g.poly2([(23, 12), (14, 9), (17, 14), (13, 17), (22, 18)], DARKB, crest)
    head = g.new_part()
    g.ellipse(32, 14, 9.5, 7.5, SCALE, head)
    g.ellipse(32, 21, 8, 5, SCALE, head)
    g.reshade(head, 29, 13, 11, 10, SCALE, dw=1)
    water = g.new_part()
    g.rect(1, 49, 62, 54, WATER, water)
    c.finish()
    finish_jiao(c, g)
    return c


# ================================================================ fire crow 火鴉 (wings spread, tail aflame)
FEATHER = Mat('o', 'r', 'd')
FLAME = Mat('o', 'r', 'd')


@design('crow', 64, 56, mirrored=True)
def crow(c):
    g = Scaled(c, 1.0000, 64, 56)
    tail = g.new_part()
    g.poly2([(32, 38), (25, 40), (21, 54), (26, 49), (28, 55), (31, 48), (32, 52)], FLAME, tail)
    g.reshade(tail, 30, 44, 8, 12, FLAME, dw=1, hi=0.5)
    wing = g.new_part()
    g.poly2([(27, 19), (20, 10), (11, 5), (2, 7), (1.5, 15), (5, 19), (3.5, 25), (9, 27), (8.5, 33), (14, 32),
             (15, 38), (20, 35), (27, 36)], FEATHER, wing)
    g.reshade(wing, 16, 14, 20, 18, FEATHER, dw=1)
    feet = g.new_part()
    g.capsule2(29, 38, 28, 44, 1.2, flat('e'), feet)
    g.capsule(32, 39, 32, 45, 1.2, flat('e'), feet)
    body = g.new_part()
    g.ellipse(32, 29, 8, 10.5, FEATHER, body)
    g.reshade(body, 30, 26, 9, 11, FEATHER, dw=1)
    head = g.new_part()
    g.ellipse(32, 15, 6.5, 6, FEATHER, head)
    g.poly2([(29, 9), (26, 2), (31, 7)], FEATHER, head)
    beak = g.new_part()
    g.poly2([(32, 16), (29.5, 17), (32, 23.5)], Mat('e', 'e', 'e'), beak)
    c.finish()
    finish_crow(c, g)
    return c


# ================================================================ giant toad 大蟾蜍 (warty, throat swelling)
TOAD = Mat('a', 'b', 'd')
THROAT = Mat('a', 'a', 'b')


@design('toad', 64, 56, mirrored=True)
def toad(c):
    g = Scaled(c, 1.0000, 64, 48)
    hind = g.new_part()
    g.ellipse2(11, 35, 9, 7.5, TOAD, hind)
    g.ellipse2(9, 44, 8, 2.5, TOAD, hind)
    body = g.new_part()
    g.ellipse(32, 29, 22, 14, TOAD, body)
    g.reshade(body, 27, 22, 23, 16, TOAD, dw=2)
    throat = g.new_part(sep=False)
    g.ellipse(32, 36, 11, 7, THROAT, throat)
    fl = g.new_part()
    g.capsule2(22, 36, 20, 42, 3.0, TOAD, fl)
    g.ellipse2(19, 44, 5, 2.4, TOAD, fl)
    eye = g.new_part()
    g.ellipse2(20.5, 13, 6.5, 6, TOAD, eye)
    c.finish()
    finish_toad(c, g)
    return c



# ---------------------------------------------------------------- the hand-finishing passes
class Off:
    """The canvas seen with the first version's coordinates (same size, shifted down by dy)."""

    def __init__(self, c, dy):
        self.c, self.dy, self.w, self.h = c, dy, c.w, c.h - dy
        self.tone = c.tone[dy:]

    def stamp(self, x, y, text, part=None, mirror=False):
        self.c.stamp(x, y + self.dy, text, part, mirror)

    def paint(self, x, y, slot, part=None):
        self.c.paint(x, y + self.dy, slot, part)

    def put(self, pts, slot):
        self.c.put([(x, y + self.dy) for x, y in pts], slot)

    def put2(self, pts, slot):
        self.c.put2([(x, y + self.dy) for x, y in pts], slot)


def finish_ape(c, g):
    c.stamp(24, 16, "kkkkkkk", mirror=True)
    c.stamp(26, 17, "kkk", mirror=True)
    c.stamp(26, 18, "kkkk", mirror=True)
    c.stamp(26, 19, "krrk", mirror=True)
    c.stamp(27, 20, "kk", mirror=True)
    c.put([(27, 19), (35, 19)], 'w')
    c.put([(31, 19), (32, 19), (31, 20), (32, 20), (31, 21), (32, 21)], 'b')
    c.stamp(29, 22, "kk", mirror=True)
    c.put2([(24, 22), (24, 23), (25, 24)], 'k')
    c.put([(x, 24) for x in range(29, 35)], 'b')
    c.stamp(27, 25, "kkkkkkkkkk")
    c.put2([(28, 26)], 'w')
    c.put2([(28, 27)], 'k')
    for pts in (((28, 9), (29, 8)), ((24, 11), (25, 10)), ((13, 24), (14, 25), (14, 26)), ((10, 32), (11, 33)),
                ((19, 36), (20, 37), (20, 38)), ((9, 41), (10, 42)), ((22, 46), (23, 47))):
        c.put2(list(pts), 'b')
    c.put2([(x, y) for x in (8, 11) for y in (54, 55, 56)], 'k')
    c.put2([(18, 58), (21, 58)], 'k')
    c.stamp(48, 49, """
...kk
..kgk
.kkkkk
krrrrrk
krwrrrk
krrrrrk
.krrrk
..kkk
""")


def finish_tiger(c, g):
    c.stamp(28, 12, "kkkkkkkk")
    c.stamp(31, 13, "kk")
    c.stamp(29, 14, "kkkkkk")
    c.stamp(31, 15, "kk")
    c.stamp(28, 16, "kkkkkkkk")
    for (x, y) in ((16, 18), (16, 21), (17, 24)):
        c.stamp(x, y, "kkk", mirror=True)
        c.stamp(x + 1, y + 1, "kk", mirror=True)
    c.stamp(20, 19, "wwwwww", mirror=True)
    c.stamp(21, 21, "kkkkk", mirror=True)
    c.stamp(21, 22, "kyykk", mirror=True)
    c.stamp(22, 23, "kkk", mirror=True)
    c.put([(22, 22), (39, 22)], 'w')
    c.stamp(29, 27, "pppppp")
    c.stamp(30, 28, "pppp")
    c.stamp(31, 29, "kk")
    c.stamp(31, 30, "kk")
    c.stamp(27, 31, "kkkk..kkkk")
    c.put2([(28, 32)], 'w')
    c.put2([(24, 29), (26, 30), (24, 31)], 'k')
    for (x, y) in ((17, 40), (16, 44), (17, 48), (21, 45), (22, 49)):
        c.put2([(x, y), (x + 1, y), (x + 2, y + 1)], 'k')
    c.put2([(21, 57), (24, 57)], 'k')
    for (x, y) in ((54, 47), (57, 41), (56, 52)):
        c.put([(x, y), (x + 1, y)], 'k')


def finish_lion(c, g):
    c.stamp(20, 16, "kkkkkkkk", mirror=True)
    c.stamp(21, 17, "kbbkkk", mirror=True)
    c.stamp(22, 19, ".kkkk", mirror=True)
    c.stamp(22, 20, "kwwwwk", mirror=True)
    c.stamp(22, 21, "kwrrrk", mirror=True)
    c.stamp(22, 22, "kwrrrk", mirror=True)
    c.stamp(22, 23, ".kkkk", mirror=True)
    c.put([(23, 21), (37, 21)], 'w')
    c.stamp(28, 24, "kkkkkkkk")
    c.stamp(28, 25, "kaabbbdk")
    c.stamp(29, 26, "kk..kk")
    c.put2([(27, 28), (29, 28), (27, 29)], 'w')
    for i in range(14):
        a = math.pi * 2 * i / 14 + math.pi / 14
        x, y = round(g.X(28 + 15 * math.cos(a))), round(g.Y(20 + 14 * math.sin(a)))
        c.put([(x - 1, y - 1), (x, y - 1), (x + 1, y), (x, y + 1)], 'd')
    c.put([(x, 41) for x in range(22, 42)], 'd')
    c.stamp(30, 42, "kkkk")
    c.stamp(30, 43, "kyyk")
    c.stamp(30, 44, "kkkk")
    for (x, y) in ((12, 56), (13, 59), (46, 58), (30, 57), (52, 60)):
        c.stamp(x, y, "mmm")
    for pts in (((20, 57), (21, 58), (21, 59)), ((40, 56), (41, 57))):
        c.put(list(pts), 'k')


def finish_jiangshi(c, g):
    c.stamp(28, 10, """
kkkkkkkk
kyyyyyyk
kyrrrryk
kyyryyyk
kyrrrryk
kyyyyryk
kyrrrryk
kyyyyyyk
kyrryryk
kyyyyyyk
kkkkkkkk
""")
    c.stamp(31, 0, "kk")
    c.stamp(30, 1, "krrk")
    c.put2([(26, 3), (27, 4), (27, 5), (28, 6)], 'r')
    c.stamp(22, 16, "kkkkk", mirror=True)
    c.stamp(22, 17, "kkerk", mirror=True)
    c.stamp(23, 18, "kkk", mirror=True)
    c.put([(24, 17), (39, 17)], 'w')
    c.put2([(23, 20), (24, 21), (25, 21)], 'k')
    c.put2([(27, 23)], 'w')
    c.put2([(27, 24)], 'k')
    c.put([(x, y) for y in (37, 41) for x in range(27, 37)], 'd')
    c.put([(29, 38), (30, 39), (33, 39), (34, 38)], 'd')
    c.put2([(2, 38), (4, 38), (2, 39), (4, 39)], 'w')


def finish_shanxiao(c, g):
    c.stamp(23, 17, "kkkkkkk", mirror=True)
    c.stamp(24, 18, "kkk", mirror=True)
    c.stamp(24, 19, "kyyk", mirror=True)
    c.stamp(25, 20, "kk", mirror=True)
    for y in range(18, 29):
        c.stamp(30, y, "rr", mirror=True)
    c.put2([(30, 17), (31, 17)], 'r')
    c.stamp(30, 29, "kr", mirror=True)
    for i, y in enumerate(range(21, 29)):
        c.stamp(23, y, ("BBkBB" if i % 2 == 0 else "BkBBk")[:5], mirror=True)
    c.stamp(26, 31, "kkkkkk", mirror=True)
    c.put2([(27, 32)], 'y')
    c.put2([(27, 33)], 'k')
    for pts in (((14, 14), (15, 13)), ((12, 20), (12, 21)), ((14, 27), (13, 28)), ((18, 40), (19, 41)),
                ((22, 46), (23, 47)), ((10, 43), (10, 44))):
        c.put2(list(pts), 'g')


def finish_fox(c, g):
    c.stamp(24, 20, "kk", mirror=True)
    c.stamp(25, 21, "krrk", mirror=True)
    c.stamp(26, 22, "kk", mirror=True)
    c.put([(26, 21), (37, 21)], 'w')
    c.put([(31, 16), (32, 16), (31, 17), (32, 17), (31, 18)], 'r')
    c.stamp(31, 26, "kk")
    c.put([(31, 26)], 'w')
    c.stamp(29, 28, "k....k")
    c.stamp(30, 29, "kkkk")
    c.put2([(26, 27), (25, 28)], 'k')
    c.put2([(21, 25), (22, 26), (20, 27)], 'b')


def finish_jiao(c, g):
    o = Off(c, 0)
    o.stamp(25, 13, "kkkk", mirror=True)
    o.stamp(26, 14, "krr", mirror=True)
    o.stamp(27, 15, "kk", mirror=True)
    o.stamp(29, 20, "k", mirror=True)
    o.stamp(26, 23, "kkkkk", mirror=True)
    o.stamp(27, 24, "e.e", mirror=True)
    o.stamp(25, 21, "kk", mirror=True)
    o.stamp(22, 22, "kkk", mirror=True)
    o.stamp(19, 23, "kkk", mirror=True)
    o.stamp(17, 24, "kk", mirror=True)
    for y in (30, 34, 38, 42, 46):
        o.stamp(29, y, "bbbbbb")
    for x in range(2, 62, 8):
        o.stamp(x, 50, "www")
        o.stamp(x + 1, 49, "w")
        if x + 5 < 62:
            o.stamp(x + 4, 52, "hh")
    for (x, y) in ((27, 33), (36, 33), (26, 38), (37, 38), (27, 43), (36, 43)):
        o.put([(x, y), (x + 1, y + 1), (x + 2, y)], 'd')
    o.put2([(17, 26), (15, 27), (13, 27), (11, 26)], 'e')
    o.put2([(21, 5), (20, 3)], 'k')
    o.put2([(24, 10), (23, 11)], 'a')
    o.put([(25, 14), (37, 14)], 'w')


def finish_crow(c, g):
    o = Off(c, 0)
    for (a, b) in (((22, 14), (6, 9)), ((21, 18), (4, 20)), ((21, 22), (8, 29)), ((22, 27), (13, 33))):
        for t in range(1, 12):
            x = round(a[0] + (b[0] - a[0]) * t / 12)
            y = round(a[1] + (b[1] - a[1]) * t / 12)
            if c.tone[y][x] not in '.k':
                o.paint(x, y, 'd')
                c.paint(63 - x, y, 'd')
    o.stamp(28, 13, "kk", mirror=True)
    o.stamp(28, 14, "kW", mirror=True)
    for (x, y) in ((28, 52), (31, 47), (24, 47)):
        if c.tone[y][x] not in '.k':
            c.stamp(x, y, "e", mirror=True)
    o.put2([(28, 14)], 'W')
    o.put2([(30, 19), (31, 20)], 'k')
    for (x, y) in ((4, 8), (2, 15), (5, 22), (9, 29)):
        o.put2([(x, y), (x + 1, y)], 'e')
    o.put2([(27, 45), (29, 45), (31, 46)], 'k')
    for (x, y) in ((16, 24), (12, 18), (19, 30), (24, 12)):
        o.put2([(x, y)], 'o')


def finish_toad(c, g):
    o = Off(c, 8)
    o.stamp(17, 9, """
..kkkk
.kooook
kooooook
kkkkkkkk
kooooook
.kooook
..kkkk
""", mirror=True)

    o.stamp(11, 26, "kk", mirror=True)
    o.stamp(13, 27, "kk", mirror=True)
    o.stamp(15, 28, "kkkkkkkkkkkkkkkkk", mirror=True)
    for (x, y) in ((14, 21), (20, 23), (26, 20), (10, 30), (44, 21), (49, 25), (38, 19), (53, 31), (30, 17)):
        o.stamp(x, y, "aa")
        o.stamp(x, y + 1, "bb")
    o.put2([(19, 11), (18, 12)], 'w')
    for y in (36, 38, 40):
        o.put([(x, y) for x in range(26, 38) if (x + y) % 3 == 0], 'b')
    o.put2([(14, 46), (17, 46), (6, 46), (9, 46)], 'k')
