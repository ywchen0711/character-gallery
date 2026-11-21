"""書生 Scholar - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_scholar',
    name={'zh': '書生', 'en': 'Scholar'},
    style_name={'zh': '讀書人', 'en': 'Scholar'},
    title={'zh': '讀書人', 'en': 'Scholar'},
    bio={'zh': '藍衫書生，懷裡抱著書，進京趕考的路上。', 'en': 'A scholar in blue with a book at his chest, on his way to the capital exams.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_scholar')]
