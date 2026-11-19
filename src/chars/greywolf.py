"""Grey Wolf greywolf - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='greywolf',
    name={'zh': '灰狼', 'en': 'Grey Wolf'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '成群在山林小徑邊游蕩的灰狼，餓了就敢圍住落單的旅人。', 'en': 'Grey wolves roam the forest paths in packs and will circle a lone traveller when hungry.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='wolf',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('greywolf')]
