from pymongo import MongoClient
# Connect to local MongoDB server
client=MongoClient("mongodb://localhost:27017/")
db=client["student"]
students=db["studmarks"]
count=students.count_documents({})
print("Total students: ",count)
max_marks=students.count_documents({"marks":{"$gt":80}})
print("Students with marks > 80: ",max_marks)