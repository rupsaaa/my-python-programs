nums=[7,8,-9,11,12]
m=max(nums)
lt=[]
for i in range(1,m):
    if i not in nums:
        lt.append(i)
    else:
         lt.append(m+1)
print(min(lt))