"""Little Jiangshi littlejiangshi - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='littlejiangshi',
    name={'zh': '小殭屍', 'en': 'Little Jiangshi'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '還沒長大就入了土的小殭屍，跳起來比大人還快。', 'en': 'A jiangshi buried before it could grow up; it hops faster than the grown ones.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='littlejiangshi',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('littlejiangshi')]
