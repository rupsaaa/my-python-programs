# creating datetime object and changes its contents
from datetime import *
# create a datetime object
dt1=datetime(year=2016,month=6,day=24,hour=15,minute=30,second=15)
print(dt1)

# change its year, month and hour values
dt2=dt1.replace(year=2017,hour=20,month=10)
print(dt2)