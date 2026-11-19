"""程遠志 Cheng Yuanzhi - an enemy general of 三國志 霸王之路 (stage: 黃巾之亂). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='chengyuanzhi',
    name={'zh': '程遠志', 'en': 'Cheng Yuanzhi'},
    style_name={'zh': '黃巾頭目', 'en': 'Yellow Turban captain'},
    title={'zh': '黃巾之亂・黃巾頭目', 'en': 'The Yellow Turban Rebellion - Yellow Turban captain'},
    bio={'zh': '黃巾軍的頭目，頭綁黃巾、眉上一道疤，帶著一群拿長槍的農民兵。霸王之路的第一戰，新任主將的試刀石。', 'en': 'A Yellow Turban captain with a yellow head-cloth and a scar over one brow, leading peasant spearmen. The first battle of the road, where a new general proves himself.'},
    weapon={'zh': '長槍', 'en': 'Spear'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('chengyuanzhi')]
