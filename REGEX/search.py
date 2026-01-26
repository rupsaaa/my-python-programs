import re
pat=r"hello"
str="hello code hub sodpur hello"
mat=re.search(pat,str,re.IGNORECASE) #searches until match found.If found doesn't search further(duplicate strings won't be printed)
if mat:
    print("Match found:",mat.group())
