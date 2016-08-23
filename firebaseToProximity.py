# Google Firebase Account https://testautonomous.firebaseio.com/
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

print "Getting Results In Progress"

time.sleep(1)

db = firebase.database()
#data = db.child("autonomous").get()

#print(data.val())
#print(data.key())

def stream_handler(post):
    print(post["event"]) # put
    print(post["path"]) # /-K7yGTTEp7O549EzTYtI
    print(post["data"]) # {'title': 'Pyrebase', "body": "etc..."}
   # print(post["number"])
   
my_stream = db.child("autonomous").stream(stream_handler)
