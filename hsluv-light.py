#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0321,C0301
"""Light scheme for Sigma-theme"""

import os
from hsluv import hsluv_to_rgb
from PIL import Image, ImageDraw

# Colors
BA = 155

H01 = BA  ; S01 = 100 ; L01 = 18 ; COL01 = [] ; ZIP01 = [] #base1
H02 = BA  ; S02 = 100 ; L02 = 40 ; COL02 = [] ; ZIP02 = [] #base2
H03 = BA  ; S03 = 100 ; L03 = 62 ; COL03 = [] ; ZIP03 = [] #base3
H04 = BA  ; S04 = 100 ; L04 = 84 ; COL04 = [] ; ZIP04 = [] #base4
H05 = BA  ; S05 = 100 ; L05 = 84 ; COL05 = [] ; ZIP05 = [] #base4
H06 = BA  ; S06 = 100 ; L06 = 84 ; COL06 = [] ; ZIP06 = [] #base4
H07 = BA  ; S07 = 100 ; L07 = 84 ; COL07 = [] ; ZIP07 = [] #base4
H08 = BA  ; S08 = 100 ; L08 = 84 ; COL08 = [] ; ZIP08 = [] #base4
H09 = BA  ; S09 = 100 ; L09 = 84 ; COL09 = [] ; ZIP09 = [] #base4
H10 = BA  ; S10 = 100 ; L10 = 84 ; COL10 = [] ; ZIP10 = [] #base4
H11 = BA  ; S11 = 100 ; L11 = 84 ; COL11 = [] ; ZIP11 = [] #base4
H12 = BA  ; S12 = 100 ; L12 = 84 ; COL12 = [] ; ZIP12 = [] #base4

# Conversion to RGB

A01 = hsluv_to_rgb([H01, S01, L01])
for i in A01: i = round(i*255); COL01.extend([i])

A02 = hsluv_to_rgb([H02, S02, L02])
for i in A02: i = round(i*255); COL02.extend([i])

A03 = hsluv_to_rgb([H03, S03, L03])
for i in A03: i = round(i*255); COL03.extend([i])

A04 = hsluv_to_rgb([H04, S04, L04])
for i in A04: i = round(i*255); COL04.extend([i])

A05 = hsluv_to_rgb([H05, S05, L05])
for i in A05: i = round(i*255); COL05.extend([i])

A06 = hsluv_to_rgb([H06, S06, L06])
for i in A06: i = round(i*255); COL06.extend([i])

A07 = hsluv_to_rgb([H07, S07, L07])
for i in A07: i = round(i*255); COL07.extend([i])

A08 = hsluv_to_rgb([H08, S08, L08])
for i in A08: i = round(i*255); COL08.extend([i])

A09 = hsluv_to_rgb([H09, S09, L09])
for i in A09: i = round(i*255); COL09.extend([i])

A10 = hsluv_to_rgb([H10, S10, L10])
for i in A10: i = round(i*255); COL10.extend([i])

A11 = hsluv_to_rgb([H11, S11, L11])
for i in A11: i = round(i*255); COL11.extend([i])

A12 = hsluv_to_rgb([H12, S12, L12])
for i in A12: i = round(i*255); COL12.extend([i])


# Conversion to HEX
for i in A01: i = round(i*255); ZIP01.extend([f'{i:02X}']); HEX01 = '#'+''.join(ZIP01)
for i in A02: i = round(i*255); ZIP02.extend([f'{i:02X}']); HEX02 = '#'+''.join(ZIP02)
for i in A03: i = round(i*255); ZIP03.extend([f'{i:02X}']); HEX03 = '#'+''.join(ZIP03)
for i in A04: i = round(i*255); ZIP04.extend([f'{i:02X}']); HEX04 = '#'+''.join(ZIP04)
for i in A05: i = round(i*255); ZIP05.extend([f'{i:02X}']); HEX05 = '#'+''.join(ZIP05)
for i in A06: i = round(i*255); ZIP06.extend([f'{i:02X}']); HEX06 = '#'+''.join(ZIP06)
for i in A07: i = round(i*255); ZIP07.extend([f'{i:02X}']); HEX07 = '#'+''.join(ZIP07)
for i in A08: i = round(i*255); ZIP08.extend([f'{i:02X}']); HEX08 = '#'+''.join(ZIP08)
for i in A09: i = round(i*255); ZIP09.extend([f'{i:02X}']); HEX09 = '#'+''.join(ZIP09)
for i in A10: i = round(i*255); ZIP10.extend([f'{i:02X}']); HEX10 = '#'+''.join(ZIP10)
for i in A11: i = round(i*255); ZIP11.extend([f'{i:02X}']); HEX11 = '#'+''.join(ZIP11)
for i in A12: i = round(i*255); ZIP12.extend([f'{i:02X}']); HEX12 = '#'+''.join(ZIP12)

# Define the individual width
W = 100
H = 100
SEP = 0

w, h = W*4, H*1+SEP*2

# Background
BG = []
A0 = hsluv_to_rgb([H01, S01, L01])
for i in A0: i = round(i*255); BG.extend([i])
image = Image.new("RGB", (w, h), color=(BG[0], BG[1], BG[2]))

# COL01
SHAPE01 = [(W*0, 0), (W*0+W, H)]
fig1 = ImageDraw.Draw(image)
fig1.rectangle(SHAPE01, fill=(COL01[0], COL01[1], COL01[2]))

# COL02
SHAPE02 = [(W*1, 0), (W*1+W, H)]
fig2 = ImageDraw.Draw(image)
fig2.rectangle(SHAPE02, fill=(COL02[0], COL02[1], COL02[2]))

# COL03
SHAPE03 = [(W*2, 0), (W*2+W, H)]
fig3 = ImageDraw.Draw(image)
fig3.rectangle(SHAPE03, fill=(COL03[0], COL03[1], COL03[2]))

# COL04
SHAPE04 = [(W*3, 0), (W*3+W, H)]
fig4 = ImageDraw.Draw(image)
fig4.rectangle(SHAPE04, fill=(COL04[0], COL04[1], COL04[2]))

# Output
print("col01", HEX01)
print("col02", HEX02)
print("col03", HEX03)
print("col04", HEX04)
print("col05", HEX05)
print("col06", HEX06)
print("col07", HEX07)
print("col08", HEX08)
print("col09", HEX09)
print("col10", HEX10)
print("col11", HEX11)
print("col12", HEX12)

# Generate the image
IMAGE='light.png'
image.save(IMAGE)

PS=str("ps -ef | grep -v grep | grep 'mupdf' ")
FL=str("| grep -o '" + IMAGE + "' > /dev/null")
CHECK=os.system(PS+FL)

if CHECK == 256:
    os.system("mupdf '" + IMAGE + "' 2>/dev/null &")
else:
    os.system("pkill -HUP mupdf 2>/dev/null")
