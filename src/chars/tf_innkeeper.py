"""客棧掌櫃 Innkeeper - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_innkeeper',
    name={'zh': '客棧掌櫃', 'en': 'Innkeeper'},
    style_name={'zh': '店家', 'en': 'Innkeeper'},
    title={'zh': '店家', 'en': 'Innkeeper'},
    bio={'zh': '白頭巾、白圍裙的客棧掌櫃，一碗熱湯就能讓人說出心事。', 'en': 'An innkeeper in a white kerchief and apron; one bowl of hot soup and travellers tell him everything.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_innkeeper')]
