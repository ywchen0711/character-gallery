"""邪教徒 Cultist - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_cultist',
    name={'zh': '邪教徒', 'en': 'Cultist'},
    style_name={'zh': '幽冥教眾', 'en': 'Netherworld cultist'},
    title={'zh': '幽冥教眾', 'en': 'Netherworld cultist'},
    bio={'zh': '紫色兜帽、白色鬼面的幽冥教徒，在鎮外的破廟聚會。', 'en': 'A Netherworld cultist in a purple hood and white ghost mask who gathers in the ruined shrine outside town.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_cultist')]
