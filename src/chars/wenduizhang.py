"""文對仗 Wen Duizhang - Scholar. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='wenduizhang',
    name={'zh': '文對仗', 'en': 'Wen Duizhang'},
    style_name={'zh': '對聯書生', 'en': 'The Couplet Scholar'},
    title={'zh': '書生', 'en': 'Scholar'},
    bio={'zh': '蘇河城的書生，只用對聯說話，一句上聯一句下聯，從不落單。手裡的大毛筆寫得出驚雷。', 'en': 'A scholar of Suhe who speaks only in couplets, a first line and a second, never one alone. His great brush can write thunder.'},
    weapon={'zh': '如椽大筆', 'en': 'Rafter-sized brush'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('wenduizhang')]
