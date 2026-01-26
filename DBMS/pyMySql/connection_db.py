import pymysql
def get_connection():
     conn=pymysql.connect(
          host="localhost",
          user="root",
          password="",
          port=3306
     )
     try:
          with conn.cursor() as cursor:
               # Creating the database if does not exists
               cursor.execute("""CREATE DATABASE IF NOT EXISTS employee""")
               print("\n***employee database created successfully***\n")
               conn.commit()
     except pymysql.Error as e:
          print("Error: ",e)
     finally:
          conn.close()
     try:
          conn=pymysql.connect(
               host="localhost",
               user="root",
               password="",
               database="employee",
               port=3306
          )
          cursor=conn.cursor()
          cursor.execute("create table if not exists emp(eno int primary key,ename varchar(50),dept varchar(25),salary int)")
     except pymysql.Error as e:
          print("Error: ",e)
     return conn