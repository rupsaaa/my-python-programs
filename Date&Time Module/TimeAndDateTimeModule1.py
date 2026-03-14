from datetime import datetime,date,time
import time as t
now=datetime.now()
print("Current DateTime : ",now)
print("Current Date     :",date.today())
print("Current Time     :",now.time())

print("\nYear   :",now.year)
print("Month    :",now.month)
print("Day      :",now.day)
print("Hour     :",now.hour)
print("Minute   :",now.minute)
print("Second   :",now.second)