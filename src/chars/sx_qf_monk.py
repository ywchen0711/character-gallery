"""羅漢僧 Arhat Monk - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_qf_monk',
    name={'zh': '羅漢僧', 'en': 'Arhat Monk'},
    style_name={'zh': '笑羅漢', 'en': 'The Laughing Arhat'},
    title={'zh': '千佛寺的武僧', 'en': 'Fighting monk of the Thousand Buddha Temple'},
    bio={'zh': '光頭、杏黃僧袍、紅袈裟、一串念珠和一根禪杖。站定了，誰也推不動。', 'en': 'Shaved head, saffron robe, red kasaya, prayer beads and a ringed staff. Once he plants his feet, no one can move him.'},
    weapon={'zh': '禪杖', 'en': 'Ringed staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_qf_monk')]
