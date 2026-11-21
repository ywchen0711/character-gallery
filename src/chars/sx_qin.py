"""琴師 Qin Player - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_qin',
    name={'zh': '琴師', 'en': 'Qin Player'},
    style_name={'zh': '高山流水', 'en': 'High Mountains, Flowing Water'},
    title={'zh': '撫琴的樂師', 'en': 'A player of the qin'},
    bio={'zh': '藍袍長髮的琴師，懷裡橫抱一張古琴。一曲鼓舞同伴，一曲亂人心神。', 'en': "A long-haired musician in blue holding a qin across his chest. One tune lifts his friends, another scatters the foe's wits."},
    weapon={'zh': '古琴', 'en': 'Qin'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_qin')]
