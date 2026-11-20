"""狼牙棒手 Wolf-tooth Clubman - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_hf_club',
    name={'zh': '狼牙棒手', 'en': 'Wolf-tooth Clubman'},
    style_name={'zh': '黑風嘍囉頭', 'en': 'Head of the Black Wind Boys'},
    title={'zh': '黑風寨的棒手', 'en': 'Clubman of the Black Wind Fort'},
    bio={'zh': '刺蝟頭、一臉黑鬍子、棕色皮背心，扛著釘滿鐵釘的狼牙棒。黑熊說什麼他就做什麼。', 'en': 'Spiky hair, a black beard and a brown leather vest, with a nail-studded wolf-tooth club on his shoulder. Whatever Black Bear says, he does.'},
    weapon={'zh': '狼牙棒', 'en': 'Wolf-tooth club'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_hf_club')]
