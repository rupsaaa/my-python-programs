from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost',27017)
print(client.list_database_names()) #returns a list of all existing databases on your MongoDb server
db=client.newdb #connects to a database named mydb
pricelist=[{'ProID':1,'Name':'Laptop','price':25000},
           {'ProID':2,'Name':'TV','price':55000},
           {'ProID':3,'Name':'Printer','price':15000},
           {'ProID':4,'Name':'Mobile','price':20000},
           {'ProID':5,'Name':'Tab','price':15000}]
db.products.insert_many(pricelist)
