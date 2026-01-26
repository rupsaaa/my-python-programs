#range of left over elements:
#Input:3 90 5 [7 22 50 66 78] 
#output:[[3 6] [8 21] [23 49] [51 65] [67 77] [79 90]]
l=int(input("Enter starting range:"))
u=int(input("Enter ending range:"))
n=int(input("Enter size of the array"))
arr=list(map(int,input().split()))
lt=[]
l2=[]
lt.append(l)
for i in arr:
        lt.append(i-1)
        lt.append(i+1)
lt.append(u)
arr.sort()
if arr[0]<l or arr[-1]>u:
       exit()
''''for x,y in zip(lt[::2],lt[1::2]):
    print([x,y])'''
for i in range(0,len(lt)-1,2):
    l2.append([lt[i],lt[i+1]])
if len(lt)%2!=0:
        l2.append([lt[-1]])
print(str(l2).replace(","," "))

