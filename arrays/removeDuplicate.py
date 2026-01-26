from collections import Counter
lt=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    lt.append(num)
#method 1
unique_list=list(dict.fromkeys(lt))
print(unique_list)
#method 2: use set and sorted basd on index

