"""Bronze Guardian bronzeman - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bronzeman',
    name={'zh': '銅人', 'en': 'Bronze Guardian'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '寺裡試武用的銅人，機關一開就擺出拳架。', 'en': 'A temple bronze man for testing fighters; trip its mechanism and it takes a stance.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='bronze',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bronzeman')]
