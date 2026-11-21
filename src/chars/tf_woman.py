"""鎮上的女子 Townswoman - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_woman',
    name={'zh': '鎮上的女子', 'en': 'Townswoman'},
    style_name={'zh': '布衣百姓', 'en': 'Commoner'},
    title={'zh': '布衣百姓', 'en': 'Commoner'},
    bio={'zh': '高髻插紅簪、一身綠衣的鎮上女子，消息總比衙門快。', 'en': 'A townswoman with a red-pinned bun and a green dress; she hears the news before the magistrate does.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_woman')]
