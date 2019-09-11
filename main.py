#!/usr/bin/env python3

import sys
import logging

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor, MoveTank, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

channel = 1

tank_drive = MoveSteering(OUTPUT_C, OUTPUT_B)

shooter = MediumMotor(OUTPUT_A)
sensor = InfraredSensor(INPUT_4)

# Add logging
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Functions
def corno_ahead():
    head = sensor.heading(channel)
    dist = sensor.distance(channel)

    log.info("heading: ")
    log.info(head)
    log.info("distance: ")
    log.info(dist)

    if (dist is not None and dist < 50):
        if (head is not None and head > -5 and head < 5):
            shooter.on_for_rotations(SpeedPercent(100), 3)

def roda_roda_jequiti():
    tank_drive.on_for_rotations(-100, SpeedPercent(80), 1)

# Code
def main():
    log.info("Starting MATADOR")
    # shooter.reset()

    while True:
        roda_roda_jequiti()
        corno_ahead()
    
    log.info("Finishing MATADOR")

if __name__ == '__main__':
    main()
