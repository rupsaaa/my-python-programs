import re
txt="python pound apple orange pond proud"
pat=r"\bp\w*" #start with p
#+:atleast 1 or more *:0 times or more
wrd=re.findall(pat,txt,re.IGNORECASE)
print("words starting with p:",wrd)
patt=r"\w+n\b" #end with n
wd=re.findall(patt,txt,re.IGNORECASE)
print("words ending with n:",wd)