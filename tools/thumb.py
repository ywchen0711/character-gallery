"""960x540 lobby thumbnail: the 8-bit family roster (main style) at 4x on black.
python tools/thumb.py"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = Image.open(os.path.join(ROOT, 'chars', 'family', 'group-nes.png')).convert('RGB')
T = Image.new('RGB', (960, 540), (0, 0, 0))
big = g.resize((g.width * 4, g.height * 4), Image.NEAREST)
T.paste(big, ((960 - big.width) // 2, (540 - big.height) // 2))
T.save(os.path.join(ROOT, 'thumb.jpg'), quality=95)
