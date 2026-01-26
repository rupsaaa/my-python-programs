#find one missing letter from a string that has been shuffled
#Input:Banana suppose after shuffling(banna) missing letter is a 
s="banana"
s2="abnna"
f=0
for i in s:
    if s.count(i)!=s2.count(i):
        f=1
        break
if f==1:
    print("missing letter is ",i)
else:
    print("No missing letter")


