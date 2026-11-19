"""鬼面護法 the Ghost-mask Warden of the Netherworld Sect. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='guimian',
    name={'zh': '鬼面護法', 'en': 'Ghost-mask Warden'},
    style_name={'zh': '護法', 'en': 'Warden'},
    title={'zh': '幽冥教護法', 'en': 'Warden of the Netherworld Sect'},
    bio={'zh': '幽冥教的護法，身披血紅尖帽斗篷，臉藏在一張畫著獠牙的白色鬼面後，面具的眼洞裡透著紅光。擋在路中央時一句話也不說。', 'en': 'A warden of the Netherworld Sect in a pointed blood-red hood and cloak, his face hidden behind a white ghost mask painted with fangs, red light in its eye holes. When he blocks the road he says nothing at all.'},
    weapon={'zh': '幽冥掌', 'en': 'Netherworld palm'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('guimian')]
