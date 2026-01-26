import re
match=re.search(r'world','hello world like World')
print(match.group()) #frst occurrance of the word
print(match.start()) #index of first occurrance
print(match.end())   #index of last occurrance
print(match.span())  #both first and last occurrance index