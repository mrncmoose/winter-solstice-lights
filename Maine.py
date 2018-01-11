#!/usr/bin/python 
'''
Created on Dec 20, 2017
A collection of light patterns on 4 lamp posts with 5 LED's in each
@author: moose
'''
import LED_controller
import time
import random

leds = ['red', 'blue', 'green', 'white', 'yellow']

lamp1 = LED_controller.ledLamp( 1, {
        "red":2,    #pin 13
        "blue":3,   #pin 15
        "green":4,  #pin 16
        "white":5,  #pin 18
        "yellow":6  #pin 22
    })
#TODO:  confirm GPIO numbers
# is this done???
lamp2 = LED_controller.ledLamp( 2, {
        "red":7, #pin 24
        "blue":8, # pin 26
        "green":9, #pin 21
        "white":10, #pin 19
        "yellow":11 # pin 23
    })
 
lamp3 = LED_controller.ledLamp( 3, {
        "red":12, #pin 12
        "blue":13, # pin 33
        "green":14, #pin 8
        "white":15, #pin 10
        "yellow":16 #pin 36
    })
 
lamp4 = LED_controller.ledLamp( 4, {
        "red":17, # pin 11
        "blue":18, # pin 18
        "green":19, # pin 35
        "white":20, # pin 38
        "yellow":21 # pin 40
    })

def rotateAllLamps(onTime, offTime):
    for color in leds:
        lamp1.ledOn(color)
        lamp2.ledOn(color)
        lamp3.ledOn(color)
#        lamp4.ledOn(color)
        time.sleep(onTime)
        lamp1.ledOff(color)
        lamp2.ledOff(color)
        lamp3.ledOff(color)
#        lamp4.ledOff(color)
        time.sleep(offTime)

def randomOnAllLamps(nTimes, onTime, offTime):
    print "Random led on each lamp"
    for i in range(1, nTimes):
        j = random.randrange(1, len(leds), 1)
        print "Random color: {0}".format(leds[j])
        lamp1.ledOn(leds[j])
        lamp2.ledOn(leds[j])
        lamp3.ledOn(leds[j])
#        lamp4.ledOn(leds[j])
        time.sleep(onTime)
        lamp1.ledOff(leds[j])
        lamp2.ledOff(leds[j])
        lamp3.ledOff(leds[j])
#        lamp4.ledOff(leds[j])
        time.sleep(offTime)

def rotateEach(onTime, offTime, nRotations):
    print "Lamp 1"
    lamp1.rotateLeds(onTime, offTime, nRotations)
    print "Lamp 2"
    lamp2.rotateLeds(onTime, offTime, nRotations)
    print "Lamp 3"
    lamp3.rotateLeds(onTime, offTime, nRotations)
    print "Lamp 3"
#    lamp4.rotateLeds(onTime, offTime, nRotations)
    
nRotations = 50
longOnTime = .25
shortOnTime = 0.1
longPauseTime = 0.1
shortPauseTime = 0.01

while(True):
    # Strobe all
    print "Strobing all leds"
    for i in range(1, nRotations):
        lamp1.allOn()
        lamp2.allOn()
        lamp3.allOn()
        time.sleep(shortOnTime)
        lamp1.allOff()
        lamp2.allOff()
        lamp3.allOff()
        time.sleep(shortPauseTime)
    
    #Turn on all of the same color in each lamp
    print "Random color"
    randomOnAllLamps(nRotations, longOnTime, shortPauseTime)
            
    # rotate down the line
    rotateEach(longOnTime, shortPauseTime, nRotations)
        
    # rotate all lamps quickly
    print "Rotating all quickly"
    for i in range(1, nRotations):
        rotateAllLamps(shortOnTime, shortPauseTime)
    
    # rotate slowly
    print "Rotating all slowly"
    for j in range(1, nRotations):
        rotateAllLamps(5, longPauseTime)
      
    # another rotate down the line.
    rotateEach(shortOnTime, shortPauseTime, nRotations)  
    
    #Turn on all of the same color in each lamp
    print "Random color"
    randomOnAllLamps(nRotations, longOnTime, shortPauseTime)
    
    print "Rotating all quickly"
    for i in range(1, nRotations):
        rotateAllLamps(shortOnTime, shortPauseTime)
    
    # Strobe all
    print "Strobing all leds"
    for i in range(1, nRotations):
        lamp1.allOn()
        lamp2.allOn()
        lamp3.allOn()
        time.sleep(shortOnTime)
        lamp1.allOff()
        lamp2.allOff()
        lamp3.allOff()
        time.sleep(shortPauseTime)
        
    # another rotate down the line.
    rotateEach(shortOnTime, shortPauseTime, nRotations)  
    
    #Turn on all of the same color in each lamp
    print "Random color"
    randomOnAllLamps(nRotations, longOnTime, shortPauseTime)
    
    print "Rotating all quickly"
    for i in range(1, nRotations):
        rotateAllLamps(shortOnTime, shortPauseTime)
