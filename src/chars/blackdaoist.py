"""Black-robed Daoist blackdaoist - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='blackdaoist',
    name={'zh': '黑袍妖道', 'en': 'Black-robed Daoist'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '投靠幽冥教的妖道，符紙上畫的全是死人的名字。', 'en': "A rogue Daoist who joined the Netherworld Sect; the charms he draws bear dead men's names."},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='sorcerer',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('blackdaoist')]
