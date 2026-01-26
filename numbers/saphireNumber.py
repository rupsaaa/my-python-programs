import math
n=int(input("enter a number:"))
cube=int(math.cbrt(n+1))
if cube**3==n+1:
    print("saphire number")
else:
    print("Not a saphire number")
