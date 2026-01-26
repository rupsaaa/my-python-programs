from pymongo import MongoClient
from urllib.parse import quote_plus
username=quote_plus("Rupsa")#quote plus encrypts the username and password
password=quote_plus("Rupsa@2004")
conn_str=f"mongodb+srv://{username}:{password}@cluster0.uxitsue.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client=MongoClient(conn_str)
db=client["testdb"]
coll=db["student"]
def insert_stud():
    id=int(input("enter student id:"))
    name=input("enter a name:")
    marks=float(input("enter marks:"))
    student={"stu_id":id,"name":name,"marks":marks}
    coll.insert_one(student)
    print("Student added successfully...")
def view_records():
    print("\n Student Records:")
    for s in coll.find():
        print(f"student id:{s['stu_id']}  Name:{s['name']}  marks:{s['marks']}")
    print()
def update_rec():
    id=int(input("enter a student id whose marks you want to update:"))
    student=coll.find_one({"stu_id":id})
    if student:
        new_marks=float(input("enter new marks:")) 
        coll.update_one({"stu_id":id},{"$set":{"marks":new_marks}})
        print("Marks updated\n")
    else:
        print("Student not found\n")
def delete_stud():
    id=int(input("enter a student id whose details you want to delete:"))
    student=coll.delete_one({"stu_id":id})
    if student.deleted_count:
        print("Student deleted\n")
    else:
        print("Student not found\n")
while True:
    print("\nStudent Management Menu:")
    print("1.Add Student")
    print("2.View all Students")
    print("3.Update student")
    print("4.Delete student")
    print("5.EXIT")
    choice=input("Enter your choice: ")
    if choice=='1':
        insert_stud()
    elif choice=='2':
        view_records()
    elif choice=='3':
        update_rec()
    elif choice=='4':
        delete_stud()
    elif choice=='5':
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again..")
