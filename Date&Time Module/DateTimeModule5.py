# formatting the date
from datetime import *

# get current date into td object
td=date.today()
print(td)

# format the td and convert into string str
str=td.strftime("%d, %B, %Y")
print(str)