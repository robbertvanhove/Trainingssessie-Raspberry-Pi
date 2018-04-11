#!/usr/bin/env python
import cgitb ; cgitb.enable()
import RPi.GPIO as GPIO
import os
import sys
# export pin GPIO18 
os.system( 'gpio export 18 out' )
# stel pin in
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.OUT)

number = int(sys.argv[1])
if number==1:
	GPIO.output(18,1)
	comment= "The Led is now on"
elif number==0:
	GPIO.output(18,0)
	comment= "The Led is now off"
else:	
	GPIO.output(18,0)
	comment= "Wrong argument number"

# show the HTML page
print "Content-Type: text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Control GPIO18 LED</title>"
print "</head>"
print "<body>"
print "%s" % comment
print "</body>"
print "</html>"