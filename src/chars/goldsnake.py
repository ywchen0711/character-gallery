"""Gold-ring Snake goldsnake - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='goldsnake',
    name={'zh': '金環蛇', 'en': 'Gold-ring Snake'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '南疆竹林裡的毒蛇，一圈黑一圈金，咬一口半天走不動。', 'en': 'A poisonous snake of the southern bamboo, ringed black and gold.'},
    habitat={'zh': '南疆的竹林與海島', 'en': 'The southern bamboo and isles'},
    tier=4,
    base='snake',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('goldsnake')]
