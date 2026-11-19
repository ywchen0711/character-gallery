"""Monster designs (second version), part 2: the snake, the monkey and the bugs, 48x48, finished by hand."""
import math

from mondraw import Mat, flat
from mon_designs import design, BODY, DARKB

DD = flat('d')
KK = flat('k')


def arc(cx, cy, rx, ry, a0, a1, n=14):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n))
            for i in range(n + 1)]


DIAMOND = (".d.", "ddd", ".d.")


def diamond(c, x, y, slot='d'):
    for dy, r in enumerate(DIAMOND):
        for dx, ch in enumerate(r):
            if ch != '.' and 0 <= y + dy < c.h and 0 <= x + dx < c.w and c.tone[y + dy][x + dx] not in '.k':
                c.paint(x + dx, y + dy, slot)


# ================================================================ snake (a coiled viper, head raised)
@design('snake', 48, 48, mirrored=True)
def snake(c):
    rings = [(24, 40, 17, 3.6, 3.8), (24, 33.5, 13.5, 3.2, 3.5), (24, 28, 9.5, 2.8, 3.2)]
    for (cx, cy, rx, ry, r) in rings:
        c.tube(arc(cx, cy, rx, ry, math.pi, 2 * math.pi), r, BODY)
    neck = c.new_part()
    c.capsule(24, 28, 24, 15, 4.4, BODY, neck, r1=3.8)
    fronts = []
    for (cx, cy, rx, ry, r) in rings:
        fronts.append(c.tube(arc(cx, cy, rx, ry, 0, math.pi), r, BODY))
    belly = c.new_part(sep=False)
    c.rect(22, 16, 25, 27, Mat('a', 'a', 'b'), belly, shade='flat')
    head = c.new_part()
    c.poly([(13, 10), (18, 4.5), (30, 4.5), (35, 10), (33, 15), (28, 18.5), (20, 18.5), (15, 15)], BODY, head)
    c.reshade(head, 21, 8, 13, 10, BODY, dw=1)
    c.finish()
    for y in range(17, 28, 2):
        c.put([(22, y), (23, y), (24, y), (25, y)], 'b')
    for p in fronts:
        c.rim(p, 'a', only='b', side='u')
    c.put2([(19, 7), (20, 6), (21, 6)], 'd')
    c.stamp(17, 8, "kkkk", mirror=True)
    c.stamp(17, 9, "kyky", mirror=True)
    c.stamp(18, 10, "kk", mirror=True)
    c.put2([(18, 9)], 'w')
    c.put2([(21, 14)], 'k')
    c.stamp(19, 16, "kkkkkkkkkk")
    c.put2([(20, 17)], 'w')
    c.stamp(23, 18, "rr")
    c.stamp(22, 19, "r..r")
    c.put2([(16, 12), (15, 11)], 'a')
    return c


# ================================================================ monkey (front, sitting, grinning)
FACE = Mat('a', 'a', 'b')


@design('monkey', 48, 48, mirrored=True)
def monkey(c):
    tail = c.new_part()
    c.tube([(34, 40), (40, 38), (42, 31), (39, 26), (36, 28)], 1.9, DARKB, tail)
    legs = c.new_part()
    c.capsule2(18, 37, 16.5, 43, 3.6, BODY, legs)
    c.ellipse2(15.5, 45, 4.5, 2.4, FACE, legs)
    body = c.new_part()
    c.ellipse(24, 33, 10, 10, BODY, body)
    c.ellipse(24, 34.5, 5.5, 6.5, FACE, body)
    c.reshade(body, 21, 29, 12, 12, BODY)
    arms = c.new_part()
    c.capsule2(14.5, 27, 10, 37, 2.9, BODY, arms)
    c.ellipse2(10, 39, 3.2, 2.9, FACE, arms)
    ears = c.new_part()
    c.ellipse2(11.5, 16, 3.8, 4.2, BODY, ears)
    c.ellipse2(11.8, 16.2, 1.8, 2.4, flat('b'), ears)
    head = c.new_part()
    c.ellipse(24, 15, 11.5, 10.5, BODY, head)
    c.poly2([(16, 7), (18, 2.5), (21, 6), (24, 1.5), (24, 7)], BODY, head)
    c.reshade(head, 21, 12, 12, 11, BODY, dw=1)
    face = c.new_part(sep=False)
    c.ellipse2(19.5, 15.5, 4.6, 4.8, FACE, face)
    c.ellipse(24, 21, 7.5, 4.6, FACE, face)
    c.finish()
    c.stamp(16, 12, ".kkk", mirror=True)
    c.stamp(17, 14, "kkk", mirror=True)
    c.stamp(18, 15, "kk", mirror=True)
    c.put2([(18, 15)], 'w')
    c.put2([(22, 19)], 'k')
    c.put2([(21, 18), (22, 18)], 'b')
    c.stamp(19, 22, "kkkkkkkkkk")
    c.stamp(20, 23, "kwwwwwwk")
    c.stamp(21, 24, "kkkkkk")
    c.put2([(15, 22), (16, 23)], 'b')
    for (x, y) in ((16, 30), (18, 33), (30, 30), (32, 33), (14, 34)):
        c.put([(x, y), (x + 1, y + 1)], 'd')
    c.put2([(9, 40), (11, 40), (14, 46), (16, 46)], 'k')
    return c


# ================================================================ hornet (front, wings up)
WINGW = Mat('a', 'a', 'a')


@design('hornet', 48, 48, mirrored=True)
def hornet(c):
    wing = c.new_part()
    c.poly2([(21, 15), (12, 2), (3.5, 2.5), (1.5, 11), (16, 19)], WINGW, wing)
    c.poly2([(20, 18), (6, 18), (3, 23), (8, 26), (19, 21)], WINGW, wing)
    legs = c.new_part()
    c.capsule2(20, 23, 14, 30, 1.1, DD, legs)
    c.capsule2(14, 30, 12.5, 37, 1.0, DD, legs)
    c.capsule2(21, 27, 17, 37, 1.1, DD, legs)
    c.capsule2(17, 37, 16.5, 42, 1.0, DD, legs)
    ant = c.new_part()
    c.capsule2(22, 7, 17, 2.5, 0.7, DD, ant)
    c.ellipse2(16.5, 2.5, 1.1, 1.1, DD, ant)
    abd = c.new_part()
    c.ellipse(24, 33, 8.5, 10, BODY, abd)
    c.poly([(21, 41.5), (27, 41.5), (24, 47)], BODY, abd)
    th = c.new_part()
    c.ellipse(24, 22, 6.8, 5, Mat('b', 'd', 'd'), th)
    head = c.new_part()
    c.ellipse(24, 13, 7.5, 6, BODY, head)
    eyes = c.new_part()
    c.ellipse2(19.5, 12, 2.8, 4, Mat('d', 'd', 'd'), eyes)
    c.finish()
    for y in (28, 29, 35, 36, 41):
        for x in range(14, 35):
            if c.part[y][x] == abd and c.tone[y][x] not in 'k':
                c.paint(x, y, 'd')
    c.put2([(18, 10), (19, 9), (19, 13)], 'a')
    c.put2([(18, 12)], 'w')
    c.stamp(21, 17, "kkkkkk")
    c.stamp(21, 18, "a....a")
    c.stamp(22, 18, "k..k")
    c.put2([(22, 20), (21, 22), (23, 24), (20, 24)], 'b')
    for (a, b) in (((19, 15), (7, 4)), ((18, 16), (4, 10)), ((18, 19), (6, 22))):
        for t in range(1, 10):
            x = round(a[0] + (b[0] - a[0]) * t / 10)
            y = round(a[1] + (b[1] - a[1]) * t / 10)
            if c.part[y][x] == wing and c.tone[y][x] not in 'k':
                c.paint(x, y, 'b')
                c.paint(47 - x, y, 'b')
    c.put([(24, 46)], 'w')
    return c


# ================================================================ centipede (rearing up, facing the viewer)
@design('centipede', 48, 48, mirrored=True)
def centipede(c):
    segs = [(43, 10.5, 3.8), (37.5, 9.8, 3.6), (32, 9.0, 3.4), (27, 8.2, 3.2), (22.5, 7.5, 3.0)]
    for (y, rx, ry) in segs:
        legs = c.new_part()
        c.capsule2(24 - rx + 1, y, 24 - rx - 4.5, y - 1.8, 1.0, DD, legs)
        c.capsule2(24 - rx - 4.5, y - 1.8, 24 - rx - 6.5, y + 3, 0.9, DD, legs)
    segp = []
    for (y, rx, ry) in segs:
        segp.append(c.ellipse(24, y, rx, ry, BODY))
    ant = c.new_part()
    c.capsule2(21, 10, 13, 2, 0.8, DD, ant)
    c.capsule2(13, 2, 9, 4.5, 0.7, DD, ant)
    head = c.new_part()
    c.ellipse(24, 14, 7.5, 6, BODY, head)
    jaw = c.new_part()
    c.poly2([(19, 16), (16, 21), (18.5, 23.5), (20.5, 20), (22.5, 18)], Mat('a', 'a', 'b'), jaw)
    c.finish()
    for p, (y, rx, ry) in zip(segp, segs):
        c.rim(p, 'a', only='b', side='u')
        c.put2([(24 - round(rx * 0.55), round(y)), (24 - round(rx * 0.55), round(y) + 1)], 'd')
    c.stamp(19, 12, "kkk", mirror=True)
    c.stamp(19, 13, "kyk", mirror=True)
    c.put2([(19, 13)], 'w')
    c.put2([(17, 21), (18, 22)], 'w')
    c.put2([(16, 2), (12, 4)], 'k')
    c.put2([(10, 8), (9, 11), (7, 15), (6, 20)], 'w')
    return c


# ================================================================ scorpion (front, tail over the head)
@design('scorpion', 48, 48)
def scorpion(c):
    legs = c.new_part()
    for (a, b, d) in (((19, 36), (11, 37), (8, 44)), ((20, 38), (14, 41), (13, 46)), ((18, 34), (10, 33), (5, 39))):
        c.capsule2(a[0], a[1], b[0], b[1], 1.4, DARKB, legs)
        c.capsule2(b[0], b[1], d[0], d[1], 1.4, DARKB, legs, r1=0.9)
    tsegs = [(24, 29, 3.8), (26, 23.5, 3.6), (29, 18, 3.4), (31.5, 12.5, 3.2), (30, 7, 3.0), (26, 4.5, 2.8)]
    tp = []
    for (x, y, r) in tsegs:
        tp.append(c.ellipse(x, y, r, r, BODY))
    sting = c.new_part()
    c.poly([(23.5, 2.5), (19.5, 4), (19.5, 9.5), (23, 6.5)], Mat('a', 'a', 'b'), sting)
    arm = c.new_part()
    c.capsule2(16, 34, 9, 30, 2.2, BODY, arm)
    claw = c.new_part()
    c.ellipse2(7, 25, 5.8, 5.5, BODY, claw)
    c.cut([(1.5, 17.5), (5.5, 25.5), (7.5, 25.5), (6.5, 17.5)], m=True)
    body = c.new_part()
    c.ellipse(24, 35, 10.5, 7.5, BODY, body)
    c.reshade(body, 22, 33, 11, 9, BODY)
    c.finish()
    for p in tp:
        c.rim(p, 'a', only='b', side='ul')
    c.rim(body, 'a', only='b', side='u')
    c.put2([(18, 33), (18, 34), (19, 35), (19, 36)], 'd')
    c.put([(24, 30), (24, 31), (24, 32)], 'd')
    c.stamp(21, 36, "kkk.kkk")
    c.stamp(21, 37, "kr...rk")
    c.put([(22, 37), (26, 37)], 'k')
    c.put([(21, 37), (27, 37)], 'r')
    c.put([(20, 6)], 'w')
    c.put2([(3, 21), (4, 20), (10, 21), (9, 20)], 'd')
    c.put2([(2, 23), (3, 22)], 'a')
    return c
