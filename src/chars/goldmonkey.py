"""Golden Monkey goldmonkey - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='goldmonkey',
    name={'zh': '金毛猴', 'en': 'Golden Monkey'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '金毛發亮的猴王手下，棍法居然有幾分章法。', 'en': "A golden-furred monkey from the ape king's band; its stick work is oddly disciplined."},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='monkey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('goldmonkey')]
