"""神偷 Thief - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_thief',
    name={'zh': '神偷', 'en': 'Thief'},
    style_name={'zh': '妙手空空', 'en': 'Empty Hands'},
    title={'zh': '江湖神偷', 'en': 'A thief of the jianghu'},
    bio={'zh': '紅頭帶、黑短褂，腰裡一把小匕首。手比眼睛快，摸走你的錢袋時還會對你笑。', 'en': 'Red headband, black jacket, a little dagger at the waist. Hands faster than eyes; he smiles at you as he lifts your purse.'},
    weapon={'zh': '匕首', 'en': 'Dagger'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_thief')]
