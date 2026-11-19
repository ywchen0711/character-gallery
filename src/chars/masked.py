"""蒙面人 the Masked Man of the Stratagem Pavilion. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='masked',
    name={'zh': '蒙面人', 'en': 'The Masked Man'},
    style_name={'zh': '蒙面人', 'en': 'Masked Man'},
    title={'zh': '天機閣中人', 'en': 'In the Stratagem Pavilion'},
    bio={'zh': '在天機閣裡等候的人。深紫兜帽，黑布蒙臉，只露出一雙劍眉和眼睛；紫袍滾金邊，出手時掌心泛起紫光。沒有人見過他的真面目。', 'en': 'The one who waits in the Stratagem Pavilion: a deep purple hood, black cloth over everything but his sword brows and eyes, a purple robe edged in gold, and a violet glow in his palms when he strikes. Nobody has seen his face.'},
    weapon={'zh': '掌法', 'en': 'Palm arts'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('masked')]
