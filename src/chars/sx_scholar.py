"""書生 Scholar - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_scholar',
    name={'zh': '書生', 'en': 'Scholar'},
    style_name={'zh': '如椽大筆', 'en': 'The Rafter Brush'},
    title={'zh': '讀書人', 'en': 'A man of letters'},
    bio={'zh': '青衫白頭巾，肩上扛著一支比人還長的大毛筆。墨是水，字是風。', 'en': 'A teal gown and a white headband, a brush taller than he is on his shoulder. Ink is water; characters are wind.'},
    weapon={'zh': '大毛筆', 'en': 'Great brush'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_scholar')]
