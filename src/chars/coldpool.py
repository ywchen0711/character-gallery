"""Cold Pool Ghost coldpool - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='coldpool',
    name={'zh': '寒潭鬼', 'en': 'Cold Pool Ghost'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '寒潭底下的女鬼，經過的水面都會結一層薄冰。', 'en': 'A ghost from the bottom of the cold pool; the water she passes skins over with ice.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='drowned',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('coldpool')]
