from datetime import datetime,date,time
import time as t
now=datetime.now()
y=int(input("Enter year of DOB: "))
m=int(input("Enter Month of DOB: "))
d=int(input("Enter Date of DOB: "))
dob=date(y,m,d)
print("Age: ",now.year - dob.year)