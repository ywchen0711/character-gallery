"""落星弓手 Star-felling Archer - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_starbow',
    name={'zh': '落星弓手', 'en': 'Star-felling Archer'},
    style_name={'zh': '金弓落星', 'en': 'A Golden Bow to Fell Stars'},
    title={'zh': '神射手', 'en': 'A peerless archer'},
    bio={'zh': '紅甲金弓，箭能射落天上的流星——至少說書人是這麼說的。', 'en': 'Red armour, golden bow; his arrows can bring down a falling star - or so the storytellers say.'},
    weapon={'zh': '金弓', 'en': 'Golden bow'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_starbow')]
