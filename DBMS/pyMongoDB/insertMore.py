from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/') #connect to the mongo DB server
mydb=con["StudentInfo"] # create a new database
col=mydb["mystud"]
def insertRec():
    while True:
        name=input("Enter name of the student:")
        age=int(input("Enter age of the student:"))
        city=input("Enter city of the student:")
        stud_data={"name":name,"age":age,"city":city}
        col.insert_one(stud_data)
        print("Inserted successfully!")
        ch=input("Do you want to continue?yes or no:")
        if ch!="yes":
            break
insertRec()
print(f"Data successfully added to collection '{col.name}'")