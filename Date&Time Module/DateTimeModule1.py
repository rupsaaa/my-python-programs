# finding current date and time
from datetime import *
now=datetime.now()
print(now)
print('Date now: {}/{}/{}'.format(now.day,now.month,now.year))
print('Time now: {}:{}:{}'.format(now.hour,now.minute,now.second))