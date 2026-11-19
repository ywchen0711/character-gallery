// Character gallery: loads chars/index.json, draws pixel art on canvases at integer scales.
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const ANIM_NAMES = {
    idle: { zh: '待機', en: 'Idle' }, walk: { zh: '行走（正面）', en: 'Walk (front)' },
    walk_side: { zh: '行走（側面）', en: 'Walk (side)' }, action: { zh: '招式', en: 'Signature move' },
  };
  const DL = [
    ['portrait', { zh: '頭像', en: 'Portrait' }, '56×64'], ['portrait4x', { zh: '頭像 4x', en: 'Portrait 4x' }, '224×256'],
    ['body', { zh: '全身', en: 'Body' }, '56×64'], ['body4x', { zh: '全身 4x', en: 'Body 4x' }, '224×256'],
    ['sheet', { zh: '動畫表', en: 'Sprite sheet' }, ''], ['sheet4x', { zh: '動畫表 4x', en: 'Sprite sheet 4x' }, ''],
    ['sheetJson', { zh: '動畫表 JSON', en: 'Sheet JSON' }, ''],
  ];
  let lang = 'zh';
  try { lang = localStorage.getItem('cg-lang') || 'zh'; } catch (e) { /* storage blocked */ }
  let chars = [];
  let filter = 'all';
  const players = new Set();     // running sprite animations
  let open = null;

  const img = (src) => new Promise((ok, bad) => { const i = new Image(); i.onload = () => ok(i); i.onerror = bad; i.src = src; });
  const t = (o) => (o && (o[lang] || o.zh)) || '';

  // draws one sheet animation into a canvas at integer scale, fixed-timestep
  function player(canvas, sheetImg, meta, anim, scale) {
    const fw = meta.frameWidth, fh = meta.frameHeight;
    const p = { canvas, anim, scale, frame: 0, acc: 0, mirror: false, sheetImg, meta };
    p.size = () => { canvas.width = fw * p.scale; canvas.height = fh * p.scale; };
    p.draw = () => {
      const a = meta.animations[p.anim]; const c = canvas.getContext('2d');
      c.imageSmoothingEnabled = false; c.clearRect(0, 0, canvas.width, canvas.height);
      c.drawImage(sheetImg, p.frame * fw, a.row * fh, fw, fh, 0, 0, fw * p.scale, fh * p.scale);
    };
    p.tick = (dt) => {
      const a = meta.animations[p.anim]; p.acc += dt;
      const step = 1 / a.fps; let changed = false;
      while (p.acc >= step) {
        p.acc -= step; p.frame = (p.frame + 1) % a.frames; changed = true;
        if (p.frame === 0 && !a.loop) p.acc -= 0.5;     // pause between plays of a one-shot move
      }
      if (changed) p.draw();
    };
    p.set = (name) => { p.anim = name; p.frame = 0; p.acc = 0; p.draw(); };
    p.size(); p.draw(); players.add(p);
    return p;
  }

  let last = performance.now();
  function loop(now) {
    const dt = Math.min(0.1, (now - last) / 1000); last = now;
    players.forEach((p) => { if (p.canvas.isConnected) p.tick(dt); else players.delete(p); });
    requestAnimationFrame(loop);
  }

  function drawStill(canvas, image, scale) {
    canvas.width = image.width * scale; canvas.height = image.height * scale;
    const c = canvas.getContext('2d'); c.imageSmoothingEnabled = false;
    c.drawImage(image, 0, 0, canvas.width, canvas.height);
  }

  function applyLang() {
    document.documentElement.lang = lang === 'zh' ? 'zh-Hant' : 'en';
    document.querySelectorAll('[data-zh]').forEach((el) => { el.textContent = el.dataset[lang]; });
    $('#lang').textContent = lang === 'zh' ? 'EN' : '中文';
    renderGrid();
    if (open) fillDetail(open);
  }

  function renderGrid() {
    const grid = $('#grid'); grid.textContent = '';
    const list = chars.filter((c) => filter === 'all' || c.faction === filter);
    $('#empty').hidden = list.length > 0;
    for (const c of list) {
      const b = document.createElement('button');
      b.className = 'card'; b.type = 'button'; b.style.setProperty('--fc', c.colour);
      b.setAttribute('aria-label', t(c.name));
      b.innerHTML = '<div class="art"><canvas class="p"></canvas><canvas class="b"></canvas></div>' +
        `<div class="nm"><b>${t(c.name)}</b><span>${lang === 'zh' ? c.name.en : c.name.zh}</span><em class="fac">${t(c.factionName)}</em></div>`;
      b.addEventListener('click', () => showDetail(c));
      grid.appendChild(b);
      drawStill($('canvas.p', b), c._por, 2);
      player($('canvas.b', b), c._sheet, c._meta, 'idle', 2);
    }
  }

  function fitScale(maxW) { return Math.max(2, Math.min(6, Math.floor(maxW / 56))); }

  function fillDetail(c) {
    const d = $('#detail'); d.querySelector('.sheet').style.setProperty('--fc', c.colour);
    $('#d-faction').textContent = t(c.factionName);
    $('#d-name').textContent = lang === 'zh' ? `${c.name.zh}　${c.name.en}` : `${c.name.en}  ${c.name.zh}`;
    $('#d-title').textContent = `${t(c.title)} · ${lang === 'zh' ? '字' : 'courtesy name '}${t(c.style_name)}`;
    $('#d-bio').textContent = t(c.bio);
    $('#d-meta').textContent = (lang === 'zh' ? '兵器：' : 'Weapon: ') + t(c.weapon) +
      (lang === 'zh' ? `　頭像 ${c.sizes.portrait.join('×')}，${c.colours.portrait} 色` : ` · portrait ${c.sizes.portrait.join('×')}, ${c.colours.portrait} colours`);
    const box = $('#d-anims'); box.textContent = '';
    Object.keys(c._meta.animations).forEach((n) => {
      const b = document.createElement('button'); b.type = 'button'; b.className = 'chip' + (n === open._anim ? ' on' : '');
      b.textContent = t(ANIM_NAMES[n]) || n;
      b.addEventListener('click', () => { open._anim = n; open._player.set(n); box.querySelectorAll('.chip').forEach((x) => x.classList.toggle('on', x === b)); });
      box.appendChild(b);
    });
    const dl = $('#d-dl'); dl.textContent = '';
    for (const [k, label, size] of DL) {
      const a = document.createElement('a'); a.href = c.files[k]; a.download = `${c.id}-${c.files[k].split('/').pop()}`;
      a.textContent = t(label) + (size ? ` (${size})` : ''); dl.appendChild(a);
    }
  }

  function showDetail(c) {
    open = c; c._anim = c._anim || 'idle';
    fillDetail(c);
    const d = $('#detail'); d.hidden = false; document.body.classList.add('locked');
    const w = Math.min(760, window.innerWidth) - 80;
    const s = fitScale(window.innerWidth < 600 ? Math.min(w, 300) : Math.min(w / 2, 400));
    drawStill($('#d-por'), c._por, s);
    players.forEach((p) => { if (p.canvas.id === 'd-chi') players.delete(p); });
    c._player = player($('#d-chi'), c._sheet, c._meta, c._anim, s);
    $('#close').focus();
  }

  function hideDetail() { $('#detail').hidden = true; document.body.classList.remove('locked'); open = null; }

  $('#close').addEventListener('click', hideDetail);
  $('#detail').addEventListener('click', (e) => { if (e.target.id === 'detail') hideDetail(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && open) hideDetail(); });
  $('#lang').addEventListener('click', () => {
    lang = lang === 'zh' ? 'en' : 'zh';
    try { localStorage.setItem('cg-lang', lang); } catch (e) { /* storage blocked */ }
    applyLang();
  });
  $('#filters').addEventListener('click', (e) => {
    const b = e.target.closest('[data-f]'); if (!b) return;
    filter = b.dataset.f;
    document.querySelectorAll('#filters .chip').forEach((x) => x.classList.toggle('on', x === b));
    renderGrid();
  });

  fetch('chars/index.json').then((r) => r.json()).then(async (data) => {
    chars = data.characters;
    await Promise.all(chars.map(async (c) => {
      const [por, sheet, meta] = await Promise.all([img(c.files.portrait), img(c.files.sheet), fetch(c.files.sheetJson).then((r) => r.json())]);
      c._por = por; c._sheet = sheet; c._meta = meta;
    }));
    applyLang();
    requestAnimationFrame(loop);
  }).catch((e) => { $('#empty').hidden = false; $('#empty').textContent = 'Failed to load characters: ' + e.message; });
})();
