import RPi.GPIO as GPIO

from tkinter import *
import tkinter.font

from gpiozero import LED

import time
import math

GPIO.setmode(GPIO.BCM)

led0 = LED(7)
led1 = LED(8)
led2 = LED(25)
led3 = LED(23)
led4 = LED(24)
led5 = LED(18)
led6 = LED(15)
led7 = LED(14)

#leds = [led7, led6, led5, led4, led3, led2, led1, led0]

textInput = input("How many blinkies? Type \"1\" for every blink. ")

try:
    for i in str(textInput):
        led0.on()
        time.sleep(1)
        led0.off()
        time.sleep(1)

        led1.on()
        time.sleep(1)
        led1.off()
        time.sleep(1)

        led2.on()
        time.sleep(1)
        led2.off()
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
