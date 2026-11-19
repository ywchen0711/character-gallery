"""Rogue Monk roguemonk - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='roguemonk',
    name={'zh': '惡僧', 'en': 'Rogue Monk'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '被逐出寺門的和尚，念珠還掛著，心早就不在了。', 'en': 'A monk driven out of his temple; he still wears his beads, but his heart left long ago.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='roguemonk',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('roguemonk')]
