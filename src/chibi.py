"""Chibi full-body sprites in a pixel-baseball look: ~2.3 heads tall, big round head,
tiny dot eyes, short body, 2-3 tones per colour with a dark outline.

Frame 56x64; character centred on x=28, feet on y=62. Heads, torsos, arms, legs
and props are hand-authored grids; animations re-use them with small offsets.

Slots (shared by all characters, coloured per character in CPAL):
k outline, S s d skin, E eye, B brow, r mouth,
X x z hair, G g h hat, Y y gold, R e accent, P p q main cloth, C c trim, W w inner,
M m n metal, L l legs, O o boots, F f blade, T t shaft.
"""
from pixlib import Layer, G

FW, FH = 56, 64
HX, HY = 18, 22          # head grid origin in the frame (front)
TX, TY = 16, 39          # torso grid origin
LY = 52                  # legs origin y (x = TX)
HAND_L = (15, 47)        # where the viewer's-left hand holds things (front)

HEAD = G('''
.......kkkkkk.......
....kkkSSSSSSkkk....
...kSSSSSSSSSSssk...
..kSSSSSSSSSSSsssk..
.kSSSSSSSSSSSSssssk.
.kSSSSSSSSSSSSssssk.
kSSSSSSSSSSSSSsssssk
kSSSSSSSSSSSSSsssssk
kSSSSSSSSSSSSsssssdk
kSSSSSSSSSSSssssssdk
kSSSSESSSSSSsEssssdk
kSSSSESSSSSSsEssssdk
kdSSSSSSSSSSssssssdk
.kSSSSSSSSssssssddk.
.kdSSSSSSrrssssdddk.
..kdSSSSSsssssdddk..
...kkddSsssdddkkk...
.....kkkkkkkkkk.....
''')

TORSO = {
    'armor': G('''
.....kkkkkkkkkkkkkk.....
....kPPPPPPcWWcppppk....
...kPPPPPPPcWWcppppqk...
..kPPPPPPPPPcWcpppqqqk..
..kPPPPPPPPPPccpppqqqk..
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPPpppppqqk..
..kYYYYYYYYYYYyyyyyyyk..
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPkpppppqqk..
..kPPPPPPPPPPkpppppqqk..
..kPPPPPPPPPPkpppppqqk..
...kkkkkkkkkkkkkkkkkk...
'''),
    'robe': G('''
.....kkkkkkkkkkkkkk.....
....kPPPPPPcWWcppppk....
...kPPPPPPPcWWcppppqk...
..kPPPPPPPPPcWcpppqqqk..
..kPPPPPPPPPPcWcppqqqk..
..kPPPPPPPPPPPccppppqk..
..kPPPPPPPPPPPppcpppqk..
..kPPPPPPPPPPPpppcppqk..
..kYYYYYYYYYYYyyyyyyyk..
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPPpppppqqk..
.kPPPPPPPPPPPPppppppqqk.
.kPPPPPPPPPPPPppppppqqk.
'''),
    'dress': G('''
......kkkkkkkkkkkk......
.....kPPPPPcWWcpppk.....
....kPPPPPPcWWcppppk....
....kPPPPPPPcWcpppqk....
....kPPPPPPPPccppqqk....
....kPPPPPPPPPcpppqk....
....kPPPPPPPPPpcppqk....
....kYYYYYYYYYyyyyyk....
...kPPPPPPPPPPppppqqk...
...kPPPPPPPPPPppppqqk...
..kPPPPPPPPPPPpppppqqk..
..kPPPPPPPPPPPpppppqqk..
.kPPPPPPPPPPPPppppppqqk.
.kPPPPPPPPPPPPppppppqqk.
'''),
}

ARM_L = G('''
.kkk.
kPPPk
kPPPk
kPPPk
kPPPk
kPPPk
kPPqk
kSSSk
kSSsk
.kkk.
''')
ARM_R = G('''
.kkk.
kpqqk
kpqqk
kpqqk
kpqqk
kpqqk
kqqqk
ksssk
kssdk
.kkk.
''')

# legs for short costumes; phase 0 stand, 1 viewer's-left foot lifted, 2 right foot lifted
LEGS = {
    0: G('''
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLlkkllllk......
......kLLLlkkllllk......
.....kOOOOOkkooooOk.....
.....kOOOOokkoooook.....
.....kkkkkkkkkkkkkk.....
'''),
    1: G('''
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
.....kOOOOOkklllqk......
.....kOOOOokkllllk......
.....kkkkkkkkllllk......
............kooooOk.....
............koooook.....
............kkkkkkk.....
'''),
    2: G('''
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkklllqk......
......kLLLLkkooooOk.....
......kLLLlkkoooook.....
......kLLLlkkkkkkkk.....
.....kOOOOOk............
.....kOOOOok............
.....kkkkkkk............
'''),
}

# long robe / dress skirt with feet peeking out
HEM = {
    0: G('''
.kPPPPPPPPPPPPppppppqqk.
.kPPPPPPPPPPPPppppppqqk.
kPPPPPPPPPPPPPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kkkkkkkkkkkkkkkkkkkkkkkk
.....kOOOOOk.kooooOk....
.....kkkkkkk.kkkkkkk....
........................
'''),
    1: G('''
.kPPPPPPPPPPPPppppppqqk.
.kPPPPPPPPPPPPppppppqqk.
kPPPPPPPPPPPPPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kkkkkkkkkkkkkkkkkkkkkkkk
.............kooooOk....
.............kkkkkkk....
........................
'''),
    2: G('''
.kPPPPPPPPPPPPppppppqqk.
.kPPPPPPPPPPPPppppppqqk.
kPPPPPPPPPPPPPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kPPPPPPPPPPPkPpppppppqqk
kkkkkkkkkkkkkkkkkkkkkkkk
.....kOOOOOk............
.....kkkkkkk............
........................
'''),
}


def _stamp_items(L, items, ox, oy, flip=False):
    for item in items:
        g, x, y = item[:3]
        L.stamp(g, ox + x, oy + y, flip=flip)


def front(ch, phase=0, bob=0, arm=(0, 0), extra=None):
    """Front-facing frame. phase: legs (0 stand, 1/2 a foot lifted). bob: body/head dy.
    arm: (left dy, right dy) for swinging arms."""
    C = ch.CHIBI
    L = Layer(FW, FH)
    _stamp_items(L, C.get('back', []), HX, HY + bob)
    if callable(C.get('prop_back')):
        C['prop_back'](L, 'front', phase, bob, arm)
    cos = C.get('costume', 'armor')
    if cos == 'armor':
        L.stamp(C.get('legs', LEGS)[phase], TX, LY)
    else:
        L.stamp(HEM[phase][7:], TX, LY + 8)          # feet stay planted
        L.stamp(HEM[phase][:7], TX, LY + 1 + bob)    # skirt moves with the body
    L.stamp(C.get('torso', TORSO[cos]), TX, TY + bob)
    _stamp_items(L, C.get('torso_over', []), TX, TY + bob)
    if callable(C.get('prop')):
        C['prop'](L, 'front', phase, bob, arm)
    dx = 1 if cos == 'dress' else 0
    L.stamp(C.get('arm_l', ARM_L), TX - 2 + dx * 2, TY + 1 + bob + arm[0])
    L.stamp(C.get('arm_r', ARM_R), TX + 21 - dx * 2, TY + 1 + bob + arm[1])
    L.stamp(C.get('head', HEAD), HX, HY + bob)
    _stamp_items(L, C.get('face', []), HX, HY + bob)
    if callable(C.get('prop_front')):
        C['prop_front'](L, 'front', phase, bob, arm)
    if extra:
        extra(L)
    return L


def frames(ch):
    """All animation frames -> dict name -> list of Layers."""
    out = {}
    out['idle'] = [front(ch, 0, 0), front(ch, 0, 1)]
    out['walk'] = [front(ch, 0, 0, (0, 0)), front(ch, 1, -1, (1, -1)), front(ch, 0, 0, (0, 0)), front(ch, 2, -1, (-1, 1))]
    if callable(ch.CHIBI.get('side')):
        out['walk_side'] = ch.CHIBI['side']()
    if callable(ch.CHIBI.get('action')):
        out['action'] = ch.CHIBI['action']()
    return out


def hshaft(L, y, x0, x1, core='T'):
    """A horizontal 3-pixel pole."""
    for x in range(x0, x1 + 1):
        if L.get(x, y - 1) == '.':
            L.set(x, y - 1, 'k')
        L.set(x, y, core)
        if L.get(x, y + 1) == '.':
            L.set(x, y + 1, 'k')
    L.set(x0 - 1, y, 'k')
    L.set(x1 + 1, y, 'k')


def shaft(L, x, y0, y1, core='T'):
    """A vertical 3-pixel pole: outline, core, outline."""
    for y in range(y0, y1 + 1):
        if L.get(x - 1, y) == '.':
            L.set(x - 1, y, 'k')
        L.set(x, y, core)
        if L.get(x + 1, y) == '.':
            L.set(x + 1, y, 'k')
    L.set(x, y0 - 1, 'k')
    L.set(x, y1 + 1, 'k')


def polearm(L, x, y_hand, head, hox, hoy, length_up=36, length_down=10, core='T'):
    """Vertical polearm held at (x, y_hand); head grid placed relative to the pole top."""
    top = y_hand - length_up
    shaft(L, x, top, y_hand + length_down, core)
    L.stamp(head, x + hox, top + hoy)


# ---------------- side view (facing right) ----------------
HEAD_SIDE = G('''
.......kkkkkk.......
....kkkSSSSSSkk.....
...kSSSSSSSSSSSk....
..kSSSSSSSSSSSSSk...
.kSSSSSSSSSSSSSSsk..
.kSSSSSSSSSSSSSSsk..
kSSSSSSSSSSSSSSSssk.
kSSSSSSSSSSSSSSSssk.
kSSSSSSSSSSSSSSSSsk.
kSSSSkkSSSSSSSSSSsk.
ksSSkSdkSSSSSESSSSk.
ksSSkSdkSSSSSESSSSSk
ksSSSkkSSSSSSSSSSSk.
.ksSSSSSSSSSSSSSSk..
.kssSSSSSSSSSSrrk...
..kssSSSSSSSSSSk....
...kkssSSSSSSkk.....
.....kkkkkkkk.......
''')

TORSO_SIDE = G('''
....kkkkkkkk....
...kPPPPPPcck...
..kPPPPPPPPcWk..
..kPPPPPPPPcWk..
..kPPPPPPPPPck..
..kPPPPPPPPPpk..
..kPPPPPPPPPpk..
..kPPPPPPPPPpk..
..kYYYYYYYYYyk..
..kPPPPPPPPPpk..
..kPPPPPPPPPpk..
..kPPPPPPPPPpk..
.kPPPPPPPPPPpqk.
.kPPPPPPPPPPpqk.
''')

SKIRT_SIDE = G('''
.kPPPPPPPPPPpqk.
kPPPPPPPPPPPppqk
kPPPPPPPPPPPppqk
kPPPPPPPPPPPppqk
kPPPPPPPPPPPppqk
kPPPPPPPPPPPppqk
kkkkkkkkkkkkkkkk
''')

FEET_SIDE = {
    'a': G('''
.kooook....kOOOOOk
.kkkkkk....kkkkkkk
'''),
    'p': G('''
......kOOOOOk.....
......kkkkkkk.....
'''),
    'b': G('''
.kOOOOk....koooook
.kkkkkk....kkkkkkk
'''),
}

ARM_SIDE = G('''
.kkk.......
kPPPk......
kPPPk......
kPPPPk.....
kPPPPPkkk..
.kPPPPPkSSk
..kkkkkkSsk
........kk.
''')

SX = 20      # side torso x


def side(ch, step='a', bob=0):
    C = ch.CHIBI
    L = Layer(FW, FH)
    _stamp_items(L, C.get('side_back', []), HX, HY + bob)
    L.stamp(FEET_SIDE[step], SX - 1, LY + 8)
    L.stamp(SKIRT_SIDE, SX, LY + 1 + bob)
    L.stamp(TORSO_SIDE, SX, TY + bob)
    if callable(C.get('side_prop')):
        C['side_prop'](L, step, bob)
    L.stamp(ARM_SIDE, SX + 9, TY + 2 + bob)
    L.stamp(HEAD_SIDE, HX, HY + bob)
    _stamp_items(L, C.get('side_face', []), HX, HY + bob)
    return L


def side_walk(ch):
    return [side(ch, 'a', 0), side(ch, 'p', -1), side(ch, 'b', 0), side(ch, 'p', -1)]
