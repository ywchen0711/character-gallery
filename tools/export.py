"""Re-export every character variant in src/roster.py and rebuild chars/index.json.

    python tools/export.py

Per character and style, in chars/<id>/<style>/:
  portrait.png, portrait@4x.png   the portrait
  body.png, body@4x.png           first idle frame of the full body
  sheet.png, sheet@4x.png         all animation frames, one animation per row
  sheet.json                      frame size, anchor, rows, frame counts, fps
"""
import importlib
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

from PIL import Image  # noqa: E402
from pixlib import count_colours, scale  # noqa: E402
from roster import ROSTER  # noqa: E402
from styles import STYLES  # noqa: E402

FACTION_COLOUR = {'wu': '#c8402e', 'shu': '#3f8f4e', 'wei': '#3b5ba8', 'qun': '#b08a3a', 'west': '#3a7ca8', 'longmen': '#5a6ab8', 'beast': '#6a8a3a', 'foe': '#8a6a3a', 'sango': '#a83a3a'}
FACTION_NAME = {'wu': {'zh': '吳', 'en': 'Wu'}, 'shu': {'zh': '蜀', 'en': 'Shu'},
                'wei': {'zh': '魏', 'en': 'Wei'}, 'qun': {'zh': '群', 'en': 'Other'},
                'west': {'zh': '旅人一家', 'en': 'The travelling family'},
                'longmen': {'zh': '龍門武林', 'en': 'Longmen Wulin'},
                'sango': {'zh': '霸王之路', 'en': 'Path of the Hegemon'},
                'beast': {'zh': '怪物與野獸', 'en': 'Monsters & Beasts'},
                'foe': {'zh': '小怪', 'en': 'Common Foes'}}


def export_variant(cid, v):
    out = os.path.join(ROOT, 'chars', cid, v.style)
    os.makedirs(out, exist_ok=True)
    por = v.portrait()
    por.save(os.path.join(out, 'portrait.png'))
    scale(por, 4).save(os.path.join(out, 'portrait@4x.png'))
    fr = v.frames()
    names = list(fr)
    fw, fh = fr[names[0]][0].size
    body = fr['idle'][0] if 'idle' in fr else fr[names[0]][0]
    body.save(os.path.join(out, 'body.png'))
    scale(body, 4).save(os.path.join(out, 'body@4x.png'))
    cols = max(len(fr[n]) for n in names)
    sheet = Image.new('RGBA', (cols * fw, len(names) * fh), (0, 0, 0, 0))
    anims = {}
    for row, n in enumerate(names):
        for i, f in enumerate(fr[n]):
            assert f.size == (fw, fh), (cid, v.style, n, f.size)
            sheet.alpha_composite(f, (i * fw, row * fh))
        a = {'row': row, 'frames': len(fr[n]), 'fps': v.fps.get(n, 8), 'loop': v.loop.get(n, True)}
        if n in v.notes:
            a['note'] = v.notes[n]
        anims[n] = a
    sheet.save(os.path.join(out, 'sheet.png'))
    scale(sheet, 4).save(os.path.join(out, 'sheet@4x.png'))
    meta = {'image': 'sheet.png', 'frameWidth': fw, 'frameHeight': fh,
            'anchor': {'x': v.anchor[0], 'y': v.anchor[1], 'note': 'feet centre in each cell'},
            'animations': anims}
    with open(os.path.join(out, 'sheet.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    base = f'chars/{cid}/{v.style}/'
    files = {k: base + n for k, n in {
        'portrait': 'portrait.png', 'portrait4x': 'portrait@4x.png', 'body': 'body.png',
        'body4x': 'body@4x.png', 'sheet': 'sheet.png', 'sheet4x': 'sheet@4x.png', 'sheetJson': 'sheet.json'}.items()}
    summary = ', '.join('%sx%d' % (n, anims[n]['frames']) for n in names)
    print(f'  {cid}/{v.style}: portrait {por.size[0]}x{por.size[1]} {count_colours(por)}c, '
          f'frame {fw}x{fh}, sheet {count_colours(sheet)}c, {summary}')
    return {'style': v.style, 'styleName': STYLES[v.style]['name'], 'primary': v.primary, 'files': files,
            'sizes': {'portrait': list(por.size), 'frame': [fw, fh]},
            'colours': {'portrait': count_colours(por), 'sheet': count_colours(sheet)},
            'animations': names}


def export(cid):
    ch = importlib.import_module(cid)
    d = os.path.join(ROOT, 'chars', cid)
    if os.path.isdir(d):              # drop stale files from older layouts
        for n in os.listdir(d):
            p = os.path.join(d, n)
            if os.path.isfile(p):
                os.remove(p)
            elif n not in STYLES and n != 'doll':   # yirui/doll is made by Longmen Quest's js/doll.js
                shutil.rmtree(p)
    if cid in ('family', 'longmen', 'beasts', 'foes', 'sango'):
        raise ValueError('family and longmen are reserved for group pictures')
    vs = [export_variant(cid, v) for v in ch.variants()]
    M = ch.META
    return dict(M, kind=getattr(ch, 'KIND', 'person'), faction=ch.FACTION, factionName=FACTION_NAME[ch.FACTION],
                colour=FACTION_COLOUR[ch.FACTION], variants=vs)


def main():
    entries = []
    for c in ROSTER:
        print(c)
        entries.append(export(c))
    styles = {k: {'name': s['name'], 'blurb': s['blurb']} for k, s in STYLES.items()}
    # the family group picture
    from family_variant import group
    gd = os.path.join(ROOT, 'chars', 'family')
    os.makedirs(gd, exist_ok=True)
    from nes_variant import group as nes_group
    for name, im in (('group', group()), ('group-scene', group(scene=True)), ('group-nes', nes_group()), ('group-nes-2x2', nes_group(cols=2))):
        im.save(os.path.join(gd, name + '.png'))
        scale(im, 4).save(os.path.join(gd, name + '@4x.png'))
    groups = {'family': {'name': {'zh': '一家四口', 'en': 'The family'},
                         'members': ['jeff', 'erin', 'josh', 'jasper'], 'style': 'nes',
                         'files': {k: 'chars/family/' + v for k, v in (('nes', 'group-nes.png'), ('nes4x', 'group-nes@4x.png'),
                                                                        ('nesTall', 'group-nes-2x2.png'), ('nesTall4x', 'group-nes-2x2@4x.png'),
                                                                        ('group', 'group.png'), ('group4x', 'group@4x.png'),
                                                                        ('scene', 'group-scene.png'), ('scene4x', 'group-scene@4x.png'))}}}
    # the 龍門武林 cast as one roster screen: six in a row (desktop) or 3x2 (phones)
    LONGMEN = ['yirui', 'yishuo', 'xiaotian', 'baixian', 'liuhanyan', 'kuchan']
    ld = os.path.join(ROOT, 'chars', 'longmen')
    os.makedirs(ld, exist_ok=True)
    for name, im in (('group-nes', nes_group(LONGMEN, cols=6)), ('group-nes-3x2', nes_group(LONGMEN, cols=3))):
        im.save(os.path.join(ld, name + '.png'))
        scale(im, 4).save(os.path.join(ld, name + '@4x.png'))
    groups['longmen'] = {'name': {'zh': '龍門武林', 'en': 'Longmen Wulin'}, 'faction': 'longmen',
                         'members': LONGMEN, 'style': 'nes',
                         'files': {k: 'chars/longmen/' + v for k, v in (('nes', 'group-nes.png'), ('nes4x', 'group-nes@4x.png'),
                                                                         ('nesTall', 'group-nes-3x2.png'), ('nesTall4x', 'group-nes-3x2@4x.png'))}}
    # the second Longmen group: the Black Wind Fort bandits and the master of the Netherworld Sect
    FOES = ['heixiong', 'daoba', 'shouhou', 'tuqianqiu']
    for name, im in (('group-nes-foes', nes_group(FOES, cols=4)), ('group-nes-foes-2x2', nes_group(FOES, cols=2))):
        im.save(os.path.join(ld, name + '.png'))
        scale(im, 4).save(os.path.join(ld, name + '@4x.png'))
    groups['longmenFoes'] = {'name': {'zh': '黑風寨與幽冥教', 'en': 'Black Wind Fort and the Netherworld Sect'},
                             'faction': 'longmen', 'members': FOES, 'style': 'nes',
                             'files': {k: 'chars/longmen/' + v for k, v in (('nes', 'group-nes-foes.png'), ('nes4x', 'group-nes-foes@4x.png'),
                                                                             ('nesTall', 'group-nes-foes-2x2.png'), ('nesTall4x', 'group-nes-foes-2x2@4x.png'))}}
    # the third Longmen group: more of the cast from the Longmen stories
    MORE = ['tiewusi', 'qianwanli', 'wenruyu', 'xiaolian', 'lihanshan', 'yuweng', 'guimian', 'masked']
    for name, im in (('group-nes-more', nes_group(MORE, cols=8)), ('group-nes-more-4x2', nes_group(MORE, cols=4))):
        im.save(os.path.join(ld, name + '.png'))
        scale(im, 4).save(os.path.join(ld, name + '@4x.png'))
    groups['longmenMore'] = {'name': {'zh': '龍門江湖眾生', 'en': 'More of the Longmen jianghu'},
                             'faction': 'longmen', 'members': MORE, 'style': 'nes',
                             'files': {k: 'chars/longmen/' + v for k, v in (('nes', 'group-nes-more.png'), ('nes4x', 'group-nes-more@4x.png'),
                                                                             ('nesTall', 'group-nes-more-4x2.png'), ('nesTall4x', 'group-nes-more-4x2@4x.png'))}}
    # Longmen Quest II: its new people (longmen2) and its foes (longmen2Foes)
    L2 = ['hubanxian', 'jiabafang', 'wudadan', 'wenduizhang', 'suxiaowan', 'chutiankuo', 'niubaobao', 'mojide', 'huotianxia', 'mowuya', 'aman']
    for name, im in (('group-nes-l2', nes_group(L2, cols=6)), ('group-nes-l2-4col', nes_group(L2, cols=4))):
        im.save(os.path.join(ld, name + '.png'))
        scale(im, 4).save(os.path.join(ld, name + '@4x.png'))
    groups['longmen2'] = {'name': {'zh': '龍門刀客傳 貳 登場人物', 'en': 'People of Longmen Quest II'},
                          'faction': 'longmen', 'members': L2, 'style': 'nes',
                          'files': {k: 'chars/longmen/' + v for k, v in (('nes', 'group-nes-l2.png'), ('nes4x', 'group-nes-l2@4x.png'),
                                                                          ('nesTall', 'group-nes-l2-4col.png'), ('nesTall4x', 'group-nes-l2-4col@4x.png'))}}
    from nes_foes import group as foe_group2
    L2F = [c for c in ROSTER if getattr(importlib.import_module(c), 'GROUP', '') == 'longmen2Foes']
    fd2 = os.path.join(ROOT, 'chars', 'foes')
    os.makedirs(fd2, exist_ok=True)
    for name, im in (('group-nes-l2', foe_group2(L2F, cols=8)), ('group-nes-l2-4col', foe_group2(L2F, cols=4))):
        im.save(os.path.join(fd2, name + '.png'))
        scale(im, 4).save(os.path.join(fd2, name + '@4x.png'))
    groups['longmen2Foes'] = {'name': {'zh': '龍門刀客傳 貳 的妖物', 'en': 'Creatures of Longmen Quest II'}, 'faction': 'foe', 'members': L2F, 'style': 'nes',
                              'files': {k: 'chars/foes/' + v for k, v in (('nes', 'group-nes-l2.png'), ('nes4x', 'group-nes-l2@4x.png'),
                                                                           ('nesTall', 'group-nes-l2-4col.png'), ('nesTall4x', 'group-nes-l2-4col@4x.png'))}}
    # 奕叡's paper doll (made by Longmen Quest's js/doll.js, so the pictures are kept as they are, not redrawn here)
    groups['yiruiDoll'] = {'name': {'zh': '奕叡的紙娃娃', 'en': "Yi Rui's paper doll"}, 'faction': 'longmen', 'members': ['yirui'], 'style': 'nes', 'files': {'nes': 'chars/yirui/doll/group-nes-doll.png', 'nes4x': 'chars/yirui/doll/group-nes-doll@4x.png', 'nesTall': 'chars/yirui/doll/group-nes-doll-3x2.png', 'nesTall4x': 'chars/yirui/doll/group-nes-doll-3x2@4x.png', 'outfits': 'chars/yirui/doll/outfits.png', 'pieces': 'chars/yirui/doll/pieces.png', 'json': 'chars/yirui/doll/doll.json'}}
    # monsters & beasts as one NES encounter screen
    from nes_beasts import BEASTS, group as beast_group
    bd = os.path.join(ROOT, 'chars', 'beasts')
    os.makedirs(bd, exist_ok=True)
    for name, im in (('group-nes', beast_group(BEASTS)), ('group-nes-3x3', beast_group(BEASTS, cols=3))):
        im.save(os.path.join(bd, name + '.png'))
        scale(im, 4).save(os.path.join(bd, name + '@4x.png'))
    groups['beasts'] = {'name': {'zh': '怪物與野獸', 'en': 'Monsters & Beasts'}, 'faction': 'beast',
                        'members': BEASTS, 'style': 'nes',
                        'files': {k: 'chars/beasts/' + v for k, v in (('nes', 'group-nes.png'), ('nes4x', 'group-nes@4x.png'),
                                                                       ('nesTall', 'group-nes-3x3.png'), ('nesTall4x', 'group-nes-3x3@4x.png'))}}
    # the common foes (小怪), ordered by tier
    from nes_foes import group as foe_group
    FOE_IDS = [c for c in ROSTER if importlib.import_module(c).FACTION == 'foe']
    fd = os.path.join(ROOT, 'chars', 'foes')
    os.makedirs(fd, exist_ok=True)
    for name, im in (('group-nes', foe_group(FOE_IDS, cols=10)), ('group-nes-5col', foe_group(FOE_IDS, cols=5))):
        im.save(os.path.join(fd, name + '.png'))
        scale(im, 4).save(os.path.join(fd, name + '@4x.png'))
    groups['foes'] = {'name': {'zh': '小怪', 'en': 'Common Foes'}, 'faction': 'foe', 'members': FOE_IDS, 'style': 'nes',
                      'files': {k: 'chars/foes/' + v for k, v in (('nes', 'group-nes.png'), ('nes4x', 'group-nes@4x.png'),
                                                                   ('nesTall', 'group-nes-5col.png'), ('nesTall4x', 'group-nes-5col@4x.png'))}}
    # 三國志 霸王之路: Jeff as the main general, then each stage's enemy general
    SANGO = ['jeff_sango', 'chengyuanzhi', 'zhangbao', 'huaxiong', 'jiling', 'yanliang', 'wenchou', 'zhangliao', 'xiahoudun', 'lubu']
    sd = os.path.join(ROOT, 'chars', 'sango')
    os.makedirs(sd, exist_ok=True)
    for name, im in (('group-nes', nes_group(SANGO, cols=10)), ('group-nes-5col', nes_group(SANGO, cols=5))):
        im.save(os.path.join(sd, name + '.png'))
        scale(im, 4).save(os.path.join(sd, name + '@4x.png'))
    groups['sango'] = {'name': {'zh': '三國志 霸王之路', 'en': 'Three Kingdoms: Path of the Hegemon'}, 'faction': 'sango',
                       'members': ['jeff'] + SANGO[1:], 'style': 'nes',
                       'files': {k: 'chars/sango/' + v for k, v in (('nes', 'group-nes.png'), ('nes4x', 'group-nes@4x.png'),
                                                                     ('nesTall', 'group-nes-5col.png'), ('nesTall4x', 'group-nes-5col@4x.png'))}}
    groups['family']['faction'] = 'west'
    with open(os.path.join(ROOT, 'chars', 'index.json'), 'w', encoding='utf-8') as f:
        json.dump({'version': 3, 'mainStyle': 'nes', 'styles': styles, 'groups': groups, 'characters': entries},
                  f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
