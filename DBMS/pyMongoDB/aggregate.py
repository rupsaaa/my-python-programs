from pymongo import MongoClient
client=MongoClient("localhost",27017)
db=client["Employee"]
col=db["emp"]
emp21=col.aggregate([{'$group':{'_id':'$age','total_sal':{'$sum':'$salary'}}}])
for doc in list(emp21):
     print(f"Total salary of employees aged {doc['_id']} is {doc['total_sal']}")