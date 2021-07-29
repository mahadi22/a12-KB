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
#a12KB.tap_time = 750
#a12KB.pixel_pin = board.GP15
#a12KB.num_pixels = 3

#a12KB.rgb_config['pixel_pin'] = board.GP15
#a12KB.rgb_config['num_pixels'] = 3
#a12KB.rgb_config['rgb_order'] = (1, 0, 2)

#a12KB.rgb_config['hue_step'] = 10
#a12KB.rgb_config['sat_step'] = 17
#a12KB.rgb_config['val_step'] = 17
#a12KB.rgb_config['hue_default'] = 100
#a12KB.rgb_config['sat_default'] = 102
#a12KB.rgb_config['val_default'] = 102
#a12KB.rgb_config['val_limit'] = 255

#a12KB.rgb_config['knight_effect_length'] = 2
#a12KB.rgb_config['animation_mode'] = 'static'
#a12KB.rgb_config['animation_speed'] = 1

#pi pico pinout are in here https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf
a12KB.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
a12KB.row_pins = (board.GP8, board.GP9, board.GP10)

#diode orientation, COLUMNS or ROWS
a12KB.diode_orientation = DiodeOrientation.COLUMNS


#Key Setup
xxxx = KC.NO  #no key
____ = KC.TRANSPARENT  #Transparent layer

num00 = send_string("00")

#keycodes are listed in here https://github.com/KMKfw/kmk_firmware/blob/master/docs/keycodes.md
#6x3 matrix
a12KB.keymap = [
    #[ #Default layer
    #    KC.TG(1),   KC.BSPC,  KC.P0,     KC.P1,     KC.P4,     KC.P7,
    #    KC.TG(2),   KC.DEL,   num00,     KC.P2,     KC.P5,     KC.P8,
    #    KC.TG(3),   KC.PENT,  KC.PDOT,   KC.P3,     KC.P6,     KC.P9,
    #],
    #[ #MediaPlayer Layer
    #    KC.MUTE,   KC.VOLU,   KC.VOLD,   xxxx,      KC.UP,     KC.DOWN,
    #    KC.TAB,    KC.S,      KC.O,      KC.C,      KC.V,      KC.W,
    #    KC.LCTL,   KC.LGUI,   KC.LALT,   KC.SPC,    KC.TG(0),  KC.TG(2),
    #],
    #[ #Misc1 Layer
    #    KC.MUTE,   KC.VOLU,   KC.VOLD,   xxxx,      KC.UP,     xxxx,
    #    KC.MNXT,   KC.MPRV,   KC.MPLY,   KC.LEFT,   KC.DOWN,   KC.RIGHT,
    #    ____,      ____,      ____,      KC.TG(0),  KC.TG(1),  KC.TG(3),
    #],
    #[ #Misc2 Layer
    #    KC.UC_MODE_NOOP,      KC.UC_MODE_LINUX,      KC.UC_MODE_MACOS,      KC.UC_MODE_WINC,      xxxx,      xxxx,
    #    xxxx,      xxxx,      xxxx,      xxxx,      xxxx,      xxxx,
    #    ____,      ____,      ____,      KC.TG(0),  KC.TG(1),  KC.TG(2),
    #],
    [  #Soundpad Layer
        KC.F13,   KC.F14,   KC.F15,   KC.F16,   KC.F17,   KC.F18,
        KC.F19,   KC.F20,   KC.F21,   KC.F22,   KC.F23,   KC.F24,
        KC.LALT(KC.F13),   KC.LALT(KC.F13),   KC.LALT(KC.F13),   KC.LALT(KC.F13),   KC.LALT(KC.F13),   KC.LALT(KC.F13), #Combi LeftAlt+Fxx
    ],
]

#marker for board ready, disable this after config done and working properly
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True

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