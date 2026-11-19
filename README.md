# 人物圖庫 Character Gallery

A pixel-art character library for the games in this collection. Each character can come in several art styles ("variants"). Every variant has a portrait and an animated full body.

| Style id | Look (imitated, original art) | Portrait | Sprite |
|---|---|---|---|
| `nes` (**main**) | 8-bit Famicom, in the manner of 三國志 霸王の大陸 (Namco, 1992): bold black lines, flat 2-3 tone shading | 48×56 on black; only NES (2C02) palette colours, one 3-colour sub-palette per 16×16 area (max 4), sprite overlays for eye whites and lips | 16×24 NES field sprite, 3 colours + transparent, 2-frame front and side walk; Josh 20 and Jasper 16 rows tall |
| `family` | HD-2D (Octopath-like), cuter: round faces, small dark eyes, warm soft light | 72×80 painterly, bokeh background | 40×60 cell, one baseline for everyone; idle, walk in 4 directions, signature action |
| `koei` | 16-bit Three Kingdoms strategy portraits (霸王の大陸-like) × pixel-baseball chibis | 56×64, 3/4 view, side-lit | 56×64 cell, about 2.3 heads |
| `hd2d` | HD-2D (Octopath-like) | 80×104 painterly, bokeh background | 40×56 cell, about 3 heads, soft ramps, tiny dark eyes |
| `snes` | SNES JRPG (FF6-like) | 48×48 in a blue menu window | 16×24 field sprite, 4-direction walk |
| `gba` | GBA tactics (Fire Emblem-like) | 64×64, strict 16 colours, cel-shaded | 48×48 chunky battle sprite |
| `dq` | 8-bit NES (Dragon Quest-like) | 48×48 window, 4 colours per 16×16 block | 16×16, 3 colours per 8×8 sprite, 2-frame walk |

Characters so far:
- The family from *Saga of Jiangdong*, drawn in the main 8-bit `nes` style, with their earlier styles kept as alternates:
  - Jeff, the father (also `family`, `hd2d` and `koei`)
  - Erin, the mother (also `family`, `snes` and `koei`)
  - Josh, 10 (also `family`, `gba` and `koei`)
  - Jasper, 8 (also `family`, `dq` and `koei`)
- 關羽 Guan Yu (`nes`, also `koei`).
- 三國志 霸王之路 (Path of the Hegemon), faction `sango`: Jeff as the main general (his `sango` style), and each stage's
  enemy general in `nes`: 程遠志, 張寶, 華雄, 紀靈, 顏良, 文醜, 張遼, 夏侯惇, 呂布 (關羽 also shows under this filter).
  Drawn in `src/nes_sango.py`. Each general's 16x24 field sprite matches his portrait: the same helmet, crown or
  head cloth, plume or pheasant feathers, beard, eye patch or glasses, armour colours and his weapon in hand (dao,
  spear, 三尖刀, 方天畫戟, talisman, jian). The sprites use two stacked NES sprite layers, the way Famicom games
  layered a second sprite over a figure: `pal` (black, skin, main colour) and `pal2` (three more colours), each
  layer at most 3 colours + transparent (checked by `nes.sprite_image`).
- 龍門武林 (Longmen Wulin), the cast of 龍門雙奕, in `nes` only (faction `longmen`):
  - 奕叡 Yi Rui, the elder brother: indigo robe, blue headband, ring-pommel saber on his back
  - 奕碩 Yi Shuo, his little brother: red headband, vermilion jacket, a mole, his football (shorter sprite)
  - 冷笑天 Leng Xiaotian, the Tyrant Dragon: silver hair, gold dragon horns, black-and-gold robe, crimson cape
  - 白先生 Mr Bai, the storyteller: square scholar's cap, goatee, grey robe, clapper block
  - 柳寒煙 Liu Hanyan, Mistress of the Cold River Pavilion: high bun with a pin, white over pale blue, a slim sword
  - 苦禪 Kuchan, abbot of the Thousand Buddhas: white brows and beard, saffron robe, red kasaya, beads, staff
  - 黑熊 Black Bear, chief of the Black Wind Fort bandits: wild hair, full black beard, bear-fur mantle, spiked club
  - 刀疤 Scar, the fort's second: shaved sides and a topknot, a long scar across his face, a broad dao
  - 瘦猴 Skinny Monkey, the fort's lackey: thin, buck-toothed grin, patched clothes, a short knife
  - 屠千秋 Tu Qianqiu, master of the Netherworld Sect: pale, long black hair with a white streak, silver ghost half-mask, violet robe, bone beads, bone fan
  - 鐵無私 Tie Wusi, Master of the Law Hall: official cap with side wings, black moustache, charcoal robe, iron chain
  - 錢萬里 Qian Wanli, the treasurer: melon-skin cap with a red knob, maroon robe, gold-beaded abacus
  - 溫如玉 Wen Ruyu, the clerk: green-wrapped bun, pale green gown, ink on the collar, the ledger
  - 小蓮 Xiaolian, Liu Hanyan's little apprentice: two buns with red ribbons, pink robe (shorter sprite)
  - 厲寒山 Li Hanshan of the Blood Saber Sect: long white hair, dark red robe, blood-red curved blade
  - 獨臂漁翁 the One-Armed Fisherman: straw hat, long white beard, knotted empty sleeve, fishing rod
  - 鬼面護法 the Ghost-mask Warden: blood-red hood, white fanged ghost mask with red eye-light
  - 蒙面人 the Masked Man: purple hood, black face cloth, purple robe edged in gold
- 怪物與野獸 (Monsters & Beasts), original creatures in `nes` only (faction `beast`, `kind: "monster"` in index.json):
  a front-view NES battle picture (64x64 or 64x56, transparent backdrop) and a 16x16 / 16x24 field sprite
  with one two-frame animation `move` (idle and move): 白猿 White Ape, 吊睛白額虎 White-Browed Tiger, 鎮宅石獅
  Stone Guardian Lion, 符咒殭屍 Talisman Jiangshi, 山魈 Shanxiao, 九尾狐 Nine-Tailed Fox, 江蛟 River Jiao,
  三足火鴉 Fire Crow, 毒蟾 Venom Toad. Monsters have `habitat` instead of `weapon`; people have `kind: "person"`.
- 小怪 (Common Foes), 50 small regular monsters (faction `foe`, `kind: "monster"`, `tier` 1-5 from early to late areas,
  `habitat`, `base`): 26 base designs with NES-style palette swaps (灰狼 -> 血狼 -> 霜狼 ...), colours in
  `src/nes_foes_art.py`. Since 2026-11-19 they are drawn in the 霸王之路 style (`src/foe_busts.py`,
  `foe_busts_people.py`, `foe_busts_animals.py`): 48x56 busts on the black NES panel like the generals - people
  and the undead as head-and-shoulders busts with the generals' robe and armour shapes, hand-typed faces and
  iconic gear; animals, bugs and spirits as head-and-forequarters close-ups. The bust is also the battle picture
  in Longmen Quest. Higher-tier swaps change a detail or two (a scar, nails in the club and an eye patch, frost,
  a brow jewel, riveted plates, glowing eyes, a skull rosary ...). The 16x16 field sprite (`src/nes_foes_fields.py`)
  uses the bust's slot letters, so it has the same colours, spread over two stacked sprite layers
  (`field_pals()`), with a two-frame `move`. Group picture `chars/foes/group-nes.png` (10 per row, by tier, in NES
  window frames) and `group-nes-5col.png`.
- How the beasts are drawn (redrawn 2026-11-19 to get rid of crooked shapes, then refined to the level
  of the people portraits): each design is a Python function built with the helper `src/mondraw.py` (ellipses,
  limbs, tubes and polygons rasterised on pixel centres, so fronts mirror exactly; one light from the top-left in
  three tones per material; separation lines between parts; a traced 1-px black outline), then finished by hand:
  faces with brows, eye strokes and glints, noses, teeth and fangs; fur strokes, bristles, chitin plates, bark
  grain, rivets and cloth folds; rim light; props and costume details. `mon_b.py`: the beasts (drawn bigger
  through `mondraw.Scaled`; `nes_beasts_art.APPROVED` pins the few pixels that moved when mondraw's ties became
  sorted, so the beasts stay exactly as approved). mondraw breaks every tie by sorting, so all pictures come out
  the same on every run and re-exports are stable. `mondraw.famicom()` splits a picture into the background layer and a sprite overlay (skin, glints and
  accents; any attribute area that would need a fourth colour has that colour lifted onto sprites) and finds the
  sub-palettes that keep every 16x16 area and 8x8 sprite tile legal. Field sprites are one hand-typed frame each
  (`src/nes_foes_fields.py`, `SPRITES` in `src/nes_beasts_art.py`); `src/nes_walk_mon.py` makes frame 2 so only
  what should move moves (a step over planted feet, a hop, or a float). `python -P tools/lint.py` checks every
  picture for orphan pixels, broken or doubled outlines, jaggies in the silhouette and mirror symmetry (busts are
  cut by their panel, so pixels beyond the picture edge count as filled).

Group pictures in `chars/family/`: `group-nes.png` (the main-style roster: four framed portraits with their sprites on one baseline) and `group-nes-2x2.png` for narrow screens; the older `group.png` (transparent) and `group-scene.png`. Each also at 4x.

Longmen group pictures in `chars/longmen/`: `group-nes.png` (the six heroes in a row) and `group-nes-3x2.png` for narrow screens; `group-nes-foes.png` (Black Bear, Scar, Skinny Monkey, Tu Qianqiu) and `group-nes-foes-2x2.png`; each also at 4x. The gallery shows the roster that matches the faction filter.

`compare.html` lays the styles side by side so you can pick one.

**Style note:** all art is original, drawn *in the style of* those games. Nothing is traced, copied or downloaded from them. The main style is 8-bit: the Famicom portraits are hand-typed palette-indexed grids (`src/nes_portraits.py`), and `src/nes.py` checks the Famicom colour rules on every export.

## Using the assets in a game

```
chars/index.json                    styles, and every character: id, names (zh/en), faction, bio, variants[]
chars/<id>/<style>/portrait.png     the portrait, plus portrait@4x.png
chars/<id>/<style>/body.png         first idle frame, plus body@4x.png
chars/<id>/<style>/sheet.png        sprite sheet, one animation per row, plus sheet@4x.png
chars/<id>/<style>/sheet.json       frameWidth/Height, anchor (feet), animations {row, frames, fps, loop, note}
```

- Animation names include:
  - `idle`
  - `walk` (front; in `nes` frame 2 keeps the body of frame 1 and only the bottom leg rows change, see src/nes_walk.py)
  - `move` (monsters: two frames for idle and move)
  - `walk_side` (faces right; mirror it for left)
  - `walk_down`, `walk_up`, `walk_left`, `walk_right`
  - `action` / `guard` (signature moves)
- Each variant's `animations` list in `index.json` says which names it has.
- Draw with nearest-neighbour scaling (`image-rendering: pixelated`, `imageSmoothingEnabled = false`) at whole-number scales.

## Editing or adding a character

The pixels live as text grids in Python under `src/`. Each character is one per pixel. `.` is transparent, and letters are colour slots.

- `src/nes.py`: the NES palette table and the Famicom rule checker; `src/nes_portraits.py`: the 8-bit portraits (rows of exactly 48 pixels ending in `|`); `src/nes_sprites.py`: the 16x24 field sprites; `src/nes_longmen.py`: the 龍門武林 portraits and sprites (merged into both), with the bandits and the sect master in `src/nes_longmen2.py` and more of the cast in `src/nes_longmen3.py` (merged into nes_longmen); `src/nes_walk.py`: walk frame 2 (legs only); `src/nes_beasts_art.py` + `src/nes_beasts.py`: the monsters and their encounter-screen group picture; `src/nes_variant.py`: the variant and the roster picture
- `src/pixlib.py`: grids, run-length rows, layers, palettes, strand/stroke/rotation helpers
- `src/paint.py`: soft per-material shading used by the HD-2D styles
- `src/family.py`, `src/family_portraits.py`: family portraits; `src/family_sprites.py`, `src/family_members.py`: family sprites (heads, body sizes, props, actions); `src/family_variant.py`: the variant and group picture
- `src/faces.py`: the hand-drawn portrait heads (male and female templates, jaw/age overlays)
- `src/portrait.py`, `src/chibi.py`: the `koei` portrait and chibi builders
- `src/variants.py`: what a variant provides; `src/styles.py`: style names and descriptions
- `src/chars/<id>.py`: one file per character, holding metadata, palettes, grids and `variants()`
- `src/roster.py`: the characters to export

To add a character:
1. Copy the file of the character whose style you want, e.g. `src/chars/guanyu.py` for `koei`.
2. Change `META`, `FACTION` (`wu`, `shu`, `wei`, `qun`, `west` or `longmen`), the palettes and the grids.
3. Add the id to `ROSTER` in `src/roster.py`.
4. Run `python tools/export.py`. It writes `chars/<id>/<style>/` and rebuilds `chars/index.json`.

Helpers (Python 3 with Pillow):
- `python tools/look.py <id> <style> out.png 6`: one variant zoomed
- `python tools/contact.py out.png`: every variant at 4x
- `python tools/preview.py in.png out.png 12`: zoomed grid for editing
- `python tools/thumb.py`: lobby thumbnail

## Licence

Art and code © the repository owner (ywchen0711), released under **CC BY 4.0**: you may reuse and adapt them with credit. This is a default chosen for you; change it here if you prefer another licence.
