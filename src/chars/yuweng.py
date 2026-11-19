"""獨臂漁翁 the One-Armed Fisherman. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='yuweng',
    name={'zh': '獨臂漁翁', 'en': 'The One-Armed Fisherman'},
    style_name={'zh': '漁翁', 'en': 'Fisherman'},
    title={'zh': '江邊隱者', 'en': 'Recluse of the River'},
    bio={'zh': '住在斷崖下江邊的老漁翁，一頂斗笠、一部白鬍子，左袖空蕩蕩地打了個結。整天只是釣魚，不問名姓；可他看人出刀的眼光，比刀還快。', 'en': 'An old fisherman living by the river under the broken cliff: a straw hat, a long white beard, the empty left sleeve tied in a knot. He only fishes and gives no name, yet his eye for a man drawing a blade is quicker than the blade.'},
    weapon={'zh': '釣竿', 'en': 'Fishing rod'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('yuweng')]
