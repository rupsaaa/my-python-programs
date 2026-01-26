def HCF(a,b):
    m=min(a,b)
    for i in range(1,m+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(hcf)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
hcf=HCF(a,b)
print("HCF of ",a," and ",b,"is:",hcf)
lcm=(a*b)/hcf
print("LCM of ",a," and ",b,"is:",lcm)

