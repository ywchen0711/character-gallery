"""鐵鍊捕快 Iron Chain Constable - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_zf_chain',
    name={'zh': '鐵鍊捕快', 'en': 'Iron Chain Constable'},
    style_name={'zh': '鐵鎖連環', 'en': 'Iron Locks in a Chain'},
    title={'zh': '執法堂的捕快', 'en': 'Constable of the Hall of Law'},
    bio={'zh': '烏紗帽、八字鬍、炭灰長袍，腰間一條鐵鍊。和鐵無私一樣不認交情。', 'en': 'Black gauze cap, a stern moustache, a charcoal robe and an iron chain at the waist. Like Tie Wusi, he does not care whose friend you are.'},
    weapon={'zh': '鐵鍊', 'en': 'Iron chain'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_zf_chain')]
