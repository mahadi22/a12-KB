#Raspberry Pi PICO keyboard
#Library Setup
import board
import digitalio
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
from kmk.consts import UnicodeMode

#Keyboard Setup
a12KB = KMKKeyboard()
a12KB.debug_enabled = False #True/False, only enabled to debug error

#pi pico pinout are in here https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf
#vertical setup, 3x6 setup like numpad
a12KB.col_pins = (board.GP2, board.GP3, board.GP4)
a12KB.row_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)

#diode orientation, COLUMNS or ROWS
a12KB.diode_orientation = DiodeOrientation.COLUMNS

#Key Setup
xxxx = KC.NO  #no key
____ = KC.TRANSPARENT  #Transparent layer

#keycodes are listed in here https://github.com/KMKfw/kmk_firmware/blob/master/docs/keycodes.md
#3x6 matrix
a12KB.keymap = [
    [ #Default layer
        KC.TG(1),  KC.TG(2),  KC.TG(3),
        KC.PSLS,   KC.PAST,   KC.PMNS,
        KC.PPLS,   KC.P0,     KC.PENT,   
        KC.P7,     KC.P8,     KC.P9,
        KC.P4,     KC.P5,     KC.P6,
        KC.P1,     KC.P2,     KC.P3,
    ],
    [ #Soundpad layer
        KC.TG(0),  KC.TG(2),  KC.TG(3),
        KC.F13,    KC.F14,    KC.F15,
        KC.F16,    KC.F17,    KC.F18,
        KC.F19,    KC.F20,    KC.F21,
        KC.F22,    KC.F23,    KC.F24,
        KC.LALT(KC.F13),   KC.LALT(KC.F14),   KC.LALT(KC.F15)
    ],
    [ #MediaPlayer layer
        KC.TG(0),  KC.TG(1),  KC.TG(3),
        KC.MUTE,   KC.VOLU,   KC.VOLD,
        KC.MNXT,   KC.MPRV,   KC.MPLY,      
        KC.LCTL(KC.O), xxxx,  KC.MSTP,
        KC.LCTL,   KC.UP,     KC.LALT,
        KC.LEFT,   KC.DOWN,   KC.RIGHT,
    ],
    [ #Empty layer
        KC.TG(0),  KC.TG(1),  KC.TG(2),
        xxxx,      xxxx,      xxxx,
        xxxx,      xxxx,      xxxx,
        xxxx,      xxxx,      xxxx,
        xxxx,      xxxx,      xxxx,
        xxxx,      xxxx,      xxxx,
    ],
]

#marker for board ready, disable this after config done and working properly
#led = digitalio.DigitalInOut(board.GP25)
#led.direction = digitalio.Direction.OUTPUT
#led.value = True

if __name__ == '__main__':
    a12KB.go(hid_type=HIDModes.USB) #Wired USB enables
    raise Exception('Something has caused an error.') #error trap
        
try:
    usbfunc()
except Exception as e:
    import supervisor
    print(e)
    led.value = False
    supervisor.reload()

supervisor.reload()
#last ditch effort to reset the MCU, if this is being ran then something really is wrong
