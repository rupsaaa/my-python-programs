import re
pat=r"hello" #r refers to raw string
str="hello code hub sodpur"
match=re.match(pat,str) #checks whether a string is present at the beginning of another string
if match:
    print("Match Found",match.group())#group()is used to print the string found(if group is not written it returns as object)
else:
    print("No Match")
