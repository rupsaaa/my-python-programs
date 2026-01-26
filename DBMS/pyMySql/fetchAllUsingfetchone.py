import pymysql
db = pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
cursor=db.cursor()
sql="SELECT * FROM DEPARTMENT"
cursor.execute(sql)

for i in range(cursor.rowcount):
    row=cursor.fetchone()
    if row:
       print(row)
db.close()