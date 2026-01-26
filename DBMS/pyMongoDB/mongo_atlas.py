from pymongo import MongoClient
from urllib.parse import quote_plus
username=quote_plus("Rupsa")#quote plus encrypts the username and password
password=quote_plus("Rupsa@2004")
conn_str=f"mongodb+srv://{username}:{password}@cluster0.uxitsue.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client=MongoClient(conn_str)
db=client["testdb"]
coll=db["student"]
student={"stu_id":3,"name":"Debrup","marks":95}
coll.insert_one(student)
print("Student added")
print("All students are:")
for i in coll.find():
    print(i)
