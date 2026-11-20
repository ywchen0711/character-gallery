"""Snow Monkey snowmonkey - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='snowmonkey',
    name={'zh': '雪猴', 'en': 'Snow Monkey'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '北地的白毛猴，最愛偷旅人的乾糧。', 'en': "A white-furred monkey of the north that loves to steal travellers' rations."},
    habitat={'zh': '北地雪原', 'en': 'The northern snowfields'},
    tier=5,
    base='monkey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('snowmonkey')]
