'''
Created on Dec 17, 2017

@author: moose
'''

import RPi.GPIO as GPIO
import time


class ledLamp:
    "Holds the details for a given lamp with it's 5 LED's"
#     LampNumber=1
#     gpioLed = {
#         "red":2,
#         "blue":3,
#         "green":4,
#         "white":5,
#         "yellow":6
#     }
    
    def __init__(self, lampNum = 1, leds = {
        "red":2,
        "blue":3,
        "green":4,
        "white":5,
        "yellow":6
    }):
        self.LampNumber = lampNum
        self.gpioLed = leds
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for gpio in self.gpioLed.itervalues():
            GPIO.setup(gpio, GPIO.OUT)
        self.allOff()
    
    def allOn(self):
        for gpio in self.gpioLed:
#            print "Turning {0} on.".format(gpio)
            self.ledOn(gpio)

    def allOff(self):
        for gpio in self.gpioLed:
            self.ledOff(gpio)
    
    def ledOn(self, led):
        if led in self.gpioLed:
#            print "Turing on {0} led.".format(led)
            GPIO.output(self.gpioLed[led], GPIO.HIGH)
        else:
            print "Wrong LED to turn on bonehead! {0}".format(led)

    def ledOff(self, led):
        if led in self.gpioLed: 
            GPIO.output(self.gpioLed[led], GPIO.LOW)
        else:
            print "Wrong LED to turn off bonehead! {0}".format(led)

    def rotateLeds(self, timeOn, timeOff, nTimes):
        print("Rotating lights")
        for j in range(0, nTimes):
            for color in self.gpioLed:
                self.blink(color, timeOn)
                time.sleep(timeOff)  
        
    def blink(self, color, timeOn):
        self.ledOn(color)
        time.sleep(timeOn)
        self.ledOff(color)