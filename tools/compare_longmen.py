"""Build compare-longmen.html (old `nes` vs new `nes2` for the whole Longmen cast, grouped in tabs so a phone only
loads one group's pictures) and review pictures in chars/longmen/:
  compare-nes2-<group>.png   old and new portraits plus the new walk frames, per group, at 3x
  compare-nes2.png           the six heroes at 4x
  town-nes2.png              old and new sprites on an LQ-like town floor at the in-game 3x scale

    python -P tools/compare_longmen.py        (after tools/export_nes2.py)
"""
import json
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = json.load(open(os.path.join(ROOT, 'chars', 'index.json'), encoding='utf-8'))
BY = {c['id']: c for c in IDX['characters']}
HEROES = ['yirui', 'yishuo', 'liuhanyan', 'baixian', 'kuchan', 'xiaotian']
JOBS = IDX['groups']['tacticsJobs']['members']
NES2 = [c['id'] for c in IDX['characters'] if any(v['style'] == 'nes2' for v in c['variants'])]
LQ = [c for c in ['heixiong', 'daoba', 'shouhou', 'tuqianqiu', 'tiewusi', 'qianwanli', 'wenruyu', 'xiaolian',
                  'lihanshan', 'yuweng', 'guimian', 'masked'] if c in NES2]
LQ2 = [c for c in NES2 if BY[c]['faction'] == 'longmen' and c not in HEROES + LQ]
SECTS = [c for c in NES2 if BY[c]['faction'] == 'sects' and c not in JOBS]
GROUPS = [('heroes', '六位主角', 'The six heroes', HEROES), ('lq', '龍門刀客傳', 'Longmen Quest', LQ),
          ('lq2', '刀客傳貳・戰記・慈雲庵', 'LQ II, Tactics, Mercy Cloud', LQ2),
          ('sects', '江湖志 各派', 'Sects of Longmen', SECTS), ('jobs', '戰記 江湖百業', 'Tactics jobs', JOBS)]


def load(cid, style):
    d = os.path.join(ROOT, 'chars', cid, style)
    por = Image.open(os.path.join(d, 'portrait.png')).convert('RGBA')
    sheet = Image.open(os.path.join(d, 'sheet.png')).convert('RGBA')
    meta = json.load(open(os.path.join(d, 'sheet.json'), encoding='utf-8'))
    fw, fh = meta['frameWidth'], meta['frameHeight']
    fr = {}
    for n, a in meta['animations'].items():
        fr[n] = [sheet.crop((i * fw, a['row'] * fh, i * fw + fw, a['row'] * fh + fh)) for i in range(a['frames'])]
    return por, fr, meta


def window(img):
    w, h = img.width + 4, img.height + 4
    out = Image.new('RGBA', (w, h), (0, 0, 0, 255))
    ImageDraw.Draw(out).rectangle((0, 0, w - 1, h - 1), outline=(252, 252, 252, 255))
    out.alpha_composite(img, (2, 2))
    return out


def group_png(ids, path, K=3, cols=4):
    cw, ch = (52 * 2 + 3 * 17 + 10) * K, (60 + 30) * K
    rows = (len(ids) + cols - 1) // cols
    out = Image.new('RGBA', (cols * cw, rows * ch), (52, 60, 56, 255))
    d = ImageDraw.Draw(out)
    for i, cid in enumerate(ids):
        x, y = (i % cols) * cw + 4 * K, (i // cols) * ch + 4 * K
        old, ofr, _ = load(cid, 'nes')
        new, nfr, _ = load(cid, 'nes2')
        out.alpha_composite(window(old).resize((52 * K, 60 * K), 0), (x, y))
        out.alpha_composite(window(new).resize((52 * K, 60 * K), 0), (x + 53 * K, y))
        seq = [nfr['walk'][0], nfr['walk_side'][0], nfr['walk_up'][0]]
        for j, f in enumerate(seq):
            out.alpha_composite(f.resize((f.width * K, f.height * K), 0), (x + (107 + j * 17) * K, y + 2 * K))
        of = ofr.get('walk', list(ofr.values())[0])[0]
        out.alpha_composite(of.resize((of.width * K, of.height * K), 0), (x + 107 * K, y + 30 * K))
        d.text((x, y + 61 * K), cid, fill=(230, 230, 220, 255))
    out.save(path)


def town_floor(w, h):
    im = Image.new('RGBA', (w, h), (0, 168, 0, 255))
    P = im.load()
    for y in range(h):
        for x in range(w):
            if 14 <= y < 30:
                P[x, y] = (172, 124, 0, 255) if (x // 8 + (y // 4) % 2) % 2 else (136, 20, 0, 255)
                if y % 4 == 0:
                    P[x, y] = (80, 48, 0, 255)
            elif y < 14:
                P[x, y] = (0, 64, 88, 255) if (x + y // 3) % 6 else (0, 0, 0, 255)
            elif 40 <= y < 72:
                t = ((x // 8) + (y // 8)) % 2
                P[x, y] = (188, 188, 188, 255) if t else (124, 124, 124, 255)
                if x % 8 == 0 or y % 8 == 0:
                    P[x, y] = (120, 120, 120, 255)
            elif (x * 7 + y * 13) % 23 == 0:
                P[x, y] = (88, 216, 84, 255)
    return im


def town_png(ids):
    S = 3
    w, h = len(ids) * 22 + 8, 96
    out = Image.new('RGBA', (w * S, h * 2 * S + 8), (0, 0, 0, 255))
    for k, st in enumerate(('nes', 'nes2')):
        im = town_floor(w, h)
        for i, cid in enumerate(ids):
            _, fr, _ = load(cid, st)
            im.alpha_composite(fr.get('walk', list(fr.values())[0])[0], (6 + i * 22, 38 if i % 2 else 50))
        out.alpha_composite(im.resize((w * S, h * S), 0), (0, k * (h * S + 8)))
    out.save(os.path.join(ROOT, 'chars', 'longmen', 'town-nes2.png'))


HTML = '''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>龍門人物 新舊對照</title>
<style>
:root { --bg: #14181a; --panel: #1f2629; --ink: #eef1ea; --dim: #9aa79f; --line: #3a4549; --accent: #e8b84a; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.5 system-ui, -apple-system, "PingFang TC", "Microsoft JhengHei", sans-serif;
       padding: max(16px, env(safe-area-inset-top)) max(16px, env(safe-area-inset-right)) 32px max(16px, env(safe-area-inset-left)); }
header, main, nav { max-width: 1100px; margin: 0 auto; }
header { margin-bottom: 12px; }
header > div { min-width: 0; }
h1 { margin: 0; font-size: 22px; overflow-wrap: anywhere; }
.sub { color: var(--dim); margin: 4px 0 0; max-width: 70ch; }
a { color: var(--accent); }
nav { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }
.bar { display: flex; gap: 8px; flex-wrap: wrap; margin: 0 auto 14px; max-width: 1100px; }
button { font: inherit; color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 999px; padding: 6px 14px; cursor: pointer; }
button.on { background: var(--accent); color: #1a1a1a; border-color: var(--accent); }
main { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 330px), 1fr)); gap: 12px; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 10px; min-width: 0; }
.card h2 { margin: 0 0 6px; font-size: 16px; }
.card h2 span { color: var(--dim); font-weight: 400; font-size: 13px; margin-left: 6px; }
.pair { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px; }
.side { display: flex; flex-direction: column; align-items: center; gap: 6px; min-width: 0; }
.tag { font-size: 12px; color: var(--dim); }
.tag.new { color: var(--accent); }
img, canvas { image-rendering: pixelated; image-rendering: crisp-edges; }
.por { width: 100%; max-width: 192px; height: auto; border: 2px solid #fcfcfc; background: #000; }
.walk { width: 64px; height: 96px; background: #00a800; border-radius: 6px; }
.town { width: 100%; height: auto; border-radius: 8px; display: block; }
.note { color: var(--dim); font-size: 14px; max-width: 75ch; }
footer { max-width: 1100px; margin: 18px auto 0; }
</style>
</head>
<body>
<header><div>
  <h1>龍門人物 新舊對照 <span style="font-size:15px;color:var(--dim)">Longmen cast, old vs new</span></h1>
  <p class="sub">左：舊版 <b>nes</b>；右：新版 <b>nes2</b>（頭像有明暗與背景、小黑眼、鼻子只留一筆淡陰影；小人兩層精靈並有背面）。分組顯示，只載入目前這一組。</p>
</div></header>
<nav id="tabs" aria-label="groups"></nav>
<div class="bar" role="group" aria-label="walk direction">
  <button data-d="walk" class="on">正面</button><button data-d="walk_side">側面</button><button data-d="walk_left">左</button><button data-d="walk_up">背面</button>
</div>
<main id="cards"></main>
<footer>
  <section class="card"><h2>小鎮上的實際大小 <span>in-game 3x on a town floor: top old, bottom new</span></h2>
  <img class="town" alt="old and new sprites on a town floor" src="chars/longmen/town-nes2.png" loading="lazy"></section>
  <p class="note">小人仍是 16×24 格，列序 idle、walk、walk_side 不變，另加 walk_up（背面）。車、器械、船與騎兵沿用原本的小人圖（新頭像是乘員）。</p>
  <p><a href="index.html">← 回人物圖庫 Back to the gallery</a></p>
</footer>
<script>
const GROUPS = __GROUPS__;
const tabs = document.getElementById('tabs'), cards = document.getElementById('cards');
let anims = [], dir = 'walk', tick = 0;
function img(src, cls, alt) { const i = new Image(); i.src = src; i.decoding = 'async'; if (cls) i.className = cls; i.alt = alt || ''; return i; }
function show(g) {
  anims = []; cards.textContent = '';
  tabs.querySelectorAll('button').forEach((b) => b.classList.toggle('on', b.dataset.g === g.id));
  try { localStorage.setItem('lm-cmp-tab', g.id); } catch (e) {}
  for (const c of g.chars) {
    const card = document.createElement('section'); card.className = 'card';
    const h = document.createElement('h2'); h.textContent = c.zh; const s = document.createElement('span'); s.textContent = c.en; h.appendChild(s);
    const pair = document.createElement('div'); pair.className = 'pair';
    for (const st of ['nes', 'nes2']) {
      const v = c[st]; const side = document.createElement('div'); side.className = 'side';
      const tag = document.createElement('div'); tag.className = 'tag' + (st === 'nes2' ? ' new' : ''); tag.textContent = st === 'nes' ? '舊 old' : '新 new';
      const cv = document.createElement('canvas'); cv.width = 16; cv.height = 24; cv.className = 'walk';
      side.append(tag, img('chars/' + c.id + '/' + st + '/portrait.png', 'por', c.en + ' ' + st), cv);
      pair.appendChild(side);
      const sheet = img('chars/' + c.id + '/' + st + '/sheet.png');
      sheet.addEventListener('load', draw);
      anims.push({ cv, sheet, v });
    }
    card.append(h, pair); cards.appendChild(card);
  }
  draw();
}
function draw() {
  for (const a of anims) {
    if (!a.sheet.complete || !a.sheet.naturalWidth) continue;
    const g = a.cv.getContext('2d'); g.imageSmoothingEnabled = false; g.clearRect(0, 0, 16, 24);
    const key = dir === 'walk_left' ? 'walk_side' : dir;
    const r = a.v.rows[key] || a.v.rows.walk || a.v.rows.move || a.v.rows.idle || [0, 1];
    const f = tick % r[1], fw = a.v.fw, fh = a.v.fh;
    const dx = (16 - fw) >> 1, dy = 24 - fh;
    if (dir === 'walk_left') { g.save(); g.translate(16, 0); g.scale(-1, 1); }
    g.drawImage(a.sheet, f * fw, r[0] * fh, fw, fh, dx, dy, fw, fh);
    if (dir === 'walk_left') g.restore();
  }
}
for (const g of GROUPS) {
  const b = document.createElement('button'); b.dataset.g = g.id; b.textContent = g.zh + ' (' + g.chars.length + ')'; b.title = g.en;
  b.addEventListener('click', () => show(g)); tabs.appendChild(b);
}
document.querySelectorAll('[data-d]').forEach((b) => b.addEventListener('click', () => {
  dir = b.dataset.d; document.querySelectorAll('[data-d]').forEach((x) => x.classList.toggle('on', x === b)); draw();
}));
let start = GROUPS[0];
try { const s = localStorage.getItem('lm-cmp-tab'); start = GROUPS.find((g) => g.id === s) || start; } catch (e) {}
show(start);
setInterval(() => { tick++; draw(); }, 260);
</script>
</body>
</html>
'''


def main():
    os.makedirs(os.path.join(ROOT, 'chars', 'longmen'), exist_ok=True)
    groups = []
    for gid, zh, en, ids in GROUPS:
        chars = []
        for cid in ids:
            e = {'id': cid, 'zh': BY[cid]['name']['zh'], 'en': BY[cid]['name']['en']}
            for st in ('nes', 'nes2'):
                meta = json.load(open(os.path.join(ROOT, 'chars', cid, st, 'sheet.json'), encoding='utf-8'))
                e[st] = {'fw': meta['frameWidth'], 'fh': meta['frameHeight'],
                         'rows': {k: [a['row'], a['frames']] for k, a in meta['animations'].items()}}
            chars.append(e)
        groups.append({'id': gid, 'zh': zh, 'en': en, 'chars': chars})
        group_png(ids, os.path.join(ROOT, 'chars', 'longmen', 'compare-nes2-%s.png' % gid))
    group_png(HEROES, os.path.join(ROOT, 'chars', 'longmen', 'compare-nes2.png'), K=4, cols=2)
    town_png(HEROES + ['heixiong', 'tuqianqiu', 'qianwanli', 'xiaolian', 'chutiankuo', 'jingci'])
    html = HTML.replace('__GROUPS__', json.dumps(groups, ensure_ascii=False))
    open(os.path.join(ROOT, 'compare-longmen.html'), 'w', encoding='utf-8').write(html)
    print('compare-longmen.html', len(html) // 1024, 'KB;', sum(len(g[3]) for g in GROUPS), 'characters')


if __name__ == '__main__':
    main()
