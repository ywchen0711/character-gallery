"""Fire Hornet firehornet - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='firehornet',
    name={'zh': '火蜂', 'en': 'Fire Hornet'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '火山口飛出的紅蜂，翅膀一振就冒火星。', 'en': 'Red hornets from the crater; sparks fly when they beat their wings.'},
    habitat={'zh': '焰口村與赤焰窟', 'en': 'Yankou and the Red Flame Caves'},
    tier=4,
    base='hornet',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('firehornet')]
