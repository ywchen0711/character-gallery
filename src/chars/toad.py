"""毒蟾 the Venom Toad of the Marsh. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='toad',
    name={'zh': '毒蟾', 'en': 'Venom Toad'},
    style_name={'zh': '毒物', 'en': 'Poison beast'},
    title={'zh': '沼澤毒王', 'en': 'Poison King of the Marsh'},
    bio={'zh': '蹲在沼澤爛泥裡的大毒蟾，比水牛還寬，背上長滿冒綠光的毒疣，一雙紅眼睛。嘴角滴著毒涎，噴一口毒霧，十步內的草全枯了。', 'en': 'A huge toad squatting in the marsh mud, wider than a water buffalo, its back covered in glowing green poison warts, its eyes red. Venom drips from its mouth, and one breath of its poison mist withers the grass for ten paces.'},
    habitat={'zh': '沼澤與毒瘴林', 'en': 'Marshes and miasma forests'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('toad')]
