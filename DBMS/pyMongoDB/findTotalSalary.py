from pymongo import MongoClient
client=MongoClient("localhost",27017)
db=client["Employee"]
col=db["emp"]
s30=s25=0

for sal in col.find({'age':25}):
     s25+=sal["salary"]
for sal in col.find({'age':30}):
     s30+=sal["salary"]

print("Total salary of employee aged 30: ",s30)
print("Total salary of employee aged 25: ",s25)