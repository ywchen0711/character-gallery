"""Iron-bound Dummy irondummy - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='irondummy',
    name={'zh': '鐵木人', 'en': 'Iron-bound Dummy'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '包了鐵皮的木人，守在高塔的練功房。', 'en': 'A dummy sheathed in iron that guards the practice room of the tower.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='dummy',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('irondummy')]
