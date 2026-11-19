"""The family set: one cute HD-2D (Octopath-like) style shared by Jeff, Erin, Josh and Jasper.

Portraits (72x80): soft painterly shading on hand-specified face contours, hair built
from rounded locks and buns, and hand-placed small dark eyes, brows, nose, mouth.
Sprites live in family_sprites.py.
"""
import math
from PIL import Image
from paint import Soft, tint_image
from pixlib import G, hex2rgba

PW, PH = 72, 80

SKIN = ['#7a4836', '#9c6046', '#bc7c5c', '#d69a76', '#e8b690', '#f4cea8', '#fde4c8']
HAIR_BLACK = ['#07070c', '#10101a', '#1a1a28', '#262638', '#34364c', '#4a5068', '#6a7490']
HAIR_BROWN = ['#140c08', '#22140e', '#321e14', '#44291b', '#583624', '#6e4630', '#86583e']

# face contour: (y, half-width) keys, interpolated; the far (left) side is narrowed for a slight 3/4 turn
FACE_KEYS = {
    'man': [(12, 7), (14, 11), (16, 14), (20, 16), (26, 16.5), (36, 16.5), (42, 16.2), (46, 15.4), (50, 13.8),
            (54, 11.4), (57, 8.4), (59, 5.5), (60, 3)],
    'woman': [(13, 7), (15, 11), (17, 13.5), (21, 15.2), (27, 15.6), (36, 15.6), (42, 15.2), (46, 14), (50, 11.8),
              (53, 9), (56, 5), (57, 2.5)],
    'boy': [(13, 9), (15, 13), (17, 16), (21, 18), (27, 18.5), (37, 18.5), (43, 17.5), (47, 15.8), (51, 13),
            (54, 9.5), (56, 5)],
    'kid': [(14, 9), (16, 13), (18, 16), (22, 18), (28, 19), (38, 19), (43, 18), (47, 16), (50, 13), (53, 9),
            (55, 4)],
}
EYE_Y = {'man': 36, 'woman': 36, 'kid': 38, 'boy': 37}
CX = 36


def interp(keys, y):
    if y < keys[0][0] or y > keys[-1][0]:
        return None
    for (y0, a), (y1, b) in zip(keys, keys[1:]):
        if y0 <= y <= y1:
            return a + (b - a) * (y - y0) / max(1, y1 - y0)
    return None


def ellipse(cx, cy, rx, ry):
    return lambda x, y: ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1


def lock(x0, y0, w, length, lean=0.0):
    """A rounded, tapered lock of hair hanging from (x0, y0)."""
    def f(x, y):
        if y < y0 or y > y0 + length:
            return False
        t = (y - y0) / length
        cx = x0 + lean * t * length
        half = w * (1 - t ** 1.6) + 0.3
        return abs(x - cx) <= half
    return f


class Portrait:
    def __init__(self, kind, bg=('#3a3040', '#6a5040'), lights=()):
        self.kind = kind
        self.S = Soft(PW, PH, {'skin': SKIN, 'neck': SKIN})
        self.tints = {}
        self.fixed = {}
        self.bg = bg
        self.lights = lights

    # ---- building blocks
    def ramp(self, name, colours):
        self.S.ramps[name] = colours

    def fill(self, mat, test, tone, box=(0, 0, PW, PH)):
        x0, y0, x1, y1 = box
        for y in range(y0, y1):
            for x in range(x0, x1):
                if test(x, y):
                    self.S.put(x, y, mat, tone(x, y) if callable(tone) else tone)

    def face(self):
        keys = FACE_KEYS[self.kind]
        top, bot = keys[0][0], keys[-1][0]
        for y in range(top, bot + 1):
            hw = interp(keys, y)
            for x in range(PW):
                u = (x - CX) / hw
                if u < 0:
                    u = u / 0.93
                if abs(u) > 1:
                    continue
                v = (y - top) / (bot - top)
                t = 5.1 - 1.7 * u - 0.7 * v
                if abs(u) > 0.78:
                    t -= 1.6 * (abs(u) - 0.78) / 0.22
                if v > 0.9:
                    t -= (v - 0.9) * 8
                self.S.put(x, y, 'skin', max(0.3, min(6, t)))
        # ears (near ear on the right)
        ey = EYE_Y[self.kind]
        hw = interp(keys, ey + 3)
        self.fill('skin', ellipse(CX + hw + 0.5, ey + 4, 2.6, 4.6), 2.6, (0, 0, PW, PH))
        self.fill('skin', ellipse(CX + hw + 0.2, ey + 4, 1.0, 2.6), 1.6, (0, 0, PW, PH))

    def neck(self, half=6):
        keys = FACE_KEYS[self.kind]
        bot = keys[-1][0]
        for y in range(bot - 8, PH):
            for x in range(CX - half, CX + half + 1):
                if self.S.get(x, y) is None:
                    self.S.put(x, y, 'neck', 1.8 if y < bot + 3 else 2.8 - (x - CX) / half)

    def eyes(self, grid_l, grid_r, gap=7, dy=0):
        ey = EYE_Y[self.kind] + dy
        self.stamp_fixed(grid_l, CX - 2 - gap - len(grid_l[0]) + 2, ey)
        self.stamp_fixed(grid_r, CX - 2 + gap - 1, ey)

    def stamp_fixed(self, rows, x0, y0, pal=None):
        pal = pal or FEAT
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                if c == '.':
                    continue
                if c in pal:
                    self.fixed[(x0 + x, y0 + y)] = pal[c]
                elif c in '0123456':          # skin tone override
                    self.S.t[y0 + y][x0 + x] = float(c)

    def blush(self, dx=10, dy=7, rx=3.4, ry=1.8, col='#f08a80', a=0.38):
        ey = EYE_Y[self.kind]
        for side, k in ((-1, 0.8), (1, 1.0)):
            cx, cy = CX - 2 + side * dx, ey + dy
            for y in range(int(cy - ry - 1), int(cy + ry + 2)):
                for x in range(int(cx - rx - 1), int(cx + rx + 2)):
                    d = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
                    if d <= 1 and self.S.get(x, y) == 'skin':
                        self.tints[(x, y)] = (col, a * k * (1 - d * 0.6))

    def shade_under(self, mat='hair', target='skin', depth=2, amount=1.3):
        """Soft shadow cast by hair (fringe) on the skin just below it."""
        S = self.S
        for y in range(PH):
            for x in range(PW):
                if S.get(x, y) == target and any(S.get(x, y - d) == mat for d in range(1, depth + 1)):
                    S.t[y][x] = max(0.3, S.t[y][x] - amount)

    def render(self, soften=2, edge=('hair',)):
        self.S.soften(passes=soften)
        S = self.S
        for y in range(PH):            # crisp darker rim where hair meets the background
            for x in range(PW):
                if S.get(x, y) in edge and any(S.get(x + dx, y + dy) is None
                                               for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    S.t[y][x] = min(S.t[y][x], 0.6)
        for (x, y), c in self.fixed.items():
            self.S.paint(x, y, c)
        bg0, bg1 = hex2rgba(self.bg[0]), hex2rgba(self.bg[1])
        lights = self.lights

        def bg(x, y):
            t = y / PH
            c = [bg0[i] + (bg1[i] - bg0[i]) * t for i in range(3)]
            for (lx, ly, lr, col) in lights:
                d = math.hypot(x - lx, y - ly)
                if d < lr:
                    k = 0.5 * (1 - (d / lr) ** 2)
                    lc = hex2rgba(col)
                    c = [c[i] + (lc[i] - c[i]) * k for i in range(3)]
            q = 5
            return tuple(int(v) // q * q for v in c) + (255,)
        im = self.S.image(bg)
        return tint_image(im, self.tints)


FEAT = {
    'k': '#2a1814',      # lash / lid line
    'E': '#1c1418',      # iris
    'e': '#4a3430',      # iris lower (warm)
    'W': '#fff8f0',      # catchlight
    'b': '#2a2026',      # brow
    'm': '#a0524a',      # mouth line
    'l': '#e88a80',      # lip / tongue
    'w': '#fffaf2',      # teeth
    'n': '#b8785a',      # nose shadow
    'N': '#fde8d0',      # nose highlight
    'g': '#5a4434',      # glasses rim
    'G': '#c8dcec',      # glasses glint
}


def hair_tone(cx, cy, sheen_r, sheen_w=2.2):
    """Soft lit hair: brighter up-left, a sheen ring, fine strands."""
    def f(x, y):
        a = math.atan2(y - cy, x - cx)
        r = math.hypot(x - cx, y - cy)
        t = 3.6 - (x - cx) / 22 * 1.6 - (y - cy) / 30 * 0.8
        if abs(r - sheen_r) < sheen_w and -2.6 < a < -0.5:
            t += 1.8 * (1 - abs(r - sheen_r) / sheen_w)
        if math.sin(a * 22 + r * 0.1) > 0.78:
            t -= 0.9
        return max(0.2, min(6, t))
    return f
