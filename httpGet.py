from firebase import firebase

firebase = firebase.FirebaseApplication('https://testautonomous.firebaseio.com', None)

a=1

while a<6:
   result = firebase.get('/number', None)
   print result
