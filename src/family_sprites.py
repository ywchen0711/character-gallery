"""Family sprites (cute HD-2D): same 40x60 canvas for all four, feet on the y=57 baseline.

Heads (front / back / side) are hand-authored grids per member. Bodies are built from a
few size parameters per member (shoulder width, torso, robe and leg lengths), so the
adults stand ~2.8 heads tall, Josh (10) ~2.4 and Jasper (8) ~2.2. Rendering goes through
the soft per-material shader, then a dark outline is drawn around the silhouette.
"""
from PIL import Image
from paint import Soft
from pixlib import G, hex2rgba, fliph

FW, FH = 40, 60
BASE = 57          # last row of the feet
CXS = 20           # centre column

SKIN = ['#7a4836', '#9c6046', '#bc7c5c', '#d69a76', '#e8b690', '#f4cea8', '#fde4c8']
HAIR = ['#07070c', '#10101a', '#1a1a28', '#262638', '#34364c', '#4a5068', '#6a7490']
OUTLINE = '#1e1418'

# head grid letters -> (material, tone); capitals lighter
HEAD_KEY = {
    'S': ('skin', 5.4), 's': ('skin', 4.3), 'd': ('skin', 3.0),
    'H': ('hair', 4.6), 'h': ('hair', 3.0), 'j': ('hair', 1.6),
}
FIX = {'k': OUTLINE, 'E': '#1a1218', 'm': '#c0705e', 'b': '#f0a090', 'g': '#5a4030', 'w': '#fff8f0'}


class Member:
    """Everything that differs between family members."""
    def __init__(self, name, ramps, head_front, head_back, head_side, extra_key=None, extra_fix=None,
                 sw=12, th=14, legs=14, robe=0, hem=0, cloth='cloth', trim='trim', legs_mat='pants',
                 boots='boots', sash='sash', head_dy=0):
        self.name = name
        self.ramps = ramps
        self.hf, self.hb, self.hs = head_front, head_back, head_side
        self.key = dict(HEAD_KEY, **(extra_key or {}))
        self.fix = dict(FIX, **(extra_fix or {}))
        self.sw, self.th, self.legs, self.robe, self.hem = sw, th, legs, robe, hem
        self.cloth, self.trim, self.legs_mat, self.boots, self.sash = cloth, trim, legs_mat, boots, sash
        self.head_dy = head_dy
        self.props = []        # callables (canvas, view, frame) drawn last

    @property
    def top(self):
        """Top row of the torso."""
        return BASE - self.legs - self.th + 1


class Canvas:
    def __init__(self, m):
        self.m = m
        self.S = Soft(FW, FH, dict(m.ramps, skin=SKIN, hair=HAIR))
        self.fixed = {}

    def put(self, x, y, mat, tone):
        self.S.put(x, y, mat, tone)

    def head(self, rows, x0, y0, flip=False):
        w = max(len(r) for r in rows)
        for y, r in enumerate(rows):
            r = r.ljust(w, '.')
            if flip:
                r = r[::-1]
            for x, c in enumerate(r):
                if c == '.':
                    continue
                if c in self.m.key:
                    mat, tone = self.m.key[c]
                    self.S.put(x0 + x, y0 + y, mat, tone)
                    self.fixed.pop((x0 + x, y0 + y), None)
                elif c in self.m.fix:
                    self.S.put(x0 + x, y0 + y, 'skin', 3)
                    self.fixed[(x0 + x, y0 + y)] = self.m.fix[c]

    def image(self):
        S = self.S
        S.soften(passes=1, weight=3.0)
        for (x, y), c in self.fixed.items():
            S.paint(x, y, c)
        im = S.image()
        P = im.load()
        oc = hex2rgba(OUTLINE)
        add = []
        for y in range(FH):
            for x in range(FW):
                if P[x, y][3] == 0 and any(0 <= x + dx < FW and 0 <= y + dy < FH and P[x + dx, y + dy][3] > 0
                                           and P[x + dx, y + dy][:3] != oc[:3]
                                           for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    add.append((x, y))
        for (x, y) in add:
            P[x, y] = oc
        # soft ground shadow under the feet
        sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
        Q = sh.load()
        for y in range(BASE - 1, FH):
            for x in range(FW):
                if ((x - CXS) / 10) ** 2 + ((y - BASE - 0.5) / 2) ** 2 <= 1:
                    Q[x, y] = (20, 14, 24, 80)
        sh.alpha_composite(im)
        return sh


# ------------------------------------------------------------------ bodies
def torso_front(c, m, top, back=False, arm=(0, 0), skirt_sway=0):
    """Torso with crossed Han collar (front) or plain back; arms with sleeves and hands."""
    sw, th = m.sw, m.th
    for i in range(th):
        y = top + i
        hw = sw / 2 - (0.5 if 2 < i < th - 3 else 0) + (0.5 if i == 0 else 0)
        for x in range(int(CXS - hw), int(CXS + hw + 0.99)):
            u = (x - (CXS - hw)) / max(1, 2 * hw)
            c.put(x, y, m.cloth, 5.0 - 3.0 * u - (0.6 if i < 1 else 0))
        if not back and i < 5:                            # Han crossed collar: a V, right lapel over left
            for x in range(CXS - 2 + i // 2, CXS + 3 - i):
                c.put(x, y, m.trim, 5.0)
            c.put(CXS - 3 + i, y, m.trim, 3.6)                # under lapel edge
            c.put(CXS + 3 - i, y, m.trim, 5.6)                # top lapel edge
            if i < 4:
                c.put(CXS + 4 - i, y, m.cloth, 1.4)
        if i == int(th * 0.6):                           # sash
            for x in range(int(CXS - hw), int(CXS + hw + 0.99)):
                c.put(x, y, m.sash, 4.6 - 2.2 * (x - CXS + hw) / (2 * hw))
                if not back:
                    c.put(x, y + 1, m.sash, 3.4 - 1.6 * (x - CXS + hw) / (2 * hw))
    # robe skirt below the torso
    for i in range(m.robe):
        y = top + th + i
        hw = sw / 2 + 0.6 + i * 0.25
        for x in range(int(CXS - hw + skirt_sway * (i / max(1, m.robe))), int(CXS + hw + 0.99 + skirt_sway * (i / max(1, m.robe)))):
            u = (x - (CXS - hw)) / max(1, 2 * hw)
            c.put(x, y, m.cloth, 4.6 - 3.0 * u)
        if not back and i < m.robe - 1:
            c.put(CXS + 1, y, m.cloth, 1.6)
    # arms: sleeves then hands
    for side, dy in ((-1, arm[0]), (1, arm[1])):
        ax = int(CXS + side * (sw / 2 + 1.0))
        for i in range(1, th - 2 + dy):
            for k in range(3):
                x = ax + side * (k - 1)
                c.put(x, top + i, m.cloth, (4.2 if side < 0 else 2.2) - k * 0.6 * side)
        hy = top + th - 3 + dy
        for (dx, dyy) in ((0, 0), (side, 0), (0, 1), (side, 1)):
            c.put(ax + dx, hy + dyy, 'skin', 4.6 if side < 0 else 3.6)


def legs_front(c, m, phase=0):
    """phase 0 stand, 1 left foot forward (lower), 2 right foot forward."""
    top = BASE - m.legs + 1 + m.robe
    for side in (-1, 1):
        lift = 1 if (phase == 1 and side == 1) or (phase == 2 and side == -1) else 0
        x0 = CXS + (-3 if side < 0 else 1)
        for y in range(top, BASE + 1 - lift):
            boot = y >= BASE - 2 - lift
            for k in range(3):
                mat = m.boots if boot else m.legs_mat
                c.put(x0 + k, y, mat, (4.4 if side < 0 else 3.0) - k * 0.6)
        if not lift:
            c.put(x0 + (-1 if side < 0 else 3), BASE, m.boots, 2.4)


def legs_side(c, m, phase):
    """Side view facing left. phase: 'a' / 'b' strides, 'p' passing."""
    top = BASE - m.legs + 1 + m.robe
    n = BASE - top + 1
    if phase == 'p':
        plan = [(0, 0)]
    else:
        s = max(2, n // 3)
        plan = [(-s, 0), (s, 1)] if phase == 'a' else [(s, 0), (-s, 1)]
    for (reach, far) in plan:
        for i in range(n):
            t = i / max(1, n - 1)
            x = CXS - 1 + round(reach * t)
            y = top + i
            boot = y >= BASE - 1
            for k in range(3):
                c.put(x + k, y, m.boots if boot else m.legs_mat, (3.0 if far else 4.4) - k * 0.5)
        c.put(CXS - 2 + reach, BASE, m.boots, 3.0 if far else 4.0)


def torso_side(c, m, top, swing=0):
    sw, th = m.sw, m.th
    hw = max(3, sw / 2 - 2)
    for i in range(th):
        y = top + i
        for x in range(int(CXS - hw), int(CXS + hw + 0.99)):
            u = (x - (CXS - hw)) / max(1, 2 * hw)
            c.put(x, y, m.cloth, 4.8 - 2.6 * u)
        if i == int(th * 0.6):
            for x in range(int(CXS - hw), int(CXS + hw + 0.99)):
                c.put(x, y, m.sash, 4.2)
    for i in range(m.robe):
        y = top + th + i
        h2 = hw + 0.5 + i * 0.25
        for x in range(int(CXS - h2), int(CXS + h2 + 0.99)):
            c.put(x, y, m.cloth, 4.4 - 2.4 * (x - CXS + h2) / (2 * h2))
    # near arm swinging
    for i in range(1, th - 2):
        x = CXS + round(swing * i / th)
        for k in range(3):
            c.put(x - 1 + k, top + i, m.cloth, 3.8 - k * 0.5)
    hx = CXS + round(swing * (th - 2) / th)
    for (dx, dy) in ((0, 0), (1, 0), (0, 1), (1, 1)):
        c.put(hx - 1 + dx, top + th - 2 + dy, 'skin', 4.4)


def head_pos(m, rows):
    h, w = len(rows), max(len(r) for r in rows)
    return CXS - w // 2, m.top - h + 2 + m.head_dy


def frame(m, view='down', phase=0, bob=0, arm=(0, 0), extra=None, side_phase='p', swing=0):
    c = Canvas(m)
    top = m.top + bob
    pv = 'left' if view == 'right' else view       # right-facing frames are mirrored left ones
    for p in m.props:
        p(c, pv, 'back', phase)
    if view in ('down', 'up'):
        legs_front(c, m, phase)
        torso_front(c, m, top, back=(view == 'up'), arm=arm)
        rows = m.hf if view == 'down' else m.hb
        x0, y0 = head_pos(m, rows)
        c.head(rows, x0, y0 + bob)
    else:
        legs_side(c, m, side_phase)
        torso_side(c, m, top, swing=swing)
        x0, y0 = head_pos(m, m.hs)
        c.head(m.hs, x0, y0 + bob)
    for p in m.props:
        p(c, pv, 'front', phase)
    if extra:
        extra(c)
    im = c.image()
    if view == 'right':
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return im


def animations(m, action):
    side = lambda v: [frame(m, v, side_phase='a', swing=2), frame(m, v, bob=-1, side_phase='p', swing=0),
                      frame(m, v, side_phase='b', swing=-2), frame(m, v, bob=-1, side_phase='p', swing=0)]
    return {
        'idle': [frame(m), frame(m), frame(m, bob=1), frame(m, bob=1)],
        'walk_down': [frame(m, 'down', 1, arm=(1, -1)), frame(m, 'down', 0, bob=-1),
                      frame(m, 'down', 2, arm=(-1, 1)), frame(m, 'down', 0, bob=-1)],
        'walk_up': [frame(m, 'up', 1, arm=(1, -1)), frame(m, 'up', 0, bob=-1),
                    frame(m, 'up', 2, arm=(-1, 1)), frame(m, 'up', 0, bob=-1)],
        'walk_left': side('left'),
        'walk_right': side('right'),
        'action': action(m),
    }
