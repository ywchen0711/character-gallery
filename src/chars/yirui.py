"""奕叡 Yi Rui - the elder brother, a young saber-wielder of the Longmen Saber Manor. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='yirui',
    name={'zh': '奕叡', 'en': 'Yi Rui'},
    style_name={'zh': '刀客', 'en': 'Swordsman'},
    title={'zh': '啟程刀客', 'en': 'The Departing Blade'},
    bio={'zh': '龍門刀莊的長子，背著一把舊環首刀離家闖蕩。話不多，眉眼總是往前看；深藍長袍、藍色頭帶，頭帶的尾巴在風裡飛。他相信再遠的路，都是從第一刀開始的。', 'en': 'Elder son of the Longmen Saber Manor, who left home with an old ring-pommel saber on his back. He says little and always looks ahead, in an indigo robe with a blue headband whose ties fly in the wind. However long the road, he believes it begins with the first cut.'},
    weapon={'zh': '環首刀', 'en': 'Ring-pommel saber'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('yirui')]
