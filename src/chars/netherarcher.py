"""Netherworld Archer netherarcher - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='netherarcher',
    name={'zh': '幽冥弓手', 'en': 'Netherworld Archer'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '幽冥教的弓手，箭頭塗著冥火。', 'en': 'A Netherworld Sect archer whose arrowheads are smeared with nether-fire.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='archer',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('netherarcher')]
