def dec_to_bin(dec):
    if(dec==0):
        return 0
    else:
        return dec%2+10*dec_to_bin(dec//2)
def bin_to_dec(bin,i):
    if bin==0:
        return 0
    else:
        result=bin%10*2**i
        return result+bin_to_dec(bin//10,i+1)
print("NUMBER SYSTEM CONVERSION:")
print("Enter 1:DECIMAL TO BINARY CONVERSION \nEnter 2:BINARY TO DECIMAL CONVERSION \nPress any other number to exit")
while(True):
    x=int(input("Enter your choice:"))
    if x==1:
         num=int(input("Enter the decimal number:"))
         print("Its binary equivalent is:",dec_to_bin(num))
    elif x==2:
           num=int(input("Enter the binary number:"))
           print("Its decimal equivalent is:",bin_to_dec(num,0))
    else:
          exit("Thank you...program terminated")