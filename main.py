#!/usr/bin/env python3

import sys
import logging

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor, MoveTank, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

shooter = MediumMotor(OUTPUT_A)

# Add logging
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Functions
def shoot_ball():
    shooter.on_for_rotations(SpeedPercent(100), 2)

# Code
if __name__ == '__main__':
    main()

def main():
    log.info("Starting TRACK3RWithBallShooter")
    shooter.reset()
    shoot_ball()
    log.info("Finishing TRACK3RWithBallShooter")
