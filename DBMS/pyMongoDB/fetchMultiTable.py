from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['student']
col1=db['Student_Details']
col2=db['studmarks']
print("Records from Student_Details:")
for rec in col1.find().limit(5):
    print(rec)
print("Records from studmarks:")
for rec in col2.find().limit(5):
    print(rec)
last_threeRec=list(col1.find().sort('_id',-1).limit(3)) #last three records in descending order
print("Last three Records from Student_Details:")
for rec in last_threeRec:
    print(rec)