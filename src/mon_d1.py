"""Monster designs, part 1: the animals and bugs (see mon_designs.py for the slot letters)."""
from mondraw import Mat, flat
from mon_designs import design, BODY, DARKB, WHITE

TUSK = Mat('w', 'w', 'a')
FACE = Mat('a', 'a', 'b')
WING = Mat('a', 'a', 'a')
DD = flat('d')


# ================================================================ boar (side, facing left)
@design('boar', 48, 40)
def boar(c):
    far = c.new_part()
    c.capsule(19, 27, 19, 35, 2.4, DARKB, far)
    c.capsule(35, 27, 36, 35, 2.4, DARKB, far)
    c.capsule(43, 17, 45.5, 22, 1.2, DARKB)
    legs = c.new_part()
    c.capsule(13, 27, 13, 35, 2.8, BODY, legs)
    c.capsule(40, 27, 41, 35, 2.8, BODY, legs)
    hoof = c.new_part()
    for x in (13, 41, 19, 36):
        c.rect(x - 3, 36, x + 2, 37, DD, hoof)
    body = c.new_part()
    c.ellipse(29, 20, 16, 10.5, BODY, body)
    c.ellipse(19, 17, 10, 10, BODY, body)
    c.reshade(body, 26, 16, 18, 12, BODY)
    mane = c.new_part()
    c.poly([(11, 10), (13, 4), (16, 8), (19, 3), (22, 7), (25, 4), (28, 8), (31, 6), (34, 10), (37, 10), (36, 13),
            (14, 13)], DARKB, mane)
    head = c.new_part()
    c.ellipse(11, 20, 8, 7.5, BODY, head)
    c.poly([(1.5, 16), (7, 15), (8, 27), (2, 26)], BODY, head)
    c.reshade(head, 10, 18, 9, 8, BODY, dw=1)
    snout = c.new_part()
    c.ellipse(3, 21, 1.6, 3.6, Mat('b', 'b', 'b'), snout)
    ear = c.new_part()
    c.poly([(10, 13), (14, 8), (17, 15)], DARKB, ear)
    tusk = c.new_part()
    c.stamp(3, 22, """
.w
.w
ww
w.
""", tusk)
    c.finish()
    c.paint(9, 18, 'r')
    c.paint(10, 18, 'k')
    for x in (8, 9, 10):
        c.paint(x, 17, 'k')
    c.paint(2, 20, 'd')
    c.paint(2, 22, 'd')
    return c


# ================================================================ snake (coiled, facing the viewer)
def _arc(cx, cy, rx, ry, a0, a1, n=12):
    import math
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


@design('snake', 44, 44, mirrored=True)
def snake(c):
    import math
    rings = [(22, 36, 15.5, 3.4, 3.5), (22, 30, 12, 3.0, 3.2), (22, 25, 8.5, 2.6, 2.9)]
    for (cx, cy, rx, ry, r) in rings:
        c.tube(_arc(cx, cy, rx, ry, math.pi, 2 * math.pi), r, BODY)
    neck = c.new_part()
    c.capsule(22, 25, 22, 13, 4.0, BODY, neck, r1=3.6)
    for (cx, cy, rx, ry, r) in rings:
        c.tube(_arc(cx, cy, rx, ry, 0, math.pi), r, BODY)
    head = c.new_part()
    c.poly([(12, 8), (16, 3), (28, 3), (32, 8), (30, 13), (26, 16), (18, 16), (14, 13)], BODY, head)
    c.reshade(head, 19, 6, 12, 9, BODY, dw=1)
    c.finish()
    c.paint2(17, 7, 'k')
    c.paint2(18, 7, 'y')
    c.paint2(17, 8, 'y')
    c.paint2(18, 8, 'k')
    c.paint2(20, 12, 'k')
    for y in (18, 20, 22):
        for x in (20, 21, 22, 23):
            if c.tone[y][x] != 'k':
                c.paint(x, y, 'a')
    c.stamp(21, 17, "rr")
    return c


# ================================================================ bat (front, wings spread)
@design('bat', 48, 40, mirrored=True)
def bat(c):
    wing = c.new_part()
    c.poly2([(21, 14), (14, 7), (6, 4), (1, 9), (1.5, 24), (5, 21), (8.5, 26), (12, 22), (16, 27), (21, 23)],
            Mat('b', 'b', 'd'), wing)
    for (x1, y1) in ((6, 5), (2, 22), (8.5, 24.5), (16, 25.5)):
        c.capsule2(19, 15, x1, y1, 0.6, DD, wing)
    body = c.new_part()
    c.ellipse(24, 21, 6.5, 8.5, BODY, body)
    c.capsule2(22, 28, 21.5, 33, 1.2, BODY, body)
    head = c.new_part()
    c.ellipse(24, 12, 6.5, 5.5, BODY, head)
    c.poly2([(18, 11), (17, 2), (22.5, 8)], BODY, head)
    c.reshade(head, 22, 10, 7, 7, BODY, dw=1)
    c.finish()
    c.paint2(20, 11, 'r')
    c.paint2(21, 11, 'r')
    c.paint2(21, 12, 'k')
    c.paint2(22, 15, 'w')
    c.paint2(23, 14, 'k')
    return c


# ================================================================ crab (front, claws raised)
@design('crab', 48, 40, mirrored=True)
def crab(c):
    legs = c.new_part()
    for (a, b, d) in (((15, 24), (6, 25), (2.5, 31)), ((16, 27), (8, 30), (6, 36.5)), ((18, 29), (13, 33), (12, 38))):
        c.capsule2(a[0], a[1], b[0], b[1], 1.5, DARKB, legs)
        c.capsule2(b[0], b[1], d[0], d[1], 1.5, DARKB, legs, r1=1.0)
    arm = c.new_part()
    c.capsule2(14, 22, 9, 15, 2.2, BODY, arm)
    claw = c.new_part()
    c.ellipse2(8, 9, 6.5, 6, BODY, claw)
    c.cut([(3.5, 1.5), (7, 9.5), (9, 9.5), (8.5, 1.5)], m=True)
    stalk = c.new_part()
    c.capsule2(20, 18, 19.5, 11, 1.0, BODY, stalk)
    body = c.new_part()
    c.ellipse(24, 24, 14, 8.5, BODY, body)
    c.ellipse(24, 21, 11, 6, BODY, body)
    c.reshade(body, 21, 19, 15, 10, BODY)
    eyes = c.new_part()
    c.ellipse2(19.5, 10, 2.2, 2.2, WHITE, eyes)
    c.finish()
    c.paint2(19, 10, 'k')
    for x in range(21, 27):
        c.paint(x, 27, 'd')
    c.paint2(20, 26, 'd')
    return c


# ================================================================ monkey (front, sitting up)
@design('monkey', 40, 44, mirrored=True)
def monkey(c):
    tail = c.new_part()
    c.capsule(29, 36, 35, 34, 1.6, DARKB, tail)
    c.capsule(35, 34, 37, 27, 1.6, DARKB, tail)
    c.capsule(37, 27, 34, 23, 1.6, DARKB, tail)
    legs = c.new_part()
    c.capsule2(15, 33, 13.5, 39, 3.2, BODY, legs)
    c.ellipse2(12.5, 41, 4, 2.2, BODY, legs)
    body = c.new_part()
    c.ellipse(20, 30, 9, 9, BODY, body)
    c.ellipse(20, 31.5, 5, 6, FACE, body)
    arms = c.new_part()
    c.capsule2(12, 24, 8, 33, 2.6, BODY, arms)
    c.ellipse2(8, 35, 2.8, 2.6, FACE, arms)
    ears = c.new_part()
    c.ellipse2(9.5, 14, 3.4, 3.8, BODY, ears)
    c.ellipse2(9.8, 14.2, 1.6, 2.2, flat('b'), ears)
    head = c.new_part()
    c.ellipse(20, 13, 10, 9.5, BODY, head)
    c.reshade(head, 18, 11, 11, 10, BODY, dw=1)
    face = c.new_part(sep=False)
    c.ellipse2(16.5, 13.5, 4, 4.2, FACE, face)
    c.ellipse(20, 18.5, 6.5, 4.2, FACE, face)
    c.finish()
    c.paint2(16, 13, 'k')
    c.paint2(16, 14, 'k')
    c.paint2(19, 18, 'b')
    c.stamp(17, 20, ".kkkkk")
    return c


# ================================================================ hornet (front, wings up)
@design('hornet', 44, 40, mirrored=True)
def hornet(c):
    wing = c.new_part()
    c.poly2([(19, 13), (11, 2), (3, 2.5), (2, 9), (15, 17)], WING, wing)
    legs = c.new_part()
    c.capsule2(18, 20, 12, 26, 1.0, DD, legs)
    c.capsule2(12, 26, 11, 31, 1.0, DD, legs)
    c.capsule2(19, 23, 15, 31, 1.0, DD, legs)
    ant = c.new_part()
    c.capsule2(20, 6, 15, 1.8, 0.7, DD, ant)
    abd = c.new_part()
    c.ellipse(22, 28, 7.5, 9, BODY, abd)
    c.poly([(19.5, 35), (24.5, 35), (22, 39.6)], BODY, abd)
    th = c.new_part()
    c.ellipse(22, 18, 6, 4.5, Mat('b', 'd', 'd'), th)
    head = c.new_part()
    c.ellipse(22, 10.5, 6.5, 5, BODY, head)
    eyes = c.new_part()
    c.ellipse2(18, 10, 2.2, 3.0, Mat('a', 'd', 'd', hi=0.85), eyes)
    c.finish()
    for y in (24, 25, 30, 31):
        for x in range(14, 31):
            if c.part[y][x] == abd and c.tone[y][x] != 'k':
                c.paint(x, y, 'd')
    c.stamp(20, 14, "d..d")
    return c


# ================================================================ centipede (rearing up, facing the viewer)
@design('centipede', 44, 44, mirrored=True)
def centipede(c):
    segs = [(39, 9.5, 3.6), (34, 8.8, 3.4), (29, 8.0, 3.2), (24.5, 7.2, 3.0), (20.5, 6.5, 2.8)]
    for (y, rx, ry) in segs:
        legs = c.new_part()
        c.capsule2(22 - rx + 1, y, 22 - rx - 4, y - 1.5, 0.9, DD, legs)
        c.capsule2(22 - rx - 4, y - 1.5, 22 - rx - 6, y + 2.5, 0.9, DD, legs)
    for (y, rx, ry) in segs:
        c.ellipse(22, y, rx, ry, BODY)
    ant = c.new_part()
    c.capsule2(19, 9, 12, 1.5, 0.7, DD, ant)
    head = c.new_part()
    c.ellipse(22, 12, 7, 5.5, BODY, head)
    jaw = c.new_part()
    c.poly2([(17.5, 14), (14.5, 18), (16.5, 20.5), (18.5, 17.5), (20.5, 16)], Mat('a', 'a', 'b'), jaw)
    c.finish()
    c.paint2(18, 11, 'y')
    c.paint2(19, 11, 'k')
    return c


# ================================================================ scorpion (front, tail over the head)
@design('scorpion', 48, 40)
def scorpion(c):
    legs = c.new_part()
    for (a, b, d) in (((19, 30), (11, 31), (8, 36.5)), ((20, 32), (14, 35), (13, 38)), ((18, 28), (10, 27), (5, 33))):
        c.capsule2(a[0], a[1], b[0], b[1], 1.3, DARKB, legs)
        c.capsule2(b[0], b[1], d[0], d[1], 1.3, DARKB, legs, r1=0.9)
    tail = c.new_part()
    for (x, y, r) in ((24, 24, 3.4), (26, 19, 3.2), (29, 14.5, 3.0), (31, 9.5, 2.8), (29, 5, 2.6), (25, 3.5, 2.4)):
        c.ellipse(x, y, r, r, BODY, tail)
    sting = c.new_part()
    c.poly([(23.5, 1.5), (20, 3), (20.5, 7.5), (23.5, 5.5)], Mat('a', 'a', 'b'), sting)
    arm = c.new_part()
    c.capsule2(16, 29, 9, 25, 2.0, BODY, arm)
    claw = c.new_part()
    c.ellipse2(6.5, 21, 6, 5, BODY, claw)
    c.cut([(1.5, 14), (5.5, 21.5), (7.5, 21.5), (6.5, 14)], m=True)
    body = c.new_part()
    c.ellipse(24, 29, 9.5, 7, BODY, body)
    c.reshade(body, 22, 27, 10, 8, BODY)
    c.finish()
    c.paint2(22, 30, 'k')
    c.paint2(21, 30, 'r')
    return c
