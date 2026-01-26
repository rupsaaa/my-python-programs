import re
pat=r"\s" #matches whitespace
str="hello code hub"
nstr=re.sub(pat,"-",str) #if it gets a space it replaces it with a character
#sub():replaces occurrences of a pattern with another string
print("Replaced String:",nstr)
