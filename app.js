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
    guard: { zh: '舉盾挑釁', en: 'Shield taunt' },
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
    mk('all', lang === 'zh' ? '全部畫風（各自主畫風）' : 'All (main style each)');
    Object.keys(DATA.styles).forEach((k) => mk(k, styleName(k)));
  }

  function cards() {
    const grid = $('#grid'); grid.textContent = '';
    const items = [];
    for (const c of DATA.characters) {
      if (faction !== 'all' && c.faction !== faction) continue;
      if (styleF === 'all') items.push([c, c.variants.find((v) => v.primary) || c.variants[0]]);
      else c.variants.filter((v) => v.style === styleF).forEach((v) => items.push([c, v]));
    }
    $('#empty').hidden = items.length > 0;
    for (const [c, v] of items) {
      const b = el('button', 'card'); b.type = 'button'; b.style.setProperty('--fc', c.colour);
      b.setAttribute('aria-label', `${t(c.name)} · ${styleName(v.style)}`);
      const art = el('div', 'art');
      const pc = el('canvas'), bc = el('canvas');
      art.append(pc, bc); b.appendChild(art);
      const nm = el('div', 'nm');
      nm.append(el('b', null, t(c.name)), el('span', null, lang === 'zh' ? c.name.en : c.name.zh), el('em', 'fac', t(c.factionName)));
      b.append(nm, el('div', 'stylelab', styleName(v.style)));
      b.addEventListener('click', () => showDetail(c, v.style));
      grid.appendChild(b);
      still(pc, v._por, fit(v._por.height, 128));
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
    $('#d-meta').textContent = (lang === 'zh' ? '兵器：' : 'Weapon: ') + t(c.weapon) + ' · ' +
      (lang === 'zh' ? `頭像 ${v.sizes.portrait.join('×')}，${v.colours.portrait} 色；角色格 ${v.sizes.frame.join('×')}`
        : `portrait ${v.sizes.portrait.join('×')}, ${v.colours.portrait} colours; sprite cell ${v.sizes.frame.join('×')}`);
    const vs = $('#d-styles'); vs.textContent = '';
    c.variants.forEach((x) => {
      const b = el('button', 'chip' + (x.style === v.style ? ' on' : ''), styleName(x.style)); b.type = 'button';
      b.addEventListener('click', () => showDetail(c, x.style)); vs.appendChild(b);
    });
    $('#d-blurb').textContent = t(DATA.styles[v.style].blurb);
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
    still($('#d-por'), v._por, fitDown(v._por.height, room));
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
    for (const c of travellers) {
      const v = c.variants.find((x) => x.primary) || c.variants[0];
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

  function render() {
    if (!DATA) return;
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

  fetch('chars/index.json').then((r) => r.json()).then(async (data) => {
    DATA = data;
    const jobs = [];
    for (const c of data.characters) {
      for (const v of c.variants) {
        jobs.push(Promise.all([img(v.files.portrait), img(v.files.sheet), fetch(v.files.sheetJson).then((r) => r.json())])
          .then(([p, s, m]) => { v._por = p; v._sheet = s; v._meta = m; }));
      }
    }
    await Promise.all(jobs);
    applyLang();
    requestAnimationFrame(loop);
  }).catch((e) => { const m = $('#empty') || $('#pick-note') || document.body; m.hidden = false; m.textContent = 'Failed to load characters: ' + e.message; });
})();
