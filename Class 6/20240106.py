import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import secret key
# path/to/serviceAccount.json 請用自己的存放路徑
cred = credentials.Certificate("Class 6\python2024autumn-firebase-adminsdk-1vf2i-5e25f701d2.json")
# initiate firebase
firebase_admin.initialize_app(cred)
# initiate firestore
db = firestore.client()

doc = {
    'name':'jason',
    'email':'jason@gmail.com'
}

# # 使用給定的集合與文件名稱建立參考
# collection_name = "Autumn2023_Students"
# document_name = "student01"
# doc_ref = db.collection(collection_name).document(document_name)

# 使用文件的路徑建立參考，注意前面不能有"/"
# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)

path = "Autumn2023_Students"
collection_ref = db.collection(path)

# doc_ref.add(doc)

# try:
#     doc = doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document is : {}".format(doc_dict))
# except:
#     print("The refernece of document does not exist, please check if the path is correct or not. {}".format(path))

# docs = collection_ref.where("name","==","Louie").get()
# for doc in docs:
#     print("The content of document is: {}".format(doc.to_dict()))

# 新增生日欄位
path = "Autumn2023_Students/student01"
doc_ref = db.document(path)

# 加入巢狀資料 & 新增聯絡欄位
contacts = {
    'email': 'judy@gmail.com',
    'phone': '09123456789'
}
doc = {
    'contacts': contacts
}
doc_ref.update(doc)

# doc = {'birthday': '1231'}
# doc_ref.update(doc)

path = "Autumn2023_Students/student02"
doc_ref = db.document(path)
doc_ref.delete()

# delete things in a collection
students_ref = db.collection('Autumn2023_Students')
docs = students_ref.get()
for doc in docs:
    doc.reference.delete()