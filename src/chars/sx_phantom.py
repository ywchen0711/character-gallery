"""鬼手 Phantom Hand - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_phantom',
    name={'zh': '鬼手', 'en': 'Phantom Hand'},
    style_name={'zh': '來無影', 'en': 'Here and Gone'},
    title={'zh': '江湖最快的一雙手', 'en': 'The quickest hands in the jianghu'},
    bio={'zh': '黑兜帽、黑面巾，只露出一雙眼睛。偷東西，也偷武功。', 'en': 'A black hood and a black face-cloth, only the eyes showing. Steals things, and steals techniques.'},
    weapon={'zh': '飛鏢', 'en': 'Darts'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_phantom')]
