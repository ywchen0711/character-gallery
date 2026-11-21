"""nes2 field sprites for the rest of the Longmen cast (everyone but the six round-1 heroes), built from the kit's
sprite heads (nes2_kit.SHEADS) and body templates, each with the portrait's headgear, colours and prop.

sp(cid, head, c, d, h, b, ...) registers a sprite whose layers are
  pal  = k black, S skin, c the main cloth colour
  pal2 = d cloth shade, h hair, b headgear / accent      (one NES colour each; 3 + transparent per layer)
Template letters are swapped per character: w (collar trim) and x (headgear band) -> any of the six letters.
Props are overlays in one of the six letters, so no layer ever needs a fourth colour.
"""
import nes2_longmen_sprites as SPM
from nes2_kit import SHEADS, sprite

over = SPM.over


def _heads(base, front=(), side=(), back=()):
    f, s, b = SHEADS[base]
    return (over(f, front[0], 0, front[1]) if front else f,
            over(s, side[0], 0, side[1]) if side else s,
            over(b, back[0], 0, back[1]) if back else b)


# extra heads derived from the kit's
SHEADS['shaved'] = _heads('topknot', (['......kkkk......', '......khhk......', '....kkkkkkkk....', '...kSSkhhkSSk...',
                                       '..kSSSkhhkSSSk..', '..kSSSSSSSSSSk..', '..kSSSSSSSSSSk..'], 0),
                          (['.....kkkk.......', '.....khhk.......', '...kkkkkkkk.....', '..kSSkhhkSSk....',
                            '.kSSSSkhhkSSk...', '.kSSSSSSSSSSSk..', '.kSSSSSSSSSSSk..'], 0),
                          (['......kkkk......', '......khhk......', '....kkkkkkkk....', '...kSSkhhkSSk...',
                            '..kSSSkhhkSSSk..', '..kSSSSSSSSSSk..', '..kSSSSSSSSSSk..'], 0))
SHEADS['wild'] = _heads('spiky', (['.k.k..k..k..k.k.', 'khkhkkhkkhkkhkhk'], 0), (['k.k..k..k.......', 'hkhkkhkkhkk.....'], 0),
                        (['.k.k..k..k..k.k.', 'khkhkkhkkhkkhkhk'], 0))
SHEADS['crown'] = _heads('topknot', (['......kbbk......', '.....kbbbbk.....'], 0), (['.....kbbk.......', '....kbbbbk......'], 0),
                         (['......kbbk......', '.....kbbbbk.....'], 0))
SHEADS['melon'] = _heads('cap', (['.......kk.......', '.......kxk......'], 0), (['......kk........', '......kxk.......'], 0),
                         (['.......kk.......', '.......kxk......'], 0))
SHEADS['flat'] = _heads('cap', (['....kkkkkkkk....', '....kbbbbbbk....', '....kbbbbbbk....', '.kkkkkkkkkkkkkk.',
                                 '.kbbbbbbbbbbbbk.', '.kkkkkkkkkkkkkk.', '..khhhhhhhhhhk..'], 0),
                        (['...kkkkkkkk.....', '...kbbbbbbk.....', '...kbbbbbbk.....', 'kkkkkkkkkkkkkk..',
                          'kbbbbbbbbbbbbk..', 'kkkkkkkkkkkkkk..', '.khhhhhhhhhhhk..'], 0),
                        (['....kkkkkkkk....', '....kbbbbbbk....', '....kbbbbbbk....', '.kkkkkkkkkkkkkk.',
                          '.kbbbbbbbbbbbbk.', '.kkkkkkkkkkkkkk.', '..khhhhhhhhhhk..'], 0))
SHEADS['scholar'] = _heads('cap', (['....kkkkkkkk....', '....kbbbbbbk....', '....kbkbbkbk....', '....kbkbbkbk....',
                                    '...kkkkkkkkkk...', '..kbbbbbbbbbbk..', '..kkkkkkkkkkkk..'], 0),
                           (['....kkkkkkkk....', '....kbbbbbbk....', '....kbbbbkbk....', '....kbbbbkbk....',
                             '...kkkkkkkkkk...', '..kbbbbbbbbbbk..', '..kkkkkkkkkkkk..'], 0),
                           (['....kkkkkkkk....', '....kbbbbbbk....', '....kbbbbbbk....', '....kbbbbbbk....',
                             '...kkkkkkkkkk...', '..kbbbbbbbbbbk..', '..kkkkkkkkkkkk..'], 0))
SHEADS['feather'] = _heads('cap', (['.k.k.k.k.k.k.k..', 'kbkbkbkbkbkbkbk.', 'kbkbkbkbkbkbkbk.', '.kkkkkkkkkkkkk..',
                                    '..kbbbbbbbbbbk..', '..kbxbbxbbxbbk..', '..kkkkkkkkkkkk..'], 0),
                           (['k.k.k.k.k.k.k...', 'bkbkbkbkbkbkbk..', 'bkbkbkbkbkbkbk..', 'kkkkkkkkkkkkk...',
                             '.kbbbbbbbbbbbk..', '.kbxbbxbbxbbbk..', '.kkkkkkkkkkkkk..'], 0),
                           (['.k.k.k.k.k.k.k..', 'kbkbkbkbkbkbkbk.', 'kbkbkbkbkbkbkbk.', '.kkkkkkkkkkkkk..',
                             '..kbbbbbbbbbbk..', '..kbxbbxbbxbbk..', '..kkkkkkkkkkkk..'], 0))
SHEADS['tiger'] = _heads('hood', (['..kkk....kkk....', '.kbbbk..kbbbk...', '.kbxbkkkkbxbk...'], 0),
                         (['..kkk...........', '.kbbbk..........', '.kbxbkkkkk......'], 0),
                         (['..kkk....kkk....', '.kbbbk..kbbbk...', '.kbxbkkkkbxbk...'], 0))


# ---------------------------------------------------------------- props (front, side, back overlays)
def _col(letter, n, top=None):
    return [letter] * n


def prop(name, L='b', hilt='k'):
    if name == 'staff':
        return dict(front=[(_col(L, 21), 14, 2)], side=[(_col(L, 21), 12, 2)], back=[(_col(L, 21), 1, 2)])
    if name == 'spear':
        return dict(front=[(['k', L, L] + _col('d', 18), 14, 1)], side=[(['k', L, L] + _col('d', 18), 12, 1)],
                    back=[(['k', L, L] + _col('d', 18), 1, 1)])
    if name == 'blade':
        b = ['k'] + _col(L, 7) + [hilt, hilt]
        return dict(front=[(b, 14, 8)], side=[(b, 12, 8)], back=[([L, L, hilt], 13, 11)])
    if name == 'club':
        b = ['.kk.', 'k' + L + L + 'k', 'k' + L + L + 'k', 'k' + L + L + 'k', '.k' + L + 'k', '.k' + L + 'k',
             '.k' + L + 'k', '.k' + L + 'k', '..k.']
        return dict(front=[(b, 12, 7)], side=[(b, 10, 7)], back=[([r[::-1] for r in b], 0, 7)])
    if name == 'bow':
        b = ['.k', 'k' + L, 'k' + L, 'k' + L, 'k' + L, 'k' + L, 'k' + L, 'k' + L, 'k' + L, '.k']
        return dict(front=[(b, 0, 10)], side=[(b, 1, 10)], back=[(b, 14, 10)])
    if name == 'banner':
        f = ['kkkkk', 'k' + L * 3 + 'k', 'k' + L * 3 + 'k', 'k' + L * 3 + 'k', 'kkkkk']
        return dict(front=[(_col('d', 21), 15, 2), (f, 10, 1)], side=[(_col('d', 21), 13, 2), (f, 8, 1)],
                    back=[(_col('d', 21), 0, 2), (f, 1, 1)])
    if name == 'qin':
        q = ['kkkkkkkkkkkkkk', 'k' + L * 12 + 'k', 'kkkkkkkkkkkkkk']
        return dict(front=[(q, 1, 16)], side=[(q[:][0:3], 2, 16)], back=[])
    if name == 'gourd':
        g = ['.k.', 'k' + L + 'k', 'k' + L + 'k', '.k.']
        return dict(front=[(g, 12, 17)], side=[(g, 10, 17)], back=[(g, 1, 17)])
    if name == 'book':
        g = ['kkkk', 'k' + L * 2 + 'k', 'k' + L * 2 + 'k', 'kkkk']
        return dict(front=[(g, 9, 15)], side=[(g, 10, 15)], back=[])
    if name == 'fan':
        g = ['kkkk', 'k' + L * 2 + 'k', '.kk.']
        return dict(front=[(g, 12, 14)], side=[(g, 10, 14)], back=[])
    if name == 'pack':
        g = ['kkkkkkkkkkkk', 'k' + L * 10 + 'k', 'k' + L * 10 + 'k', 'k' + L * 10 + 'k', 'kkkkkkkkkkkk']
        return dict(front=[], side=[(g[:][0:5], 0, 13)] if False else [], back=[(g, 2, 13)])
    raise KeyError(name)


def merge(*ds):
    out = dict(front=[], side=[], back=[])
    for d in ds:
        for k in out:
            out[k] += d.get(k, [])
    return out


# ---------------------------------------------------------------- face overlays (front head rows; heads are 14 rows)
def beard_rows(kind, L='h'):
    if kind == 'full':
        return [(['..k' + L * 10 + 'k..'[:0] + '', ], 0, 0)] if False else [
            (['..kS' + L * 8 + 'Sk..'], 0, 11),
            (['...k' + L * 8 + 'k...'], 0, 12), (['....k' + L * 6 + 'k....'], 0, 13)]
    if kind == 'long':
        return [(['..kk' + L * 8 + 'kk..'], 0, 11), (['...k' + L * 8 + 'k...'], 0, 12),
                (['....k' + L * 6 + 'k....'], 0, 13)]
    if kind == 'moustache':
        return [(['.....kkkkkk.....'], 0, 11)]
    if kind == 'goatee':
        return [(['......kkkk......'], 0, 12), (['.......kk.......'], 0, 13)]
    if kind == 'glasses':
        return [(['...kkkk..kkkk...'], 0, 9)]
    if kind == 'cloth':
        return [(['..k' + L * 10 + 'k..'], 0, 11), (['...k' + L * 8 + 'k...'], 0, 12)]
    if kind == 'mask':          # a full mask over the face
        return [(['..k' + L * 10 + 'k..'], 0, 8), (['.k' + L + 'k' + L * 8 + 'k' + L + 'k.'], 0, 9),
                (['.k' + L * 12 + 'k.'], 0, 10), (['..k' + L + 'kkkkkk' + L + 'k..'], 0, 11),
                (['...k' + L * 8 + 'k...'], 0, 12)]
    if kind == 'half':
        return [(['........' + L * 4 + 'k...'], 0, 8), (['........' + L + 'k' + L + L + 'k...'], 0, 9),
                (['........' + L * 4 + 'k...'], 0, 10)]
    raise KeyError(kind)


def sp(cid, head, c, d, h, b, S=0x37, body='robe', w='b', x='b', props=None, face=None, short=False, extra_m=None,
       hairfill=False, hm=None):
    m = {'w': w, 'x': x}
    m.update(extra_m or {})
    f, s, bk = [list(r) for r in SHEADS[head]]
    hm = dict(hm or {})
    hm.setdefault('x', x)
    hm.setdefault('w', w)
    f, s, bk = [SPM.sub(v, hm) for v in (f, s, bk)]
    for rows, x0, y0 in face or []:
        f = over(f, rows, x0, y0)
    sprite(cid, (f, s, bk), dict(k=0x0F, S=S, c=c), dict(d=d, h=h, b=b), body=body, m=m,
           extra=props or dict(front=[], side=[], back=[]), short=short, hairfill=hairfill)


def old(cid):
    SPM.SPRITES[cid] = dict(old=True)


BK = 0x0C          # black hair, drawn as dark slate with black strands (as in the round-1 heroes)
TAN = 0x27

# ================================================================ Longmen Quest
sp('heixiong', 'wild', 0x10, 0x07, BK, 0x17, body='robe', w='d', props=prop('club', 'b'), face=beard_rows('full', 'h'))
sp('daoba', 'shaved', 0x16, 0x06, BK, 0x30, w='S', props=prop('blade', 'b'))
sp('shouhou', 'spiky', 0x18, 0x08, BK, 0x30, w='S', props=prop('blade', 'b'))
sp('tuqianqiu', 'long', 0x14, 0x04, BK, 0x30, S=0x36, w='b', props=prop('fan', 'b'), face=beard_rows('half', 'b'))
sp('tiewusi', 'official', 0x00, 0x0C, BK, 0x0C, w='S', props=prop('staff', 'S'), face=beard_rows('moustache'))
sp('qianwanli', 'melon', 0x16, 0x06, BK, 0x28, w='b', hm={'b': 'c', 'x': 'b'}, props=prop('book', 'b'))
sp('wenruyu', 'topknot', 0x3A, 0x2A, BK, 0x30, w='b', props=prop('book', 'd'))
sp('xiaolian', 'twinbuns', 0x25, 0x15, BK, 0x16, body='boy', w='S', x='b', short=True)
sp('lihanshan', 'long', 0x16, 0x06, 0x30, 0x26, w='b', props=prop('blade', 'b'))
sp('yuweng', 'straw', 0x00, 0x2D, 0x30, 0x38, w='h', x='b', props=prop('staff', 'd'), face=beard_rows('long', 'h'))
sp('guimian', 'hood', 0x16, 0x06, 0x30, 0x16, w='d', face=beard_rows('mask', 'h'))
sp('masked', 'hood', 0x14, 0x04, 0x28, 0x04, w='h', face=beard_rows('cloth', 'd'))

# ================================================================ Longmen Quest II, Tactics story people, the abbess
sp('hubanxian', 'flat', 0x10, 0x00, BK, 0x00, w='S', props=prop('banner', 'S'), face=beard_rows('glasses'))
sp('jiabafang', 'cap', 0x27, 0x17, BK, 0x16, w='S', x='k', props=prop('pack', 'd'))
sp('wudadan', 'cap', 0x16, 0x06, BK, 0x16, S=TAN, w='S', x='k', props=prop('staff', 'd'), face=beard_rows('full', 'h'))
sp('wenduizhang', 'flat', 0x21, 0x11, BK, 0x10, w='S', props=prop('staff', 'h'))
sp('suxiaowan', 'bun_f', 0x2A, 0x1A, BK, 0x30, S=0x31, body='gown', w='b', hairfill=False)
sp('chutiankuo', 'band', 0x1C, 0x0C, 0x0F, 0x30, w='b', props=prop('blade', 'b'))
sp('niubaobao', 'bald', 0x27, 0x17, BK, 0x30, w='b', props=prop('gourd', 'b'))
sp('mojide', 'cap', 0x1A, 0x0A, BK, 0x10, w='b', x='k', props=prop('book', 'd'), face=beard_rows('glasses'))
sp('huotianxia', 'band', 0x27, 0x16, BK, 0x28, w='b',
   props=dict(front=[(['d'] * 8, 1, 14), (['d'] * 8, 14, 14)], side=[(['dd'] * 8, 1, 14)],
              back=[(['dddddddddddd'] * 8, 2, 14)]))
sp('mowuya', 'topknot', 0x13, 0x03, 0x02, 0x28, S=0x36, w='b', props=prop('staff', 'b'))
sp('aman', 'feather', 0x12, 0x02, BK, 0x30, S=TAN, body='boy', w='b', x='k', short=True)
sp('jingci', 'hood', 0x00, 0x2D, 0x16, 0x30, w='h', props=prop('staff', 'b'))
sp('yichangfeng', 'topknot', 0x12, 0x02, 0x10, 0x30, w='b', props=prop('blade', 'b'), face=beard_rows('long', 'h'))
sp('xiaowuying', 'official', 0x14, 0x04, BK, 0x00, w='S', props=prop('blade', 'S'))

# ================================================================ Sects of Longmen and the Tactics jobs
sp('sx_grandmaster', 'topknot', 0x21, 0x11, 0x30, 0x28, w='h', props=prop('staff', 'b'), face=beard_rows('long', 'h'))
sp('sx_smith', 'cap', 0x17, 0x07, BK, 0x10, S=TAN, w='S', x='k', props=prop('club', 'b'))
sp('sx_founder', 'topknot', 0x27, 0x17, BK, 0x2A, w='S', props=prop('staff', 'b'))
sp('sx_scout', 'straw', 0x1A, 0x0A, BK, 0x38, w='S', x='d')
sp('sx_disciple', 'band', 0x10, 0x00, BK, 0x30, w='b', props=prop('staff', 'd'))
sp('sx_archer', 'band', 0x1A, 0x0A, BK, 0x16, w='S', props=prop('bow', 'b'))
sp('sx_saber', 'topknot', 0x17, 0x07, BK, 0x30, w='S', props=prop('blade', 'b'))
sp('sx_sword', 'band', 0x21, 0x11, BK, 0x30, w='b', props=prop('blade', 'b'))
sp('sx_hidden', 'hood', 0x13, 0x03, BK, 0x10, w='b')
sp('sx_spear', 'helmet', 0x16, 0x06, BK, 0x10, w='b', x='c', props=prop('spear', 'b'))
sp('sx_inner', 'long', 0x30, 0x10, BK, 0x21, body='robe', w='b')
sp('sx_swordform', 'helmet', 0x11, 0x02, BK, 0x10, w='b', x='b', props=prop('blade', 'b'))
sp('sx_crossbow', 'cap', 0x1C, 0x0C, 0x0F, 0x10, w='b', x='k', props=prop('bow', 'b'))
sp('sx_master', 'topknot', 0x00, 0x0C, 0x30, 0x28, w='b', props=prop('blade', 'h'))
sp('sx_starbow', 'helmet', 0x16, 0x06, BK, 0x28, w='b', x='c', props=prop('bow', 'b'))
old('sx_rider')
old('sx_ironcav')
old('sx_caravan')
old('sx_ram')
old('sx_catapult')
old('sx_thunder')
old('sx_boat')
old('sx_warship')
sp('sx_lm_saber', 'band', 0x12, 0x02, BK, 0x21, w='b', props=prop('blade', 'b'))
sp('sx_hj_sword', 'bun_f', 0x31, 0x21, BK, 0x10, body='gown', w='b', props=prop('blade', 'b'), hairfill=False)
sp('sx_qf_monk', 'bald', 0x28, 0x18, BK, 0x16, w='b', props=prop('staff', 'h'))
sp('sx_bl_palm', 'spiky', 0x16, 0x06, BK, 0x28, S=TAN, w='S', x='b')
sp('sx_ym_assassin', 'hood', 0x14, 0x04, 0x30, 0x04, w='h', face=beard_rows('half', 'h'))
sp('sx_yy_tiger', 'tiger', 0x1A, 0x0A, BK, 0x2A, w='b', x='h')
sp('sx_qj_escort', 'melon', 0x28, 0x18, BK, 0x16, w='b', hm={'x': 'c'}, props=prop('banner', 'b'))
sp('sx_hf_club', 'wild', 0x17, 0x07, BK, 0x10, S=TAN, w='S', props=prop('club', 'd'), face=beard_rows('full', 'h'))
sp('sx_xd_blood', 'topknot', 0x16, 0x06, BK, 0x26, w='b', props=prop('blade', 'b'))
sp('sx_zf_chain', 'official', 0x00, 0x0C, BK, 0x2D, w='S', face=beard_rows('moustache'))
sp('sx_cy_nun', 'hood', 0x25, 0x15, 0x10, 0x30, w='b', props=prop('blade', 'b'))
sp('sx_physician', 'topknot', 0x1A, 0x0A, BK, 0x27, w='S', props=prop('gourd', 'b'))
sp('sx_physician_f', 'bun_f', 0x1C, 0x0C, BK, 0x27, body='gown', w='S', props=prop('gourd', 'b'), hairfill=False)
sp('sx_thief', 'band', 0x00, 0x0C, BK, 0x16, S=TAN, w='b', props=prop('blade', 'S'))
sp('sx_daoist', 'crown', 0x28, 0x18, BK, 0x38, w='S', props=prop('blade', 'S'))
sp('sx_qin', 'long', 0x21, 0x11, BK, 0x17, w='b', props=prop('qin', 'b'))
sp('sx_qin_f', 'bun_f', 0x25, 0x15, BK, 0x17, body='gown', w='S', props=prop('qin', 'b'), hairfill=False)
sp('sx_poison', 'hood', 0x14, 0x04, BK, 0x1A, w='S', hm={'b': 'c'}, props=prop('gourd', 'b'))
sp('sx_strategist', 'cap', 0x10, 0x00, BK, 0x30, w='b', x='k', hm={'b': 'h'}, props=prop('fan', 'b'), face=beard_rows('goatee'))
sp('sx_teller', 'scholar', 0x17, 0x07, BK, 0x00, w='S', props=prop('fan', 'S'), face=beard_rows('goatee'))
sp('sx_scholar', 'band', 0x1C, 0x0C, 0x0F, 0x30, w='b', props=prop('staff', 'h'))
sp('sx_phantom', 'hood', 0x00, 0x2D, BK, 0x0C, w='S', face=beard_rows('cloth', 'b'))
