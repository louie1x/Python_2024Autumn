import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("python2024autumn-firebase-adminsdk-1vf2i-d95ad9f777.json")
firebase_admin.initialize_app(cred)