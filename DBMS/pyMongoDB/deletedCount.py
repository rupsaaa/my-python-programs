from pymongo import MongoClient
#Connect to local MongoDB server
client=MongoClient("mongodb://localhost:27017/")
db=client["student"]
students=db["studmarks"]
result=students.delete_one({"Name":"Suraj"})
print("Deleted count: ",result.deleted_count)
print("After deletion following records.....")
for s in students.find():
     print(s)
res=students.delete_many({"marks":{"$lt":80}})
print("Deleted count: ",res.deleted_count)
print("After deletion following records.....")
for s in students.find():
     print(s)