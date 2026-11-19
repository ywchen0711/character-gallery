"""Monster designs (second version), part 1: the animals, 48x48, finished by hand to the level of the people
portraits: faces with eye glints, brows, fangs and noses; fur tufts, bristles and scales in clean clusters; rim
light along the lit edges; claws, whiskers and other small details. Slots: see mon_designs.py.
"""
import math

from mondraw import Mat, flat
from mon_designs import design, BODY, DARKB

DD = flat('d')
KK = flat('k')
FUR_TICKS = """
......
..d...
...d..
......
.....d
....d.
"""


# ================================================================ wolf (side, snarling, tail up)
@design('wolf', 48, 48)
def wolf(c):
    far = c.new_part()
    c.capsule(18, 31, 16.5, 43, 2.0, DARKB, far)
    c.ellipse(15.5, 44.5, 2.8, 1.6, DARKB, far)
    c.capsule(34, 31, 36.5, 43, 2.0, DARKB, far)
    c.ellipse(37, 44.5, 2.8, 1.6, DARKB, far)
    ear2 = c.new_part()
    c.poly([(14, 10), (18, 2), (20.5, 11)], DARKB, ear2)
    tail = c.new_part()
    c.tube([(37, 24), (41.5, 21), (44, 15), (43, 8)], 3.6, BODY, tail, r1=2.6)
    c.poly([(40.5, 10), (41.5, 3), (43.5, 6.5), (45.5, 3.5), (45.5, 11)], BODY, tail)
    legs = c.new_part()
    c.capsule(14.5, 30, 12.5, 43, 2.5, BODY, legs, r1=2.0)
    c.ellipse(12, 44.5, 3.4, 1.8, BODY, legs)
    c.ellipse(38.5, 28, 5, 6.5, BODY, legs)
    c.capsule(40, 31, 42, 43, 2.3, BODY, legs, r1=1.9)
    c.ellipse(42.5, 44.5, 3.4, 1.8, BODY, legs)
    body = c.new_part()
    c.ellipse(27, 25, 12.5, 7.5, BODY, body)
    c.ellipse(16.5, 25, 8, 9, BODY, body)
    c.poly([(10, 30), (12, 36.5), (14, 31.5), (16.5, 37), (18.5, 31.5), (21, 35), (23, 29)], BODY, body)
    c.poly([(13, 18), (16, 13.5), (18, 17), (20.5, 14.5), (22, 18), (25, 16), (26, 19)], BODY, body)
    c.reshade(body, 24, 21, 15, 10, BODY, hi=0.95)
    head = c.new_part()
    c.ellipse(11.5, 17.5, 6.5, 6, BODY, head)
    c.poly([(1.5, 16.5), (8, 14), (10, 21), (2.5, 21)], BODY, head)
    c.poly([(9.5, 12.5), (12.5, 3.5), (16, 12)], BODY, head)
    c.poly([(5, 20), (10, 20), (14, 24), (13, 26), (8, 23.5), (4, 23.5)], BODY, head)
    c.reshade(head, 10, 15, 8, 8, BODY, dw=1, hi=0.95)
    c.finish()
    for (x, y) in ((20, 21), (22, 23), (31, 21), (33, 23), (35, 25), (26, 27), (28, 29), (17, 29), (19, 31)):
        c.put([(x, y), (x + 1, y + 1)], 'd')
    c.rim(body, 'a', only='b', side='u')
    c.rim(tail, 'a', only='b', side='u')
    # face: inner ear, brow, eye with a glint, nose, snarling mouth with fangs
    c.put([(12, 7), (12, 8), (13, 9), (12, 9)], 'd')
    c.put([(6, 12), (7, 12), (8, 13), (9, 13)], 'k')
    c.stamp(6, 14, "kkkk")
    c.stamp(6, 15, ".krwk")
    c.stamp(7, 16, "kk")
    c.put([(1, 16), (2, 16), (1, 17)], 'k')
    c.paint(2, 17, 'w')
    c.stamp(2, 20, "kkkkkkkk")
    c.put([(4, 21), (8, 21)], 'w')
    c.put([(4, 22), (8, 22)], 'k')
    c.put([(5, 18), (7, 18), (6, 19)], 'd')
    c.put([(11, 19), (12, 20), (13, 18)], 'd')
    # claws
    return c


# ================================================================ boar (side, charging)
BRISTLE = Mat('b', 'd', 'd')


@design('boar', 48, 48)
def boar(c):
    far = c.new_part()
    c.capsule(19, 33, 19, 42, 2.6, DARKB, far)
    c.capsule(35, 33, 36, 42, 2.6, DARKB, far)
    c.capsule(43.5, 22, 45.5, 27, 1.2, DARKB)
    legs = c.new_part()
    c.capsule(13, 33, 13, 42, 3.0, BODY, legs)
    c.capsule(40, 33, 41, 42, 3.0, BODY, legs)
    hoof = c.new_part()
    for x in (13, 41, 19, 36):
        c.poly([(x - 3, 42), (x + 3, 42), (x + 3.5, 45), (x - 3.5, 45)], DD, hoof)
    body = c.new_part()
    c.ellipse(29, 26, 16, 11, BODY, body)
    c.ellipse(19, 23, 10.5, 11, BODY, body)
    c.reshade(body, 26, 21, 18, 13, BODY)
    mane = c.new_part()
    c.poly([(10, 15), (12, 8), (15, 13), (17.5, 6), (20.5, 12), (23.5, 7), (26, 13), (29, 9.5), (31, 14.5),
            (34, 12.5), (36.5, 16.5), (38, 16), (37, 19), (14, 18.5)], BRISTLE, mane)
    head = c.new_part()
    c.ellipse(11, 26, 8.5, 8, BODY, head)
    c.poly([(1.5, 22), (7, 20.5), (8, 33), (2, 32)], BODY, head)
    c.reshade(head, 10, 23, 9, 9, BODY, dw=1)
    snout = c.new_part()
    c.ellipse(3, 27, 2.2, 5, Mat('b', 'b', 'd'), snout)
    ear = c.new_part()
    c.poly([(10, 19), (14.5, 13), (17.5, 21)], BRISTLE, ear)
    tusk = c.new_part()
    c.poly([(5, 31.5), (7, 31.5), (6.5, 28), (8.5, 25), (7.5, 24.5), (4.5, 28)], Mat('w', 'w', 'a'), tusk)
    c.finish()
    for (x, y) in ((22, 22), (27, 20), (32, 22), (36, 25), (24, 28), (30, 27), (20, 30)):
        c.put([(x, y), (x + 1, y + 1), (x + 1, y + 2)], 'd')
    c.rim(body, 'a', only='b', side='u')
    for x in range(14, 36, 3):
        c.put([(x, 14 if x < 30 else 16), (x + 1, 13 if x < 30 else 15)], 'b')
    c.stamp(9, 23, "kkk")
    c.stamp(9, 24, "krw")
    c.stamp(10, 25, "kk")
    c.put([(7, 22), (8, 22), (11, 22)], 'k')
    c.put([(2, 25), (2, 26), (2, 28), (2, 29)], 'k')
    c.put([(3, 32), (4, 32), (5, 33), (6, 33)], 'k')
    c.put([(13, 29), (14, 31), (15, 28)], 'd')
    for x in (13, 41):
        c.put([(x, 43), (x, 44)], 'k')
    return c


# ================================================================ bat (front, wings spread)
WINGM = Mat('b', 'b', 'd')


@design('bat', 48, 48, mirrored=True)
def bat(c):
    wing = c.new_part()
    c.poly2([(21, 16), (14, 8), (6, 4), (1, 9), (1.5, 30), (5, 26.5), (8.5, 32), (12, 27), (16, 33), (21, 28)],
            WINGM, wing)
    for (x1, y1) in ((6, 5), (2, 28), (8.5, 30.5), (16, 31.5)):
        c.capsule2(19, 17, x1, y1, 0.6, DD, wing)
    feet = c.new_part()
    c.capsule2(22, 33, 21.5, 39, 1.2, BODY, feet)
    body = c.new_part()
    c.ellipse(24, 25, 7, 9.5, BODY, body)
    c.reshade(body, 22, 22, 8, 10, BODY)
    head = c.new_part()
    c.ellipse(24, 14, 7.5, 6.5, BODY, head)
    c.poly2([(17.5, 13), (16, 1.5), (23, 9)], BODY, head)
    c.reshade(head, 22, 12, 8, 8, BODY, dw=1)
    c.finish()
    c.put2([(20, 22), (21, 23), (20, 27), (21, 28), (22, 31)], 'd')
    c.put2([(18, 5), (18, 6), (19, 8), (19, 9)], 'd')
    c.stamp(19, 12, "kk", mirror=True)
    c.stamp(19, 13, "krr", mirror=True)
    c.stamp(20, 14, "kw", mirror=True)
    c.put2([(23, 15)], 'd')
    c.stamp(20, 17, "kkkkkkkk")
    c.stamp(21, 18, "w....w")
    c.put2([(21, 39), (20, 40), (22, 40)], 'k')
    c.rim(wing, 'a', only='b', side='u')
    for (x, y) in ((5, 7), (9, 9), (3, 12)):
        c.put2([(x, y)], 'a')
    return c


# ================================================================ crab (front, claws raised)
@design('crab', 48, 48, mirrored=True)
def crab(c):
    legs = c.new_part()
    for (a, b, d) in (((15, 30), (6, 31), (2.5, 38)), ((16, 33), (8, 37), (6, 44)), ((18, 35), (13, 40), (12, 45.5))):
        c.capsule2(a[0], a[1], b[0], b[1], 1.6, DARKB, legs)
        c.capsule2(b[0], b[1], d[0], d[1], 1.6, DARKB, legs, r1=1.0)
    arm = c.new_part()
    c.capsule2(14, 27, 9, 19, 2.4, BODY, arm)
    claw = c.new_part()
    c.ellipse2(8, 11.5, 7.2, 7, BODY, claw)
    c.cut([(3.5, 2), (7.5, 12.5), (9.5, 12.5), (9, 2)], m=True)
    stalk = c.new_part()
    c.capsule2(20, 22, 19.5, 14, 1.1, BODY, stalk)
    body = c.new_part()
    c.ellipse(24, 30, 15, 9.5, BODY, body)
    c.ellipse(24, 26.5, 12, 6.5, BODY, body)
    c.reshade(body, 21, 24, 16, 11, BODY)
    eyes = c.new_part()
    c.ellipse2(19.5, 12.5, 2.6, 2.6, flat('w'), eyes)
    c.finish()
    c.stamp(19, 12, "kk", mirror=True)
    c.stamp(19, 13, "kk", mirror=True)
    c.put2([(17, 26), (18, 25), (19, 25)], 'd')
    c.put2([(14, 28), (15, 29), (12, 31)], 'd')
    c.put2([(21, 22), (22, 22), (20, 23)], 'a')
    c.stamp(20, 33, "kkkkkkkk")
    c.stamp(21, 34, "w.ww.w")
    c.put2([(5, 9), (4, 13), (13, 14), (12, 10)], 'd')
    c.put2([(2, 9), (3, 6)], 'a')
    c.put2([(x, 36) for x in range(13, 21) if x % 3 == 0], 'd')
    return c
