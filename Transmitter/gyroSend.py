# ADXL345 Python example
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
#
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

import pyrebase
import time
from adxl345 import ADXL345

config = {
  "apiKey": "usefSxG47MiRpAoQSRjIL7anAZNad11P1D9GftxI",
  "authDomain": "testautonomous.firebaseapp.com",
  "databaseURL": "https://testautonomous.firebaseio.com",
  "storageBucket": "testautonomous.appspot.com"
}

firebase = pyrebase.initialize_app(config)

a = 1

while a < 1000:
  adxl345 = ADXL345()
  axes = adxl345.getAxes(False)
  db = firebase.database()
  #data = {"direction": axes['x']}
  x = axes['x']
  y = axes['y']
#  print "   y = %.3fG" % ( axes['y'] )

  if x < (-1.6) and y > (-7):
    data = {"direction": "sag dondu"}
    db.update(data)
    print "sag"
  #axes = adx1345.getAxes(False)
  #print "ADXL345 on address 0x%x:" % (adxl345.address)
  #print "   x = %.3fG" % ( axes['x'] )
  #print "   y = %.3fG" % ( axes['y'] )
  #print "   z = %.3fG" % ( axes['z'] )
    #print axes['x']
    time.sleep(0.1)

  elif x > (-0.6) and y < (-12):
    data = {"direction": "sola dondu"}
    db.update(data)
    #print axes['x']
    time.sleep(0.1)
    print "sol"
  else :
    #data = {"direction": "sabit"}
    #db.update(data)
    #print axes['x']
    time.sleep(0.01)
