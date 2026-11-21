"""奕長風 Yi Changfeng - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'tactics'
META = dict(
    id='yichangfeng',
    name={'zh': '奕長風', 'en': 'Yi Changfeng'},
    style_name={'zh': '龍門刀莊莊主', 'en': 'Master of the Longmen Manor'},
    title={'zh': '龍門刀莊莊主・兩兄弟的父親', 'en': 'Master of the Longmen Sabre Manor, father of the brothers'},
    bio={'zh': '龍門刀莊的莊主，奕叡和奕碩的父親。灰髮長鬚，深藍長袍，腰間一柄環首刀。把戰旗交給兒子們時，只說了一句：「人在，旗在。」', 'en': 'Master of the Longmen Sabre Manor and father of Yi Rui and Yi Shuo: grey hair, a long beard, a deep blue robe and a ring-pommel sabre at his side. When he handed his sons the banner he said only: "While you stand, the banner stands."'},
    weapon={'zh': '環首刀', 'en': 'Ring-pommel sabre'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('yichangfeng')]
