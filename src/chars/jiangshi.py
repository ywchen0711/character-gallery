"""符咒殭屍 the Talisman Jiangshi. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='jiangshi',
    name={'zh': '符咒殭屍', 'en': 'Talisman Jiangshi'},
    style_name={'zh': '殭屍', 'en': 'Undead'},
    title={'zh': '義莊的跳屍', 'en': 'Hopper of the Coffin House'},
    bio={'zh': '穿著紫色官服、頭戴官帽的殭屍，額前貼著一張黃符，雙臂直直伸向前，一跳一跳地走。符一掉下來，就再也停不住了。', 'en': 'A corpse in a purple official robe and cap with a yellow talisman stuck to its brow, arms stretched straight out, moving in hops. If the talisman falls off, nothing can stop it.'},
    habitat={'zh': '義莊、古墓與夜路', 'en': 'Coffin houses, old tombs and night roads'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('jiangshi')]
