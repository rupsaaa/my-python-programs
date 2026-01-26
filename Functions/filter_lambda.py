import math
l1=[4,8,9,2,6,100]
res=filter(lambda x: x==pow(math.sqrt(x),2),l1)
print(list(res))