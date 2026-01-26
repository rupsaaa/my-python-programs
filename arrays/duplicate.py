#duplicate elements from the list
from collections import Counter #collection is module and Counter is class
lt=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    lt.append(num)
freq=Counter(lt)
if len(lt)!=len(set(lt)):
    print("Not a Unique list")
    duplicate=[key for key,value in freq.items() if value>1]
    print ("Numbers that have duplicate values",str(duplicate).replace('[','').replace(']',''))
else:
    print("Unique list")
    