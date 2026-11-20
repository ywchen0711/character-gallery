"""槍陣 Spear Wall - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_spear',
    name={'zh': '槍陣', 'en': 'Spear Wall'},
    style_name={'zh': '紅纓長槍', 'en': 'Red-tasselled Spear'},
    title={'zh': '列陣的槍手', 'en': 'Spearman of the line'},
    bio={'zh': '鐵盔紅甲，紅纓長槍一字排開，騎兵最怕這一排槍尖。', 'en': 'Iron helmet, red armour; a row of red-tasselled spears is what horsemen fear most.'},
    weapon={'zh': '紅纓槍', 'en': 'Red-tasselled spear'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_spear')]
