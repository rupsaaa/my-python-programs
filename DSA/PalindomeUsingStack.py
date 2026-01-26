st=input("Enter a word:")
lt=list(st)
l=""
for i in range(len(lt)):
    l=l+lt.pop()
if st==l:
    print("palindrome")
else:
    print("Not Palindome")
