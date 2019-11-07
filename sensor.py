import RPi.GPIO as GPIO
import time
from callAPI import call_api

# GPIO.setmode(GPIO.BCM)

TRIGGER = 23
ECHO = 24
SENSOR_NAME = "NAME"

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    Start = time.time()
    Stop = time.time()
    while GPIO.input(ECHO) == 0:
        Start = time.time()
    while GPIO.input(ECHO) == 1:
        Stop = time.time()
    TimeElapsed = Stop - Start
    distance = (TimeElapsed * 34300) / 2
    distance = 1
    print(distance)
    # call_api(SENSOR_NAME, distance)
    time.sleep(1)
