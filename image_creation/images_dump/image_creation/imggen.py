
#
# Imggen.py for Keyboard
# Generating images for my discord RPC. 
# 
# Made on October 16th 2021
#
# Purpose is to generate an image for every key
# Manually making 134 images is too much work. 
# So I streamlined it in just a few lines of code. 
# I can tinker and edit every image with ease. 



import os
import sys
from PIL import Image, ImageDraw, ImageFont

keys = ['Key.media_play_pause', 'Key.enter', 'Key.cmd', 'Key.ctrl_l', 'Key.alt_l', 'Key.space', 'Key.alt_gr', 'Key.menu', 'Key.ctrl_r', 'Key.shift', "'z'", "'x'", "'c'", "'v'", "'b'", "'n'", "'m'", "','", "'.'", "'/'", 'Key.shift_r', 'Key.caps_lock', "'a'", "'s'", "'d'", "'f'", "'g'", "'h'", "'j'", "'k'", "'l'", "';'", '"\'"', 'Key.tab', "'q'", "'w'", "'e'", "'r'", "'t'", "'y'", "'u'", "'i'", "'o'", "'p'", "'['", "']'", "'\\\\'", "'`'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'0'", "'-'", "'='", 'Key.backspace', 'Key.f1', 'Key.f2', 'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f12', 'Key.print_screen', 'Key.scroll_lock', 'Key.pause', "'~'", "'!'", "'@'", 
"'#'", "'$'", "'%'", "'^'", "'&'", "'*'", "'('", "')'", "'_'", "'+'", "'Q'", "'W'", "'E'", "'R'", "'T'", "'Y'", "'U'", "'I'", "'O'", "'P'", "'{'", "'}'", "'|'", "'A'", "'S'", "'D'", "'F'", "'G'", "'H'", "'J'", "'K'", "'L'", "':'", '\'"\'', "'Z'", "'X'", "'C'", "'V'", "'B'", "'N'", "'M'", "'<'", "'>'", "'?'", 'Key.up', 'Key.down', 'Key.right', 'Key.left', 'Key.insert', 'Key.home', 'Key.page_up', 'Key.page_down', 'Key.end', 'Key.delete', '<12>', 'Key.num_lock', 
'<103>', '<100>', '<97>', '<99>', '<98>', '<102>', '<101>', '<104>', '<105>', '<96>', '<110>', 'Key.media_next', 'Key.media_play_pause', 'Key.media_previous', 'Key.media_volume_mute', 'Key.media_volume_up', 'Key.media_volume_down', 
'Key.esc']

illegal_chars = {
    "\\": "backslash", 
    "/": "slash", 
    ":": "colon", 
    "*": "asteriks", 
    "?": "question", 
    "\"": "quote", 
    "<": "greater", 
    ">": "lesser", 
    "|": "pipe",
    "$": "dollar",
    ")": "closeP",
    "(": "openP",
    "{": "openCB",
    "}": "closeCB",
    "+": "plus",
    ",": "comma",
    "=": "equals",
    "&": "and",
    "%": "percent",
    "@": "at",
    ".": "dot",
    "^": "upp",
    ";": "semicolon",
    "[": "openB",
    "]": "closeB",
    "!": "exclaim",
    "`": "tick",
    "~": "tild",
    "#": "hash"
}

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Testing


global pathf
pathf = f"{ROOT_DIR}/image_dump/"




i = 0
for key in keys:
    k = str(key).strip("'")
    if len(k) == 1 and (i < 5):
        image = Image.new(mode = "RGB", size = (512, 512), color=(0,0,0))
        myFont = ImageFont.truetype(f'{ROOT_DIR}PressStart2P-vaV7.ttf', 512)
        d1 = ImageDraw.Draw(image)
        d1.text((32-5, 32+5), k, font=myFont, fill =(0, 0, 255))
        d1.text((32, 32), k, font=myFont, fill =(255, 0, 0))
        if k not in illegal_chars:
            if str(k).islower():
                image.save(f"{pathf}lower{k}key.png")
        else:
            image.save(f"{pathf}{illegal_chars[k]}key.png")
        # i+=1

i = 0 
for key in keys:
    
    if key.startswith("Key.") and i < 5:
        # Defining
        k = str(key).removeprefix("Key.")
        image = Image.new(mode = "RGB", size = (512, 512), color=(0,0,0))
        d1 = ImageDraw.Draw(image)
        

        # Calculating Offsets

        sizeOffset = int(512/(len(k)+1))

        xOffset  = 32  #*len(k)  #// I don't think I should start it any different tbh.
        yOffset  = 256-sizeOffset#*len(k)
        #
        # Drawing
        #

        myFont = ImageFont.truetype('C:\\Users\\mwt13\\AppData\\Local\\Microsoft\\Windows\\Fonts\\PressStart2P-vaV7.ttf', sizeOffset  )

        d1.text((xOffset-5, yOffset+5), k, font=myFont, fill =(0, 0, 255)) # Shadow/Behind Text
        d1.text((xOffset  , yOffset  ), k, font=myFont, fill =(255, 0, 0))     # Front Part of the text. 
        if k not in illegal_chars:
            image.save(f"{pathf}{k}key.png")
        else:
            image.save(f"{pathf}{illegal_chars[k]}key.png")
#         # i+=1