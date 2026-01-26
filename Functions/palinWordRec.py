def ispalin(word):
    if(len(word)<=1):
        return 1
    if(word[0]==word[-1]):
        return (ispalin(word[1:-1]))
    else:
        return 0
        
word=input("Enter a word:")
if (ispalin(word)):
    print(word," is a palindrome word")
else:
    print(word," is not a palindrome word")