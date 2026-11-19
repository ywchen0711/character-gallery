"""Rogue Daoist daoist - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='daoist',
    name={'zh': '妖道', 'en': 'Rogue Daoist'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '畫符招鬼的妖道，長鬚飄飄，一臉仙氣，滿肚子壞水。', 'en': 'A rogue Daoist who draws charms to summon ghosts: flowing beard, saintly face, a bellyful of mischief.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='sorcerer',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('daoist')]
