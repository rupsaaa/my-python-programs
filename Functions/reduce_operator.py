from functools import reduce
import operator
l1=[1,2,3,4,5,6]
l2=["I","Love","Code","Hub"]
sum=reduce(operator.add,l1)
prod=reduce(operator.mul,l1)
conc=reduce(operator.concat,l2)
conc2=reduce(operator.add,l2)
print("Sum of all integers:",sum)
print("Product of all integers:",prod)
print("Concatenation of all strings using add:",conc2)
print("Concatenation of all strings usint concat:",conc)