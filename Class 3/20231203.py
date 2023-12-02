import pyrebase

config = {
  "apiKey": "AIzaSyCXtsclqUECts_ouaWTTXz4ydFltCKfAfM",
  "authDomain": "python2024autumn.firebaseapp.com",
  "projectId": "python2024autumn",
  "storageBucket": "python2024autumn.appspot.com",
  "messagingSenderId": "1023316537277",
  "appId": "1:1023316537277:web:7193d64e37c774ad01acd4",
  "databaseURL": ""
}

#connect firebase and the python script by using app config
firebase = pyrebase.initialize_app(config)

#get a reference to the auth service
auth = firebase.auth()

def signup():
    email = input("Please enter your email:")
    password = input("Please enter your password:")
    user = auth.create_user_with_email_and_password(email, password)
    print("Successfully signup!")

signup()