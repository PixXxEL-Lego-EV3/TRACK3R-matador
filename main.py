#!/usr/bin/env python3

import sys
import logging

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor, MoveTank, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

CHANNEL_OPPONENT = 1

shooter = MediumMotor(OUTPUT_A)
sensor = InfraredSensor(INPUT_4)
tank_drive = MoveSteering(OUTPUT_C, OUTPUT_B)

# Add logging
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Functions
def shoot_ball():
    shooter.on_for_rotations(SpeedPercent(100), 3)

# testar
def shoot_ball_forever():
    shooter.on(SpeedPercent(100))
    # ou
    # shooter.run_forever()

# testar
def stop_shooting():
    log.info("Stop shooting")
    shooter.stop()

def spin_matador(turns):
    log.info("Spinning robot")
    tank_drive.on_for_rotations(-100, SpeedPercent(80), turns)

# testar
def spin_matador_forever():
    log.info("Spinning robot forever")
    tank_drive.on(-100, SpeedPercent(80))

# testar
def stop_spinning():
    tank_drive.off()

def corno_ahead():
    head = sensor.heading(CHANNEL_OPPONENT)
    dist = sensor.distance(CHANNEL_OPPONENT)

    if (dist is not None and dist < 50):
        if (head is not None and head > -5 and head < 5):
            return True
    
    return False

# Code
def main():
    log.info("Starting MATADOR")

    # while True:
    #     spin_matador()
    #     corno_ahead()

    # testar
    while True:
        if corno_ahead():
            stop_spinning()
            shoot_ball_forever()
        else:
            stop_shooting()
            spin_matador_forever()
    
    log.info("Finishing MATADOR")

if __name__ == '__main__':
    main()

# Utilidades
# shooter.reset()
# log.info("Heading: " + head) # testar