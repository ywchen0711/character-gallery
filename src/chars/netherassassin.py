"""Netherworld Assassin netherassassin - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='netherassassin',
    name={'zh': '幽冥刺客', 'en': 'Netherworld Assassin'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '幽冥教的刺客，紫紗下的眼睛泛著紅光。', 'en': 'A Netherworld Sect assassin whose eyes glow red under the violet veil.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='assassin',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('netherassassin')]
