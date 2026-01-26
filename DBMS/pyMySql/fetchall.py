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
rows=cursor.fetchall() #fetches all records
for row in rows:
    print("Location:",row[0])
db.close()