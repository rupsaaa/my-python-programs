'''keith number is 14 because
14=1+4=5
4+5=9
5+9=14'''
n=int(input("Enter a number"))
n1=n
digits=[]
while(n!=0):
    digits.append(n%10)
    n=n//10
digits.reverse()
while(sum(digits)<n1):
    digits.append(sum(digits))
    digits.remove(digits[0])
if sum(digits)==n1:
    print(n1," is a keith number")
else:
    print(n1," is not a keith number")