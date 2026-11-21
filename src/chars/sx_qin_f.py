"""琴姬 Qin Maid - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_qin_f',
    name={'zh': '琴姬', 'en': 'Qin Maid'},
    style_name={'zh': '陽春白雪', 'en': 'Spring Snow'},
    title={'zh': '撫琴的女樂師', 'en': 'A woman player of the qin'},
    bio={'zh': '粉衣高髻的琴姬，金簪紅帶，懷抱古琴。', 'en': 'A qin maid in pink with a high bun, a gold pin and a red ribbon, a qin in her arms.'},
    weapon={'zh': '古琴', 'en': 'Qin'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_qin_f')]
