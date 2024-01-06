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

# def signup():
#     email = input("Please enter your email:")
#     password = input("Please enter your password:")
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         print("Successfully signup!")
#     except:
#         print("Email account has already exist!")

# signup()

def login():
    print("Logging in...")
    #輸入email
    email = input("Please enter your email: ")
    #輸入password
    password = input("Please enter your password: ")
    try:
        #帳號密碼對
        login = auth.sign_in_with_email_and_password(email, password)
        print(login["idToken"])
        print("Successfully logged in!")
    except:
        #帳號密碼錯
        print("Invalid email or password!")

login()