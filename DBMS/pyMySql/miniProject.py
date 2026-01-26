from connection_db import get_connection
from tabulate import tabulate
def add_employee():
    conn=get_connection()
    cursor=conn.cursor()
    try:
        eno=input("Enter Employee ID: ")
        ename=input("Enter Name: ")
        dept=input("Enter Position: ")
        salary=int(input("Enter Salary: "))
        cursor.execute("INSERT INTO EMP(eno,ename,dept,salary)  VALUES (%s,%s,%s,%s)",(eno,ename,dept,salary))
        print("Employee added...")
        conn.commit()
    except Exception as e:
        print(f"Error adding employee...{e}")
    finally:
        conn.close()
def view_all_employee():
    conn=get_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM EMP")
        rows=cursor.fetchall()
        headers=[i[0] for i in cursor.description] #get column names
        print("\nEmployee List:")
        print(tabulate(rows,headers=headers,tablefmt="grid"))
    except Exception as e:
        print(f"Error in fetching records...{e}")
    finally:
        conn.close()
def update_employee():
    conn=get_connection()
    cursor=conn.cursor()
    emp_id=input("Enter Employee ID to update: ")
    field=input("Enter the field to update(ename,dept,salary): ")
    if field not in ["ename","dept","salary"]:
        print("Invalid field..")
        return
    new_value=input("Enter new value:")
    if field=="salary":
        try:
            new_value=float(new_value)
        except ValueError:
            print("Salary must be a number...")
            return
    try:
        query=f"UPDATE EMP SET {field}=%s WHERE eno=%s"
        cursor.execute(query,(new_value,emp_id))
        conn.commit()
        if cursor.rowcount>0:
            print("Employee updated...") 
        else:
            print("Employee not found...")
    except Exception as e:
        print(f"Error updating employee...{e}")
    finally:
        conn.close()
def delete_employee():
    conn=get_connection()
    cursor=conn.cursor()
    emp_id=input("Enter the employee Id whose details you want to delete:")
    try:
        cursor.execute(f"DELETE FROM EMP WHERE eno={emp_id}")
        conn.commit()
        if cursor.rowcount>0:
            print("Employee deleted...")
        else:
            print("Employee not found...")
    except Exception as e:
        print(f"Error deleting employee...{e}")
    finally:
        conn.close()

while True:
    print("\nEmployee Management Menu:")
    print("1.Add Employee")
    print("2.View all Employees")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.EXIT")
    choice=input("Enter your choice: ")
    if choice=='1':
        add_employee()
    elif choice=='2':
        view_all_employee()
    elif choice=='3':
        update_employee()
    elif choice=='4':
        delete_employee()
    elif choice=='5':
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again..")