# finding the day of the year
from datetime import *

# get today's date
td=date.today()
print(td) # display content of td object

# %j returns day of the year as: 001, 002, ....366.
s1=td.strftime("%j")
print('Today is ',s1,'yh day of the current year')

# find the week day name
s2=td.strftime("%A")
print('It is ',s2)