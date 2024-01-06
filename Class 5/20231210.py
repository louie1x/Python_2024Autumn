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

doc = {
    "name": "Louie",
    "email": "louie@chiang1.com"
}

#根據路徑建立文件參考
doc_ref = db.collection("Autumn2023_Students").document("student01")
#透過參考，使用 set 寫入文件
doc_ref.set(doc)

# #因為不用指定 id ，因此是用 collection 做為參考，並對其追加內容
# collection_ref = db.collection("Autumn2023_Students")
# collection_ref.add(doc)

doc = {
    "name": "Jaclyn",
    "email": "jaclyn@gmail.com"
}

#根據路徑建立文件參考
doc_ref = db.collection("Autumn2023_Students").document("student02")
#透過參考，使用 set 寫入文件
doc_ref.set(doc)