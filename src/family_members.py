"""The four family members as sprites: hand-drawn heads, body sizes, colours, props, actions.

Heights on the shared 40x60 canvas (feet on y=57): Jeff ~45 px (2.8 heads), Erin ~43 (2.7),
Josh (10) ~36 (2.4), Jasper (8) ~33 (2.2).
"""
from pixlib import G
import family_sprites as fs

INNER = ['#7a6e5a', '#968a72', '#b2a68c', '#cabfa4', '#ddd4ba', '#ece6d0', '#f8f4e6']
WOOD = ['#3a2414', '#54341c', '#6e4626', '#885a32', '#a2703e', '#ba884e', '#d0a264']
BOOTS = ['#1a120e', '#261a12', '#342318', '#422d1e', '#523826', '#644430', '#78523a']
PANTS_DARK = ['#1a1a20', '#26262e', '#34343e', '#44444f', '#565662', '#6a6a76', '#80808c']
PANTS_BROWN = ['#2a1e14', '#3a2a1e', '#4a3826', '#5a4630', '#6c563a', '#806a48', '#947e58']
LEATHER = ['#4a3018', '#5e3c1e', '#744a26', '#8a5a30', '#a06c3a', '#b88048', '#cc9658']
METAL = ['#30343c', '#4a505a', '#666e7a', '#868e9a', '#a4acb8', '#c4ccd6', '#e2e8f0']
GOLD = ['#3a2a10', '#5a4018', '#7a5a22', '#9a742e', '#b8903c', '#d2ac52', '#e8c86e']
LEAF = ['#1c3a18', '#285020', '#36682a', '#4a8236', '#62a046', '#80ba5c', '#a2d27a']
GLOW = ['#3a7a50', '#4c9a62', '#62b876', '#80d090', '#a0e4ac', '#c4f2cc', '#eafff0']

# ================================================================== Jasper (8): little scout
J_FRONT = G('''
.kkk........kkk.
kHHhk......kHhhk
kHhhkkkkkkkkhhjk
kkHHHHHHhhhhhhkk
kHHHHHHHhhhhhhjk
kHHkHHkHhkhkhhjk
kHkSSkSSSkSSkhjk
kjSSSSSSSSSSSsjk
kSSSSSSSSSSSSssk
kSSSESSSSSSESssk
kSSSESSSSSSESssk
kSbbSSSSSSSbbssk
.kSSSSSmmSSSssk.
..kSSSSSSSSssk..
...kkkkkkkkkk...
''')
J_BACK = G('''
.kkk........kkk.
kHHhk......kHhhk
kHhhkkkkkkkkhhjk
kkHHHHHHhhhhhhkk
kHHHHHHHhhhhhhjk
kHHHHHHhhhhhhhjk
kHHHHHhhhhhhhhjk
kHHHHhhhhhhhhjjk
kjHHhhhhhhhhjjjk
kjjhhhhhhhhhjjjk
kjjjhhhhhhhjjjjk
kSjjjjjjjjjjjjsk
.kSSjjjjjjjjssk.
..kSSSSSSSSssk..
...kkkkkkkkkk...
''')
J_SIDE = G('''
.........kkk...
........kHHhk..
....kkkkkHhhk..
...kHHHHHhhkk..
..kHHHHHHhhhhk.
.kHHkHHHhhhhjk.
.kHkSSkHhhhjjk.
kSSSSSSkhhhjjk.
kSSSSSSSdkhjjk.
kSESSSSSddkjk..
kSESSSSSSdkjk..
.kSbbSSSSSdk...
.kmSSSSSSssk...
..kkSSSSssk....
....kkkkkk.....
''')
J_RAMPS = {
    'cloth': ['#1c3a1e', '#285028', '#346a32', '#46843e', '#5ea04e', '#7cba64', '#9cd07e'],
    'trim': INNER, 'sash': WOOD, 'pants': PANTS_BROWN, 'boots': BOOTS, 'wood': WOOD, 'bag': LEATHER,
    'stone': METAL,
}


def jasper():
    m = fs.Member('jasper', J_RAMPS, J_FRONT, J_BACK, J_SIDE, sw=10, th=10, legs=10, robe=0, head_dy=1)

    def bag(c, view, layer, phase):
        if layer != 'front':
            return
        top = m.top
        if view == 'down':                    # satchel on the hip, strap across the chest
            for i in range(m.th - 1):
                c.put(fs.CXS - 4 + i, top + i, 'bag', 3.6)
            for y in range(top + m.th - 3, top + m.th + 1):
                for x in range(fs.CXS + 3, fs.CXS + 7):
                    c.put(x, y, 'bag', 4.4 - (x - fs.CXS - 3) * 0.6)
        elif view == 'up':
            for i in range(m.th - 1):
                c.put(fs.CXS + 4 - i, top + i, 'bag', 3.0)
        else:
            for y in range(top + m.th - 3, top + m.th + 1):
                for x in range(fs.CXS + 1, fs.CXS + 5):
                    c.put(x, y, 'bag', 4.0)
    m.props.append(bag)
    return m


def jasper_action(m):
    """Slingshot, side view: raise and aim, pull, release (a pebble flies off), settle."""
    def sling(pull, shot, fly=0):
        def f(c):
            top = m.top
            hx, hy = fs.CXS - 8, top + 2
            for x in range(hx + 1, fs.CXS + 1):                # arm stretched forward
                for dy in (0, 1, 2):
                    c.put(x, hy + 4 + dy, 'cloth', 4.6 - dy * 0.8)
            for (dx, dy) in ((0, 0), (1, 0), (0, 1), (1, 1)):
                c.put(hx + dx, hy + 4 + dy, 'skin', 4.8)
            for y in range(hy + 1, hy + 5):                    # Y-shaped slingshot
                c.put(hx, y, 'wood', 4.6)
            for k in (1, 2):
                c.put(hx - k, hy + 1 - k, 'wood', 4.4)
                c.put(hx + k, hy + 1 - k, 'wood', 3.2)
            back = hx + pull
            for x in range(hx - 1, back + 1):                   # band pulled back toward the cheek
                c.fixed[(x, hy - 1)] = '#e0b080'
            if not shot and pull > 3:
                c.put(back, hy - 1, 'stone', 4.5)
            if shot:
                for i in range(3):
                    c.fixed[(hx - 4 - fly - i * 2, hy - 2)] = '#fff4c0' if i else '#9a9aa4'
        return f
    return [fs.frame(m, 'left', side_phase='a', swing=0, extra=sling(3, False)),
            fs.frame(m, 'left', side_phase='a', bob=1, extra=sling(7, False)),
            fs.frame(m, 'left', side_phase='a', extra=sling(1, True, 0)),
            fs.frame(m, 'left', side_phase='a', extra=sling(1, True, 8))]


# ================================================================== Josh (10): the brave protector
O_FRONT = G('''
......kkkk......
.....kHHhhk.....
...kkkkYYkkkk...
..kHHHHHHhhhhk..
.kHHHkHHkhhkhjk.
kHHkHHkHHkhhkhjk
kYYYYYYYYyyyyyyk
kSSkSSSSSSSkSsjk
kSSSSSSSSSSSSssk
kSkkSSSSSSkkSssk
kSSESSSSSSESSssk
kSSESSSSSSESSssk
kSbbSSkwwkSbbssk
.kSSSSSmmSSSssk.
..kSSSSSSSSssk..
...kkkkkkkkkk...
''')
O_BACK = G('''
......kkkk......
.....kHHhhk.....
...kkkkYYkkkk...
..kHHHHHHhhhhk..
.kHHHHHHhhhhhjk.
kHHHHHHhhhhhhhjk
kYYYYYYYyyyyyyyk
kHHHHHhhhhhhhjjk
kjHHhhhhhhhhhjjk
kjjhhhhhhhhhjjjk
kjjjhhhhhhhjjjjk
kSjjjjjjjjjjjjsk
.kSSjjjjjjjjssk.
..kSSSSSSSSssk..
...kkkkkkkkkk...
''')
O_SIDE = G('''
.......kkkk....
......kHHhhk...
....kkkkYYkk...
...kHHHHHhhhk..
..kHHkHHHhhhhk.
.kHHkHHHhhhhjk.
.kYYYYYYYyyyyky
kSSkSSkHhhhjjky
kSSSSSSSdkhjjk.
kSkkSSSSddkjk..
kSESSSSSSdkjk..
.kSbbSSSSSdk...
.kmwSSSSSssk...
..kkSSSSssk....
....kkkkkk.....
''')
O_RAMPS = {
    'cloth': ['#4a1410', '#6a1e16', '#8a2c1e', '#aa4028', '#c85a34', '#e07a46', '#f09c62'],
    'trim': INNER, 'sash': GOLD, 'band': GOLD, 'pants': PANTS_DARK, 'boots': BOOTS, 'wood': WOOD, 'metal': METAL,
}
O_KEY = {'Y': ('band', 5.0), 'y': ('band', 3.4)}


def shield_disc(c, cx, cy, r=5.5, face=True):
    for y in range(int(cy - r - 1), int(cy + r + 2)):
        for x in range(int(cx - r - 1), int(cx + r + 2)):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if d <= r:
                if d > r - 1.2:
                    c.put(x, y, 'metal', 4.6 if (x - cx) + (y - cy) < 0 else 2.6)
                elif face and d < 1.2:
                    c.put(x, y, 'metal', 5.2)
                else:
                    c.put(x, y, 'wood', 4.8 - ((x - cx) + (y - cy)) / r * 1.4)


def josh():
    m = fs.Member('josh', O_RAMPS, O_FRONT, O_BACK, O_SIDE, extra_key=O_KEY, sw=11, th=12, legs=11, head_dy=1)

    def gear(c, view, layer, phase):
        top = m.top
        if layer == 'back' and view == 'down':            # shield on his back peeks out
            shield_disc(c, fs.CXS + 6, top + 3, 5.5, face=False)
        if layer == 'front' and view == 'up':
            shield_disc(c, fs.CXS, top + 5, 6)
        if layer == 'back' and view == 'left':
            shield_disc(c, fs.CXS + 4, top + 5, 5.5)
        if layer == 'front' and view == 'down':           # wooden practice stick in his hand
            for y in range(top + 2, top + m.th + 4):
                c.put(fs.CXS - 8, y, 'wood', 4.4)
    m.props.append(gear)
    return m


def josh_action(m):
    """Shield up: brace, shield thrust forward with the stick raised, hold (a glint), relax."""
    def block(raise_, glint=False):
        def f(c):
            top = m.top
            if raise_:
                shield_disc(c, fs.CXS - 2, top + 7 + (1 if raise_ == 2 else 0), 6.5)
                for i in range(9):                               # stick raised high
                    c.put(fs.CXS + 8 - i // 3, top - 6 + i, 'wood', 4.6)
                if glint:
                    for (dx, dy) in ((0, -1), (-1, 0), (0, 0), (1, 0), (0, 1)):
                        c.fixed[(fs.CXS - 5 + dx, top + 2 + dy)] = '#fffbe0'
        return f
    return [fs.frame(m, 'down', 0, bob=1),
            fs.frame(m, 'down', 1, bob=1, extra=block(1)),
            fs.frame(m, 'down', 1, bob=1, extra=block(2, True)),
            fs.frame(m, 'down', 0, extra=block(1))]


# ================================================================== Jeff (father): engineer and tactician
F_FRONT = G('''
......kkkk......
.....kHHhhk.....
...kkkkggkkkk...
..kHHHHHHhhhhk..
.kHHHHHHHHhhhjk.
kHHHHHHHHHhhhhjk
kHHkkSSkkHhhhhjk
kHkSSSSSSkkhhhjk
kjSSSSSSSSSSkhjk
kSaaaSSSSaaaSsjk
kSaEaaaaaaEaSssk
kSaEaSSSSaEaSssk
kSaaaSSSSaaaSssk
kSSSSSmmmSSSsddk
.kSSSSSSSSSSsdk.
..kkSSSSSSssdk..
....kkkkkkkk....
''')
F_BACK = G('''
......kkkk......
.....kHHhhk.....
...kkkkggkkkk...
..kHHHHHHhhhhk..
.kHHHHHHHhhhhjk.
kHHHHHHHhhhhhhjk
kHHHHHHhhhhhhhjk
kHHHHHhhhhhhhjjk
kHHHHhhhhhhhhjjk
kjHHhhhhhhhhjjjk
kjjhhhhhhhhhjjjk
kSjjhhhhhhhhjjsk
kSSjjjjjjjjjjssk
kSSSSSSSSSSSsddk
.kSSSSSSSSSSsdk.
..kkSSSSSSssdk..
....kkkkkkkk....
''')
F_SIDE = G('''
......kkkk.....
.....kHHhhk....
....kkkggkk....
...kHHHHHhhhk..
..kHHHHHHhhhhk.
.kHHHHHHhhhhjk.
.kHkkSHHhhhhjk.
kSSSSSkHhhhjjk.
kSSSSSSkdhhjjk.
kSaaSSSSdkjjk..
aaEaaaaSddkjk..
kaEaSSSSSdkk...
kSaaSSSSSdk....
kSSSSSSSssk....
.kmmSSSSssk....
..kkSSSSsk.....
....kkkkk......
''')
F_RAMPS = {
    'cloth': ['#1e2014', '#2c301c', '#3e4426', '#525a32', '#68723e', '#808a4e', '#9aa264'],
    'trim': INNER, 'sash': LEATHER, 'pants': PANTS_DARK, 'boots': BOOTS, 'metal': METAL, 'strap': LEATHER,
    'spark': ['#a06010', '#c88020', '#e8a830', '#f8c848', '#ffe070', '#fff0a0', '#fffbe0'],
}
F_FIX = {'a': '#b08c6c', 'g': '#5e3816'}


def jeff():
    m = fs.Member('jeff', F_RAMPS, F_FRONT, F_BACK, F_SIDE, extra_fix=F_FIX, sw=13, th=16, legs=15, robe=6, head_dy=1)

    def tools(c, view, layer, phase):
        if layer != 'front':
            return
        top = m.top
        if view == 'down':                         # wrench hanging at the hip
            x = fs.CXS + 5
            for y in range(top + 10, top + 15):
                c.put(x, y, 'metal', 4.6)
            c.put(x - 1, top + 15, 'metal', 4.0); c.put(x + 1, top + 15, 'metal', 3.0)
        elif view == 'left':
            for y in range(top + 10, top + 14):
                c.put(fs.CXS + 2, y, 'metal', 4.4)
    m.props.append(tools)
    return m


def jeff_action(m):
    """Fix-it: raise the wrench, give it a twist, a spark flies, a satisfied nod."""
    def wrench(up, spark=0):
        def f(c):
            top = m.top
            hx = fs.CXS + 9
            hy = top + (1 if up else 8)
            for y in range(hy, hy + 6):                       # arm raised
                for k in range(3):
                    c.put(hx - 1 + k, y + 2, 'cloth', 3.4 - k * 0.5)
            c.put(hx, hy + 1, 'skin', 4.6); c.put(hx + 1, hy + 1, 'skin', 4.0)
            for i in range(6):                                 # wrench
                c.put(hx + i // 3, hy - i, 'metal', 5.0 - i * 0.2)
            c.put(hx + 1, hy - 6, 'metal', 4.4); c.put(hx + 3, hy - 6, 'metal', 4.4); c.put(hx + 2, hy - 7, 'metal', 3.6)
            if spark:
                sx, sy = hx + 4, hy - 9
                pts = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)] + ([(2, -2), (-2, 2), (2, 2), (-2, -2)] if spark > 1 else [])
                for (dx, dy) in pts:
                    c.fixed[(sx + dx, sy + dy)] = '#fff4b0' if (dx, dy) == (0, 0) else '#f8c040'
        return f
    return [fs.frame(m, 'down', 0, extra=wrench(False)),
            fs.frame(m, 'down', 0, bob=-1, extra=wrench(True)),
            fs.frame(m, 'down', 0, bob=-1, extra=wrench(True, 1)),
            fs.frame(m, 'down', 0, bob=0, extra=wrench(True, 2))]


# ================================================================== Erin (mother): healer, reads the weather
E_FRONT = G('''
.....kkkkkk.....
...kkHHHhhhkk...
..kHHHHkhhhhhk..
.kHHHHHjhhhhhhk.
.kHHHHjSjhhhhhk.
kHHHHjSSSjhhhhjk
kHHHjSSSSSjhhhjk
kHHjSSSSSSSjhhjk
kHjSSSSSSSSSjhjk
kHjSSESSSSESShjk
kHjSSESSSSESShjk
kHjSbbSSSSbbShjk
kHHjSSSmmSSShhjk
kHHjkSSSSSSkhhjk
kHHk.kkkkkk.khjk
.kHk........khk.
..k..........k..
''')
E_BACK = G('''
.....kkkkkk.....
...kkHHHhhhkk...
..kHHHHHhhhhhk..
.kHHHHHHhhhhhhk.
.kHHHHHhhhhhhhk.
kHHHHHhhhhhhhhjk
kHHHHhhhhhhhhhjk
kHHHHhhhhhhhhhjk
kHHHhhhhhhhhhhjk
kHHhhhhjjjhhhjjk
kHjhhhjHhhjhhjjk
kHjjhhjhhjjPPPjk
kHjjjhhhhhhjjjjk
kHjjjjjhhjjjjjjk
kHHjjjjjjjjjjhjk
.kHjjjjjjjjjjhk.
..kkkkkkkkkkkk..
''')
E_SIDE = G('''
....kkkkkk.....
...kHHHhhhkk...
..kHHHHHhhhhk..
.kHHHHHHhhhhjk.
kSjHHHHHhhhhjk.
kSSjHHHhhhkkhk.
kSSSjHhhhkHhhk.
kSSSSjhhhkhhjk.
kSSSSSjhhhkkjk.
kSESSSSjhhhjjk.
kSESSSSdjhhjjk.
.kSbbSSdjhhjjk.
.kmmSSSdjhhjk..
..kkSSSdjhhjk..
....kkkkkhhjk..
........khhk...
.........kk....
''')
E_RAMPS = {
    'cloth': ['#10303a', '#164450', '#1e5a66', '#2a727c', '#3c8c94', '#58a6aa', '#7cc0c0'],
    'trim': INNER, 'sash': ['#4a2a3a', '#623848', '#7c4858', '#965a6a', '#b0707c', '#c8889a', '#dca4b2'],
    'pants': ['#2a3a30', '#364a3c', '#425a48', '#506a56', '#5e7a64', '#6e8a74', '#80a086'],
    'boots': BOOTS, 'pouch': LEATHER, 'leaf': LEAF, 'glow': GLOW, 'pin': WOOD,
}
E_KEY = {'P': ('pin', 4.6)}


def erin():
    m = fs.Member('erin', E_RAMPS, E_FRONT, E_BACK, E_SIDE, extra_key=E_KEY, sw=11, th=15, legs=14, robe=10, head_dy=2)

    def pouch(c, view, layer, phase):
        if layer != 'front':
            return
        top = m.top
        if view == 'down':                          # herb pouch at the hip with a sprig poking out
            for y in range(top + 10, top + 14):
                for x in range(fs.CXS - 6, fs.CXS - 2):
                    c.put(x, y, 'pouch', 4.6 - (x - fs.CXS + 6) * 0.5)
            c.put(fs.CXS - 5, top + 9, 'leaf', 4.8); c.put(fs.CXS - 4, top + 8, 'leaf', 4.0)
        elif view == 'left':
            for y in range(top + 10, top + 13):
                for x in range(fs.CXS - 2, fs.CXS + 2):
                    c.put(x, y, 'pouch', 4.2)
        elif view == 'up':                          # hairpin through the bun
            pass
    m.props.append(pouch)
    return m


def erin_action(m):
    """Healing: hands together, a soft green glow gathers, leaves rise, the glow fades."""
    def glow(level):
        def f(c):
            top = m.top
            cx, cy = fs.CXS, top + 7
            for (dx, dy) in ((-2, 0), (-1, 0), (1, 0), (2, 0), (-1, 1), (0, 1), (1, 1)):
                c.put(cx + dx, cy + dy, 'skin', 4.8)                    # hands meeting at the chest
            if level:
                r = 2 + level * 2
                for y in range(cy - r, cy + r + 1):
                    for x in range(cx - r, cx + r + 1):
                        d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                        if r - 1 <= d <= r:
                            c.fixed[(x, y)] = '#a8f0b8' if (x + y) % 2 else '#eafff0'
                for i, (lx, ly) in enumerate(((-7, -6), (6, -9), (-4, -13), (8, -2))[:level + 1]):
                    c.put(cx + lx, cy + ly - level, 'leaf', 4.8)
                    c.put(cx + lx + 1, cy + ly - level, 'leaf', 3.6)
        return f
    return [fs.frame(m, 'down', 0, extra=glow(0)),
            fs.frame(m, 'down', 0, bob=-1, extra=glow(1)),
            fs.frame(m, 'down', 0, bob=-1, extra=glow(2)),
            fs.frame(m, 'down', 0, bob=0, extra=glow(3))]


MEMBERS = ['jeff', 'erin', 'josh', 'jasper']
