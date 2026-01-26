import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)

cursor = db.cursor()  # Create a cursor object to execute any SQL query
while(True):
    ch=input("Press Y to continue and N to exit:")
    if ch=='Y':
      a=int(input("Enter Dept no:"))
      b=input("Enter dept name:")
      c=input("Enter location:")
      sql = "INSERT INTO DEPARTMENT (DEPTNO, DEPT_NAME, LOCATION) VALUES (%s, %s, %s)"
      values = (a, b, c)
      cursor.execute(sql,values)
      db.commit()
      print("Inserted successfully...")
    elif ch=='N':
       print("Exiting...")
       break
    else:
       print("Wrong choice...")
db.close()
