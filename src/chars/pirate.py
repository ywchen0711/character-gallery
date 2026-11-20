"""River Pirate pirate - a common foe of Longmen Quest II (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='pirate',
    name={'zh': '水寇', 'en': 'River Pirate'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '在蘇河水道上打劫的水寇，頭綁白巾，扛著船槳當棍子。', 'en': 'A river pirate of the Suhe canals: white head cloth, an oar for a club.'},
    habitat={'zh': '水鄉的河道與碧波洞', 'en': 'The canal country and Green Wave Cave'},
    tier=2,
    base='lackey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('pirate')]
