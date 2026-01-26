#squares of even numbers in the range 1 to 10:
even_sq=(x*x for x in range(10) if x%2==0)
for x in even_sq:
         print(x)
l=[x*x for x in range(5)]#stores as list
print(l)
print("SUM of squares of 1,2,3,4,5=",sum(l))
print(sum((x*2 for x in range(10))))
print(sum(x for x in range(20,50) if x%2==0))