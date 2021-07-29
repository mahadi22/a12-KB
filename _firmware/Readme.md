## ⚠️Note:                         
*Use it on your own risk, i'm not responsible for anything wrong that will happen to your RPI Pico for using this script/firmware. If its bricked but bootloader still accessible, you can use FlashNuke.uf2 to reflash your Pico*


# Firmware

1. Circuit Python for Pi PICO can be downloaded from [Here](https://circuitpython.org/board/raspberry_pi_pico/).  
Additional Library for circuitpython can be downloaded from [Here](https://circuitpython.org/libraries).

2. KMK Firmware
    * PreCompiled can be downloaded from [Here](https://cdn.kmkfw.io/kmk-latest.zip);
    * Raw and editable can be downloaded from [here](https://cdn.kmkfw.io/kmk-latest.unoptimized.zip). 

***

Step to upload CircuitPython Bootloader into RPi Pico
1. Press and hold Bootloader button on Pico, connect usb to pico to enter Bootloader Mode, release the button after pico connected,
2. Open windows explorer, open RPI-RP2 Drive, copy and paste/drop circuitpython-xxxxxx.uf2 to pico drive. Pico will restart automatically to boot circuitpython.

Loading KMK Firmware to RPi Pico
1. Connect usb to Pi Pico,
2. Open CircuitPython Drive on windows explorer, copy and paste/extract the content of [a12-KB_FW.zip](./a12-KB_FW.zip) to pico drive. Pico will restart automatically to load kmk firmware,
3. To configure the keypad/keyboard, open/edit main.py with notepad and edit the keymap. Keycodes can be look in [Here](https://github.com/KMKfw/kmk_firmware/blob/master/docs/keycodes.md)




## Special Case
Reset RPi Pico (if bricked/running rogue code and not accessible)
1. Press and hold Bootloader button on Pico, connect usb to pico to enter Bootloader Mode, release the button after pico connected,
2. Open windows explorer, open RPI-RP2 Drive, copy and paste/drop [flash_nuke.uf2](https://github.com/mahadi22/a12-KB/raw/main/_firmware/flash_nuke.uf2) to pico drive. Pico will restart automatically with empty drive,
3. Reflash Pico with circuitpython / micropython.
