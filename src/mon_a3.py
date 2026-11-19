"""Monster designs (second version), part 3: spirits, plants and things, finished by hand."""
import math

from mondraw import Mat, flat
from mon_designs import design, BODY, DARKB

DD = flat('d')
KK = flat('k')


# ================================================================ wisp 鬼火 (a ghost flame with a face)
OUTER = Mat('a', 'b', 'b')
CORE = Mat('w', 'a', 'a')


@design('wisp', 48, 48, mirrored=True)
def wisp(c):
    body = c.new_part()
    c.ellipse(24, 32, 15, 13.5, OUTER, body)
    c.poly2([(10, 30), (4, 12), (12, 21), (13, 6), (19, 15), (21, 4), (24, 1.5), (24, 24)], OUTER, body)
    c.reshade(body, 21, 27, 17, 17, OUTER, dw=1)
    core = c.new_part(sep=False)
    c.ellipse(24, 33, 10, 9.5, CORE, core)
    c.poly2([(15, 32), (17, 21), (22, 14), (24, 12), (24, 32)], CORE, core)
    c.reshade(core, 22, 30, 11, 12, CORE, dw=1, hi=0.0)
    c.finish()
    c.put2([(16, 9), (17, 12), (11, 16), (12, 19), (21, 8)], 'a')
    c.stamp(17, 30, "kkk", mirror=True)
    c.stamp(17, 31, "kwk", mirror=True)
    c.stamp(17, 32, "kkk", mirror=True)
    c.stamp(17, 33, ".k.", mirror=True)
    c.put2([(15, 28), (16, 27), (17, 27)], 'b')
    c.stamp(22, 36, ".kk.")
    c.stamp(22, 37, "kbbk")
    c.stamp(22, 38, ".kk.")
    c.put2([(14, 35), (15, 35)], 'b')
    return c


# ================================================================ paper effigy 紙人 (a stiff paper doll)
PAPER = Mat('a', 'a', 'd')


@design('paperghost', 48, 56, mirrored=True)
def paperghost(c):
    sleeve = c.new_part()
    c.poly2([(18, 21), (3, 24), (2, 33), (4.5, 31.5), (6.5, 34), (9, 31.5), (11, 33.5), (18, 31)], PAPER, sleeve)
    robe = c.new_part()
    c.poly2([(24, 19), (16, 20), (10, 49), (13, 54), (16.5, 50), (20, 54), (24, 50)], PAPER, robe)
    sash = c.new_part(sep=False)
    c.poly2([(10.6, 44), (24, 44), (24, 47), (10.2, 47)], flat('b'), sash)
    c.rect(22, 20, 25, 41, flat('b'), sash, shade='flat')
    hair = c.new_part()
    c.ellipse(24, 11, 10, 9.5, flat('h'), hair)
    c.rect(14, 10, 33, 21, flat('h'), hair, shade='flat')
    head = c.new_part(sep=False)
    c.ellipse(24, 14, 7, 6.2, PAPER, head)
    c.rect(18, 9, 29, 14, PAPER, head, shade='flat')
    c.finish()
    for x in (16, 19, 28, 31):
        for y in range(4 if x in (19, 28) else 8, 21):
            if c.part[y][x] == hair and c.tone[y][x] == 'h' and y % 5 != 0:
                c.paint(x, y, 'k')
    c.put([(x, 9) for x in range(18, 30)], 'k')
    c.put2([(18, 13), (19, 12), (20, 12), (21, 13)], 'k')
    c.put2([(18, 15), (19, 15)], 'r')
    c.put([(23, 17), (24, 17)], 'b')
    c.put([(22, 1), (23, 1), (24, 1), (25, 1)], 'b')
    c.put2([(13, 25), (14, 26), (15, 27), (12, 36), (13, 38), (14, 40)], 'd')
    c.put2([(6, 26), (9, 25)], 'd')
    c.put2([(19, 22), (20, 23), (19, 28), (20, 29)], 'd')
    return c


# ================================================================ tree sprite 樹精 (a walking little tree)
LEAF = Mat('e', 'f', 'b')
BARK = Mat('f', 'b', 'd')


@design('treesprite', 48, 56, mirrored=True)
def treesprite(c):
    arm = c.new_part()
    c.capsule2(17, 33, 8, 27, 1.9, BARK, arm)
    c.capsule2(8, 27, 5, 20, 1.5, BARK, arm)
    c.capsule2(8, 27, 3, 28, 1.2, BARK, arm)
    trunk = c.new_part()
    c.poly2([(24, 24), (17, 24), (15, 46), (9, 54), (16, 53), (19.5, 49), (24, 52)], BARK, trunk)
    c.reshade(trunk, 20, 32, 10, 18, BARK)
    tuft = c.new_part()
    c.ellipse2(5, 18, 4, 3.4, LEAF, tuft)
    crown = c.new_part()
    for (x, y, rx, ry) in ((24, 11, 10.5, 8), (14, 15, 8, 6.8), (16.5, 6.5, 7.5, 5.5), (24, 18.5, 13, 6)):
        c.ellipse2(x, y, rx, ry, LEAF, crown)
    c.reshade(crown, 18, 9, 20, 14, LEAF, dw=2)
    c.finish()
    for (x, y) in ((12, 12), (19, 5), (24, 9), (9, 17), (30, 14)):
        c.put2([(x, y), (x + 1, y), (x, y + 1)], 'e')
    c.put2([(14, 18), (15, 19), (21, 15), (22, 16)], 'b')
    for x in (19, 22):
        for y in range(26, 50, 1):
            if c.part[y][x] == trunk and c.tone[y][x] in 'fb' and (y // 3) % 3 != 0:
                c.paint(x + ((y // 6) % 2), y, 'd')
                c.paint(47 - x - ((y // 6) % 2), y, 'd')
    c.stamp(18, 31, ".kkk", mirror=True)
    c.stamp(18, 32, "kkyk", mirror=True)
    c.stamp(18, 33, ".kk.", mirror=True)
    c.stamp(21, 38, ".kkkk")
    c.stamp(21, 39, "kddddk")
    c.stamp(21, 40, ".kkkk")
    c.put2([(17, 29), (18, 28), (19, 28)], 'd')
    return c


# ================================================================ poison mushroom 毒菇妖 (an ink-cap spirit)
CAP = BODY
STEM = Mat('e', 'e', 'f')


@design('mushroom', 48, 48, mirrored=True)
def mushroom(c):
    feet = c.new_part()
    c.ellipse2(17, 44.5, 5, 2.5, STEM, feet)
    arms = c.new_part()
    c.capsule2(17, 28, 10, 34, 2.0, STEM, arms)
    c.ellipse2(9, 35, 2.2, 2.0, STEM, arms)
    stem = c.new_part()
    c.poly2([(24, 17), (16, 18), (14.5, 40), (17, 44), (24, 44.5)], STEM, stem)
    c.reshade(stem, 21, 26, 10, 16, STEM)
    gill = c.new_part()
    c.poly2([(24, 15), (6, 15), (9, 19), (12, 17.5), (15, 20), (18, 18), (21, 20.5), (24, 18.5)], flat('f'), gill)
    cap = c.new_part()
    c.poly2([(24, 1.5), (18, 2), (12, 5.5), (7, 10.5), (4.5, 14), (4.5, 16), (24, 16)], CAP, cap)
    c.reshade(cap, 18, 6, 16, 11, CAP, dw=2)
    c.finish()
    for x in (10, 15, 20):
        for y in range({10: 9, 15: 5, 20: 3}[x], 15):
            if c.tone[y][x] != 'k':
                c.paint(x, y, 'd')
                c.paint(47 - x, y, 'd')
    c.put2([(13, 6), (14, 5), (17, 3), (8, 10)], 'a')
    c.put2([(10, 17), (16, 19)], 'd')
    c.stamp(16, 22, "kk", mirror=True)
    c.stamp(17, 23, ".kk", mirror=True)
    c.stamp(18, 24, "kk", mirror=True)
    c.stamp(19, 25, "kk", mirror=True)
    c.stamp(19, 26, "ky", mirror=True)
    c.stamp(19, 31, "kkkkkkkkkk")
    c.stamp(20, 32, "e.e.e.e.")
    c.stamp(20, 33, "kkkkkkkk")
    c.put2([(17, 37), (18, 38), (16, 40)], 'f')
    c.put2([(7, 16), (7, 17)], 'f')
    return c


# ================================================================ ink spirit 墨靈 (a drop of living ink)
INK = Mat('b', 'b', 'd')


@design('inkblot', 48, 48, mirrored=True)
def inkblot(c):
    body = c.new_part()
    c.ellipse(24, 27, 17, 14, INK, body)
    c.poly2([(24, 1.5), (16, 15), (24, 14)], INK, body)
    for (x, y1, r) in ((11, 42, 2.2), (18, 44, 2.4)):
        c.capsule2(x, 33, x, y1, r, INK, body)
    c.capsule(24, 35, 24, 42, 2.2, INK, body)
    c.reshade(body, 19, 21, 17, 16, Mat('w', 'b', 'd'), dw=2, hi=0.97)
    drop = c.new_part()
    c.ellipse2(4, 18, 2.2, 2.4, INK, drop)
    c.ellipse2(7, 9, 1.8, 2, INK, drop)
    eyes = c.new_part()
    c.ellipse2(17.5, 25, 4.2, 5.2, flat('w'), eyes)
    c.finish()
    c.stamp(18, 24, "kk", mirror=True)
    c.stamp(18, 25, "kk", mirror=True)
    c.stamp(18, 26, "kk", mirror=True)
    c.put2([(19, 24)], 'w')
    c.stamp(21, 33, "k....k")
    c.stamp(22, 34, "kkkk")
    c.put2([(13, 9), (14, 8), (12, 11)], 'w')
    return c


# ================================================================ wind sprite 風精 (a little whirlwind with a face)
GUST = Mat('w', 'a', 'b')


@design('windsprite', 48, 48)
def windsprite(c):
    bands = [(44, 27, 3.4, 2.2), (39.5, 25.5, 6.5, 2.6), (34, 23, 10, 3.2), (27.5, 22, 14, 3.8), (14.5, 24, 19.5, 9)]
    parts = []
    for (y, x, rx, ry) in bands:
        parts.append(c.ellipse(x, y, rx, ry, GUST))
    leaf = c.new_part()
    c.ellipse(5, 33, 2.2, 1.4, flat('b'), leaf)
    c.ellipse(43, 40, 2.2, 1.4, flat('b'), leaf)
    c.finish()
    c.stamp(15, 11, "kkk........kkk")
    c.stamp(15, 12, "kwk........kwk")
    c.stamp(15, 13, "kkk........kkk")
    c.stamp(21, 17, "kk..kk")
    c.stamp(23, 18, "kk")
    c.put([(13, 15), (14, 15), (33, 15), (34, 15)], 'b')
    for (y, x, rx, ry), p in zip(bands, parts):
        c.put([(int(x - rx * 0.5) + i, int(y - ry * 0.3)) for i in range(int(rx * 0.6))], 'w')
        c.put([(int(x + rx * 0.2) + i, int(y + ry * 0.4)) for i in range(int(rx * 0.5))], 'b')
    return c


# ================================================================ stone toad 石蟾 (a squat toad of stone)
@design('stonetoad', 48, 48, mirrored=True)
def stonetoad(c):
    legs = c.new_part()
    c.capsule2(10, 35, 6, 42, 3.4, BODY, legs)
    c.ellipse2(6.5, 43.5, 5.2, 2.6, BODY, legs)
    body = c.new_part()
    c.ellipse(24, 31, 21, 13, BODY, body)
    c.ellipse(24, 23, 16, 10, BODY, body)
    c.reshade(body, 20, 24, 21, 16, BODY, dw=2)
    eyes = c.new_part()
    c.ellipse2(14, 14, 6.5, 6, BODY, eyes)
    c.finish()
    c.stamp(11, 12, "kkkkk", mirror=True)
    c.stamp(11, 13, "kwyyk", mirror=True)
    c.stamp(11, 14, "kkkkk", mirror=True)
    c.put2([(10, 11), (11, 10), (12, 10)], 'd')
    c.put2([(11, 9), (12, 9)], 'a')
    c.stamp(8, 30, "kk", mirror=True)
    c.stamp(10, 31, "kkkkkkkkkkkkkk", mirror=True)
    c.stamp(23, 20, "kk")
    c.stamp(22, 21, "kyyk")
    c.stamp(22, 22, "kyyk")
    c.stamp(23, 23, "kk")
    c.put([(23, 21)], 'w')
    for pts in (((14, 24), (15, 25), (15, 26), (16, 27)), ((32, 22), (31, 23), (31, 24)),
                ((19, 37), (20, 38), (21, 38)), ((30, 36), (29, 37)), ((38, 28), (39, 29))):
        c.put(list(pts), 'k')
    for (x, y) in ((10, 22), (16, 19), (35, 20), (40, 26), (27, 27), (12, 36), (36, 37)):
        c.put([(x, y), (x + 1, y)], 'a')
        c.put([(x, y + 1), (x + 1, y + 1)], 'd')
    return c


# ================================================================ wooden dummy 木人樁 (a training dummy come alive)
WOOD = BODY


@design('dummy', 48, 56, mirrored=True)
def dummy(c):
    base = c.new_part()
    c.rect(8, 50, 39, 53, DARKB, base)
    arms = c.new_part()
    c.capsule2(19, 17, 5, 10, 2.5, WOOD, arms)
    c.capsule2(19, 30, 5, 32, 2.5, WOOD, arms)
    post = c.new_part()
    c.capsule(24, 9, 24, 46, 8.0, WOOD, post)
    c.reshade(post, 21, 16, 9, 34, WOOD, dw=2)
    c.finish()
    for y in (22, 37):
        for x in range(15, 34):
            if c.part[y][x] == post and c.tone[y][x] != 'k':
                c.paint(x, y, 'k')
                c.paint(x, y + 1, 'd')
    for (x, y0, y1) in ((20, 25, 35), (27, 40, 47), (21, 41, 46)):
        c.put([(x, y) for y in range(y0, y1)], 'd')
    c.stamp(18, 10, ".kkk", mirror=True)
    c.stamp(18, 11, "kkrk", mirror=True)
    c.stamp(18, 12, ".kkk", mirror=True)
    c.put2([(21, 11)], 'w')
    c.stamp(20, 15, "kkkkkkkk")
    c.stamp(21, 16, "dddddd")
    c.put2([(17, 8), (18, 7), (19, 7)], 'd')
    for (x, y) in ((12, 52), (35, 52)):
        c.put([(x, y)], 'w')
    c.put2([(6, 9), (6, 31)], 'd')
    return c
