'''Given an unsorted array upto n terms there is one number missing and one number occurs twice find both the numbers
eg: 1,2,3,5,6,1
o/p:missing:4 and repeated:1'''
from collections import Counter #collection is module and Counter is class
lt=[1,2,3,3,5]
freq=Counter(lt)
k=[key for key,value in freq.items() if value==2]
print("Repeated:",k)
n=5
missing=n*(n+1)//2-sum(set(lt)) #sum of all numbers upto n-sum of list without repeated number
print("missing:",missing)