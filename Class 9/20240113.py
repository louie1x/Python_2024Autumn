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


dir_name = "taipei"
#get a reference to the auth service
storage = firebase.storage()

all_files = storage.list_files()
# for file in all_files:
#     if file.name.startswith(dir_name): #only need the file starts with directory we want.
#         file.download_to_filename(file.name)
print(all_files)