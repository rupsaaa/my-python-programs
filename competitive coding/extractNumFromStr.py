'''Extract all numbers from the string.
Reverse their order (because the map is upside down).
Return the sum of these numbers.
Input Format:
A single string S containing letters and digits (a-z, A-Z, 0-9).
"gold12silver34bronze56"
Numbers in the string: 12, 34, 56
Reverse order: 56, 34, 12
Sum: 56 + 34 + 12 = 102'''
import re
pat=r"\d+" 
str="hhhbhbh134bhbkb3vhvh6bfbh8jjf90"
if not(str.isalnum()):
    print("INVALID INPUT")
else:
    mat=re.findall(pat,str) 
    mat1=list(map(int,mat))
    print("Original:",mat)
    print("Reverse:",mat[::-1])
    print("Sum:",sum(mat1))
