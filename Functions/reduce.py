from functools import reduce
def add(a,b):
    return a+b
num=[1,2,3,4,5,6,7,8,9,10,12]
sum=reduce(add,num) 
print(f"sum of the integers of num list:{sum}") #f is written to format the print statement
sum=reduce(add,num,10) #third parameter is optional for initialisation
print(f"Sum of integers of num list with initial value 10 is:{sum}")


