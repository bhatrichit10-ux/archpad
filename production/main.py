import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap
from kmk.extensions.neopixel import NeoPixel

keyboard = KMKKeyboard()

# Macros module
macros = Macros()
keyboard.modules.append(macros)

# 6 switches, GPIO -> GND
keyboard.matrix = KeysScanner(
    pins=[
        board.GP3,   # SW1
        board.GP4,   # SW2
        board.GP2,   # SW3
        board.GP1,   # SW4
        board.GP26,  # SW5
        board.GP27,  # SW6
    ],
    value_when_pressed=False,
)

# Macros
ARCH_BTW = KC.MACRO(
    Tap(KC.I), Tap(KC.SPACE),
    Tap(KC.U), Tap(KC.SPACE),
    Tap(KC.A), Tap(KC.R), Tap(KC.C), Tap(KC.H), Tap(KC.SPACE),
    Tap(KC.B), Tap(KC.T), Tap(KC.W),
)

SAVE_AS = KC.LCTL(KC.LSFT(KC.S))
PASTE = KC.LCTL(KC.V)

# Vim exit: Esc : w q Enter
VIM_EXIT = KC.MACRO(
    Tap(KC.ESC),
    Tap(KC.COLON),
    Tap(KC.W),
    Tap(KC.Q),
    Tap(KC.ENTER),
)

TERMINAL = KC.LCTL(KC.LALT(KC.T))

HALO = KC.MACRO(
    Tap(KC.A), Tap(KC.M), Tap(KC.E), Tap(KC.R), Tap(KC.I),
    Tap(KC.C), Tap(KC.A), Tap(KC.Y), Tap(KC.A),
    Tap(KC.SPACE),
    Tap(KC.H), Tap(KC.A), Tap(KC.L), Tap(KC.O),
    Tap(KC.EXCLAMATION),
)

# Keymap order = SW1 → SW6
keyboard.keymap = [[
    ARCH_BTW,   # SW1
    SAVE_AS,    # SW2
    PASTE,      # SW3
    VIM_EXIT,   # SW4
    TERMINAL,   # SW5
    HALO,       # SW6
]]

# NeoPixel
neopixel = NeoPixel(
    pin=board.GP28,
    num_pixels=1,
    brightness=0.3,
)

keyboard.extensions.append(neopixel)

keyboard.go()
