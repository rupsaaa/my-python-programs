def ispalin(num,rev):
    if(num==0):
        return rev
    else:
        rev=rev*10+num%10
        return ispalin(num//10,rev)
num=int(input("Enter a number:"))
f=ispalin(num,0)
if f==num:
    print(num," is a palindrome number")
else:
    print(num," is not a palindrome number")
