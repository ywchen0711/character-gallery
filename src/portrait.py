"""Portrait builder: 56x64 bust, 3/4 view facing left, light from the left.

Layers, back to front: background panel, back hair/headgear, body (clothes),
neck, head (faces.py), character overlays (beard, hair, hat ...).
Clothes silhouettes are shaded in bands from a contour; collars, armour plates,
hats, hair and beards are hand-authored grids in each character file.
"""
from pixlib import Layer, G
import faces

W, H = 56, 64
HEAD_X, HEAD_Y = 15, 10          # where the head grid's (0,0) goes

# shoulder contour: (row, left, right) - linear interpolation between keys
SHOULDERS = [(41, 21, 34), (42, 15, 40), (43, 11, 45), (44, 8, 48), (45, 6, 50),
             (47, 4, 52), (50, 3, 53), (63, 2, 55)]


def contour(keys, y):
    for (y0, l0, r0), (y1, l1, r1) in zip(keys, keys[1:]):
        if y0 <= y <= y1:
            t = (y - y0) / max(1, y1 - y0)
            return round(l0 + (l1 - l0) * t), round(r0 + (r1 - r0) * t)
    return None


def shade_band(t, ramp):
    """t in 0..1 across the body, left (lit) to right (shade)."""
    if t < 0.22:
        return ramp[0]
    if t < 0.55:
        return ramp[1]
    if t < 0.84:
        return ramp[2]
    return ramp[3]


def body_layer(keys=SHOULDERS, ramp='Ppqq', top=40):
    L = Layer(W, H)
    for y in range(top, H):
        c = contour(keys, y)
        if not c:
            continue
        l, r = c
        for x in range(l, r + 1):
            t = (x - l) / max(1, r - l)
            L.set(x, y, shade_band(t, ramp))
    return L


SHOULDERS_F = [(42, 22, 33), (43, 17, 38), (44, 14, 41), (45, 12, 44), (47, 9, 47),
               (50, 7, 49), (63, 5, 51)]


NECK_F = G('''
kSsdDDk
kSsdDDk
ksddDDk
kddDDDk
kdDDDDk
kDDDDDk
kDDDDDk
kDDDDk
''')


def neck_layer(female=False):
    L = Layer(W, H)
    if female:
        L.stamp(NECK_F, 24, 36)
        return L
    L.stamp(G('''
    kSsddDDDk
    kSsddDDDk
    ksdddDDDk
    kdddDDDDk
    kddDDDDDk
    kdDDDDDDk
    kDDDDDDDk
    kDDDDDDk
    '''), 23, 36)
    return L


def cross_collar(L, top=42, under='c', over='c', edge='C', inner='w', inner_hi='W', length=16, ox=0, wide=2):
    """Right-over-left (右衽) crossed collar: the top lapel runs from the right
    side of the neck down to the left; the under lapel from the left side of the
    neck down to the right until it meets the top lapel."""
    # under lapel and the inner garment
    for i in range(6):
        y = top + i
        x = 22 + i + ox
        L.set(x, y, under); L.set(x + 1, y, under)
        for xx in range(x + 2, 31 - i + ox):
            L.set(xx, y, inner_hi if xx < x + 4 else inner)
    # top lapel
    for i in range(length):
        y = top + i
        x = 31 - i + ox
        L.set(x, y, edge)
        for j in range(1, wide + 1):
            L.set(x + j, y, over)
        L.set(x + wide + 1, y, 'k' if i > 3 else over)
    return L


def panel(top, bot, frame='#0c0a10', inner='#c8a868'):
    """Plain vertical-gradient background panel with a thin frame (returns bg fn)."""
    from pixlib import hex2rgba
    a, b = hex2rgba(top), hex2rgba(bot)
    fr, inn = hex2rgba(frame), hex2rgba(inner)

    def bg(x, y):
        if x == 0 or y == 0 or x == W - 1 or y == H - 1:
            return fr
        t = y / (H - 1)
        # 4-step banding keeps the palette small and the look 16-bit
        t = round(t * 4) / 4
        return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3)) + (255,)
    return bg


FACTION_BG = {
    'wu': ('#3a1c1c', '#140a0c'),
    'shu': ('#1c2e1e', '#0a120c'),
    'wei': ('#1a2236', '#0a0c16'),
    'qun': ('#2e2416', '#100c08'),
}


def build(ch):
    """ch: module with PAL, FACTION, and optional BACK, BODY(L), FRONT overlays."""
    L = Layer(W, H)
    for item in getattr(ch, 'BACK', []):
        if callable(item):
            item(L)
            continue
        L.stamp(item[0], item[1], item[2], remap=item[3] if len(item) > 3 else None)
    body = ch.BODY() if hasattr(ch, 'BODY') else body_layer()
    fem = getattr(ch, 'HEAD', None) is faces.FEMALE
    if not getattr(ch, 'NO_ARMLINES', False):
        if fem:
            arm_lines(body, near=((40, 49), (42, 63)), far=((16, 51), (13, 63)))
        else:
            arm_lines(body)
    L.stamp(body.rows())
    L.stamp(neck_layer(getattr(ch, 'HEAD', None) is faces.FEMALE).rows(), only={'.'} | set('PpqQwW'))
    head = getattr(ch, 'HEAD', faces.MALE)
    L.stamp(head, HEAD_X, HEAD_Y)
    for item in getattr(ch, 'FACE', []):       # hair, beard, feature tweaks in head coords
        L.stamp(item[0], HEAD_X + item[1], HEAD_Y + item[2], remap=item[3] if len(item) > 3 else None)
    for item in getattr(ch, 'FRONT', []):
        if callable(item):
            item(L)
            continue
        L.stamp(item[0], item[1], item[2], remap=item[3] if len(item) > 3 else None)
    return L


def render(ch):
    L = build(ch)
    top, bot = FACTION_BG[ch.FACTION]
    return L.image(ch.PAL, bg=panel(top, bot))


def lamellar(L, ramp_from='PpqQ', light='MmnN', top=44, rows=None, xr=(0, 56)):
    """Re-tone body pixels into lamellar armour: bands of small plates 4 rows tall -
    a lit top edge, two rows of plates split by staggered dark seams, a dark lacing row.
    Body tones map to metal tones so the side light is kept."""
    tone = dict(zip(ramp_from, light))
    up = {light[0]: light[0], light[1]: light[0], light[2]: light[1], light[3]: light[2]}
    dn = {light[0]: light[1], light[1]: light[2], light[2]: light[3], light[3]: light[3]}
    for y in range(top, H if rows is None else min(H, top + rows)):
        band, ry = divmod(y - top, 4)
        for x in range(*xr):
            c = L.get(x, y)
            if c not in tone:
                continue
            t = tone[c]
            if ry == 0:
                t = up[t]
            elif ry == 3:
                t = dn[dn[t]]
            elif (x + band * 2) % 4 == 0:
                t = dn[t]
            L.set(x, y, t)
    return L


def arm_lines(L, ramp='PpqQ', near=((43, 48), (46, 63)), far=((13, 50), (10, 63))):
    """Darken one tone along the line where each upper arm meets the chest."""
    dn = {ramp[0]: ramp[1], ramp[1]: ramp[2], ramp[2]: ramp[3], ramp[3]: 'k'}
    for (x0, y0), (x1, y1) in (near, far):
        for y in range(y0, y1 + 1):
            x = round(x0 + (x1 - x0) * (y - y0) / max(1, y1 - y0))
            c = L.get(x, y)
            if c in dn:
                L.set(x, y, dn[c])
    return L


PAULDRON_NEAR = '''
.......kkkkkkk....
....kkkMMmmmmmnkk.
...kMMMmmmmmmmnnnk
..kMMmmmmmmmmnnnNk
..knnnnnnnnnnnNNNk
..kMMmmmmmmmmnnnNk
.kMmmmmmmmmmnnnNNk
.knnnnnnnnnnnNNNNk
.kMmmmmmmmmnnnNNNk
.kMmmmmmmmnnnnNNNk
.knnnnnnnnnnNNNNk.
..kkkkkkkkkkkkkk..
'''

PAULDRON_FAR = '''
.....kkkkk
...kkMMmmk
..kMMMmmnk
.kMMmmmmnk
.knnnnnnnk
kMMmmmmnnk
kMmmmmmnnk
knnnnnnnnk
kMmmmmmnnk
kMmmmmnnnk
knnnnnnnk.
.kkkkkkk..
'''
