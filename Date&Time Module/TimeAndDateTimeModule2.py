from datetime import datetime,date,time
import time as t
now=datetime.now()
format=now.strftime("%d-5m-%Y %H:%M:%S")
print("\nFormatted= ",format)

daynm=now.strftime("%A, %B %d, %Y")
print("Full Date= ",daynm)

dt1=date(2023,1,31)
dt2=date(2023,11,30)
diff=dt2-dt1
print("\nDays between Jan 1 and Nov 30: ",diff.days)