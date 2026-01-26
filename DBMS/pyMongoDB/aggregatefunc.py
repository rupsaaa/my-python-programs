from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['newdb']
col=db["products"]
result=col.aggregate([{'$group':{'_id':None,'maxPrice':{'$max':'$price'}}}])
maxres=list(result)[0]['maxPrice']
print(f"Maximum price of product ({maxres}):")
for prod in col.find({'price':maxres}):
    print(prod)
