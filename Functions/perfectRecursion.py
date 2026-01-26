def perfect(a,i):
    if i==1:
        return 1
    elif a%i==0 and i>1:
        return i+perfect(a,i-1)
    elif a%i!=0 and i>1:
        return perfect(a,i-1)
num=int(input("Enter a number:"))
i=num-1
f=perfect(num,i)
if f==num:
    print(num," is a perfect number")
else:
    print(num," is not a perfect number")
