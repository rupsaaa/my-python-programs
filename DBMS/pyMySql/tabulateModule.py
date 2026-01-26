import pymysql
from tabulate import tabulate
conn=pymysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
print("Successfully connected...",conn)
try:
    with conn.cursor() as cursor:
        #selecting student table's attributes and all other attributes of marks table(denoted by *) and then joinin the two tables using primary key of student table(stu_id)
        cursor.execute("""
                       SELECT student.name,RollNo, marks.* 
                       FROM student
                       INNER JOIN marks on student.Stu_id=marks.Stu_id
                    """
                       )
        result=cursor.fetchall()
        headers=[desc[0] for desc in cursor.description]
        formatted_result=[]
        for row in result:
            formatted_row=[field for field in row]
            formatted_result.append(formatted_row)
        print(tabulate(formatted_result,headers=headers,tablefmt="grid"))
except pymysql.Error as e:
    print("Error:",e)
finally:
    conn.close()