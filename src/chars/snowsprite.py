"""Snow Sprite snowsprite - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='snowsprite',
    name={'zh': '雪精', 'en': 'Snow Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '暴風雪裡凝出的精怪，一轉身就捲起一陣雪。', 'en': 'A sprite born in a blizzard; it whirls up snow when it turns.'},
    habitat={'zh': '北地雪原與冰魄窟', 'en': 'The northern snowfields and the Ice Soul Caves'},
    tier=5,
    base='windsprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('snowsprite')]
