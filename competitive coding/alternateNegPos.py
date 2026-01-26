lt=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    lt.append(num)
positive = list(filter(lambda x: x>0,lt))
negative =  list(filter(lambda x: x<0,lt))
lt2 = []
i = j = 0
while i < len(positive) and j < len(negative):
        lt2.append(positive[i])
        lt2.append(negative[j])
        i += 1
        j += 1
lt2.extend(positive[i:])
lt2.extend(negative[j:])
print(lt2)
#without loop using zip() function
a=[1,9,-5,-6,3,-4,2,1,0]
pos = list(filter(lambda x: x>=0,a))
neg =  list(filter(lambda x: x<0,a))
#paired = [item for pair in zip(pos, neg) for item in pair]
paired=list(zip(pos, neg))
result= paired + pos[len(neg):] + neg[len(pos):]
print(str(result).replace("(","").replace(")",""))




