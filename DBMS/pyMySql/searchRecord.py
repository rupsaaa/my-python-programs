import pymysql
db = pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
cursor=db.cursor()
sql="SELECT * FROM DEPARTMENT WHERE DEPTNO in(131,123)"
cursor.execute(sql)
rows=cursor.fetchall() 
for row in rows:
    print(row)
db.close()