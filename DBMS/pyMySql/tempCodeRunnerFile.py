import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",         # Corrected username
    password="",
    database="test"
)

cursor = db.cursor()  # Create a cursor object to execute any SQL query

sql = """INSERT INTO DEPARTMENT VALUES(
    100,'CSE','Sodpur'
)"""

cursor.execute(sql)
db.commit()
db.close()
