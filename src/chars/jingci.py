"""靜慈師太 Abbess Jingci - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'sectsPeople'
META = dict(
    id='jingci',
    name={'zh': '靜慈師太', 'en': 'Abbess Jingci'},
    style_name={'zh': '慈雲庵主', 'en': 'Abbess of Mercy Cloud'},
    title={'zh': '慈雲庵住持', 'en': 'Abbess of the Mercy Cloud Nunnery'},
    bio={'zh': '慈雲庵的住持。白頭巾、灰色長袍、一串紅念珠和一柄拂塵。說話輕聲細語，出手卻從不留情面——對傷人的人。她說：「刀劍無眼，人心有情。」', 'en': 'Abbess of the Mercy Cloud Nunnery: a white hood, a grey robe, red prayer beads and a horsetail whisk. She speaks softly and shows no mercy - to those who hurt others. "Blades have no eyes; hearts have feeling."'},
    weapon={'zh': '拂塵', 'en': 'Horsetail whisk'},
    alsoIn=['sects'],
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('jingci')]
