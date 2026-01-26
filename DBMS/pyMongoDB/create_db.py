from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/') #connect to the mongo DB server
mydb=con["StudentInfo"] # create a new database
collection=mydb["mystud"] #create a collection(table)
stdata={"name":"Rupsa","age":20,"city":"Barrackpore"}
collection.insert_one(stdata)
print(f"collection '{"mystud"}' created successfully!")