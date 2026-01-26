def isPalin(str):
    if str==str[len(str)-1::-1]:
        return 1
s=input("enter a word:")
if(isPalin(s)==1):
    print("The word is Palindrome as well as Special")
elif(isPalin(s)!=1 and s[0]==s[-1]):
    print("The word is not Palindrome but is Special")
else:
    print("The word is neither palindrome nor special")