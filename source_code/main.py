
# Keyboard Project for discord RPC
# Have your discord status tell everyone
# what keys you are typing!
# October 16th 2021 (Started Late night October 15th 2021)

import threading
import json
import os
import sys
import datetime
from time import sleep, time

from pynput.keyboard import Key, Listener
from pypresence import Presence

#
# > Defining Vars
#

global ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# This is the clientid of the discord app.
global clientid
clientid = 898771124177997875  # I hate hardcoding but this is a constant. 

# This is the list of characters that can't 
# or shouldn't be in filenames. (Ones that discord doesn't like in image lable names too.)
global illegal_chars
illegal_chars = { "\\": "backslash",  "/": "slash", ":": "colon",  
    "*": "asteriks",  "?": "question",  "\"": "quote",  "<": "greater",  ">": "lesser",  "|": "pipe", "$": "dollar", ")": "closeP", "(": "openP", "{": "openCB", "}": "closeCB", "+": "plus",
    ",": "comma", "=": "equals", "&": "and", "%": "percent", "@": "at", ".": "dot", "^": "upp", ";": "semicolon", "[": "openB", "]": "closeB", "!": "exclaim", "`": "tick", "~": "tild", "#": "hash" }

# Possible Keys that can be pressed.
# This list was collected by pressing
# Every key on my keyboard.
global possible_keys
possible_keys = ['Key.media_play_pause', 'Key.enter', 'Key.cmd', 'Key.ctrl_l', 'Key.alt_l', 'Key.space', 'Key.alt_gr', 'Key.menu', 'Key.ctrl_r', 'Key.shift', "'z'", "'x'", "'c'", "'v'", "'b'", "'n'", "'m'", "','", "'.'", "'/'", 'Key.shift_r', 'Key.caps_lock', "'a'", "'s'", "'d'", "'f'", "'g'", "'h'", "'j'", "'k'", "'l'", "';'", '"\'"', 'Key.tab', "'q'", "'w'", "'e'", "'r'", "'t'", "'y'", "'u'", "'i'", "'o'", "'p'", "'['", "']'", "'\\\\'", "'`'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'0'", "'-'", "'='", 'Key.backspace', 'Key.f1', 'Key.f2', 'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f12', 'Key.print_screen', 'Key.scroll_lock', 'Key.pause', "'~'", "'!'", "'@'", 
"'#'", "'$'", "'%'", "'^'", "'&'", "'*'", "'('", "')'", "'_'", "'+'", "'Q'", "'W'", "'E'", "'R'", "'T'", "'Y'", "'U'", "'I'", "'O'", "'P'", "'{'", "'}'", "'|'", "'A'", "'S'", "'D'", "'F'", "'G'", "'H'", "'J'", "'K'", "'L'", "':'", '\'"\'', "'Z'", "'X'", "'C'", "'V'", "'B'", "'N'", "'M'", "'<'", "'>'", "'?'", 'Key.up', 'Key.down', 'Key.right', 'Key.left', 'Key.insert', 'Key.home', 'Key.page_up', 'Key.page_down', 'Key.end', 'Key.delete', '<12>', 'Key.num_lock', 
'<103>', '<100>', '<97>', '<99>', '<98>', '<102>', '<101>', '<104>', '<105>', '<96>', '<110>', 'Key.media_next', 'Key.media_play_pause', 'Key.media_previous', 'Key.media_volume_mute', 'Key.media_volume_up', 'Key.media_volume_down', 
'Key.esc']

global keypresses 
keypresses = {}

global session_keypresses
session_keypresses = {}

global keypress
keypress = ""

global last_keypress
last_keypress = ""

global session_tkeypresses
session_tkeypresses = 0

global lifetime_tkeypresses
lifetime_tkeypresses = 0

# -- More Vars (Status Vars)
global details
details = "Typing... "
global state
state = "default"
global start_time
start_time = time()


# -- Beginning RPC Vars
RPC = Presence(client_id=clientid)
RPC.connect()


# ----- End Vars.


#
# > Functions 
#

def update_status():
    print(get_label(keypress))

    if state == "default":
        ss = f"The {keypress} key."
    else:
        ss = state

    RPC.update(
        details="Typing...",
        state=ss,
        large_image=get_label(keypress),
        large_text = f"Current Key: {keypress} Key.",
        small_image = get_label(last_keypress),
        small_text= f"Previous Key: {last_keypress} Key.",
        start = start_time
    )


def strip_key(key):
    # Key.backspace will return backspace
    # "'s'" will return s and so and so.
    nkey = str(key).strip("'")
    nkey = str(nkey).removeprefix("Key.")

    return nkey

# This function returns the label name based on the rules I generated them for the 
# RPC. 
def get_label(key):
    s = strip_key(key)
    if s in illegal_chars:
        return f"{illegal_chars[s]}key"
    if s.islower() and len(s) == 1:
        return f"lower{s}key"
    return f"{s.lower()}key"

# -- Key Specific Functions
def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    # We need to
    # Update key
    global keypress              #
    global last_keypress         #
    global session_tkeypresses   #
    global session_keypresses    #
    global keypresses            #
    global lifetime_tkeypresses  #

    nkey = strip_key(key)

    # Updating the 2 vars, keypress and last_keypress.
    last_keypress = keypress
    keypress = nkey

    # Updating Counter
    session_tkeypresses += 1
    lifetime_tkeypresses += 1

    # Updating Dict. 
    if str(nkey) not in session_keypresses:
        session_keypresses[str(nkey)] = 0
    if str(nkey) not in keypresses:
        keypresses[str(nkey)] = 0

    session_keypresses[str(nkey)] += 1
    keypresses[str(nkey)] += 1

    pass

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        return False

def listen():
    with Listener (on_press=on_press) as listener:
        listener.join()

# -- Console Function
# This function is to be written to produce a command menu
# and to allow the users of the program to interact with it. 
# I'm using a text console because I'm too lazy to make
# a GUI with tkinter. 
#
# Want to see what I can do with a gui? github.com/Grubbsy1896/encounter 
# (Old work of mine I can definitely improve though.)
#
# - INCOMPLETE FUNCTION - 
def console():
    running = True
    while running:
        inp = input("Waiting For Command: ")
        print(inp)
        if str(inp) == "1":
            print("Hello.")
        if str(inp) == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        if str(inp) == "stats": 
            print(keypresses)
        if str(inp) == "stop":
            running = False

# -- Data Functions
def load_keypresses():
    global lifetime_tkeypresses
    global keypresses
    with open(f"{ROOT_DIR}/data.json", 'r') as datafile:
        kys = json.load(datafile)

        if kys == {} or len(kys) < 1:
            kys['total_keypresses'] = 0
            pass # This is where I'll put in default variables I wish to store. 

        keypresses = kys
        lifetime_tkeypresses = keypresses['total_keypresses']
        return kys

def save_keypresses():
    global keypresses
    global lifetime_tkeypresses
    keypresses['total_keypresses'] = lifetime_tkeypresses
    with open(f"{ROOT_DIR}/data.json", 'w') as datafile:
        json.dump(keypresses, datafile, indent=4)

# -- Looping Functions
def looping():
    while True:
        sleep(15)
        try:
            update_status()
        except:
            print("Error Updating Status. Discord is not responding. (You may want to check your internet connection)")
        try:
            save_keypresses()
        except:
            print("Error Saving Data. The file may have corrupt.")

# ----- End Functions 




# Executing

load_keypresses()

# Starting Threads

threading.Thread(target=listen).start()
threading.Thread(target=console).start()
threading.Thread(target=looping).start()
