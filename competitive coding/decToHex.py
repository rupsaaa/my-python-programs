def decToHex(n):
    digits="0123456789ABCDEF"
    hexa=""
    while(n!=0):
        d=n%16
        hexa=digits[d]+hexa
        n=n//16
    return hexa
n=int(input("Enter a decimal number:"))
print("Its equivalent hexa decimal number is:",decToHex(n))