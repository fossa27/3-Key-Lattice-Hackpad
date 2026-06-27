import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.col_pins = ()
keyboard.row_pins = (10, 9, 8)

keyboard.keymap = [
    [
        KC.LGUI(KC.C),
        KC.LGUI(KC.V),
        KC.LGUI(KC.Z), 
    ]
]

if __name__ == '__main__':
    keyboard.go()
