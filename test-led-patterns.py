import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#guessing at which LED is what color on which GPIO pin.
redLED=2
blueLED=3
greenLED=4
whiteLED=5
yellowLED=6

leds = ['red', 'blue', 'green', 'white', 'yellow']
gpios = [3, 6, 4, 2, 5]

onTime=0.2
offTime=0.1

GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(whiteLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)

#flash all on/off
for i in range(1,10):
	GPIO.output(redLED, GPIO.HIGH)
	GPIO.output(blueLED, GPIO.HIGH)
	GPIO.output(greenLED, GPIO.HIGH)
	GPIO.output(whiteLED, GPIO.HIGH)
	GPIO.output(yellowLED, GPIO.HIGH)
	time.sleep(onTime)
	GPIO.output(redLED, GPIO.LOW)
	GPIO.output(blueLED, GPIO.LOW)
	GPIO.output(greenLED, GPIO.LOW)
	GPIO.output(whiteLED, GPIO.LOW)
	GPIO.output(yellowLED, GPIO.LOW)
	time.sleep(offTime)

print "Rotating colors"
#rotate colors
onTime=0.05
offTime=0.02
for j in range(1, 20):
	for led, gpio in zip(leds, gpios):
#		print '{0} on gpio {1} on?'.format(led, gpio)
		GPIO.output(gpio, GPIO.HIGH)
		time.sleep(onTime)
		GPIO.output(gpio, GPIO.LOW)
		time.sleep(offTime) 

print "Random"
# turn on in random order & time.
for k in range(1,10):
	ledOnNum = random.randrange(1, 5, 1)
	print "Turning on GPIO: ", ledOnNum
	ledOn = gpios[ledOnNum]
	onTime = random.randrange(1,4,1)
	print "Duration of: ", onTime
	GPIO.output(ledOn, GPIO.HIGH)
	time.sleep(onTime)
	GPIO.output(ledOn, GPIO.LOW)
	time.sleep(offTime)