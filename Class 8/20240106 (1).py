import firebase_admin
import os
from firebase_admin import credentials, storage
cred = credentials.Certificate("Class 6\python2024autumn-firebase-adminsdk-1vf2i-5e25f701d2.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'python2024autumn.appspot.com'})

file_path = "Tucker (@tuckerwelt) _ TikTok.jpg"
bucket = storage.bucket() #storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)

def upload_blob(bucket, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}")

upload_blob(bucket, "Class 7\image\\banner.jpg", "images\photo1.png")

dir_path = "Class 8\Img"
filelist = [f for f in os.listdir(dir_path)]
print(filelist)

bucket = storage.bucket() #storage bucket
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "taipei/"+file
    print("Now uploading file {}.".format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)
