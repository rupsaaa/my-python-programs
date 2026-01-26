#1.display all records 2.count total no.of students 3.sort by rollno 4.export data from DB to CSV
import pymysql as mysql
import csv
conn=mysql.connect(
    host="localhost",
    user="root",        
    password="",
    database="test"
)
cursor=conn.cursor()
def display_stud():
    print("\nAll Student Records:")
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        print(row)
def count_stud():
    cursor.execute("SELECT COUNT(*) FROM student") #count is an aggregation func that counts no.of rows
    print("\nTotal students:",cursor.fetchone()[0]) #count creates a column COUNT containing 1 row with value fetchone()[0] refers to that row
def display_sorted():
    cursor.execute("SELECT * FROM student ORDER BY RollNo DESC")
    for row in cursor.fetchall():
        print(row)
def export_to_csv(myfile):
    cursor.execute("SELECT * FROM student")
    records=cursor.fetchall()
    with open(myfile,mode='w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['Stud Id','Name','Roll no'])
        writer.writerows(records)
    print(f"\nData exported successfully to {myfile}")  
display_stud()
count_stud()
display_sorted()
export_to_csv('Student_data.csv')
cursor.close()