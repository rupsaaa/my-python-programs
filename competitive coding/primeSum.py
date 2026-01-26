def isprime(n):
    c=0
    for i in range(1,n+1):
        if(n%i)==0:
            c=c+1
    if c==2:
        return 1
n=10
sum=0
for i in range(10):
    if(isprime(i)):
        sum=sum+i
print(sum)