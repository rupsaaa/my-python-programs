import re
pat=r"\d+" #digits match one or more
#\d+:match and prints 256 as 256 
#\d:match and prints individual digits 256 as 2,5,6
str="There are 256 java programs and 412 python program."
mat=re.findall(pat,str) #returns a list of all matches
print("All matches",mat)
str2="The priceof a laptop is 420 dollars or 35000 rupees"
num=re.findall(r"\d+",str2)
print(num)