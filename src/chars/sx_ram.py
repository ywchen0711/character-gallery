"""攻城木 Battering Ram - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_ram',
    name={'zh': '攻城木', 'en': 'Battering Ram'},
    style_name={'zh': '一撞開城', 'en': 'One Blow Opens the Gate'},
    title={'zh': '扛攻城木的力士', 'en': 'The ram-bearer'},
    bio={'zh': '包鐵的巨木架在小屋頂下，推著輪子撞城門。肖像是扛木頭的光頭力士。', 'en': 'An iron-capped log slung under a little roof, rolled up to the gate. The portrait is the bald strongman who carries it.'},
    weapon={'zh': '包鐵巨木', 'en': 'Iron-capped log'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_ram')]
