"""Nether Flame netherflame - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='netherflame',
    name={'zh': '冥火', 'en': 'Nether Flame'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '幽冥殿裡點不滅的紫火，碰到就渾身發冷。', 'en': 'A purple flame of the Netherworld Hall that never goes out; its touch chills to the bone.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='wisp',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('netherflame')]
