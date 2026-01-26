from functools import reduce
num=[1,2,3,6,5,2]
prod=reduce(lambda x,y:x*y,num)
print("Product of all the numbers in the list:",prod)
