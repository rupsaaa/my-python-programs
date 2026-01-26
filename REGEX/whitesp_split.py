import re
txt="hello code hub sodepur"
pat=r"\s+" #split based on whitespace
wrd=re.split(pat,txt)#prints as list
print("words:",wrd)
for w in wrd:
    print(w)
