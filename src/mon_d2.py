"""Monster designs, part 2: spirits, plants and things (see mon_designs.py for the slot letters)."""
from mondraw import Mat, flat
from mon_designs import design, BODY, BODY2, DARKB, WHITE

DD = flat('d')


# ================================================================ wisp 鬼火 (a ghost flame with a face)
@design('wisp', 40, 40, mirrored=True)
def wisp(c):
    outer = Mat('a', 'b', 'b')
    body = c.new_part()
    c.ellipse(20, 26, 12.5, 11.5, outer, body)
    c.poly2([(8, 24), (4, 9), (11, 17), (13, 5), (17, 12), (20, 1.5), (20, 20)], outer, body)
    c.reshade(body, 18, 22, 14, 14, outer, dw=1)
    core = c.new_part(sep=False)
    c.ellipse(20, 28, 8, 7.5, Mat('w', 'a', 'a'), core)
    c.poly2([(13, 26), (15, 17), (20, 11), (20, 26)], Mat('w', 'a', 'a'), core)
    c.reshade(core, 18, 25, 9, 10, Mat('w', 'a', 'a'), dw=1, hi=0.0)
    c.finish()
    c.stamp(15, 24, "kk", mirror=True)
    c.stamp(15, 25, "kk", mirror=True)
    c.stamp(15, 26, "kk", mirror=True)
    c.stamp(19, 31, "kk")
    return c


# ================================================================ paper effigy 紙人 (a stiff paper doll)
PAPER = Mat('a', 'a', 'd')


@design('paperghost', 40, 48, mirrored=True)
def paperghost(c):
    sleeve = c.new_part()
    c.poly2([(15, 17), (3, 20), (2.5, 27), (15, 25)], PAPER, sleeve)
    robe = c.new_part()
    c.poly2([(20, 15), (13, 16), (8.5, 41), (13, 46), (16.5, 42), (20, 46)], PAPER, robe)
    hem = c.new_part(sep=False)
    c.poly2([(9.5, 37), (20, 37), (20, 39.5), (9.2, 39.5)], flat('b'), hem)
    c.rect(18, 16, 21, 34, flat('b'), hem, shade='flat')
    hair = c.new_part()
    c.ellipse(20, 9.5, 8.5, 8, flat('d'), hair)
    c.rect(12, 9, 27, 17, flat('d'), hair, shade='flat')
    head = c.new_part(sep=False)
    c.ellipse(20, 12, 5.5, 5, PAPER, head)
    c.rect(15, 8, 24, 12, PAPER, head, shade='flat')
    c.finish()
    c.stamp(16, 11, "kk", mirror=True)
    c.stamp(15, 13, "r", mirror=True)
    c.stamp(19, 14, "bb")
    c.stamp(13, 9, "k", mirror=True)
    c.stamp(13, 13, "k", mirror=True)
    c.stamp(19, 3, "kk")
    c.stamp(19, 4, "kk")
    for y in range(21, 34, 4):
        c.stamp(11, y, "d", mirror=True)
    return c


# ================================================================ tree sprite 樹精 (a walking little tree)
LEAF = Mat('e', 'f', 'b')
BARK = Mat('f', 'b', 'd')


@design('treesprite', 40, 48, mirrored=True)
def treesprite(c):
    arm = c.new_part()
    c.capsule2(14, 28, 6, 22, 1.6, BARK, arm)
    c.capsule2(6, 22, 4.5, 17, 1.3, BARK, arm)
    trunk = c.new_part()
    c.poly2([(20, 20), (14, 20), (12.5, 40), (8, 46), (14, 45), (17, 42), (20, 44)], BARK, trunk)
    c.reshade(trunk, 17, 26, 8, 16, BARK)
    tuft = c.new_part()
    c.ellipse2(4.5, 14, 3.5, 3.0, LEAF, tuft)
    crown = c.new_part()
    for (x, y, rx, ry) in ((20, 9, 9, 7), (11.5, 12.5, 7, 6), (14, 5.5, 6.5, 4.5), (20, 15, 11, 5)):
        c.ellipse2(x, y, rx, ry, LEAF, crown)
    c.reshade(crown, 15, 8, 17, 12, LEAF, dw=2)
    c.finish()
    c.stamp(15, 28, "kkk", mirror=True)
    c.stamp(15, 29, "kyk", mirror=True)
    c.stamp(16, 30, "k", mirror=True)
    c.stamp(18, 34, "kkkk")
    c.stamp(17, 23, "d", mirror=True)
    c.stamp(19, 38, "d")
    return c


# ================================================================ poison mushroom 毒菇妖 (an ink-cap spirit)
CAP = BODY
STEM = Mat('e', 'e', 'f')


@design('mushroom', 40, 44, mirrored=True)
def mushroom(c):
    feet = c.new_part()
    c.ellipse2(14, 40.5, 4.5, 2.5, STEM, feet)
    arms = c.new_part()
    c.capsule2(14, 25, 8, 31, 1.8, STEM, arms)
    stem = c.new_part()
    c.poly2([(20, 16), (13, 17), (11.5, 36), (14, 40), (20, 40.5)], STEM, stem)
    c.reshade(stem, 17, 24, 9, 15, STEM)
    gill = c.new_part()
    c.poly2([(20, 15), (5, 15), (8, 18.5), (11, 17), (14, 19), (16.5, 17), (20, 19)], flat('f'), gill)
    cap = c.new_part()
    c.poly2([(20, 1.5), (15, 2), (10, 5), (5.5, 10), (3.5, 14), (3.5, 16), (20, 16)], CAP, cap)
    c.reshade(cap, 15, 7, 14, 11, CAP, dw=2)
    c.finish()
    for x in (9, 14):
        for y in range(6 if x == 14 else 9, 15):
            if c.tone[y][x] != 'k':
                c.paint(x, y, 'd')
                c.paint(39 - x, y, 'd')
    c.stamp(15, 23, "kkk", mirror=True)
    c.stamp(16, 24, "y", mirror=True)
    c.stamp(16, 28, "kkkkkkkk")
    c.stamp(17, 29, "e.e.e.")
    c.stamp(17, 30, "kkkkkk")
    return c


# ================================================================ ink spirit 墨靈 (a drop of living ink)
INK = Mat('b', 'b', 'd')


@design('inkblot', 40, 40, mirrored=True)
def inkblot(c):
    body = c.new_part()
    c.ellipse(20, 23, 15, 12.5, INK, body)
    c.poly2([(20, 1.5), (13, 13), (20, 12)], INK, body)
    for (x, y1, r) in ((9, 35, 2.0), (15, 36.5, 2.2)):
        c.capsule2(x, 28, x, y1, r, INK, body)
    c.capsule(20, 30, 20, 36, 2.0, INK, body)
    c.reshade(body, 16, 18, 15, 14, Mat('w', 'b', 'd'), dw=2, hi=0.96)
    eyes = c.new_part()
    c.ellipse2(14.5, 21.5, 3.5, 4.5, WHITE, eyes)
    c.finish()
    c.stamp(15, 21, "k", mirror=True)
    c.stamp(15, 22, "k", mirror=True)
    c.stamp(16, 21, "k", mirror=True)
    c.stamp(16, 22, "k", mirror=True)
    c.stamp(18, 29, "kkkk")
    return c


# ================================================================ wind sprite 風精 (a little whirlwind with a face)
GUST = Mat('w', 'a', 'b')


@design('windsprite', 40, 40)
def windsprite(c):
    bands = [(36.5, 23, 3.0, 2.0), (32.5, 21, 5.5, 2.4), (27.5, 18.5, 8.5, 3.0), (21.5, 18, 12, 3.6),
             (11, 20, 16.5, 7.5)]
    for (y, x, rx, ry) in bands:
        c.ellipse(x, y, rx, ry, GUST)
    c.finish()
    c.stamp(13, 9, "kk.......kk")
    c.stamp(13, 10, "kk.......kk")
    c.stamp(13, 11, "kk.......kk")
    c.stamp(18, 14, "kkk")
    c.stamp(8, 6, "aaaa")
    c.stamp(28, 15, "bbbbb")
    return c


# ================================================================ stone toad 石蟾 (a squat toad of stone)
@design('stonetoad', 48, 40, mirrored=True)
def stonetoad(c):
    legs = c.new_part()
    c.capsule2(10, 28, 6, 35, 3.0, BODY, legs)
    c.ellipse2(6, 36.5, 5, 2.4, BODY, legs)
    body = c.new_part()
    c.ellipse(24, 25, 20, 11.5, BODY, body)
    c.ellipse(24, 18, 15, 9, BODY, body)
    c.reshade(body, 20, 19, 20, 14, BODY, dw=2)
    eyes = c.new_part()
    c.ellipse2(14, 10.5, 6, 5.5, BODY, eyes)
    c.finish()
    c.stamp(12, 9, "kkk", mirror=True)
    c.stamp(12, 10, "kkk", mirror=True)
    c.stamp(13, 8, "w", mirror=True)
    c.stamp(9, 24, "kk", mirror=True)
    c.stamp(11, 25, "kkkkkkkkkkkkk", mirror=True)
    c.stamp(22, 15, "yy")
    c.stamp(22, 16, "yy")
    for (x, y) in ((14, 31), (17, 30), (9, 29), (30, 31), (33, 30), (38, 29), (24, 32)):
        c.stamp(x, y, "dd")
    return c


# ================================================================ wooden dummy 木人樁 (a training dummy come alive)
WOOD = BODY


@design('dummy', 40, 48, mirrored=True)
def dummy(c):
    base = c.new_part()
    c.rect(7, 42, 32, 45, DARKB, base)
    arms = c.new_part()
    c.capsule2(15, 15, 4, 9, 2.2, WOOD, arms)
    c.capsule2(15, 26, 4, 28, 2.2, WOOD, arms)
    post = c.new_part()
    c.capsule(20, 8, 20, 39, 7.0, WOOD, post)
    c.reshade(post, 17, 14, 8, 30, WOOD, dw=2)
    c.finish()
    for y in (19, 32):
        for x in range(13, 27):
            if c.tone[y][x] != 'k':
                c.paint(x, y, 'd')
    c.stamp(15, 9, "kkk", mirror=True)
    c.stamp(15, 10, "krk", mirror=True)
    c.stamp(15, 11, "kkk", mirror=True)
    c.stamp(17, 14, "kkkkkk")
    return c
