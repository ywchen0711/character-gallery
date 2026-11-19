"""Family portraits (cute HD-2D): one function per member."""
from family import Portrait, ellipse, lock, hair_tone, HAIR_BLACK, HAIR_BROWN, CX, PW, PH, interp, FACE_KEYS
from pixlib import G


def clothes(P, keys, mat, lit=5.2, dark=1.6):
    """Shoulders from a contour [(y, left, right)], lit from the left."""
    for y in range(keys[0][0], PH):
        for (y0, l0, r0), (y1, l1, r1) in zip(keys, keys[1:]):
            if y0 <= y <= y1:
                t = (y - y0) / max(1, y1 - y0)
                l, r = l0 + (l1 - l0) * t, r0 + (r1 - r0) * t
                for x in range(int(l), int(r) + 1):
                    u = (x - l) / max(1, r - l)
                    P.S.put(x, y, mat, lit - (lit - dark) * u)
                break


def cross_collar(P, top, mat, inner, w=3, depth=14, cx=CX):
    """Han crossed collar: wearer's left over right; bands are 'mat' at a lit tone, inner garment shows in the V."""
    for i in range(depth):
        y = top + i
        for x in range(cx - 4 + i // 2, cx + 6 - i):
            if P.S.get(x, y) not in (None,):
                P.S.put(x, y, inner, 5 - (x - cx) * 0.15)
        for j in range(w):
            P.S.put(cx + 6 - i + j, y, mat, 5.5 - j)        # top lapel
        if i < depth // 2:
            for j in range(w):
                P.S.put(cx - 5 + i // 2 + j, y, mat, 4.5 - j)


# ------------------------------------------------------------------ eyes
# small, gently almond eyes with a soft single-lid line, dark iris, one catchlight
EYE_KID_L = G('''
.kkkk.
kWEEek
.eEEk.
''')
EYE_KID_R = G('''
.kkkkk
kWEEek
.eEEk.
''')
EYE_ADULT_L = G('''
.kkkk.
kWEEek
..ee..
''')
EYE_ADULT_R = G('''
.kkkkk
kWEEek
..ee..
''')


def jasper():
    P = Portrait('kid', bg=('#3c4a3a', '#a07c4a'),
                 lights=((8, 14, 10, '#f0d090'), (64, 24, 8, '#fff0b0'), (60, 66, 11, '#e8a060'), (6, 60, 7, '#ffe0a0')))
    P.ramp('hair', HAIR_BLACK)
    P.ramp('cloth', ['#1c3a1e', '#285028', '#346a32', '#46843e', '#5ea04e', '#7cba64', '#9cd07e'])
    P.ramp('inner', ['#7a6e5a', '#968a72', '#b2a68c', '#cabfa4', '#ddd4ba', '#ece6d0', '#f8f4e6'])
    P.ramp('strap', ['#2e1a0c', '#46280f', '#5e3816', '#784a20', '#94602c', '#ae783c', '#c8924e'])
    hl = hair_tone(CX - 2, 26, 15)
    # back hair mass behind the face
    P.fill('hair', ellipse(CX, 28, 21, 17), hl)
    # two little Han-style buns (zongjiao) tied with green cloth
    P.fill('hair', ellipse(CX - 16, 13, 6.5, 6.5), hl)
    P.fill('hair', ellipse(CX + 16, 13, 6.5, 6.5), hl)
    P.face()
    P.neck(6)
    clothes(P, [(62, 22, 50), (65, 15, 57), (68, 11, 61), (72, 8, 64), (80, 6, 66)], 'cloth')
    cross_collar(P, 62, 'cloth', 'inner', w=3, depth=16)
    for i in range(20):                                   # satchel strap over the shoulder
        for j in range(3):
            P.S.put(22 + i + j, 64 + int(i * 0.8), 'strap', 4.5 - j)
    # fringe: short choppy locks across the forehead, a cowlick sticking up
    for (x0, w, ln, lean) in ((16, 3.2, 14, 0.15), (21, 3.4, 13, 0.1), (26, 3.6, 12, 0.05), (31, 3.6, 13, 0.0),
                              (36, 3.6, 12, -0.05), (41, 3.4, 12, -0.12), (46, 3.2, 13, -0.2), (51, 3, 15, -0.25),
                              (55, 2.6, 18, -0.15)):
        P.fill('hair', lock(x0, 17, w, ln, lean), hl)
    P.fill('hair', lambda x, y: ellipse(CX + 1, 19, 19.5, 9)(x, y) and y < 22, hl)
    P.fill('hair', lock(CX + 4, 3, 1.6, 9, -0.4), hl)
    P.fill('hair', lambda x, y: ellipse(CX + 3, 8, 3, 4)(x, y), hl)
    # separate the buns from the head with a soft dark crease
    for bx in (CX - 16, CX + 16):
        for y in range(6, 22):
            for x in range(bx - 8, bx + 9):
                d = ((x - bx) / 6.5) ** 2 + ((y - 13) / 6.5) ** 2
                if 0.8 <= d <= 1.15 and P.S.get(x, y) == 'hair' and y > 13:
                    P.S.t[y][x] = 0.4
    P.shade_under(depth=2, amount=1.4)
    # bun ties
    for bx in (CX - 16, CX + 16):
        P.fill('cloth', lambda x, y, bx=bx: abs(x - (bx + (4 if bx < CX else -4))) <= 1.2 and 15 <= y <= 19, 4.5)
    # face
    P.eyes(EYE_KID_L, EYE_KID_R, gap=8)
    ey = 38
    P.stamp_fixed(G('''
.bbb.
'''), CX - 13, ey - 4)
    P.stamp_fixed(G('''
..bb.
.b...
'''), CX + 5, ey - 6)
    P.stamp_fixed(G('''
.N
n.
'''), CX - 3, ey + 5)
    P.stamp_fixed(G('''
......m
m....m.
.mmmm..
..ll...
'''), CX - 5, ey + 8)
    P.blush(dx=11, dy=6)
    return P.render()


def josh():
    P = Portrait('boy', bg=('#4a3030', '#b07848'),
                 lights=((10, 20, 9, '#ffd890'), (62, 14, 8, '#ffe8b0'), (64, 60, 12, '#f0a060'), (8, 64, 8, '#ffc880')))
    P.ramp('hair', HAIR_BLACK)
    P.ramp('cloth', ['#4a1410', '#6a1e16', '#8a2c1e', '#aa4028', '#c85a34', '#e07a46', '#f09c62'])
    P.ramp('inner', ['#7a6e5a', '#968a72', '#b2a68c', '#cabfa4', '#ddd4ba', '#ece6d0', '#f8f4e6'])
    P.ramp('band', ['#3a2a10', '#5a4018', '#7a5a22', '#9a742e', '#b8903c', '#d2ac52', '#e8c86e'])
    P.ramp('wood', ['#3a2414', '#54341c', '#6e4626', '#885a32', '#a2703e', '#ba884e', '#d0a264'])
    hl = hair_tone(CX - 2, 25, 14)
    P.fill('hair', ellipse(CX, 27, 21, 17), hl)
    P.fill('hair', ellipse(CX + 2, 7, 5.5, 5), hl)             # small topknot
    P.face()
    P.neck(7)
    # wooden shield rim over his shoulder (carried on his back)
    P.fill('wood', lambda x, y: 13.5 <= ((x - 66) ** 2 + (y - 64) ** 2) ** 0.5 <= 16.5,
           lambda x, y: 4.6 - (x - 52) / 14 * 2.5, (40, 44, PW, PH))
    clothes(P, [(61, 21, 51), (64, 14, 58), (67, 10, 62), (71, 7, 65), (80, 5, 67)], 'cloth')
    cross_collar(P, 61, 'cloth', 'inner', w=3, depth=16)
    # short, spiky fringe swept up and to the side
    for (x0, w, ln, lean) in ((17, 3.2, 12, 0.25), (22, 3.6, 11, 0.2), (28, 3.8, 9, 0.15), (34, 3.8, 8, 0.1),
                              (40, 3.6, 9, -0.05), (46, 3.4, 11, -0.15), (51, 3, 14, -0.2), (55, 2.6, 17, -0.1)):
        P.fill('hair', lock(x0, 16, w, ln, lean), hl)
    P.fill('hair', lambda x, y: ellipse(CX + 1, 18, 19.5, 9)(x, y) and y < 21, hl)
    # headband: a protector's gold cloth band with tails
    for y in range(20, 25):
        for x in range(14, 59):
            if P.S.get(x, y) in ('hair', 'skin') and abs(y - (22 - (x - 14) * 0.03)) <= 1.3:
                P.S.put(x, y, 'band', 5.2 - (x - 14) / 45 * 3)
    P.fill('band', ellipse(CX + 2, 11, 2, 1.5), 4.5)
    for i in range(10):
        P.S.put(57 + i // 2, 22 + i, 'band', 3.5)
        P.S.put(58 + i // 2, 22 + i, 'band', 2.5)
    P.shade_under(depth=2, amount=1.2)
    P.eyes(EYE_KID_L, EYE_KID_R, gap=8, dy=-1)
    ey = 36
    P.stamp_fixed(G('''
bbbb.
...bb
'''), CX - 14, ey - 4)
    P.stamp_fixed(G('''
.bbbb
bb...
'''), CX + 5, ey - 4)
    P.stamp_fixed(G('''
.N
n.
'''), CX - 3, ey + 5)
    P.stamp_fixed(G('''
m......m
.mwwwwm.
..mllm..
'''), CX - 6, ey + 9)
    P.blush(dx=11, dy=6, a=0.3)
    return P.render()


def glasses(P, ey, col='#4a3426'):
    import math as _m
    for (gx, rx) in ((CX - 12, 5.0), (CX + 6, 5.4)):
        for k in range(90):
            a = k / 90 * 2 * _m.pi
            P.fixed[(round(gx + rx * _m.cos(a)), round(ey + 1 + 4.6 * _m.sin(a)))] = col
    for x in range(CX - 7, CX + 1):
        P.fixed[(x, ey - 1)] = col
    for x in range(CX + 12, CX + 18):
        P.fixed[(x, ey)] = col
    P.fixed[(CX - 15, ey - 2)] = '#e8f4ff'
    P.fixed[(CX + 3, ey - 2)] = '#e8f4ff'


def jeff():
    P = Portrait('man', bg=('#2e3440', '#7a6448'),
                 lights=((8, 16, 9, '#e8c890'), (64, 12, 7, '#fff0c0'), (62, 58, 12, '#d89c5c'), (6, 62, 7, '#f8d8a0')))
    P.ramp('hair', HAIR_BLACK)
    P.ramp('cloth', ['#1e2014', '#2c301c', '#3e4426', '#525a32', '#68723e', '#808a4e', '#9aa264'])
    P.ramp('inner', ['#7a6e5a', '#968a72', '#b2a68c', '#cabfa4', '#ddd4ba', '#ece6d0', '#f8f4e6'])
    P.ramp('strap', ['#2e1a0c', '#46280f', '#5e3816', '#784a20', '#94602c', '#ae783c', '#c8924e'])
    hl = hair_tone(CX - 2, 24, 14)
    P.fill('hair', ellipse(CX, 25, 18, 15), hl)
    P.fill('hair', ellipse(CX + 1, 6, 5, 4.5), hl)              # topknot
    P.face()
    P.neck(7)
    clothes(P, [(59, 18, 54), (62, 10, 62), (65, 6, 66), (70, 3, 69), (80, 1, 71)], 'cloth')
    cross_collar(P, 59, 'cloth', 'inner', w=3, depth=20)
    for i in range(24):                                          # tool strap across the chest
        for j in range(3):
            P.S.put(46 - i + j, 62 + int(i * 0.75), 'strap', 4.5 - j)
    # neat side-parted hair sweeping to the right
    for (x0, w, ln, lean) in ((19, 2.6, 13, 0.0), (23, 3.2, 9, 0.35), (28, 3.6, 8, 0.45), (34, 3.8, 8, 0.5),
                              (40, 3.8, 9, 0.4), (45, 3.4, 11, 0.2), (50, 2.8, 13, 0.0), (53, 2.2, 17, -0.05)):
        P.fill('hair', lock(x0, 14, w, ln, lean), hl)
    P.fill('hair', lambda x, y: ellipse(CX + 1, 16, 17.5, 8)(x, y) and y < 19, hl)
    P.fill('strap', lambda x, y: abs(y - 9.5) <= 0.8 and abs(x - CX - 1) <= 4, 4)   # topknot tie
    P.shade_under(depth=2, amount=1.2)
    P.eyes(EYE_ADULT_L, EYE_ADULT_R, gap=8)
    ey = 36
    P.stamp_fixed(G('''
.bbbb
bb...
'''), CX - 14, ey - 5)
    P.stamp_fixed(G('''
bbbbb
....b
'''), CX + 4, ey - 5)
    P.stamp_fixed(G('''
..N
.Nn
.n.
nnn
'''), CX - 4, ey + 3)
    P.stamp_fixed(G('''
m.....m
.mmmmm.
'''), CX - 6, ey + 11)
    glasses(P, ey)
    import random
    rnd = random.Random(5)
    for y in range(ey + 9, 62):                         # light stubble along the jaw and lip
        for x in range(CX - 18, CX + 18):
            if P.S.get(x, y) == 'skin' and rnd.random() < 0.33 and (y > ey + 13 or abs(x - CX + 2) > 6 or y == ey + 10):
                P.tints[(x, y)] = ('#3a3036', 0.28)
    P.blush(dx=12, dy=7, a=0.12)
    return P.render()


def erin():
    P = Portrait('woman', bg=('#30384a', '#8a6a5a'),
                 lights=((10, 18, 9, '#f8d8a8'), (62, 12, 8, '#fff4d0'), (62, 60, 12, '#e0a080'), (6, 62, 8, '#ffe0b8')))
    P.ramp('hair', HAIR_BLACK)
    P.ramp('cloth', ['#10303a', '#164450', '#1e5a66', '#2a727c', '#3c8c94', '#58a6aa', '#7cc0c0'])
    P.ramp('inner', ['#7a6e5a', '#968a72', '#b2a68c', '#cabfa4', '#ddd4ba', '#ece6d0', '#f8f4e6'])
    P.ramp('pin', ['#3a2414', '#54341c', '#6e4626', '#885a32', '#a2703e', '#ba884e', '#d0a264'])
    P.ramp('leaf', ['#1c3a18', '#285020', '#36682a', '#4a8236', '#62a046', '#80ba5c', '#a2d27a'])
    hl = hair_tone(CX - 2, 24, 15)
    P.fill('hair', ellipse(CX, 28, 19.5, 18), hl)
    P.fill('hair', lambda x, y: 34 <= y <= 72 and (16 <= x <= 23 or 49 <= x <= 56), hl)
    P.fill('hair', ellipse(CX + 18, 22, 7, 6.5), hl)              # low bun at the back
    P.face()
    P.neck(5)
    clothes(P, [(60, 22, 50), (63, 15, 57), (66, 11, 61), (70, 8, 64), (80, 6, 66)], 'cloth')
    cross_collar(P, 60, 'cloth', 'inner', w=3, depth=18)
    P.fill('hair', lambda x, y: 46 <= y <= 74 and (abs(x - 18 - (y - 46) * 0.05) <= 2.6 - (y - 46) * 0.04 or
                                                    abs(x - 54 + (y - 46) * 0.05) <= 2.6 - (y - 46) * 0.04), hl)
    # centre part with soft curtains of hair framing the face
    for (x0, w, ln, lean) in ((19, 2.8, 28, 0.0), (23, 3.2, 16, -0.2), (27, 3.4, 10, -0.5), (32, 3.2, 8, -0.6),
                              (40, 3.2, 8, 0.6), (45, 3.4, 10, 0.5), (49, 3.2, 16, 0.2), (53, 2.8, 28, 0.0)):
        P.fill('hair', lock(x0, 15, w, ln, lean), hl)
    P.fill('hair', lambda x, y: ellipse(CX, 16, 19, 7)(x, y) and y < 19 and abs(x - CX + 0.5) > 0.6, hl)
    for i in range(12):                                           # wooden hairpin and a sprig of herb
        P.S.put(56 + i, 18 + i // 3, 'pin', 4.5)
    P.fill('leaf', ellipse(CX + 22, 16, 2.5, 1.5), 4.5)
    P.fill('leaf', ellipse(CX + 19, 14, 1.5, 2.4), 3.5)
    P.shade_under(depth=2, amount=1.1)
    P.eyes(EYE_ADULT_L, EYE_ADULT_R, gap=8)
    ey = 36
    P.stamp_fixed(G('''
.bbb.
'''), CX - 13, ey - 4)
    P.stamp_fixed(G('''
.bbb.
'''), CX + 5, ey - 4)
    P.stamp_fixed(G('''
.N
n.
'''), CX - 3, ey + 5)
    P.stamp_fixed(G('''
.lll.
m...m
.lll.
'''), CX - 5, ey + 10)
    P.blush(dx=11, dy=7, a=0.22)
    return P.render()
