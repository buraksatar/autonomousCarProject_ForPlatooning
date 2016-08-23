# Google Firebase Account
# https://testautonomous.firebaseio.com/
# sefSxG47MiRpAoQSRjIL7anAZNad11P1D9GftxI

import time

import pyrebase

config = {
  "apiKey": "usefSxG47MiRpAoQSRjIL7anAZNad11P1D9GftxI",
  "authDomain": "testautonomous.firebaseapp.com",
  "databaseURL": "https://testautonomous.firebaseio.com",
  "storageBucket": "testautonomous.appspot.com"
}

firebase = pyrebase.initialize_app(config)

print "Distance Measurement In Progress"

time.sleep(1)

a = 1

while a < 10000 :

  time.sleep(0.1)

#  db = firebase.database()
#  distance = round(distance, 2)

#  print "Distance:",distance,"cm"

#  a += 1

#  time.sleep(0.1)

#  db = firebase.database()
#  db.child("autonomous")
#  data = {"number": distance}
#  db.child("autonomous").push(data)
#  db.update(data)
