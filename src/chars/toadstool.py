"""Toadstool Imp toadstool - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='toadstool',
    name={'zh': '毒菇妖', 'en': 'Toadstool Imp'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '紅傘白點的毒菇成了精，一跺腳就噴毒粉。', 'en': 'A red, white-spotted toadstool turned imp; it stamps and puffs out poison spores.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='mushroom',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('toadstool')]
