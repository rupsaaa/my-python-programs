import pymongo
import pandas as pd
client=pymongo.MongoClient('mongodb://localhost:27017/') 
mydb=client["StudentInfo"] 
col=mydb["mystud"]
data=list(col.find())
for rec in data:
    rec.pop('_id',None)
df=pd.DataFrame(data)#convert dataframe  tabular format using pandas.DataFrame
df.to_excel("myexport_data.xlsx",index=False)#writes the dataframe to an excel file and stop to writing row indices
print("Data exported successfully...")
