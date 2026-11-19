"""Red Chain Snake redsnake - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='redsnake',
    name={'zh': '赤鍊蛇', 'en': 'Red Chain Snake'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '身上一節一節紅黑相間的蛇，咬一口麻半天。', 'en': 'A snake banded red and black like a chain; one bite numbs you for half a day.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='snake',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('redsnake')]
