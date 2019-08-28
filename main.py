#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font
    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def main():
    '''The main function of our program'''
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('PixXxeL matadar de robo lixo!')
    sound = Sound()
    sound.speak('EH HORA DO SHOOOOOOOOOULW... PORRA')
    sound.speak('BIIIIIIIIRRRRLL')

    # print something to the output panel in VS Code
    debug_print('Debug Console Output')


    tank_drive = MoveTank(OUTPUT_C, OUTPUT_B)

    # drive in a turn for 5 rotations of the outer motor
    # the first two parameters can be unit classes or percentages.
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

    # drive in a different turn for 3 seconds
    tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)

if __name__ == '__main__':
    main()