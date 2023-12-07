#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0321,C0301
"""Night colors palette"""

import os
from hsluv import hsluv_to_rgb
from PIL import Image, ImageDraw

# Preview
xres = True
shot = True

# Hue
BA = 240

# Sat
SA = 15

H00 = BA  ; S00 = 0 ; L00 = 0   ; COL00 = [] ; ZIP00 = [] #col00

H01 = BA  ; S01 = SA ; L01 = 8  ; COL01 = [] ; ZIP01 = [] #col01
H02 = BA  ; S02 = SA ; L02 = 13 ; COL02 = [] ; ZIP02 = [] #col02
H03 = BA  ; S03 = SA ; L03 = 18 ; COL03 = [] ; ZIP03 = [] #col03
H04 = BA  ; S04 = SA ; L04 = 23 ; COL04 = [] ; ZIP04 = [] #col04
H05 = BA  ; S05 = SA ; L05 = 28 ; COL05 = [] ; ZIP05 = [] #col05
H06 = BA  ; S06 = SA ; L06 = 33 ; COL06 = [] ; ZIP06 = [] #col06
H07 = BA  ; S07 = SA ; L07 = 38 ; COL07 = [] ; ZIP07 = [] #col07
H08 = BA  ; S08 = SA ; L08 = 43 ; COL08 = [] ; ZIP08 = [] #col08
H09 = BA  ; S09 = SA ; L09 = 48 ; COL09 = [] ; ZIP09 = [] #col09
H10 = BA  ; S10 = SA ; L10 = 53 ; COL10 = [] ; ZIP10 = [] #col10
H11 = BA  ; S11 = SA ; L11 = 58 ; COL11 = [] ; ZIP11 = [] #col11
H12 = BA  ; S12 = SA ; L12 = 63 ; COL12 = [] ; ZIP12 = [] #col12
H13 = BA  ; S13 = SA ; L13 = 68 ; COL13 = [] ; ZIP13 = [] #col13
H14 = BA  ; S14 = SA ; L14 = 73 ; COL14 = [] ; ZIP14 = [] #col14
H15 = BA  ; S15 = SA ; L15 = 78 ; COL15 = [] ; ZIP15 = [] #col15
H16 = BA  ; S16 = SA ; L16 = 83 ; COL16 = [] ; ZIP16 = [] #col16

# Conversion to RGB
A00 = hsluv_to_rgb([H00, S00, L00])
for i in A00: i = round(i*255); COL00.extend([i])

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

A13 = hsluv_to_rgb([H13, S13, L13])
for i in A13: i = round(i*255); COL13.extend([i])

A14 = hsluv_to_rgb([H14, S14, L14])
for i in A14: i = round(i*255); COL14.extend([i])

A15 = hsluv_to_rgb([H15, S15, L15])
for i in A15: i = round(i*255); COL15.extend([i])

A16 = hsluv_to_rgb([H16, S16, L16])
for i in A16: i = round(i*255); COL16.extend([i])

# Conversion to HEX
for i in A00: i = round(i*255); ZIP00.extend([f'{i:02X}']); HEX00 = '#'+''.join(ZIP00)
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
for i in A13: i = round(i*255); ZIP13.extend([f'{i:02X}']); HEX13 = '#'+''.join(ZIP13)
for i in A14: i = round(i*255); ZIP14.extend([f'{i:02X}']); HEX14 = '#'+''.join(ZIP14)
for i in A15: i = round(i*255); ZIP15.extend([f'{i:02X}']); HEX15 = '#'+''.join(ZIP15)
for i in A16: i = round(i*255); ZIP16.extend([f'{i:02X}']); HEX16 = '#'+''.join(ZIP16)

# Define the individual width
W = 200
H = 40
SEP = 10

w, h = W*1+SEP*2, H*16+SEP*2

# Background
BG = []
# A0 = hsluv_to_rgb([H01, S01, L01])
# for i in A0: i = round(i*255); BG.extend([i])
image = Image.new("RGB", (w, h), color=(COL00[0], COL00[1], COL00[2]))

# COL01
SHAPE01 = [(0+SEP, H*0+SEP), (W+SEP, H*0+H+SEP)]
fig1 = ImageDraw.Draw(image)
fig1.rectangle(SHAPE01, fill=(COL01[0], COL01[1], COL01[2]))

# COL02
SHAPE02 = [(0+SEP, H*1+SEP), (W+SEP, H*1+H+SEP)]
fig2 = ImageDraw.Draw(image)
fig2.rectangle(SHAPE02, fill=(COL02[0], COL02[1], COL02[2]))

# COL03
SHAPE03 = [(0+SEP, H*2+SEP), (W+SEP, H*2+H+SEP)]
fig3 = ImageDraw.Draw(image)
fig3.rectangle(SHAPE03, fill=(COL03[0], COL03[1], COL03[2]))

# COL04
SHAPE04 = [(0+SEP, H*3+SEP), (W+SEP, H*3+H+SEP)]
fig4 = ImageDraw.Draw(image)
fig4.rectangle(SHAPE04, fill=(COL04[0], COL04[1], COL04[2]))

# COL05
SHAPE05 = [(0+SEP, H*4+SEP), (W+SEP, H*4+H+SEP)]
fig5 = ImageDraw.Draw(image)
fig5.rectangle(SHAPE05, fill=(COL05[0], COL05[1], COL05[2]))

# COL06
SHAPE06 = [(0+SEP, H*5+SEP), (W+SEP, H*5+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE06, fill=(COL06[0], COL06[1], COL06[2]))

# COL07
SHAPE07 = [(0+SEP, H*6+SEP), (W+SEP, H*6+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE07, fill=(COL07[0], COL07[1], COL07[2]))

# COL08
SHAPE08 = [(0+SEP, H*7+SEP), (W+SEP, H*7+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE08, fill=(COL08[0], COL08[1], COL08[2]))

# COL09
SHAPE09 = [(0+SEP, H*8+SEP), (W+SEP, H*8+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE09, fill=(COL09[0], COL09[1], COL09[2]))

# COL10
SHAPE10 = [(0+SEP, H*9+SEP), (W+SEP, H*9+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE10, fill=(COL10[0], COL10[1], COL10[2]))

# COL11
SHAPE11 = [(0+SEP, H*10+SEP), (W+SEP, H*10+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE11, fill=(COL11[0], COL11[1], COL11[2]))

# COL12
SHAPE12 = [(0+SEP, H*11+SEP), (W+SEP, H*11+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE12, fill=(COL12[0], COL12[1], COL12[2]))

# COL13
SHAPE13 = [(0+SEP, H*12+SEP), (W+SEP, H*12+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE13, fill=(COL13[0], COL13[1], COL13[2]))

# COL14
SHAPE14 = [(0+SEP, H*13+SEP), (W+SEP, H*13+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE14, fill=(COL14[0], COL14[1], COL14[2]))

# COL15
SHAPE15 = [(0+SEP, H*14+SEP), (W+SEP, H*14+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE15, fill=(COL15[0], COL15[1], COL15[2]))

# COL16
SHAPE16 = [(0+SEP, H*15+SEP), (W+SEP, H*15+H+SEP)]
fig6 = ImageDraw.Draw(image)
fig6.rectangle(SHAPE16, fill=(COL16[0], COL16[1], COL16[2]))

# Output
if xres is True:
    print("col00", HEX00)
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
    print("col13", HEX13)
    print("col14", HEX14)
    print("col15", HEX15)
    print("col16", HEX16)

# Generate the image
IMAGE='night.png'
image.save(IMAGE)

PS=str("ps -ef | grep -v grep | grep 'mupdf' ")
FL=str("| grep -o '" + IMAGE + "' > /dev/null")
CHECK=os.system(PS+FL)

if shot is True:
    if CHECK == 256:
        os.system("mupdf '" + IMAGE + "' 2>/dev/null &")
    else:
        os.system("pkill -HUP mupdf 2>/dev/null")
