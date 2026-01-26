from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/') #connect to the mongo DB server
mydb=con["StudentInfo"] # create a new database
col=mydb["mystud"]
mydata=col.find() #fetch all documents from collection
for doc in mydata:
    print(doc)