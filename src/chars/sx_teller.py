"""說書人 Storyteller - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_teller',
    name={'zh': '說書人', 'en': 'Storyteller'},
    style_name={'zh': '且聽下回', 'en': 'To Be Continued'},
    title={'zh': '茶館的說書人', 'en': 'A teahouse storyteller'},
    bio={'zh': '棕袍方巾、山羊鬍，手裡一把紅摺扇。醒木一拍，說得全隊熱血沸騰。', 'en': "A brown robe, a scholar's cap, a goatee and a red folding fan. One clap of the block and the whole company's blood is up."},
    weapon={'zh': '摺扇與醒木', 'en': 'Folding fan and clapper'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_teller')]
