"""Frost Wolf frostwolf - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='frostwolf',
    name={'zh': '霜狼', 'en': 'Frost Wolf'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '雪峰上的白狼，呼出的氣會結成霜，腳步聲輕得聽不見。', 'en': 'A white wolf of the snow peaks whose breath turns to frost and whose steps make no sound.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='wolf',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('frostwolf')]
