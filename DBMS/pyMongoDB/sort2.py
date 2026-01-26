from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.newdb
collection=db.products
print("Sorted by price(ascending): ")# sort by price in ascending order
for doc in collection.find().sort({"price":-1,"Name":1}):
     print(doc)



