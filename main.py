#!/usr/bin/env python3
import os
import logging
from sys import stderr
from time import sleep
from threading import Thread, Semaphore

from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.button import Button
from ev3dev2.led import Leds
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor, MediumMotor, SpeedPercent, MoveSteering
from time import sleep

# Add logging
os.system('setfont Lat15-TerminusBold14')
logging.basicConfig(level=logging.DEBUG, format="%(lineno)s: %(message)s")
log = logging.getLogger(__name__)

# Connect ultrasonic and touch sensors to any sensor port
ir = InfraredSensor(INPUT_4)
btn = Button()
leds = Leds()

CHANNEL_OPPONENT = 2

tank_drive = MoveSteering(OUTPUT_C, OUTPUT_B)

# teste thread
sem = Semaphore()

# def move_forward():
#     tank_drive.on(0, SpeedPercent(60))
# def move_reverse():
#     tank_drive.on(0, SpeedPercent(-60))
# def move_right():
#     tank_drive.on(-100, SpeedPercent(-60))
# def move_left():
#     tank_drive.on(100, SpeedPercent(60))

# def move_square():
#     while True:
#         sem.acquire()
#         print("andando")
#         move_forward()
#         sleep(4.0)
#         move_right()
#         sleep(2.0)
#         sem.release()

def check_sensors():
    sem.acquire()
    while True:
        print("Distance:" + str(ir.proximity*1.4) + "cm")
        print("Distance:" + str(ir.proximity*1.4) + "cm", file=stderr)
    sem.release()

def corno_ahead():
    sem.acquire()
    # ir.mode = "IR-SEEK"
    head = ir.heading(CHANNEL_OPPONENT)
    dist = ir.distance(CHANNEL_OPPONENT)
    while True:
        print("Head: " + str(head) + " | Dist: " + str(dist))
        print("Head: " + str(head) + " | Dist: " + str(dist), file=stderr)
    sem.release()

# Code
print("MATADOR is online (vs)", file=stderr) # printa no pc
print("MATADOR is online")
t1 = Thread(target=corno_ahead)
t2 = Thread(target=check_sensors)

while not btn.any():
    sleep(0.01)

corno_ahead()

log.info("Finishing MATADOR")

# leds.all_off() # stop the LEDs flashing (as well as turn them off)

# while not btn.any():
#     print("Distance:" + str(ir.proximity*1.4) + "cm") # to print distance
#     if ir.proximity < 40*1.4: # to detect objects closer than 40cm
#         # In the above line you can also use inches: us.distance_inches < 16
#         leds.set_color('LEFT',  'RED')
#         leds.set_color('RIGHT', 'RED')
#     else:
#         leds.set_color('LEFT',  'GREEN')
#         leds.set_color('RIGHT', 'GREEN')
#     sleep (0.01) # Give the CPU a rest