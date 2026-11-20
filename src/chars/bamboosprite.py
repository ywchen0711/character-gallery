"""Bamboo Sprite bamboosprite - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='bamboosprite',
    name={'zh': '竹精', 'en': 'Bamboo Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '竹林裡長了靈性的竹子，會替受傷的妖物療傷。', 'en': 'A bamboo stalk that came to life; it tends wounded creatures.'},
    habitat={'zh': '青竹寨外的竹海', 'en': 'The Bamboo Sea outside Green Bamboo village'},
    tier=4,
    base='treesprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bamboosprite')]
