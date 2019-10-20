#!/usr/bin/env python3

import sys
import logging

from time import sleep
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor, MoveTank, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button

CHANNEL_OPPONENT = 2

canRun = False

shooter = MediumMotor(OUTPUT_A)
sensor = InfraredSensor(INPUT_4)
sensor.mode = "IR-SEEK"
tank_drive = MoveSteering(OUTPUT_C, OUTPUT_B)
btn = Button()

# Add logging
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Functions
def shoot_ball():
    shooter.on_for_rotations(SpeedPercent(100), 3)

# testar
def shoot_ball_forever():
    shooter.on(SpeedPercent(100))

# Para de atirar
def stop_shooting():
    log.info("Stop shooting")
    shooter.stop()

# Roda n vezes
def spin_matador(turns):
    log.info("Spinning robot")
    tank_drive.on_for_rotations(-100, SpeedPercent(80), turns)


def run_matador_seconds(seconds):
    tank_drive.on_for_seconds(0, SpeedPercent(50), seconds)


def spin_matador_degrees_right(degrees):
    tank_drive.on_for_degrees(-100, SpeedPercent(60), degrees)

def spin_matador_degrees_left(degrees):
    tank_drive.on_for_degrees(100, SpeedPercent(60), degrees)

def spin_matador_forever():
    log.info("Spinning robot forever")
    tank_drive.on(-100, SpeedPercent(60))

# testar


def stop_spinning():
    log.info("Stop spinning")
    tank_drive.off()


def corno_ahead():
    head = sensor.heading(CHANNEL_OPPONENT)
    dist = sensor.distance(CHANNEL_OPPONENT)

    if (dist is not None and dist < 70):
        if (head is not None and head > -3 and head < 3):
            return True

    return False

# Code
print("Starting MATADOR")

while not btn.any():
    sleep(0.01)

cont = 0
while(cont < 8):
    if not corno_ahead():
        run_matador_seconds(1)
        if corno_ahead():
            shoot_ball()
    else:
        shoot_ball()
    cont += cont + 1
    
# run_matador_seconds(7*2)
spin_matador_degrees_left(300)

cont = 0
while(cont < 5):
    if not corno_ahead():
        run_matador_seconds(1)
        if corno_ahead():
            shoot_ball()
    else:
        shoot_ball()
    cont += cont + 1

# run_matador_seconds(5)

while True:
    log.info("Distancia: " + str(sensor.value(CHANNEL_OPPONENT)))

    if corno_ahead():
        stop_spinning()
        shoot_ball()
    else:
        stop_shooting()
        spin_matador_forever()

log.info("Finishing MATADOR")

# Utilidades
# shooter.reset()
# log.info("Heading: " + head) # testar
