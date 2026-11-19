"""Monster designs: the undead and the people of the jianghu, 48x56 and facing the viewer.

They are built like the people portraits: a big head (an 18-px face with thick brows, eye strokes, a nose shadow
and a mouth that shows the mood), a full-width body, and costume details finished by hand.
Extra slots used here:
  S s   skin and skin shadow                     H  hands (skin colour, sprite layer)
  w     glints in the eyes, blade edges          e f  a second material (hat, scarf, trousers)
  r y   small accents (sprite layer)
"""
from mondraw import Mat, flat
from mon_designs import design

SKIN = Mat('S', 'S', 's', hi=2)
HAND = flat('H')
DD = flat('d')
KK = flat('k')


def person(c, top, sleeve=None, pants=None, shoes=DD, waist=40, legx=19.5, arms=True, hands=True, armsx=9.0,
           head=True):
    """The shared body: legs, arms, torso, neck, ears and head (skin). Returns the parts."""
    sleeve = sleeve or top
    pants = pants or top
    P = {}
    P['legs'] = c.new_part()
    c.capsule2(legx, waist, legx - 0.5, 51, 3.6, pants, P['legs'])
    P['feet'] = c.new_part()
    c.ellipse2(legx - 1, 53, 5, 2.2, shoes, P['feet'])
    P['torso'] = c.new_part()
    c.poly2([(24, 21), (15.5, 21.5), (12.5, 25), (13.5, waist + 1), (24, waist + 1)], top, P['torso'])
    c.reshade(P['torso'], 20, 27, 14, 16, top, dw=2, hi=0.9)
    if arms:
        P['arms'] = c.new_part()
        c.capsule(14, 24, armsx, 35, 3.4, sleeve, P['arms'])
        if arms != 'left':
            c.capsule(34, 24, 48 - armsx, 35, 3.4, sleeve, P['arms'])
        if hands:
            P['hands'] = c.new_part()
            c.ellipse(armsx - 0.5, 37.5, 3.0, 2.8, HAND, P['hands'])
            if arms != 'left':
                c.ellipse(48.5 - armsx, 37.5, 3.0, 2.8, HAND, P['hands'])
    if head:
        P['neck'] = c.new_part()
        c.rect(21, 19, 26, 22, SKIN, P['neck'], shade='flat')
        P['ears'] = c.new_part()
        c.ellipse2(14.8, 14, 1.8, 2.4, SKIN, P['ears'])
        P['head'] = c.new_part()
        c.ellipse(24, 12.5, 9, 8.6, SKIN, P['head'])
        c.reshade(P['head'], 21, 10, 11, 11, SKIN, dw=1, hi=2)
    return P


def eyes(c, y, kind='stern', glint=True):
    """Brows and eyes in the people-portrait idiom (left half typed, mirrored), the eyes on row y."""
    if kind == 'stern':
        c.stamp(16, y - 3, ".kkk", mirror=True)
        c.stamp(17, y - 2, ".kkkk", mirror=True)
        c.stamp(17, y, "kkkk", mirror=True)
        c.stamp(18, y + 1, "kk", mirror=True)
    elif kind == 'calm':
        c.stamp(16, y - 3, ".kkkkk", mirror=True)
        c.stamp(17, y, "kkkk", mirror=True)
        c.stamp(18, y + 1, "kk", mirror=True)
    elif kind == 'bushy':
        c.stamp(15, y - 3, "kkkkkk", mirror=True)
        c.stamp(15, y - 2, ".kkkkk", mirror=True)
        c.stamp(18, y, "kk", mirror=True)
        c.stamp(18, y + 1, "kk", mirror=True)
    elif kind == 'sly':
        c.stamp(16, y - 3, "kk", mirror=True)
        c.stamp(18, y - 2, "kkk", mirror=True)
        c.stamp(17, y, "kkkkk", mirror=True)
        c.stamp(19, y + 1, "kk", mirror=True)
        glint = False
    if glint:
        c.paint(18, y + 1, 'w')
        c.paint(28, y + 1, 'w')


def nose(c, y):
    c.paint(24, y, 's')
    c.paint(23, y + 1, 's')
    c.paint(24, y + 1, 's')


# ================================================================ bandit lackey 嘍囉 (headscarf and a club)
VEST = Mat('a', 'b', 'd')


@design('lackey', 48, 56, mirrored=True)
def lackey(c):
    P = person(c, VEST, sleeve=SKIN, pants=Mat('b', 'd', 'd'), waist=40, arms='left')
    arm = c.new_part()
    c.capsule(34, 24, 37.5, 30, 3.3, SKIN, arm)
    club = c.new_part()
    c.capsule(37, 34, 41.5, 4.5, 1.7, Mat('a', 'b', 'd'), club, r1=3.4)
    fist = c.new_part()
    c.ellipse(37.5, 30.5, 3.2, 2.9, HAND, fist)
    knot = c.new_part()
    c.poly([(15, 8), (9, 3.5), (8, 9), (12, 11.5)], flat('f'), knot)
    c.poly([(15, 10), (9.5, 13.5), (12.5, 15.5), (15.5, 12)], flat('f'), knot)
    scarf = c.new_part()
    c.ellipse(24, 9, 9.8, 7, Mat('e', 'f', 'f'), scarf, clip=lambda x, y: y <= 9)
    c.finish()
    for y in range(22, 36):
        for x in range(21, 27):
            if c.part[y][x] == P['torso']:
                c.paint(x, y, 'S' if 22 <= x <= 25 else 'k')
    c.put([(x, y) for y in (36, 37) for x in range(12, 36)], 'f')
    c.put([(22, 38), (23, 39), (25, 38), (24, 39)], 'f')
    c.put([(14, 30), (15, 30), (14, 31), (33, 26), (33, 27)], 'd')
    eyes(c, 13, 'stern')
    nose(c, 15)
    c.stamp(20, 18, "kkkkkkkk")
    c.stamp(19, 19, "k")
    c.stamp(28, 19, "k")
    c.put([(18, 17), (21, 20), (26, 20), (29, 17), (23, 20)], 's')
    c.put([(30, 9), (31, 10), (31, 11)], 'k')
    c.put([(39, 8), (41, 11), (40, 15)], 'd')
    return c


# ================================================================ archer 弓手 (bow in hand, quiver on the back)
TUNIC = Mat('a', 'b', 'd')


@design('archer', 48, 56, mirrored=True, open_slots='w')
def archer(c):
    P = person(c, TUNIC, pants=Mat('b', 'd', 'd'), arms=False)
    arm = c.new_part()
    c.capsule(14, 24, 7, 25, 3.2, TUNIC, arm)
    c.capsule(34, 24, 37, 33, 3.3, TUNIC, arm)
    hand = c.new_part()
    c.ellipse(37.5, 35.5, 3.0, 2.8, HAND, hand)
    quiver = c.new_part()
    c.poly([(33, 4), (38, 3), (40, 21), (35, 22)], Mat('e', 'f', 'f'), quiver)
    hat = c.new_part()
    c.ellipse(24, 8, 10, 5.5, Mat('e', 'f', 'f'), hat, clip=lambda x, y: y <= 8)
    c.rect(13, 8, 34, 9, flat('f'), hat, shade='flat')
    c.finish()
    c.stamp(33, 0, """
.kk.kk
kwwkwwk
kwwkwwk
kkkkkkk
""")
    c.put([(x, y) for y in (35, 36) for x in range(11, 37)], 'k')
    c.put([(23, 35), (24, 35), (23, 36), (24, 36)], 'y')
    c.put([(22, 22), (21, 23), (20, 24), (25, 22), (26, 23), (27, 24)], 'd')
    c.stamp(1, 8, """
...kk
..kddk
..kdkk
.kdkwk
.kdkwk
kddkwk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kdk.wk
kddkwk
.kdkwk
.kdkwk
..kdkk
..kddk
...kk
""")
    c.stamp(3, 22, """
kkkk
kHHk
kHHk
kkkk
""")
    eyes(c, 13, 'calm')
    c.put([(28, 13), (29, 13), (30, 13), (31, 13), (28, 14), (29, 14)], 'k')
    nose(c, 15)
    c.stamp(21, 18, "kkkkk")
    c.stamp(26, 17, "k")
    return c
