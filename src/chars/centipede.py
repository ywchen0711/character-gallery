"""Centipede centipede - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='centipede',
    name={'zh': '蜈蚣', 'en': 'Centipede'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '一尺長的紅蜈蚣，從石縫裡直立起來咬人。', 'en': 'A red centipede a foot long that rears up out of the rock cracks to bite.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='centipede',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('centipede')]
