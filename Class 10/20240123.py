import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import os
from firebase_admin import credentials, storage

cred = credentials.Certificate("Class 6\python2024autumn-firebase-adminsdk-1vf2i-5e25f701d2.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'python2024autumn.appspot.com'})

dir_path = "Class 7\image"
filelist = [f for f in os.listdir(dir_path)]
print(filelist)

bucket = storage.bucket() #storage bucket
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "SofaProjectImage/"+file
    print("Now uploading file {}.".format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)
