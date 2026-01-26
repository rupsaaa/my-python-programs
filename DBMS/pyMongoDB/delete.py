from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.newdb # Creates a new database named newdb or connects to an existing one if present
collection=db.products # Creates a new collection named products or connects to an existing one if present
print("Documents before deletion")
for doc in collection.find():
     print(doc)
collection.delete_one({'ProdId':2}) # Deletes product with ProdId=2
collection.delete_many({'Price':{'$lt':20000}}) # Deletes multiple documents where price is less than 30000
print("\nDocuments after deletion...")
for doc in collection.find():
     print(doc)
