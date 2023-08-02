import pyrebase

config = {
    'apiKey': 'AIzaSyCK69RRZbFvo-Q_jUqmlXV9tpj-fH9AtVw',
    'authDomain': 'fir-pythontestconn.firebaseapp.com',
    'projectId': 'fir-pythontestconn',
    'storageBucket': 'fir-pythontestconn.appspot.com',
    'messagingSenderId': '588907221691',
    'appId': '1:588907221691:web:7f5dff564904aae7ea4f9e',
    'databaseURL': 'https://fir-pythontestconn-default-rtdb.firebaseio.com/',
}


firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {
    'Age': 25,
    'Name': 'Joe',
    'Alive': False
}

database.push(data)
database.child('Users').child('FirstPerson').set(data)
joe = database.child('Users').child('FirstPerson').get()
database.child('Users').child('FirstPerson').update({'Name': 'John'})
database.child('Users').child('FirstPerson').child('Alive').remove()
