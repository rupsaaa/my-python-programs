import pymysql
db = pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
cursor=db.cursor()
update_query="""
UPDATE DEPTNO
SET DEPTNO=DEPTNO+7
WHERE DEPT_NAME IN (SELECT DEPT_NAME FROM DEPARTMENT where DEPTNO<=100)"""
try:
    cursor.execute(update_query)
    db.commit()
    print(f"{cursor.rowcount} rows ere updated.")
except pymysql.MySQLError as err:
    print(f"Error:{err}")
    db.rollback() #unsave changes
cursor.close()
db.close()
