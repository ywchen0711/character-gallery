"""Will-o'-wisp wisp - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='wisp',
    name={'zh': '鬼火', 'en': "Will-o'-wisp"},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '墳地上飄的藍色鬼火，會跟著人走。', 'en': 'A blue ghost-flame over the graves that follows people home.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='wisp',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('wisp')]
