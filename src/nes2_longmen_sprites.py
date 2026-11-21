"""16x24 field sprites for the `nes2` Longmen heroes (round 1), same cells and rows as the `nes` sheets plus a
back view: idle, walk (front), walk_side (faces right; mirror for left), walk_up (back).

Two stacked NES sprite layers, as in src/nes_sango.py: `pal` = k black, S skin, c the main colour; `pal2` = three
more colours (cloth shade, trim, hair sheen, headgear, weapon). nes.sprite_image() checks each layer stays within
3 colours + transparent. Every head is hand-typed per view (front / side / back) to match the nes2 portrait:
same hair, headgear, colours and weapon. Bodies come from shared templates (robe, gown, boy) with each
character's letters swapped in, so the cast reads as one family. Walk frame 2 keeps every pixel above the bottom
rows (front and back: the legs swap; side: legs together), so the body never bobs.

    SPRITES[cid] = dict(pal, pal2, front, side, side2, back)      frames(cid) -> {anim: [img, img]}
"""
import nes
import nes_walk


def R(text):
    rows = [ln.strip() for ln in text.strip('\n').split('\n') if ln.strip()]
    for r in rows:
        if len(r) != 16:
            raise ValueError('sprite row is %d wide: %r' % (len(r), r))
    return rows


def sub(rows, m):
    return [''.join(m.get(ch, ch) for ch in r) for r in rows]


def over(rows, top, x0=0, y0=0):
    """Lay hand pixels over rows ('.' keeps, '_' clears)."""
    rows = [list(r) for r in rows]
    for dy, r in enumerate(top):
        for dx, ch in enumerate(r):
            if ch == '.':
                continue
            x, y = x0 + dx, y0 + dy
            if 0 <= x < 16 and 0 <= y < len(rows):
                rows[y][x] = '.' if ch == '_' else ch
    return [''.join(r) for r in rows]


# ---------------------------------------------------------------- body templates (rows 14..23 for adults)
# c main, d shade, w trim / collar, S skin (hands), k black
ROBE = dict(front=R('''
..kkccwSSwccdkk.
.kcccccwwcccddk.
.kcckcccwcckcdk.
.kcckccwccckcdk.
.kSSkkkkkkkkkSSk
..kkcccwccccdk..
...kccwcccccdk..
...kcwcccccddk..
...kkkkkkkkkkk..
...kkkk..kkkk...
'''), side=R('''
.....kccwk......
....kcccwcdk....
...kccccwccdk...
...kcckcwcSSk...
...kkkkkkkkkk...
...kccccwccdk...
...kcccck.kcdk..
..kccdk...kcdk..
..kkkk.....kkkk.
.kkkk......kkkk.
'''), side_legs=R('''
...kccccwccdk...
....kcccwcdk....
....kcccwcdk....
....kkkkkkkk....
....kkkkkkkk....
'''), back=R('''
..kkcccccccckk..
.kccccccccccddk.
.kcckccccccdkdk.
.kcckccccccdkdk.
.kSSkkkkkkkkkSSk
..kkcccccccddk..
...kcccccccddk..
...kcccccccddk..
...kkkkkkkkkkk..
...kkkk..kkkk...
'''))

GOWN = dict(front=R('''
...kkcwSSwckk...
..kcccwwwwccdk..
.kccckcwwckccdk.
.kccckcwwckccdk.
.kSSkkkddkkkSSk.
..kkcccwwcccdk..
..kccccwwccccdk.
.kcccccwwccccdk.
.kcccccwwcccccdk
.kkkkkkkkkkkkkkk
'''), side=R('''
.....kccdk......
....kcccdcck....
...kccccdccck...
...kcckcdcSSk...
...kkkdddkkkk...
...kcccdcccck...
...kccccdcccck..
..kccccdcccccck.
..kcccccdccccck.
..kkkkkkkkkkkkk.
'''), side_legs=R('''
...kcccdcccck...
...kcccdccccdk..
..kccccdccccdk..
..kcccccdcccdk..
..kkkkkkkkkkkk..
'''), back=R('''
...kkccccccckk..
..kcccccccccdk..
.kccckcccckccdk.
.kccckcccckccdk.
.kSSkkkddkkkSSk.
..kkcccccccccdk.
..kccccccccccdk.
.kccccccccccccdk
.kccccccccccccdk
.kkkkkkkkkkkkkkk
'''))

# the boy: shorter (head rows 4..16, body rows 17..23)
BOY = dict(front=R('''
..kkcwwSSwwckk..
.kSkcccwwccckSk.
.kSkkkkkkkkkkSk.
..kkccccccccdk..
...kcccddcccdk..
...kddk..kddk...
...kkkk..kkkk...
'''), side=R('''
....kcwwck......
...kccccwcck....
...kkkkkkSSk....
...kccccccdk....
...kccck.kcdk...
..kddk....kddk..
..kkkk....kkkk..
'''), side_legs=R('''
...kccccccdk....
....kcccccdk....
....kddkddk.....
....kkkkkkk.....
'''), back=R('''
..kkcccccccckk..
.kSkccccccccdSk.
.kSkkkkkkkkkkSk.
..kkccccccccdk..
...kcccddcccdk..
...kddk..kddk...
...kkkk..kkkk...
'''))

SPRITES = {}

# ================================================================ 奕叡
SPRITES['yirui'] = dict(pal=dict(k=0x0F, S=0x37, c=0x12), pal2=dict(d=0x02, h=0x0C, b=0x21), body=ROBE, m={'w': 'b'}, front=R('''
......kbbk......
......khhk......
....kkkhhkkk....
...khhhhhhhhk...
..khhkhhhhkhhk..
..khhhhhhhhhhk..
..kbbbbbbbbbbkbk
..khSSSSSSSShkbk
..kSkkSSSSkkSk..
.kkSSkSSSSkSSkk.
.kSkSkSSSSkSkSk.
..kkSSSkkSSSkk..
...kkSSSSSSkk...
....kkkSSkkk....
'''), side=R('''
.....kbbk.......
.....khhk.......
...kkkhhkkk.....
..khhhhhhhhk....
.khhhkhhhhhhk...
.khhhhhhhhhhhk..
bkbbbbbbbbbbbbk.
bbkhhhhhhhSSSSk.
.khhhhhhhSSkkSk.
.khhhhhhSSSSkSk.
.khhhhSkSSSSkSSk
..khhhhSSSSSSSk.
...khhhSSSSSkk..
.....kkSSSk.....
'''), back=R('''
......kbbk......
......khhk......
....kkkhhkkk....
...khhhhhhhhk...
..khhkhhhhkhhk..
..khhhhhhhhhhk..
.kbbbbbbbbbbbbk.
bbkhhhhhhhhhhk..
b.khhhkhhkhhhk..
.kkhhhhhhhhhhkk.
.kSkhhhhhhhhkSk.
..kkhhhhhhhhkk..
...kkhhhhhhkk...
....kkSSSSkk....
'''), extra=dict(
    front=[(['.b.', 'bkb', '.b.', '.h.', '.h.'], 0, 2)],
    side=[],
    back=[(['.b.', 'bkb', '.b.'], 13, 10), ([['h'], (12, 14)], None, None)],
), px=dict(back=[(12, 14, 'h'), (11, 15, 'h'), (10, 16, 'h'), (9, 17, 'h')]))

# ================================================================ 奕碩
SPRITES['yishuo'] = dict(pal=dict(k=0x0F, S=0x37, c=0x27), pal2=dict(d=0x17, h=0x0C, r=0x16), body=BOY, m={'w': 'r'},
                         short=True, front=R('''
....k..k..k.....
...khkkhkkhk.k..
..khhhhhhhhhkhk.
..khhhhhhhhhhhk.
..krrrrrrrrrrkrr
..khhShhhShhhkrk
..kSSSSSSSSSSk..
..kSkkSSSSkkSk..
.kkSSkSSSSkSSkk.
.kSkSkSSSSkSkSk.
..kkSSSSSSSSkk..
...kkSSkkSSkk...
....kkkSSkkk....
'''), side=R('''
...k..k.........
..khkkhkk.k.....
.khhhhhhhkhk....
.khhhhhhhhhhk...
rkrrrrrrrrrrk...
rrkhhhhhhShSk...
.khhhhhhSSSSk...
.khhhhhSSkkSk...
.khhhhSSSSkSk...
.khhhSkSSSkSSk..
..khhhSSSSkSk...
...kkhSSSSkk....
.....kkSSk......
'''), back=R('''
....k..k..k.....
...khkkhkkhk.k..
..khhhhhhhhhkhk.
..khhhhhhhhhhhk.
.krrrrrrrrrrrrk.
rrkhhhhhhhhhhk..
r.khhhhhhhhhhk..
..khhhhhhhhhhk..
.kkhhhhhhhhhhkk.
.kSkhhhhhhhhkSk.
..kkhhhhhhhhkk..
...kkhhhhhhkk...
....kkSSSSkk....
'''), extra=dict(front=[(['.kkk', 'kSkS', 'kkSk', '.kkk'], 12, 20)], side=[(['.kkk', 'kSkS', 'kkSk', '.kkk'], 12, 20)], back=[]))

# ================================================================ 柳寒煙
SPRITES['liuhanyan'] = dict(pal=dict(k=0x0F, S=0x37, c=0x30), pal2=dict(d=0x31, h=0x0C, g=0x2A), body=GOWN, m={'w': 'd'}, hairfill=True,
                            front=R('''
......kkkk.ggk..
.....khhkkkgk...
......kkkk......
....kkkkkkkk....
...kkhkkkkhkk...
..kkhkkkkkkhkk..
..kkkkSSSSkkkk..
..kkkSSSSSSkkk..
.kkkSSSSSSSSkkk.
.kkkSkkSSkkSkkk.
.kkkSSkSSkSSkkk.
.kkhkSSSSSSkhkk.
.kkkhkSSSSkhkkk.
.kkhkkkSSkkkhkk.
'''), side=R('''
....kkkk.ggk....
...khhkkkgk.....
....kkkk........
..kkkkkkkk......
.kkhkkkkkkk.....
.khkkkkkkkSk....
.kkkkkkkkSSSk...
kkkkkkkkSSSSk...
kkhkkkkSSSkSk...
kkkkkkkSSSkSSk..
kkkhkkSSSSSSk...
kkkkkkkSSSSk....
.kkhkkkkSSk.....
.kkkhkkkkk......
'''), back=R('''
......kkkk.ggk..
.....khhkkkgk...
......kkkk......
....kkkkkkkk....
...kkhkkkkhkk...
..kkhkkkkkkhkk..
..kkkhkkkkhkkk..
..kkkkhkkhkkkk..
..kkhkkkkkkhkk..
.kkkkhkkkkhkkkk.
.kkhkkkkkkkkhkk.
.kkkkhkkkkhkkkk.
.kkhkkkkkkkkhkk.
.kkkhkkkkkkhkkk.
'''), extra=dict(front=[(['k', 'k', 'k'], 1, 14), (['k', 'k', 'k'], 14, 14)],
                 side=[(['.g', 'kg', 'k.'], 0, 16)],
                 back=[(['kkhkkkkkkhkk', '.kkhkkkkhkk.', '..kkhkkhkk..', '...kkkkkk...'], 2, 14), (['g', 'k'], 13, 13)]))

# ================================================================ 白先生
SPRITES['baixian'] = dict(pal=dict(k=0x0F, S=0x37, c=0x10), pal2=dict(d=0x00, w=0x30, q=0x17), body=ROBE, m={},
                          front=R('''
.....kkkkkk.....
....kddddddk....
....kdkddkdk....
....kdkddkdk....
...kkkkkkkkkk...
..kddddddddddk..
..kdSSSSSSSSdk..
..kSSSSSSSSSSk..
..kSSkSSSSkSSk..
.kkSkSkSSkSkSkk.
.kSSSSSSSSSSSSk.
..kkSkkkkkkSkk..
...kkSSkkSSkk...
....kkkkkkkk....
'''), side=R('''
.....kkkkkk.....
....kddddddk....
....kddddkdk....
....kddddkdk....
...kkkkkkkkkk...
..kddddddddddk..
..kdddSSSSSSSk..
..kddSSSSSSSSk..
..kddSSSSSkkSk..
.kddSkSSSSSkSk..
.kddSSkSSSSSSSSk
..kdSSSSSSkkkk..
...kkkSSSSkk....
.....kkkkkk.....
'''), back=R('''
.....kkkkkk.....
....kddddddk....
....kddddddk....
....kddddddk....
...kkkkkkkkkk...
..kddddddddddk..
..kddddddddddk..
..kddddddddddk..
..kdddkkkkdddk..
.kkddkkkkkkddkk.
.kSdkkkkkkkkdSk.
..kkkkkkkkkkkk..
...kkkkkkkkkk...
....kkSSSSkk....
'''), extra=dict(front=[(['kkkk', 'kqqk', 'kkkk'], 12, 17)], side=[(['kkk', 'qqk', 'kkk'], 11, 16)], back=[]))

# ================================================================ 苦禪
SPRITES['kuchan'] = dict(pal=dict(k=0x0F, S=0x37, c=0x27), pal2=dict(r=0x16, w=0x30, y=0x28), body=ROBE, m={'d': 'r', 'w': 'r'},
                         front=R('''
.kyk............
y.ky....kk......
.kyk.kkkSSkkk...
..y.kSSSSSSSSk..
..ykSwSSSSSSSSk.
..ykSSSSSSSSSSk.
..kSSSSSSSSSSSSk
..kwwwSSSSSwwwSk
.kkwkkSSSSkkwkk.
.kSkSSSSSSSSkSk.
.kSSwwwSSwwwSSk.
..kkwwwwwwwwkk..
..ykkwwwwwwkk...
..y.kkwwwwkk....
'''), side=R('''
................
.........kk.....
.....kkkkSSkk...
....kSSSSSSSSk..
...kSwSSSSSSSk..
...kSSSSSSSSSk..
..kSSSSSSSSSSSk.
..kSSSSSSwwwSSk.
..kSSSSSSkkwSk..
..kSsSSSSSSkSSk.
..kSSSSSSSwwSSk.
...kSSSSSwwwwk..
....kkSSkwwwk...
......kkkwwk....
'''), back=R('''
................
........kk......
.....kkkSSkkk...
....kSSSSSSSSk..
...kSSSSSSSSSSk.
...kSSSSSSSSSSk.
..kSSSSSSSSSSSSk
..kSSSSSSSSSSSSk
..kSSSSSSSSSSSSk
.kkSSSSSSSSSSSSk
.kSkSSSSSSSSSkSk
..kkSSSSSSSSSkk.
...kkSSSSSSkk...
....kkkSSkkk....
'''), extra=dict(front=[(['y'] * 10, 2, 14), (['rr', 'rrr', '.rrr', '..rr'], 10, 14), (['y.y.y'], 5, 15)],
                 side=[(['.kyk', 'y.ky', '.kyk'], 11, 0), (['y'] * 20, 12, 3)],
                 back=[(['.kyk', 'y.ky', '.kyk'], 12, 0), (['y'] * 20, 13, 3), (['rr', 'rrr', 'rrrr'], 3, 14)]))

# ================================================================ 冷笑天
XT_BODY = dict(front=R('''
.ckkkykSSkykkkc.
ckkkkkykkykkkkkc
ckkykkkykkkkykkc
ckkkkykkykkykkkc
ckSSkyyyyyykSSkc
cckkkkkykkkkkkcc
.ckkykkkkkykkkc.
.ckkkkkykkkkkkc.
.cckkkkkkkkkkcc.
...kkkk..kkkk...
'''), side=R('''
..cckkkyk.......
.ccckkkkyk......
.ccckkykkkk.....
.ccckkkkkSSk....
.ccckyyyyyyk....
.ccckkkykkk.....
.ccckkkk.kkk....
.cckkkk...kkk...
.cckkk.....kkkk.
.kkkk......kkkk.
'''), side_legs=R('''
.ccckkkykkk.....
.ccckkkkkkk.....
.cccckkkkkk.....
.cccckkkkkkk....
.ccccckkkkkk....
'''), back=R('''
.ccccccccccccc..
ccccccccccccccc.
cccccccccccccccc
cccccccccccccccc
cccccccccccccccc
cccccccccccccccc
.cccccccccccccc.
.cccccccccccccc.
.cccccccccccccc.
...kkkk..kkkk...
'''))
SPRITES['xiaotian'] = dict(pal=dict(k=0x0F, S=0x37, c=0x16), pal2=dict(h=0x10, H=0x30, y=0x28), body=XT_BODY, m={},
                           front=R('''
.ky..........yk.
.kyk..kkkk..kyk.
..kyk.kHHk.kyk..
..kkyhHHHHhykk..
.khHHkyyyykHHhk.
.khHhhhhhhhhHhk.
.khhkSSSSSSkhhk.
khhkkkSSSSkkkhhk
khhSckSSSSkcShhk
khhSkkSSSSkkShhk
.khkSSSSSSSShkk.
.khkkSSkkkSSkhk.
.khhkkSSSSkkhhk.
..kkkkkSSkkkkk..
'''), side=R('''
.......ky.......
.......kyk......
....kkkkkyk.....
..kkHHHHHkyk....
.kHHHHHHHHkyk...
khHhhhhhhhkkk...
khhhhhhhhkSSk...
khhhhhhhkSSSk...
khhhhhhkSkcSk...
khhhhhkSSkkSSk..
.khhhkSSSSSSk...
.khhhkSSSSkkk...
..khhkkSSSk.....
...kkk.kkk......
'''), back=R('''
.ky..........yk.
.kyk..kkkk..kyk.
..kyk.kHHk.kyk..
..kkykHHHHkykk..
.khHHkyyyykHHhk.
.khHHHHHHHHHHhk.
.khhHHhhhhHHhhk.
khhhhhHHHhhhhhhk
khhhhhhhhhhhhhhk
khhhhhhhhhhhhhhk
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
..khhhhhhhhhhk..
..kkkkkkkkkkkk..
'''), extra=dict(front=[], side=[], back=[]))


def hairfill(rows):
    """Black hair typed with 'h' strands -> hair filled with 'h' and the strands in black; the outline stays."""
    h, w = len(rows), 16
    at = lambda x, y: rows[y][x] if 0 <= x < w and 0 <= y < h else '.'
    out = []
    for y in range(h):
        r = []
        for x in range(w):
            ch = rows[y][x]
            n4 = [at(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            if ch == 'k' and all(n in 'kh' for n in n4):
                r.append('h')
            elif ch == 'h':
                r.append('k')
            else:
                r.append(ch)
        out.append(''.join(r))
    return out


def assemble(cid, view):
    d = SPRITES[cid]
    head = [r.replace('s', 'S') for r in d[view]]
    if d.get('hairfill'):
        head = hairfill(head)
    body = sub(d['body'][view], d['m'])
    if d.get('short'):
        rows = ['.' * 16] * (24 - len(head) - len(body)) + head + body
    else:
        rows = head + body
    assert len(rows) == 24, (cid, view, len(rows))
    for top, x0, y0 in d['extra'].get(view, []):
        if x0 is None:
            continue
        rows = over(rows, top, x0, y0)
    for x, y, ch in d.get('px', {}).get(view, []):
        rows[y] = rows[y][:x] + ch + rows[y][x + 1:]
    return rows


def views(cid):
    d = SPRITES[cid]
    fr, sd, bk = assemble(cid, 'front'), assemble(cid, 'side'), assemble(cid, 'back')
    n = len(d['body']['side_legs'])
    legs = sub(d['body']['side_legs'], d['m'])
    s2 = sd[:-n] + legs
    for top, x0, y0 in d['extra'].get('side', []):     # props in the leg rows stay put
        if x0 is not None:
            s2 = over(s2, top, x0, y0)
    f2 = nes_walk.front2(fr, n=2)
    b2 = nes_walk.front2(bk, n=2)
    return fr, f2, sd, s2, bk, b2


def frames(cid):
    d = SPRITES[cid]
    if d.get('old'):                 # carts, engines, ships and mounted troops keep their old field sprite
        return old_frames(cid)
    im = lambda rows: nes.sprite_image(rows, d['pal'], d['pal2'])
    fr, f2, sd, s2, bk, b2 = views(cid)
    return {'idle': [im(fr), im(fr)], 'walk': [im(fr), im(f2)], 'walk_side': [im(sd), im(s2)],
            'walk_up': [im(bk), im(b2)]}


def old_frames(cid):
    """The character's `nes` sheet as frames, with walk_up added (the walk frames) when it has no back view."""
    import json
    import os
    from PIL import Image
    d = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chars', cid, 'nes')
    sheet = Image.open(os.path.join(d, 'sheet.png')).convert('RGBA')
    meta = json.load(open(os.path.join(d, 'sheet.json'), encoding='utf-8'))
    fw, fh = meta['frameWidth'], meta['frameHeight']
    out = {}
    for n, a in meta['animations'].items():
        fr = [sheet.crop((i * fw, a['row'] * fh, (i + 1) * fw, (a['row'] + 1) * fh)) for i in range(a['frames'])]
        if (fw, fh) != (16, 24):     # 16x16 vehicles stand on the floor of a 16x24 cell
            pad = []
            for f in fr:
                cell = Image.new('RGBA', (16, 24), (0, 0, 0, 0))
                cell.alpha_composite(f, ((16 - fw) // 2, 24 - fh))
                pad.append(cell)
            fr = pad
        out[n] = fr
    if 'idle' not in out:
        out['idle'] = out.get('walk') or out.get('move') or list(out.values())[0]
    base = out.get('walk') or out.get('move') or out['idle']
    res = {'idle': out['idle'][:2], 'walk': base[:2], 'walk_side': out.get('walk_side', base)[:2],
           'walk_up': out.get('walk_up', base)[:2]}
    for k, v in res.items():
        if len(v) == 1:
            res[k] = [v[0], v[0]]
    return res
