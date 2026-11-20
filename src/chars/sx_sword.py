"""劍客 Swordsman - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_sword',
    name={'zh': '劍客', 'en': 'Swordsman'},
    style_name={'zh': '一劍霜寒', 'en': 'One Sword, One Frost'},
    title={'zh': '江湖劍客', 'en': 'A swordsman of the jianghu'},
    bio={'zh': '淺藍長衫、白頭帶，長劍出鞘時聲音清得像玉。練劍十年，只為一個「快」字。', 'en': 'Pale blue robe and a white headband; his blade leaves the scabbard with a sound as clear as jade. Ten years of practice for one thing: speed.'},
    weapon={'zh': '長劍', 'en': 'Long sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_sword')]
