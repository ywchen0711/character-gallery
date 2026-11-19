"""Tiger Hornet tigerhornet - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='tigerhornet',
    name={'zh': '虎頭蜂', 'en': 'Tiger Hornet'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '拳頭大的虎頭蜂，嗡嗡聲一響，山路上的人都趴下。', 'en': 'A hornet as big as a fist; when its buzz comes up the path, everyone drops flat.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='hornet',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('tigerhornet')]
