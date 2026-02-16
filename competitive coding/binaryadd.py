#adding two binary numbers taking as strings of same length
b1=input("First binary number:")
b2=input("Second binary number:")
result='' 
carry=0
for i in range (len(b1)-1,-1,-1):
    r=carry
    if b1[i]=='1':
        r+=1
    if b2[i]=='1':
        r+=1
    if r%2==0:
        result='0'+result
    else:
        result='1'+result
    
    if r<2:
        carry=0
    else:
        carry=1
if carry!=0:
    result='1'+result
print(result)