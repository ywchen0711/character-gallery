"""Blood Saber Thug bloodthug - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bloodthug',
    name={'zh': '血刀門打手', 'en': 'Blood Saber Thug'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '血刀門雇來的打手，紅衣黑巾，下手不留情。', 'en': 'A thug hired by the Blood Saber Sect, red clothes and black scarf, merciless.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='lackey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bloodthug')]
