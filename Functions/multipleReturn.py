def calc(a,b):
    sum=a+b
    diff=a-b
    pro=a*b
    quo=a/b
    return sum,diff,pro,quo
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s,d,p,q=calc(a,b)
print("Sum of two numbers:",s)
print("Difference of two numbers:",d)
print("Product of two numbers:",p)
print("Quotient of two numbers:",q)