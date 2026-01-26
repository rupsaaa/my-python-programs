import pymysql
db = pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
cursor=db.cursor()
sql="SELECT LOCATION FROM DEPARTMENT"
cursor.execute(sql)
row=cursor.fetchone() #fetches the next record,here the first record
if row:
    print("Location:",row[0])
db.close()