"""Iron-head Monk ironmonk - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='ironmonk',
    name={'zh': '鐵頭惡僧', 'en': 'Iron-head Monk'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '練鐵頭功練到頭皮發青的惡僧，用頭撞門。', 'en': 'A rogue monk who trained his iron-head skill until his scalp turned grey; he opens doors with his head.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='roguemonk',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('ironmonk')]
