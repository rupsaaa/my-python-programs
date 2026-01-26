import pandas as pd
import pymongo
df=pd.read_excel("Student.xlsx")
data=df.to_dict(orient='records')
client=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=client["StudentInfo"] 
col=mydb["mystud"]
col.insert_many(data)
print("Data imported succesfully from excel to mongo")