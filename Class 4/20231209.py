from tkinter import *
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

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def login(accountentrybox, passwordentrybox):
    try:
        login = auth.sign_in_with_email_and_password(accountentrybox, passwordentrybox)
        print("Successfully logged in!")
    except Exception as e:
        print(f"登入失敗; {e}")

def signup(accountentrybox, passwordentrybox):
    try:
        user = auth.create_user_with_email_and_password(accountentrybox, passwordentrybox)
        print("Successfully signup!")
    except Exception as e:
        print(f"創建使用者失敗; {e}")

root = Tk()
root.title("Shop")
root.geometry("500x500")

title = Label(root, text="Login Page", font=("Playfair Display", 15))
title.grid(column=1, row=0, sticky=W)

account = Label(root, text="Account", font=("Playfair Display", 15))
account.grid(column=0, row=1, sticky=W)

password = Label(root, text="Password", font=("Playfair Display", 15))
password.grid(column=0, row=2)

accountentrybox = Entry(root)
accountentrybox.grid(column=1, row=1)

passwordentrybox = Entry(root)
passwordentrybox.grid(column=1, row=2)

loginbutton = Button(root, text="Login", font=("Playfair Display", 15), command = lambda:login(accountentrybox.get(), passwordentrybox.get()))
loginbutton.grid(column=0, row=3)

signupbutton = Button(root, text="Sign Up", font=("Playfair Display", 15), command = lambda:signup(accountentrybox.get(), passwordentrybox.get()))
signupbutton.grid(column=1, row=3)

root.mainloop()