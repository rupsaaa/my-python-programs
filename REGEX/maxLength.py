import re
str=input("Enter a sentence:")
res=re.split(r'\s+',str)
print(res)
ln=max(res,key=len)
print(ln)
#max_len=[wrd for wrd in res if len(wrd)==ln]
#print(max_len)