"""幽冥刺客 Netherworld Assassin - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_ym_assassin',
    name={'zh': '幽冥刺客', 'en': 'Netherworld Assassin'},
    style_name={'zh': '白骨面', 'en': 'The Bone Mask'},
    title={'zh': '幽冥教的刺客', 'en': 'Assassin of the Netherworld Sect'},
    bio={'zh': '紫色兜帽、白骨半面具，眼洞透著紅光。屠千秋的影子。', 'en': "A violet hood and a white bone half-mask with red light in the eyeholes: Tu Qianqiu's shadow."},
    weapon={'zh': '飛鏢', 'en': 'Throwing darts'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_ym_assassin')]
