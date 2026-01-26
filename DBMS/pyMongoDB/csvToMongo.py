import pandas as pd
import pymongo
df=pd.read_csv("productDetails.csv")
data=df.to_dict(orient='records')
client=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=client["newdb"] 
col=mydb["products"]
col.insert_many(data)
print("CSV Data imported succesfully to mongo")