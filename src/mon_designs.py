"""Monster designs drawn with mondraw: one function per base design, returning a finished Canvas.

Slot letters (each foe / beast maps them to NES colours, see nes_foes_art.py and nes_beasts_art.py):
  a b d   main material: light, mid, dark
  e f g   second material: light, mid, dark
  h i j   third material: light, mid, dark
  w       white / pale accent        r y   sprite-layer accents (eyes, glints)
  k       black (outline, mouths, pupils)
"""
from mondraw import Canvas, Mat, flat

BODY = Mat('a', 'b', 'd')
BODY2 = Mat('e', 'f', 'g')
BODY3 = Mat('h', 'i', 'j')
DARKB = Mat('b', 'd', 'd')          # the far limbs: in shadow
DARK2 = Mat('f', 'g', 'g')

DESIGNS = {}


def design(name, w, h, mirrored=False, open_slots=''):
    def deco(fn):
        DESIGNS[name] = dict(fn=fn, w=w, h=h, mirrored=mirrored, open_slots=open_slots)
        return fn
    return deco


def build(name):
    d = DESIGNS[name]
    c = Canvas(d['w'], d['h'])
    d['fn'](c)
    return c


# ================================================================ wolf (side, facing left)
@design('wolf', 48, 40)
def wolf(c):
    far = c.new_part()
    c.capsule(20, 26, 18, 35, 1.8, DARKB, far)
    c.ellipse(17.5, 36, 2.6, 1.6, DARKB, far)
    c.capsule(34, 25, 36, 35, 1.8, DARKB, far)
    c.ellipse(36.5, 36, 2.6, 1.6, DARKB, far)
    ear2 = c.new_part()
    c.poly([(13, 9), (17, 2), (18.5, 10)], DARKB, ear2)
    tail = c.new_part()
    c.capsule(39, 17, 44, 22, 3.0, BODY, tail)
    c.capsule(44, 22, 45, 31, 3.0, BODY, tail, r1=2.0)
    legs = c.new_part()
    c.capsule(15, 23, 14, 35, 2.4, BODY, legs, r1=1.9)
    c.ellipse(13, 36, 3.0, 1.7, BODY, legs)
    c.capsule(39, 27, 41, 35, 2.0, BODY, legs, r1=1.8)
    c.ellipse(41.5, 36, 3.0, 1.7, BODY, legs)
    body = c.new_part()
    c.ellipse(29, 20, 12, 6.5, BODY, body)
    c.ellipse(36.5, 23, 5.5, 6.5, BODY, body)
    c.ellipse(18, 20, 7, 8, BODY, body)
    c.reshade(body, 27, 19, 15, 9, BODY, hi=0.97)
    head = c.new_part()
    c.ellipse(12, 13, 6, 5.5, BODY, head)
    c.poly([(1, 12.5), (9, 10), (10, 17.5), (2, 16)], BODY, head)
    c.poly([(9, 9), (12.5, 1.5), (15.5, 9)], BODY, head)
    c.reshade(head, 11, 12, 7, 6, BODY, dw=1)
    c.finish()
    c.paint(2, 12, 'k')            # nose
    c.stamp(4, 16, "kkkk")         # mouth
    c.stamp(7, 11, "kk")           # brow
    c.stamp(8, 12, "rk")           # eye
    return c


WHITE = flat('w')

import mon_d1  # noqa: E402,F401  (registers more designs)
import mon_d2  # noqa: E402,F401
import mon_d3  # noqa: E402,F401
import mon_d4  # noqa: E402,F401
