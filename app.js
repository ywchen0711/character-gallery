// Character gallery: loads chars/index.json; draws pixel art on canvases at whole-number scales.
// Runs both index.html (gallery) and compare.html (style comparison).
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };
  const ANIM_NAMES = {
    idle: { zh: '待機', en: 'Idle' }, walk: { zh: '行走（正面）', en: 'Walk (front)' },
    walk_side: { zh: '行走（側面）', en: 'Walk (side)' }, action: { zh: '招式', en: 'Signature move' },
    walk_down: { zh: '行走（下）', en: 'Walk (down)' }, walk_up: { zh: '行走（上）', en: 'Walk (up)' },
    walk_left: { zh: '行走（左）', en: 'Walk (left)' }, walk_right: { zh: '行走（右）', en: 'Walk (right)' },
    guard: { zh: '舉盾挑釁', en: 'Shield taunt' }, move: { zh: '待機／移動', en: 'Idle / move' },
  };
  const DL = [
    ['portrait', { zh: '頭像', en: 'Portrait' }], ['portrait4x', { zh: '頭像 4x', en: 'Portrait 4x' }],
    ['body', { zh: '全身', en: 'Body' }], ['body4x', { zh: '全身 4x', en: 'Body 4x' }],
    ['sheet', { zh: '動畫表', en: 'Sprite sheet' }], ['sheet4x', { zh: '動畫表 4x', en: 'Sprite sheet 4x' }],
    ['sheetJson', { zh: '動畫表 JSON', en: 'Sheet JSON' }],
  ];
  const store = {
    get(k, d) { try { return localStorage.getItem(k) || d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage blocked */ } },
  };
  let lang = store.get('cg-lang', 'zh');
  let DATA = null;
  let faction = 'all';
  let styleF = 'all';
  const players = new Set();
  let open = null;

  const t = (o) => (o && (o[lang] || o.zh)) || '';
  const img = (src) => new Promise((ok, bad) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => bad(new Error('image ' + src)); i.src = src; });
  const fit = (h, target) => Math.max(1, Math.round(target / h));
  const fitDown = (h, room) => Math.max(1, Math.floor(room / h));

  // one sheet animation in a canvas, fixed timestep
  function player(canvas, v, anim, scale) {
    const m = v._meta, fw = m.frameWidth, fh = m.frameHeight;
    const p = { canvas, anim, frame: 0, acc: 0 };
    canvas.width = fw * scale; canvas.height = fh * scale;
    p.draw = () => {
      const a = m.animations[p.anim]; const c = canvas.getContext('2d');
      c.imageSmoothingEnabled = false; c.clearRect(0, 0, canvas.width, canvas.height);
      c.drawImage(v._sheet, p.frame * fw, a.row * fh, fw, fh, 0, 0, fw * scale, fh * scale);
    };
    p.tick = (dt) => {
      const a = m.animations[p.anim]; p.acc += dt; const step = 1 / a.fps; let ch = false;
      while (p.acc >= step) {
        p.acc -= step; p.frame = (p.frame + 1) % a.frames; ch = true;
        if (p.frame === 0 && !a.loop) p.acc -= 0.6;
      }
      if (ch) p.draw();
    };
    p.set = (n) => { p.anim = n; p.frame = 0; p.acc = 0; p.draw(); };
    p.draw(); players.add(p);
    return p;
  }
  let last = performance.now();
  function loop(now) {
    const dt = Math.min(0.1, (now - last) / 1000); last = now;
    players.forEach((p) => { if (p.canvas.isConnected) p.tick(dt); else players.delete(p); });
    requestAnimationFrame(loop);
  }
  function still(canvas, image, scale) {
    canvas.width = image.width * scale; canvas.height = image.height * scale;
    const c = canvas.getContext('2d'); c.imageSmoothingEnabled = false;
    c.drawImage(image, 0, 0, canvas.width, canvas.height);
  }
  const styleName = (s) => t(DATA.styles[s].name);
  const firstAnim = (v) => (v.animations.includes('idle') ? 'idle' : v.animations[0]);
  const walkAnim = (v) => ['walk', 'walk_down', 'walk_side'].find((a) => v.animations.includes(a)) || firstAnim(v);
  const pickLabel = (on) => (on ? (lang === 'zh' ? '★ 我選這個畫風' : '★ My pick') : (lang === 'zh' ? '選這個畫風' : 'Pick this style'));

  function applyLang() {
    document.documentElement.lang = lang === 'zh' ? 'zh-Hant' : 'en';
    document.querySelectorAll('[data-zh]').forEach((e) => { e.textContent = e.dataset[lang]; });
    const b = $('#lang'); if (b) b.textContent = lang === 'zh' ? 'EN' : '中文';
    render();
  }

  // ------------------------------------------------------------- gallery page
  function styleChips() {
    const box = $('#stylef'); if (!box) return;
    box.textContent = '';
    const mk = (k, label) => {
      const b = el('button', 'chip' + (styleF === k ? ' on' : ''), label); b.type = 'button';
      b.addEventListener('click', () => { styleF = k; render(); }); box.appendChild(b);
    };
    mk('all', lang === 'zh' ? '主畫風' : 'Main style');
    Object.keys(DATA.styles).forEach((k) => mk(k, styleName(k) + (k === DATA.mainStyle ? (lang === 'zh' ? '（主）' : ' (main)') : '')));
  }

  function cards() {
    const grid = $('#grid'); grid.textContent = '';
    const items = [];
    for (const c of DATA.characters) {
      if (faction !== 'all' && c.faction !== faction && !(c.alsoIn || []).includes(faction)) continue;
      if (styleF === 'all') items.push([c, (faction !== 'all' && c.variants.find((v) => v.style === faction)) || c.variants.find((v) => v.primary) || c.variants[0]]);
      else c.variants.filter((v) => v.style === styleF).forEach((v) => items.push([c, v]));
    }
    $('#empty').hidden = items.length > 0;
    for (const [c, v] of items) {
      const b = el('button', 'card'); b.type = 'button'; b.style.setProperty('--fc', c.colour);
      b.setAttribute('aria-label', `${t(c.name)} · ${styleName(v.style)}`);
      const art = el('div', 'art');
      const pc = el('canvas'), bc = el('canvas');
      pc.classList.toggle('nesframe', v.style === 'nes' || v.style === 'sango' || v.style === 'nes_old');
      art.append(pc, bc); b.appendChild(art);
      const nm = el('div', 'nm');
      nm.append(el('b', null, t(c.name)), el('span', null, lang === 'zh' ? c.name.en : c.name.zh), el('em', 'fac', t(c.factionName)));
      b.append(nm, el('div', 'stylelab', styleName(v.style)));
      b.addEventListener('click', () => showDetail(c, v.style));
      grid.appendChild(b);
      still(pc, v._por, fit(Math.max(v._por.height, v._por.width * 0.875), 128));
      player(bc, v, firstAnim(v), fit(v._meta.frameHeight, 128));
    }
  }

  function fillDetail() {
    const { c, v } = open;
    $('#detail .sheet').style.setProperty('--fc', c.colour);
    $('#d-faction').textContent = t(c.factionName);
    $('#d-name').textContent = lang === 'zh' ? `${c.name.zh}　${c.name.en}` : `${c.name.en}  ${c.name.zh}`;
    $('#d-title').textContent = `${t(c.title)} · ${t(c.style_name)}`;
    $('#d-bio').textContent = t(c.bio);
    const monster = c.kind === 'monster';
    const tierTxt = c.tier ? (lang === 'zh' ? `第 ${c.tier} 階 · ` : `Tier ${c.tier} · `) : '';
    const what = monster ? tierTxt + (lang === 'zh' ? '棲地：' : 'Habitat: ') + t(c.habitat) : (lang === 'zh' ? '兵器：' : 'Weapon: ') + t(c.weapon);
    $('#d-meta').textContent = what + ' · ' +
      (lang === 'zh' ? `${monster ? '戰鬥圖' : '頭像'} ${v.sizes.portrait.join('×')}，${v.colours.portrait} 色；角色格 ${v.sizes.frame.join('×')}`
        : `${monster ? 'battle picture' : 'portrait'} ${v.sizes.portrait.join('×')}, ${v.colours.portrait} colours; sprite cell ${v.sizes.frame.join('×')}`);
    $('#d-por').closest('figure').querySelector('figcaption').textContent = monster ? (lang === 'zh' ? '戰鬥圖' : 'Battle picture') : (lang === 'zh' ? '頭像' : 'Portrait');
    $('#d-chi').closest('figure').querySelector('figcaption').textContent = monster ? (lang === 'zh' ? '地圖小圖' : 'Field sprite') : (lang === 'zh' ? '全身' : 'Full body');
    const vs = $('#d-styles'); vs.textContent = '';
    c.variants.forEach((x) => {
      const b = el('button', 'chip' + (x.style === v.style ? ' on' : ''), styleName(x.style)); b.type = 'button';
      b.addEventListener('click', () => showDetail(c, x.style)); vs.appendChild(b);
    });
    $('#d-blurb').textContent = monster ? t(c.faction === 'foe' ? FOE_BLURB : BEAST_BLURB) : t(DATA.styles[v.style].blurb);
    const box = $('#d-anims'); box.textContent = '';
    v.animations.forEach((n) => {
      const b = el('button', 'chip' + (n === open.anim ? ' on' : ''), t(ANIM_NAMES[n]) || n); b.type = 'button';
      b.addEventListener('click', () => { open.anim = n; open.player.set(n); box.querySelectorAll('.chip').forEach((x) => x.classList.toggle('on', x === b)); });
      box.appendChild(b);
    });
    const dl = $('#d-dl'); dl.textContent = '';
    for (const [k, label] of DL) {
      const a = el('a', null, t(label)); a.href = v.files[k]; a.download = `${c.id}-${v.style}-${v.files[k].split('/').pop()}`;
      dl.appendChild(a);
    }
  }

  function showDetail(c, style) {
    const v = c.variants.find((x) => x.style === style) || c.variants[0];
    open = { c, v, anim: firstAnim(v) };
    $('#detail').hidden = false; document.body.classList.add('locked');
    fillDetail();
    const room = window.innerWidth < 600 ? Math.min(300, window.innerWidth - 90) : 300;
    $('#d-por').classList.toggle('nesframe', v.style === 'nes' || v.style === 'sango' || v.style === 'nes_old');
    still($('#d-por'), v._por, fitDown(v._por.height + (v.style === 'nes' || v.style === 'sango' || v.style === 'nes_old' ? 8 : 0), room));
    players.forEach((p) => { if (p.canvas.id === 'd-chi') players.delete(p); });
    open.player = player($('#d-chi'), v, open.anim, fitDown(v._meta.frameHeight, room));
    $('#close').focus();
  }
  function hideDetail() { $('#detail').hidden = true; document.body.classList.remove('locked'); open = null; }

  // ------------------------------------------------------------- compare page
  function compare() {
    const own = $('#cmp-own'); const koei = $('#cmp-koei');
    own.textContent = ''; koei.textContent = '';
    const picked = store.get('cg-pick', '');
    const travellers = DATA.characters.filter((c) => c.faction === 'west');
    const nesBox = $('#cmp-nes');
    if (nesBox) {
      nesBox.textContent = '';
      for (const c of DATA.characters) {
        const v = c.variants.find((x) => x.style === 'nes'); if (!v || c.kind === 'monster') continue;
        const col = el('article', 'cmp'); col.style.setProperty('--fc', c.colour);
        const art = el('div', 'cmp-art');
        const pc = el('canvas', 'nesframe'), a1 = el('canvas'), a2 = el('canvas');
        const spr = el('div', 'cmp-spr'); spr.append(a1, a2);
        art.append(pc, spr); col.append(art, el('div', 'cmp-name', `${t(c.name)} · ${t(c.style_name)}`));
        nesBox.appendChild(col);
        still(pc, v._por, fitDown(v._por.height + 8, 200));
        const k = fitDown(v._meta.frameHeight, 96);
        player(a1, v, 'walk', k); player(a2, v, 'walk_side', k);
      }
      const np = $('#nes-pick');
      if (np) { np.className = 'chip pick' + (picked === 'nes' ? ' on' : ''); np.textContent = pickLabel(picked === 'nes'); }
    }
    const fam = $('#cmp-family');
    if (fam) {
      fam.textContent = '';
      for (const c of travellers) {
        const v = c.variants.find((x) => x.style === 'family'); if (!v) continue;
        const col = el('article', 'cmp'); col.style.setProperty('--fc', c.colour);
        const art = el('div', 'cmp-art');
        const pc = el('canvas'), a1 = el('canvas'), a2 = el('canvas'), a3 = el('canvas');
        const spr = el('div', 'cmp-spr'); spr.append(a1, a2, a3);
        art.append(pc, spr); col.append(art, el('div', 'cmp-name', `${t(c.name)} · ${t(c.style_name)}`));
        fam.appendChild(col);
        still(pc, v._por, fitDown(v._por.height, 208));
        const k = fitDown(v._meta.frameHeight, 120);
        player(a1, v, 'idle', k); player(a2, v, 'walk_down', k); player(a3, v, 'action', k);
      }
      const fp = $('#family-pick');
      fp.className = 'chip pick' + (picked === 'family' ? ' on' : '');
      fp.textContent = pickLabel(picked === 'family');
    }
    for (const c of travellers) {
      const v = c.variants.find((x) => !['nes', 'family', 'koei'].includes(x.style)) || c.variants[0];
      const col = el('article', 'cmp'); col.style.setProperty('--fc', c.colour);
      col.append(el('div', 'cmp-style', styleName(v.style)), el('p', 'cmp-blurb', t(DATA.styles[v.style].blurb)));
      const art = el('div', 'cmp-art');
      const pc = el('canvas'), a1 = el('canvas'), a2 = el('canvas');
      const spr = el('div', 'cmp-spr'); spr.append(a1, a2);
      art.append(pc, spr); col.append(art);
      col.append(el('div', 'cmp-name', `${t(c.name)} · ${t(c.style_name)}`));
      const pick = el('button', 'chip pick' + (picked === v.style ? ' on' : ''), pickLabel(picked === v.style));
      pick.type = 'button';
      pick.addEventListener('click', () => { store.set('cg-pick', v.style); render(); });
      col.append(pick);
      own.appendChild(col);
      still(pc, v._por, fitDown(v._por.height, 208));
      player(a1, v, firstAnim(v), fitDown(v._meta.frameHeight, 112));
      player(a2, v, walkAnim(v), fitDown(v._meta.frameHeight, 112));
    }
    const ref = DATA.characters.filter((c) => c.faction !== 'west').concat(travellers);
    for (const c of ref) {
      const v = c.variants.find((x) => x.style === 'koei'); if (!v) continue;
      const col = el('article', 'cmp small'); col.style.setProperty('--fc', c.colour);
      const art = el('div', 'cmp-art');
      const pc = el('canvas'), a1 = el('canvas');
      art.append(pc, a1); col.append(art, el('div', 'cmp-name', t(c.name)));
      koei.appendChild(col);
      still(pc, v._por, 2);
      player(a1, v, 'idle', 2);
    }
    const kp = $('#koei-pick');
    kp.className = 'chip pick' + (picked === 'koei' ? ' on' : '');
    kp.textContent = pickLabel(picked === 'koei');
    $('#pick-note').textContent = picked ? (lang === 'zh' ? `你目前選的是：${styleName(picked)}。把選擇告訴 Claude，就能用這個畫風畫更多人物。`
      : `Your pick: ${styleName(picked)}. Tell Claude, and more characters can be drawn in this style.`) : '';
  }

  const BEAST_BLURB = {
    zh: '原創怪物，紅白機前視角戰鬥圖：最大 64×64，粗黑線、只用紅白機標準色盤，每 16×16 格一組三色（全圖最多四組），眼光、火焰等小亮點用精靈疊上；配 16×16 或 16×24 的地圖小圖，兩格動畫兼作待機與移動。',
    en: 'Original monsters as NES front-view battle pictures: at most 64×64, bold black lines, only NES palette colours with one 3-colour set per 16×16 area (at most four sets), and sprite overlays for glowing eyes and sparks; plus a 16×16 or 16×24 field sprite whose two frames serve to idle and to move.',
  };
  const FOE_BLURB = {
    zh: '小怪，霸王之路畫風的半身戰鬥圖：48×56 的紅白機黑底窗框，和武將頭像一樣；人形敵人畫頭與肩，鳥獸蟲妖畫頭部特寫。只用紅白機標準色盤，每 16×16 格一組三色（最多四組），兵器、眼光用精靈疊上；配 16×16 地圖小圖（兩層精靈），兩格動畫兼作待機與移動。',
    en: 'Common foes as 霸王之路-style busts: 48×56 pictures in the black NES window, like the generals’ portraits - people as head-and-shoulders busts, beasts, bugs and spirits as head close-ups. Only NES palette colours, one 3-colour set per 16×16 area (at most four), weapons and glints as sprite overlays; plus a 16×16 field sprite (two sprite layers) whose two frames serve to idle and to move.',
  };
  // group roster pictures above the grid: the one that matches the faction filter (both for 'all')
  const CAPS = {
    sango: { zh: '三國志 霸王之路：主將傑夫，與每一關的敵將（程遠志、張寶、華雄、紀靈、顏良、文醜、張遼、夏侯惇、呂布）· 8-bit 紅白機畫風',
      en: 'Three Kingdoms: Path of the Hegemon: Jeff as the main general and every stage\'s enemy general (Cheng Yuanzhi, Zhang Bao, Hua Xiong, Ji Ling, Yan Liang, Wen Chou, Zhang Liao, Xiahou Dun, Lü Bu) · 8-bit Famicom style' },
    family: { zh: '一家四口：傑夫（父）、艾琳（母）、喬許（10 歲）、賈斯珀（8 歲）· 主畫風 8-bit 紅白機（霸王の大陸風）',
      en: 'The family: Jeff (father), Erin (mother), Josh (10), Jasper (8) · main style: 8-bit Famicom (霸王の大陸-like)' },
    longmen: { zh: '龍門武林：奕叡、奕碩、冷笑天、白先生、柳寒煙、苦禪 · 8-bit 紅白機畫風',
      en: 'Longmen Wulin: Yi Rui, Yi Shuo, Leng Xiaotian, Mr Bai, Liu Hanyan, Kuchan · 8-bit Famicom style' },
    longmenFoes: { zh: '黑風寨與幽冥教：黑熊、刀疤、瘦猴、屠千秋 · 8-bit 紅白機畫風',
      en: 'Black Wind Fort and the Netherworld Sect: Black Bear, Scar, Skinny Monkey, Tu Qianqiu · 8-bit Famicom style' },
    longmenMore: { zh: '龍門江湖眾生：鐵無私、錢萬里、溫如玉、小蓮、厲寒山、獨臂漁翁、鬼面護法、蒙面人 · 8-bit 紅白機畫風',
      en: 'More of the Longmen jianghu: Tie Wusi, Qian Wanli, Wen Ruyu, Xiaolian, Li Hanshan, the One-Armed Fisherman, the Ghost-mask Warden, the Masked Man · 8-bit Famicom style' },
    yiruiDoll: { zh: '奕叡的紙娃娃（龍門刀客傳）：同一個 8-bit 奕叡換上不同的斗笠、頭盔、冠、衣甲、披風、佩飾、靴與兵器 · 頭像與正面、側面、背面小人',
      en: 'Yi Rui\'s paper doll (Longmen Quest): the same 8-bit Yi Rui in different hats, helmets, crowns, armour, cloaks, pendants, boots and weapons · portraits and front, side and back sprites' },
    foes: { zh: '小怪：50 種一般敵人，依第 1～5 階排列（早期→後期區域），同一造型的換色版本越後面越強 · 紅白機戰鬥圖與地圖小圖',
      en: 'Common Foes: 50 regular enemies ordered by tier 1-5 (early to late areas); palette-swapped kin get stronger further on · NES battle pictures and field sprites' },
    beasts: { zh: '怪物與野獸：白猿、吊睛白額虎、鎮宅石獅、符咒殭屍、山魈、九尾狐、江蛟、三足火鴉、毒蟾 · 紅白機戰鬥圖與地圖小圖',
      en: 'Monsters & Beasts: White Ape, White-Browed Tiger, Stone Guardian Lion, Talisman Jiangshi, Shanxiao, Nine-Tailed Fox, River Jiao, Fire Crow, Venom Toad · NES battle pictures and field sprites' },
  };
  function hero() {
    const box = $('#heroes'); if (!box || !DATA || !DATA.groups) return;
    const ids = faction === 'all' ? ['family', 'sango', 'longmen', 'longmenFoes', 'longmenMore', 'longmen2', 'yiruiDoll', 'sectsPeople', 'sects', 'sectsUnique', 'beasts', 'foes', 'longmen2Foes']
      : faction === 'sango' ? ['sango'] : faction === 'longmen' ? ['longmen', 'longmenFoes', 'longmenMore', 'longmen2', 'yiruiDoll', 'sectsPeople'] : faction === 'beast' ? ['beasts'] : faction === 'foe' ? ['foes', 'longmen2Foes']
        : faction === 'west' ? ['family'] : faction === 'sects' ? ['sectsPeople', 'sects', 'sectsUnique'] : [];
    box.textContent = '';
    const room = Math.max(120, (box.clientWidth || 600) - 32);
    for (const id of ids) {
      const g = DATA.groups[id]; if (!g || !g._img) continue;
      const fig = el('figure', 'hero-fig'); const cv = el('canvas');
      cv.setAttribute('role', 'img'); cv.setAttribute('aria-label', t(g.name));
      fig.append(cv, el('figcaption', 'hero-cap', t(CAPS[id]) || t(g.name)));
      box.appendChild(fig);
      const wide = g._img, tall = g._tall || wide;
      const kw = Math.floor(room / wide.width), kt = Math.floor(room / tall.width);
      if (kw >= 2 || kt < 2) still(cv, wide, Math.max(1, Math.min(5, kw)));
      else still(cv, tall, Math.min(3, kt));
    }
  }

  function render() {
    if (!DATA) return;
    hero();
    if ($('#grid')) { styleChips(); cards(); if (open) fillDetail(); }
    if ($('#cmp-own')) compare();
  }

  // ------------------------------------------------------------- wiring
  const on = (sel, ev, fn) => { const e = $(sel); if (e) e.addEventListener(ev, fn); };
  on('#close', 'click', hideDetail);
  on('#detail', 'click', (e) => { if (e.target.id === 'detail') hideDetail(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && open) hideDetail(); });
  on('#lang', 'click', () => { lang = lang === 'zh' ? 'en' : 'zh'; store.set('cg-lang', lang); applyLang(); });
  on('#filters', 'click', (e) => {
    const b = e.target.closest('[data-f]'); if (!b) return;
    faction = b.dataset.f;
    document.querySelectorAll('#filters .chip').forEach((x) => x.classList.toggle('on', x === b));
    render();
  });
  on('#koei-pick', 'click', () => { store.set('cg-pick', 'koei'); render(); });
  on('#family-pick', 'click', () => { store.set('cg-pick', 'family'); render(); });
  on('#nes-pick', 'click', () => { store.set('cg-pick', 'nes'); render(); });

  fetch('chars/index.json', { cache: 'no-cache' }).then((r) => r.json()).then(async (data) => {
    DATA = data;
    const jobs = [];
    for (const c of data.characters) {
      for (const v of c.variants) {
        jobs.push(Promise.all([img(v.files.portrait), img(v.files.sheet), fetch(v.files.sheetJson).then((r) => r.json())])
          .then(([p, s, m]) => { v._por = p; v._sheet = s; v._meta = m; }));
      }
    }
    for (const g of Object.values(data.groups || {})) {
      const gf = g.files; if (!gf.nes) continue;
      jobs.push(img(gf.nes).then((i) => { g._img = i; }));
      if (gf.nesTall) jobs.push(img(gf.nesTall).then((i) => { g._tall = i; }));
    }
    await Promise.all(jobs);
    applyLang();
    window.addEventListener('resize', hero);
    requestAnimationFrame(loop);
  }).catch((e) => { const m = $('#empty') || $('#pick-note') || document.body; m.hidden = false; m.textContent = 'Failed to load characters: ' + e.message; });
})();
