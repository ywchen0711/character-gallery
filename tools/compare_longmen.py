"""Build compare-longmen.html (old `nes` vs new `nes2` Longmen heroes; self-contained: every picture is inlined as a
data URI) and two review pictures in chars/longmen/:
  compare-nes2.png   old and new portraits and sprite frames side by side at 4x
  town-nes2.png      old and new sprites walking on an LQ-like town tile floor at the in-game 3x scale

    python -P tools/compare_longmen.py        (after tools/export_nes2.py)
"""
import base64
import io
import json
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = ['yirui', 'yishuo', 'liuhanyan', 'baixian', 'kuchan', 'xiaotian']
NAMES = {'yirui': ('奕叡', 'Yi Rui'), 'yishuo': ('奕碩', 'Yi Shuo'), 'liuhanyan': ('柳寒煙', 'Liu Hanyan'),
         'baixian': ('白先生', 'Mr Bai'), 'kuchan': ('苦禪', 'Kuchan'), 'xiaotian': ('冷笑天', 'Leng Xiaotian')}


def load(cid, style):
    d = os.path.join(ROOT, 'chars', cid, style)
    por = Image.open(os.path.join(d, 'portrait.png')).convert('RGBA')
    sheet = Image.open(os.path.join(d, 'sheet.png')).convert('RGBA')
    meta = json.load(open(os.path.join(d, 'sheet.json'), encoding='utf-8'))
    fr = {}
    for n, a in meta['animations'].items():
        fr[n] = [sheet.crop((i * 16, a['row'] * 24, i * 16 + 16, a['row'] * 24 + 24)) for i in range(a['frames'])]
    return por, sheet, fr


def uri(im):
    b = io.BytesIO()
    im.save(b, 'PNG')
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()


def window(img):
    w, h = img.width + 4, img.height + 4
    out = Image.new('RGBA', (w, h), (0, 0, 0, 255))
    d = ImageDraw.Draw(out)
    d.rectangle((0, 0, w - 1, h - 1), outline=(252, 252, 252, 255))
    out.alpha_composite(img, (2, 2))
    return out


def compare_png():
    K, G = 4, 6
    cellw = 52 + 4 * 18
    rows = []
    for cid in IDS:
        r = []
        for st in ('nes', 'nes2'):
            por, _, fr = load(cid, st)
            seq = fr['walk'] + fr['walk_side'] + fr.get('walk_up', [])
            r.append((window(por), seq))
        rows.append(r)
    SW = 56 + 3 * 17 + 8
    W = (2 * SW + 2 * G) * K
    H = len(rows) * (64 * K + G * K) + G * K
    out = Image.new('RGBA', (W, H), (52, 60, 56, 255))
    for j, r in enumerate(rows):
        y = G * K + j * (64 * K + G * K)
        x = G * K
        for por, seq in r:
            out.alpha_composite(por.resize((por.width * K, por.height * K), 0), (x, y))
            sx = x + 56 * K
            for i, f in enumerate(seq):
                fx = sx + (i % 3) * 17 * K
                fy = y + (i // 3) * 26 * K + 4
                out.alpha_composite(f.resize((16 * K, 24 * K), 0), (fx, fy))
            x += SW * K
    out.save(os.path.join(ROOT, 'chars', 'longmen', 'compare-nes2.png'))
    return out


def town_floor(w, h):
    """An LQ-like town floor: a stone road across grass, a wooden house wall at the top (NES colours)."""
    im = Image.new('RGBA', (w, h), (0, 168, 0, 255))
    P = im.load()
    for y in range(h):
        for x in range(w):
            if 14 <= y < 30:                 # wall
                P[x, y] = (172, 124, 0, 255) if (x // 8 + (y // 4) % 2) % 2 else (136, 20, 0, 255)
                if y % 4 == 0:
                    P[x, y] = (80, 48, 0, 255)
            elif y < 14:                     # roof
                P[x, y] = (0, 64, 88, 255) if (x + y // 3) % 6 else (0, 0, 0, 255)
            elif 40 <= y < 72:               # road
                t = ((x // 8) + (y // 8)) % 2
                P[x, y] = (188, 188, 188, 255) if t else (124, 124, 124, 255)
                if x % 8 == 0 or y % 8 == 0:
                    P[x, y] = (120, 120, 120, 255)
            else:                            # grass tufts
                if (x * 7 + y * 13) % 23 == 0:
                    P[x, y] = (88, 216, 84, 255)
    return im


def town_png():
    S = 3
    w, h = 6 * 28 + 8, 96
    out = Image.new('RGBA', (w * S, h * 2 * S + 8), (0, 0, 0, 255))
    for k, st in enumerate(('nes', 'nes2')):
        im = town_floor(w, h)
        for i, cid in enumerate(IDS):
            _, _, fr = load(cid, st)
            f = fr['walk'][0]
            im.alpha_composite(f, (8 + i * 28, 38 if i % 2 else 50))
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
header { max-width: 1100px; margin: 0 auto 16px; display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: baseline; justify-content: space-between; }
h1 { margin: 0; font-size: 22px; overflow-wrap: anywhere; }
header > div { min-width: 0; }
.sub { color: var(--dim); margin: 4px 0 0; max-width: 60ch; }
a { color: var(--accent); }
.bar { display: flex; gap: 8px; flex-wrap: wrap; }
button { font: inherit; color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 999px; padding: 6px 14px; cursor: pointer; }
button.on { background: var(--accent); color: #1a1a1a; border-color: var(--accent); }
main { max-width: 1100px; margin: 0 auto; display: grid; gap: 16px; }
.row { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 12px; }
.row h2 { margin: 0 0 8px; font-size: 17px; }
.row h2 span { color: var(--dim); font-weight: 400; font-size: 14px; margin-left: 6px; }
.pair { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 12px; }
.side { display: flex; flex-direction: column; align-items: center; gap: 8px; min-width: 0; }
.tag { font-size: 13px; color: var(--dim); }
.tag.new { color: var(--accent); }
img, canvas { image-rendering: pixelated; image-rendering: crisp-edges; }
.por { width: 100%; max-width: 208px; height: auto; border: 2px solid #fcfcfc; background: #000; }
.walk { width: 128px; height: 192px; background: #00a800; border-radius: 6px; }
.frames { display: flex; flex-wrap: wrap; gap: 4px; justify-content: center; }
.frames img { width: 32px; height: 48px; background: #5a6e58; }
.town { width: 100%; height: auto; border-radius: 8px; display: block; }
.note { color: var(--dim); font-size: 14px; max-width: 70ch; }
@media (max-width: 560px) { .walk { width: 96px; height: 144px; } .frames img { width: 24px; height: 36px; } }
</style>
</head>
<body>
<header>
  <div>
    <h1>龍門人物 新舊對照 <span style="font-size:15px;color:var(--dim)">Longmen heroes, old vs new</span></h1>
    <p class="sub">左：目前的 <b>nes</b> 版；右：照《霸王之路》水準重畫的 <b>nes2</b> 試作（頭像有明暗與背景、小黑眼；小人兩層精靈、加背面）。頭像與小人都放大 4 倍。</p>
  </div>
  <div class="bar" role="group" aria-label="walk direction">
    <button data-d="walk" class="on">正面</button><button data-d="walk_side">側面</button><button data-d="walk_left">左</button><button data-d="walk_up">背面</button>
  </div>
</header>
<main id="rows"></main>
<main style="margin-top:16px">
  <section class="row"><h2>小鎮上的實際大小 <span>in-game scale (3x) on a town floor: top old, bottom new</span></h2>
  <img class="town" alt="old and new sprites on a town floor" src="__TOWN__"></section>
  <section class="row"><h2>尺寸說明 <span>sprite size</span></h2>
  <p class="note">新版仍是 16×24 格、同樣的列（idle、walk、walk_side）並加一列 walk_up（背面），遊戲可直接換檔。16×24 已足夠做出臉、髮型、頭飾與兵器；若想要更細的臉，可考慮 16×32（頭不變、身體加高）作為下一步選項，但這一輪先不改格子大小。</p>
  <p><a href="index.html">← 回人物圖庫 Back to the gallery</a></p></section>
</main>
<script>
const DATA = __DATA__;
const rows = document.getElementById('rows');
const anims = [];
function img(src, cls, alt) { const i = new Image(); i.src = src; if (cls) i.className = cls; i.alt = alt || ''; return i; }
for (const c of DATA) {
  const sec = document.createElement('section'); sec.className = 'row';
  sec.innerHTML = `<h2>${c.zh}<span>${c.en}</span></h2>`;
  const pair = document.createElement('div'); pair.className = 'pair';
  for (const st of ['nes', 'nes2']) {
    const v = c[st]; const side = document.createElement('div'); side.className = 'side';
    const tag = document.createElement('div'); tag.className = 'tag' + (st === 'nes2' ? ' new' : ''); tag.textContent = st === 'nes' ? '舊 old (nes)' : '新 new (nes2)';
    side.append(tag, img(v.portrait, 'por', c.en + ' portrait ' + st));
    const cv = document.createElement('canvas'); cv.width = 16; cv.height = 24; cv.className = 'walk'; side.appendChild(cv);
    const fr = document.createElement('div'); fr.className = 'frames';
    for (const k of Object.keys(v.frames)) for (const s of v.frames[k]) fr.appendChild(img(s, '', k));
    side.appendChild(fr);
    pair.appendChild(side);
    const frames = {}; for (const k of Object.keys(v.frames)) frames[k] = v.frames[k].map((s) => img(s));
    anims.push({ cv, frames });
  }
  sec.appendChild(pair); rows.appendChild(sec);
}
let dir = 'walk', tick = 0;
document.querySelectorAll('[data-d]').forEach((b) => b.addEventListener('click', () => {
  dir = b.dataset.d; document.querySelectorAll('[data-d]').forEach((x) => x.classList.toggle('on', x === b)); draw();
}));
function draw() {
  for (const a of anims) {
    const g = a.cv.getContext('2d'); g.imageSmoothingEnabled = false; g.clearRect(0, 0, 16, 24);
    const key = dir === 'walk_left' ? 'walk_side' : dir;
    const list = a.frames[key] || a.frames.walk;
    const f = list[tick % list.length];
    if (!f.complete) continue;
    if (dir === 'walk_left') { g.save(); g.translate(16, 0); g.scale(-1, 1); g.drawImage(f, 0, 0); g.restore(); }
    else g.drawImage(f, 0, 0);
  }
}
setInterval(() => { tick++; draw(); }, 260);
window.addEventListener('load', draw);
</script>
</body>
</html>
'''


def main():
    compare_png()
    town_png()
    data = []
    for cid in IDS:
        e = {'id': cid, 'zh': NAMES[cid][0], 'en': NAMES[cid][1]}
        for st in ('nes', 'nes2'):
            por, _, fr = load(cid, st)
            e[st] = {'portrait': uri(por), 'frames': {k: [uri(f) for f in v] for k, v in fr.items() if k != 'idle'}}
        data.append(e)
    town = uri(Image.open(os.path.join(ROOT, 'chars', 'longmen', 'town-nes2.png')))
    html = HTML.replace('__DATA__', json.dumps(data)).replace('__TOWN__', town)
    open(os.path.join(ROOT, 'compare-longmen.html'), 'w', encoding='utf-8').write(html)
    print('compare-longmen.html', len(html) // 1024, 'KB')


if __name__ == '__main__':
    main()
