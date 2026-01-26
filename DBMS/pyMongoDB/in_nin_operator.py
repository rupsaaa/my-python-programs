from pymongo import MongoClient
# Connect to local MongoDB server
client=MongoClient("mongodb://localhost:27017/")
db=client["student"]
students=db["studmarks"]
print("Students whose name are in the given list: ")
result=students.find({"Name":{"$in":["Debrup","Rupsa"]}})
for student in result:
     print(student)
print("Students whose name are not in the given list: ")
result=students.find({"Name":{"$nin":["Debrup","Rupsa"]}})
for student in result:
     print(student)
print("Students whose age is greater than 20 and marks is greater than 90: ")
result=students.find({"age":{"$gte":20},"marks":{"$gt":90}})
for student in result:
     print(student)