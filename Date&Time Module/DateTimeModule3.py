# comnbining date and time
from datetime import *
d=date(2016,4,29)
t=time(15,30)
dt=datetime.combine(d,t)
print(dt)