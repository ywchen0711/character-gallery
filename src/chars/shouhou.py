"""瘦猴 Skinny Monkey - the Black Wind Fort's lackey. Drawn in the 8-bit `nes` style only (src/nes_longmen2.py)."""

FACTION = 'longmen'
META = dict(
    id='shouhou',
    name={'zh': '瘦猴', 'en': 'Skinny Monkey'},
    style_name={'zh': '嘍囉', 'en': 'Lackey'},
    title={'zh': '黑風寨的跑腿', 'en': 'Errand Boy of the Black Wind Fort'},
    bio={'zh': '黑風寨的小嘍囉，瘦得像根竹竿，一笑就露出兩顆大門牙。衣服補了又補，腰間別一把短刀；眼珠子滴溜溜地轉，哪邊有便宜就往哪邊靠。跑得比誰都快，逃得也比誰都快。', 'en': 'A lackey of the Black Wind Fort, thin as a bamboo pole, who shows two big front teeth whenever he grins. His clothes are patch on patch and a short knife sits at his belt; his eyes dart about for whatever is going cheap. Nobody runs errands faster, and nobody runs away faster either.'},
    weapon={'zh': '短刀', 'en': 'Short knife'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('shouhou')]
