def HCF(a,b):
    while True:
        m=a%b
        if m==0:
            return b
        else:
          a=b
          b=m  

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if (a>b):
  hcf=HCF(a,b)
else:
    hcf=HCF(b,a)
print("HCF of ",a," and ",b,"is:",hcf)
lcm=(a*b)/hcf
print("LCM of ",a," and ",b,"is:",lcm)

