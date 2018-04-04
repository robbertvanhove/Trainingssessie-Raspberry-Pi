 LED high   /home/pi
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def blink(pin):
	GPIO.output(pin, 1)
	time.sleep(0.5)
	GPIO.output(pin, 0)
while 1:
	
	blink(18)
	blink(17)
	blink(23)
	blink(22)