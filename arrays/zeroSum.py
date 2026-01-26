#print the pairs whose sum is 0
pair=[]
lt=[2,-2,3,-3,4,-1,-4]
n=len(lt)
for i in range(n):
    for j in range(i+1,n):
        if lt[i]+lt[j]==0:
            pair.append((lt[i],lt[j]))
print("The pairs whose sum is 0:",pair)
