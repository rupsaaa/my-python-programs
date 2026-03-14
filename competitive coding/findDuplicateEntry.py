'''A school records student attendance every day.
If a student appears more than once, it means there is a duplicate entry due to a system error.
Find all students with duplicate attendance.'''

from collections import Counter
lt=["Amit","Riya","Amit","John","Riya","Sara"]
result=[item for item, count in Counter(lt).items() if count > 1]
print(result)