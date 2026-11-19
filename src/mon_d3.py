"""Monster designs, part 3: the undead and the people of the jianghu, all 40x48 and facing the viewer.

Extra slots used here: S skin (flat, the way Famicom faces are), s skin shadow where a palette allows it.
"""
from mondraw import Mat, flat
from mon_designs import design, BODY, DARKB, WHITE

SKIN = flat('S')
BONE = Mat('w', 'w', 'a')
CLOTH = Mat('a', 'b', 'd')
DARKC = Mat('b', 'd', 'd')
DD = flat('d')
KK = flat('k')


def legs(c, mat, top=33, foot=44, x=16.5, r=2.6, feet=DD, spread=1.0):
    p = c.new_part()
    c.capsule2(x, top, x - spread, foot - 1, r, mat, p)
    f = c.new_part()
    c.ellipse2(x - spread - 0.5, foot + 0.5, 3.6, 1.9, feet, f)
    return p


def face(c, y=10, x=17, mouth=True):
    c.stamp(x, y, "k", mirror=True)
    c.stamp(x, y + 1, "k", mirror=True)
    if mouth:
        c.stamp(19, y + 4, "kk")


# ================================================================ skeleton 骷髏兵 (with a rusty sabre)
@design('skeleton', 40, 48, mirrored=True)
def skeleton(c):
    lg = c.new_part()
    c.capsule2(16.5, 32, 15.5, 38, 1.3, BONE, lg)
    c.capsule2(15.5, 38, 15.5, 43, 1.3, BONE, lg)
    c.ellipse2(16, 38, 1.8, 1.6, BONE, lg)
    c.ellipse2(14.5, 44.5, 3.2, 1.6, BONE, lg)
    arm = c.new_part()
    c.capsule(13, 18, 10.5, 24, 1.2, BONE, arm)
    c.capsule(10.5, 24, 11, 30, 1.2, BONE, arm)
    c.ellipse(11, 31, 2.0, 2.0, BONE, arm)
    c.capsule(27, 18, 31, 23, 1.2, BONE, arm)
    c.capsule(31, 23, 32.5, 17, 1.2, BONE, arm)
    blade = c.new_part()
    c.poly([(31.5, 15), (32.5, 2), (35, 1.5), (34, 15)], Mat('w', 'w', 'a'), blade)
    guard = c.new_part()
    c.rect(30, 15, 35, 15, DD, guard, shade='flat')
    fist = c.new_part()
    c.ellipse(32.5, 17, 2.0, 1.9, BONE, fist)
    spine = c.new_part()
    c.rect(19, 16, 20, 31, BONE, spine, shade='flat')
    ribs = c.new_part()
    for y in (18, 21, 24):
        c.capsule2(20, y, 14, y + 1.5, 1.0, BONE, ribs)
    sh = c.new_part()
    c.capsule2(20, 16.5, 13, 17.5, 1.3, BONE, sh)
    pelvis = c.new_part()
    c.ellipse(20, 31, 5.5, 2.8, BONE, pelvis)
    cloth = c.new_part()
    c.poly2([(20, 30), (14, 30), (13.5, 36), (16, 35), (18, 37), (20, 35.5)], Mat('d', 'd', 'd'), cloth)
    skull = c.new_part()
    c.ellipse(20, 8.5, 7, 6.5, BONE, skull)
    c.rect(16, 12, 23, 15, BONE, skull)
    band = c.new_part(sep=False)
    c.rect(13, 5, 26, 6, flat('r'), band, shade='flat')
    c.finish()
    c.stamp(16, 9, "kk", mirror=True)
    c.stamp(16, 10, "ke", mirror=True)
    c.stamp(19, 12, "kk")
    c.stamp(17, 14, "kwkwkw")
    return c


# ================================================================ the drowned 水鬼 (hair over the face)
ROBE = Mat('w', 'a', 'a')
HAIR = Mat('b', 'b', 'b')


@design('drowned', 40, 48, mirrored=True)
def drowned(c):
    robe = c.new_part()
    c.poly2([(20, 16), (11, 19), (7, 40), (9, 46), (12, 42.5), (15, 46), (18, 42.5), (20, 46)], ROBE, robe)
    c.reshade(robe, 16, 24, 11, 20, Mat('w', 'a', 'a'), dw=0, hi=0.9)
    arms = c.new_part()
    c.capsule2(12, 21, 9, 31, 2.4, ROBE, arms)
    hands = c.new_part()
    c.capsule2(9, 32, 8.5, 36, 1.4, Mat('a', 'a', 'a'), hands)
    hair = c.new_part()
    c.ellipse(20, 10, 8.5, 8, HAIR, hair)
    c.poly2([(20, 6), (12, 9), (10.5, 30), (14, 33), (16, 29), (18, 32), (20, 29)], HAIR, hair)
    face = c.new_part(sep=False)
    c.poly([(18, 9), (22, 9), (22.5, 20), (17.5, 20)], Mat('a', 'a', 'a'), face, shade='flat')
    c.finish()
    for x in (12, 15):
        for y in range(12, 28, 1):
            if c.part[y][x] == hair and c.tone[y][x] == 'b' and (y // 3) % 2 == 0:
                c.paint(x, y, 'k')
                c.paint(39 - x, y, 'k')
    c.stamp(20, 13, "e")
    c.stamp(21, 13, "k")
    c.stamp(19, 17, "kk")
    for (x, y) in ((8, 38), (31, 38)):
        c.stamp(x, y, "w")
    return c


# ================================================================ little jiangshi 小殭屍 (a hopping corpse)
ROBEJ = Mat('b', 'b', 'd')
SKINJ = flat('S')


@design('littlejiangshi', 40, 48, mirrored=True)
def littlejiangshi(c):
    legs(c, DARKC, top=36, foot=44, x=17.5, r=2.4, spread=0.0)
    robe = c.new_part()
    c.poly2([(20, 17), (12, 18), (10.5, 38), (20, 38)], ROBEJ, robe)
    c.reshade(robe, 16, 22, 10, 18, ROBEJ, dw=1, hi=2)
    sleeve = c.new_part()
    c.capsule2(12, 20, 4, 21, 3.0, ROBEJ, sleeve)
    hands = c.new_part()
    c.poly2([(2, 19), (5, 19), (4.5, 26), (2.5, 26)], SKINJ, hands)
    badge = c.new_part()
    c.rect(16, 24, 23, 30, Mat('y', 'y', 'y'), badge, shade='flat')
    head = c.new_part()
    c.ellipse(20, 12, 6.5, 6, SKINJ, head)
    brim = c.new_part()
    c.ellipse(20, 7, 11, 2.6, Mat('d', 'd', 'd'), brim)
    hat = c.new_part()
    c.ellipse(20, 4.5, 6.5, 3.5, ROBEJ, hat)
    c.finish()
    # the talisman hanging from the hat over the face
    c.stamp(18, 8, """
kkkk
kyyk
kyrk
kyyk
kyrk
kyyk
kkkk
""")
    c.stamp(19, 1, "kk")
    c.stamp(19, 2, "rr")
    c.stamp(15, 11, "kk", mirror=True)
    c.stamp(17, 26, "dddddd")
    c.stamp(17, 28, "dddddd")
    return c


# ================================================================ bronze man 銅人 (a living temple statue)
METAL = BODY


@design('bronze', 40, 48, mirrored=True)
def bronze(c):
    lg = c.new_part()
    c.capsule2(15.5, 31, 11.5, 43, 3.0, METAL, lg)
    c.ellipse2(10.5, 44.5, 4, 1.9, METAL, lg)
    shorts = c.new_part()
    c.poly2([(20, 28), (13, 28), (11.5, 35), (17, 36), (20, 33)], DARKB, shorts)
    arm = c.new_part()
    c.capsule2(10, 17, 6, 24, 2.8, METAL, arm)
    c.capsule2(6, 24, 9, 13, 2.6, METAL, arm)
    c.ellipse2(9, 11, 3.2, 3.0, METAL, arm)
    torso = c.new_part()
    c.poly2([(20, 15), (11, 15.5), (9.5, 19), (13, 29), (20, 29)], METAL, torso)
    c.reshade(torso, 17, 18, 9, 12, METAL, dw=1)
    head = c.new_part()
    c.ellipse(20, 9, 5.5, 6, METAL, head)
    c.finish()
    c.stamp(16, 21, "dddd", mirror=True)
    c.stamp(19, 22, "d")
    c.stamp(19, 25, "dd")
    c.stamp(17, 8, "kk", mirror=True)
    c.stamp(17, 9, "ke", mirror=True)
    c.stamp(19, 12, "dd")
    return c


# ================================================================ bandit lackey 嘍囉 (headscarf and a club)
VEST = Mat('a', 'a', 'd')
PANTS = Mat('b', 'b', 'd')


@design('lackey', 40, 48, mirrored=True)
def lackey(c):
    legs(c, PANTS, top=31, foot=44, x=16, r=3.0, spread=1.5)
    arm = c.new_part()
    c.capsule(12, 18, 9.5, 29, 2.5, SKIN, arm)
    c.ellipse(9.5, 30.5, 2.6, 2.4, SKIN, arm)
    c.capsule(28, 18, 31, 13, 2.5, SKIN, arm)
    club = c.new_part()
    c.capsule(31, 12, 34, 3.6, 1.5, Mat('b', 'b', 'd'), club, r1=2.4)
    fist = c.new_part()
    c.ellipse(31, 13, 2.6, 2.4, SKIN, fist)
    chest = c.new_part()
    c.poly2([(20, 15), (12, 16), (12, 31), (20, 31)], SKIN, chest)
    vest = c.new_part()
    c.poly([(12, 16), (17, 16), (17.5, 31), (12, 31)], VEST, vest)
    c.poly([(28, 16), (23, 16), (22.5, 31), (28, 31)], VEST, vest)
    sash = c.new_part()
    c.rect(12, 27, 27, 29, DD, sash, shade='flat')
    head = c.new_part()
    c.ellipse(20, 10, 6.5, 6.5, SKIN, head)
    scarf = c.new_part()
    c.ellipse(20, 6.5, 7, 4, PANTS, scarf, clip=lambda x, y: y <= 7)
    c.finish()
    face(c, y=9)
    c.stamp(17, 13, "dddddd")
    return c


# ================================================================ archer 弓手 (bow drawn)
@design('archer', 40, 48, mirrored=True, open_slots='w')
def archer(c):
    legs(c, Mat('b', 'b', 'd'), top=31, foot=44, x=16.5, r=2.8, spread=1.0)
    arm = c.new_part()
    c.capsule(12, 18, 5, 20, 2.3, Mat('b', 'b', 'd'), arm)
    c.capsule(28, 18, 24, 22, 2.3, Mat('b', 'b', 'd'), arm)
    torso = c.new_part()
    c.poly2([(20, 15), (12, 16), (12.5, 32), (20, 32)], Mat('b', 'b', 'd'), torso)
    c.reshade(torso, 17, 19, 9, 13, Mat('b', 'b', 'd'), dw=1, hi=2)
    belt = c.new_part()
    c.rect(13, 27, 26, 28, DD, belt, shade='flat')
    head = c.new_part()
    c.ellipse(20, 10, 6.5, 6.5, SKIN, head)
    hood = c.new_part()
    c.ellipse(20, 7, 7.5, 5, Mat('b', 'b', 'd'), hood, clip=lambda x, y: y <= 7)
    c.finish()
    # the bow held out on the left: a curved stave and a straight white string
    c.stamp(1, 6, """
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
kddkwk
.kdkwk
.kdkwk
..kdkk
..kddk
...kk
""")
    c.stamp(4, 17, "kSSk")
    c.stamp(4, 18, "kSSk")
    # feathers of the quiver over the right shoulder
    c.stamp(26, 9, """
.kk.kk
kwwkwwk
kwwkwwk
.kdddk
..kdk
..kkk
""")
    face(c, y=9)
    return c


# ================================================================ assassin 刺客 (straw hat and a hidden blade)
@design('assassin', 40, 48, mirrored=True)
def assassin(c):
    legs(c, Mat('a', 'b', 'b'), top=31, foot=44, x=15.5, r=2.8, spread=2.0)
    arm = c.new_part()
    c.capsule2(12, 18, 9, 28, 2.4, Mat('a', 'b', 'b'), arm)
    c.ellipse2(9, 29.5, 2.3, 2.2, SKIN, arm)
    torso = c.new_part()
    c.poly2([(20, 15), (12, 16), (12, 32), (20, 32)], Mat('a', 'b', 'b'), torso)
    c.reshade(torso, 16, 19, 9, 13, Mat('a', 'b', 'b'), dw=1)
    sash = c.new_part()
    c.rect(12, 27, 27, 28, flat('d'), sash, shade='flat')
    head = c.new_part()
    c.ellipse(20, 12, 6, 5.5, flat('b'), head)
    hat = c.new_part()
    c.poly2([(20, 1.5), (16, 3.5), (5, 10.5), (6, 12), (20, 11)], Mat('d', 'd', 'd'), hat)
    c.finish()
    c.stamp(16, 13, "eek", mirror=True)
    c.stamp(16, 12, "kkk", mirror=True)
    for x in (10, 14, 18):
        c.stamp(x, 9, "k")
        c.stamp(39 - x, 9, "k")
    # a reversed dagger in the right hand
    c.stamp(29, 27, """
..kk
.kwwk
kwwak
kwak
kwak
kak
kk
""")
    return c


# ================================================================ rogue monk 野和尚 (staff and prayer beads)
ROBEM = Mat('b', 'b', 'd')
KASAYA = Mat('a', 'a', 'd')


@design('roguemonk', 40, 48, mirrored=True)
def roguemonk(c):
    legs(c, ROBEM, top=34, foot=44, x=16, r=2.6, spread=1.0)
    arm = c.new_part()
    c.capsule2(12, 18, 9, 28, 2.8, ROBEM, arm)
    c.ellipse2(9, 29.5, 2.5, 2.3, SKIN, arm)
    robe = c.new_part()
    c.poly2([(20, 15), (12, 16), (11, 37), (20, 37)], ROBEM, robe)
    c.reshade(robe, 16, 20, 10, 15, ROBEM, dw=1, hi=2)
    kas = c.new_part()
    c.poly([(12, 16), (16, 16), (28, 30), (28, 36), (24, 36), (12, 22)], KASAYA, kas)
    head = c.new_part()
    c.ellipse(20, 10, 6.5, 6.5, SKIN, head)
    c.finish()
    face(c, y=10)
    c.stamp(16, 9, "kk", mirror=True)
    c.stamp(18, 5, "k.k")
    c.stamp(19, 6, "k")
    c.stamp(16, 16, "kkkkkkkk")
    c.stamp(15, 17, "k........k")
    # the staff on the right
    for y in range(2, 46):
        c.stamp(32, y, "kdk")
    c.stamp(32, 1, "kkk")
    c.stamp(31, 2, "kaaak")
    c.stamp(31, 3, "kkkkk")
    c.stamp(32, 46, "kkk")
    return c


# ================================================================ sorcerer 妖道 (talisman raised)
ROBES = Mat('b', 'b', 'd')


@design('sorcerer', 40, 48, mirrored=True)
def sorcerer(c):
    robe = c.new_part()
    c.poly2([(20, 15), (12, 16), (9, 45), (20, 45)], ROBES, robe)
    c.reshade(robe, 16, 22, 10, 22, ROBES, dw=1, hi=2)
    trim = c.new_part(sep=False)
    c.rect(18, 16, 21, 44, flat('a'), trim, shade='flat')
    arm = c.new_part()
    c.capsule(12, 18, 8, 27, 2.8, ROBES, arm)
    c.capsule(28, 18, 32, 10, 2.8, ROBES, arm)
    head = c.new_part()
    c.ellipse(20, 10, 6, 6.5, SKIN, head)
    beard = c.new_part()
    c.poly2([(20, 12), (15, 12), (16, 18), (20, 24)], Mat('a', 'a', 'a'), beard)
    hat = c.new_part()
    c.ellipse(20, 4.5, 5.5, 3.2, DD, hat)
    c.capsule(20, 2.5, 20, 3, 1.2, DD, hat)
    c.finish()
    c.stamp(17, 9, "k", mirror=True)
    c.stamp(19, 13, "kk")
    c.stamp(19, 2, "yy")
    c.stamp(7, 26, """
kkkk
kSSk
kSSk
kkkk
""")
    # the talisman held up in the right hand
    c.stamp(29, 1, """
kkkkk
kyyyk
kyryk
kyyyk
kyryk
kyyyk
kkkkk
.kSSk
.kSSk
.kkkk
""")
    return c
