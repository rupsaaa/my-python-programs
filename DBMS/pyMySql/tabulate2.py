import pymysql
from tabulate import tabulate
conn=pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="test"
)
cursor=conn.cursor()
query="""
SELECT student.Stu_id,student.name,student.RollNo,marks.sub,marks.marks
FROM student
JOIN marks ON student.Stu_id=marks.Stu_id
WHERE student.name LIKE %s
"""
cursor.execute(query,('%'+'R'+'%'))
# here % means one or more characters,so this query searches for any name which has 'R'(can be upper case or lowercase) in it
results=cursor.fetchall()
headers=[desc[0] for desc in cursor.description]
print(tabulate(results,headers=headers,tablefmt="grid"))
cursor.close()
conn.close()