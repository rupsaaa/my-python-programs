def multiply(a,b,c):
    return a*b*c
num=[4,6,3]
res=multiply(*num) #* means positional argument it means a is passed to a,6 to b,3 to c
print(res)
