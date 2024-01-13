import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#import secret key
#path\to\serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate("python2024autumn-firebase-adminsdk-1vf2i-3e0ed88707.json")
#Initiate firebase
firebase_admin.initialize_app(cred)
#Initiate firesotre
db = firestore.client()