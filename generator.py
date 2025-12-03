
from PIL import Image, ImageDraw, ImageFont
import os, textwrap

# constants
WIDTH, HEIGHT, MARGIN_X, MARGIN_Y = 1584, 396, 24, -6
OUTPUT = "linkedin_header.png"
code = open(os.path.abspath(__file__), "r", encoding="utf-8", errors="replace").read()

# create canvas
img = Image.new("RGB", (WIDTH, HEIGHT), "#1C1E21"); draw = ImageDraw.Draw(img)
font = ImageFont.truetype("consola.ttf", 12)
char_w, line_h = 8, 18
lines = code.splitlines()

# add syntax highlighting
for ln in lines:
    s = ln.lstrip()
    color = "#6A9955" if s.startswith("#") else "#569CD6" if s.startswith(("import ","from ")) else "#E6EEF3" if "=" in s else "#ECC48D"
    draw.text((MARGIN_X, MARGIN_Y),ln,font=font,fill=color); MARGIN_Y += line_h

img.save(OUTPUT)
