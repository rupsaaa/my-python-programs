'''print longest even words from a sentence
 Eg:hello world he goes to school a www tttttc
 output:school'''
s=input("Enter a sentence:")
even=[word for word in s.split() if (len(word))%2==0]
if len(even)==0:
    print("No even words present")
else:
    print(max(even,key=len)) 
    