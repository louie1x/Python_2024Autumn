# #import firebase packages
# import firebase_admin
# #import the firebase service
# from firebase_admin import credentials
# from firebase_admin import auth

# #connect python with firebase private service key
# cred = credentials.Certificate("python2024autumn-firebase-adminsdk-1vf2i-d95ad9f777.json")
# firebase_admin.initialize_app(cred)

# email = "test@gmail.com"
# password = "123456789"
# phone_number = "+886975211092"

# user = auth.create_user(email = email, password = password, phone_number = phone_number)
# print("User create successfully! {}".format(user.uid))



# weights = [1, 2, 3]

# for i in range(3):
#     print(f"第{i + 1}位同學的體重為{weights[i]}公斤")

# total_weight = sum(weights)
# print(f"三位學生的體重總合為 {total_weight} 公斤")


a = [
    [1, 2, 4],
    [3, 5, 7],
    [2, 4, 9]
]

b = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(len(a)):
    for j in range(len(b[0])):
        c[i][j] = a[i][j] + b[i][j]
        
for rows in c:
    print(rows)