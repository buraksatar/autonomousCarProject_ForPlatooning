# Google Firebase Account
# https://testautonomous.firebaseio.com/
# sefSxG47MiRpAoQSRjIL7anAZNad11P1D9GftxI

import RPi.GPIO as GPIO
import time

import pyrebase

config = {
  "apiKey": "usefSxG47MiRpAoQSRjIL7anAZNad11P1D9GftxI",
  "authDomain": "testautonomous.firebaseapp.com",
  "databaseURL": "https://testautonomous.firebaseio.com",
  "storageBucket": "testautonomous.appspot.com"
}

firebase = pyrebase.initialize_app(config)

GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(1)

a = 1

while a < 4 :

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print "Distance:",distance,"cm"
  
  a += 1

  time.sleep(1)

  db = firebase.database()
  db.child("autonomous")
  data = {"number": distance}
  db.child("autonomous").push(data)

GPIO.cleanup()
