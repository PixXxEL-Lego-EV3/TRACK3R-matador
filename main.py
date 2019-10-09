#!/usr/bin/env python3
import logging
import os

from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.button import Button
from ev3dev2.led import Leds
from time import sleep

# Add logging
os.system('setfont Lat15-TerminusBold14')
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Connect ultrasonic and touch sensors to any sensor port
ir = InfraredSensor(INPUT_4)
btn = Button()
leds = Leds()

# Code
print("Starting MATADOR")

leds.all_off() # stop the LEDs flashing (as well as turn them off)

while not btn.any():
    print("Distance:" + str(ir.proximity*1.4) + "cm") # to print distance
    if ir.proximity < 40*1.4: # to detect objects closer than 40cm
        # In the above line you can also use inches: us.distance_inches < 16
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
    else:
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')
    sleep (0.01) # Give the CPU a rest

log.info("Finishing MATADOR")