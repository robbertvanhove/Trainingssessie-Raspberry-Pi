# blink LED   /home/pi
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)  

while true:
 GPIO.setup(18, GPIO.OUT)
 GPIO.output(18, 1)
 time.sleep(0.5)
 GPIO.output(18,0)
 time.sleep(0.5)


