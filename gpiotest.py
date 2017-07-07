"""
This script is made for the purpose of testing the GPIO
pins on a Raspberry Pi 3 Model B.
"""

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. \
        You can achieve this by using 'sudo' to run your script")

import time

GPIO.setmode(GPIO.BCM)

def write(channel, state):
    """This function sets a GPIO pin to a specified state."""
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, state)

def read(channel):
    """This function returns the state of a specified GPIO pin."""
    GPIO.setup(channel, GPIO.IN)
    return GPIO.input(channel)

try:
    while True:
        write(18, GPIO.HIGH)
        time.sleep(0.5)
        write(18, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
