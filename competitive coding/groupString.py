#group string in pair of two consecutive characters
s=input("Enter input: ")
for i in range (0,len(s),2):
    print(s[i:i+2],end=" ")