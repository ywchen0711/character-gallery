"""Black-bone Swordsman blackbone - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='blackbone',
    name={'zh': '黑骨劍客', 'en': 'Black-bone Swordsman'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '被幽冥教煉過的骷髏，骨頭黑得發亮。', 'en': 'A skeleton refined by the Netherworld Sect; its bones shine black.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='skeleton',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('blackbone')]
