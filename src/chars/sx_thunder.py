"""霹靂車 Thunder Cart - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_thunder',
    name={'zh': '霹靂車', 'en': 'Thunder Cart'},
    style_name={'zh': '雷火一聲', 'en': 'One Clap of Thunder-fire'},
    title={'zh': '火藥師', 'en': 'The powder master'},
    bio={'zh': '滿載火藥桶的車，車頭架著銅火筒。肖像是捧著霹靂彈的火藥師，引信還在冒火星。', 'en': 'A cart full of powder kegs with a bronze fire-tube in front. The portrait is the powder master holding a thunder bomb, its fuse still sparking.'},
    weapon={'zh': '霹靂彈', 'en': 'Thunder bomb'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_thunder')]
