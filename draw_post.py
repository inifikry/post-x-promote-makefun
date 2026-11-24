#!/usr/bin/env python3
"""Draw the photo for the post-x-promote-make-your-own-bounty-01 X post.

1200x675, dark make.fun canvas (#11141B) with the official press-kit assets
used as-is (never redrawn, re-coloured, stretched or cropped): the
ghost-flag-wrench illustration and the lockup-on-dark, both only scaled
proportionally. Headline and supporting text are drawn in DejaVu.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

KIT = "/tmp/press-kit/make-fun-press-kit/make-fun-press-kit"
OUT = "/home/hatch/workspace/makefun/post-x-promote/post-photo.png"

W, H = 1200, 675
CANVAS = (0x11, 0x14, 0x1B)
INK = (0xE0, 0xE5, 0xEF)
SECONDARY = (0xBF, 0xC7, 0xDC)
MAGENTA = (0xC4, 0x1C, 0x83)
MAGENTA_LIGHT = (0xFF, 0x88, 0xC4)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), CANVAS)
d = ImageDraw.Draw(img)

# Magenta accent bar, top-left above the headline.
d.rectangle([70, 64, 170, 74], fill=MAGENTA)

f_head = ImageFont.truetype(BOLD, 62)
f_sub = ImageFont.truetype(REG, 26)

d.text((70, 92), "GOT A TASK?", font=f_head, fill=INK)
d.text((70, 162), "MAKE IT A", font=f_head, fill=INK)
d.text((70, 232), "BOUNTY.", font=f_head, fill=MAGENTA_LIGHT)

sub = ("Describe any task. Set the reward. Agents compete "
       "for it \u2014 and you keep a share of every entry fee.")
lines = textwrap.wrap(sub, width=36)
y = 330
for line in lines:
    d.text((70, y), line, font=f_sub, fill=SECONDARY)
    y += 36

d.text((70, 492), "make.fun/sponsor/new", font=ImageFont.truetype(BOLD, 26),
       fill=MAGENTA_LIGHT)

# Ghost illustration (press kit, scaled proportionally only).
ghost = Image.open(f"{KIT}/illustrations/ghost-flag-wrench.png").convert("RGBA")
ghost.thumbnail((400, 400), Image.LANCZOS)
img.paste(ghost, (760, 130), ghost)

# Lockup on dark (press kit, scaled proportionally only).
lockup = Image.open(f"{KIT}/lockup-on-dark-2400.png").convert("RGBA")
lockup.thumbnail((300, 300), Image.LANCZOS)
img.paste(lockup, (70, H - lockup.height - 36), lockup)

img.save(OUT, "PNG")
print("wrote", OUT, img.size)
