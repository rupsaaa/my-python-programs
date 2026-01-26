r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
arr=[]
for i in range (r):
   arr2=[]
   for j in range(c):
       x=int(input())  
       arr2.append(x)
   arr.append(arr2)

   l1=[]
for i in range (r):
    for j in range (c):
         
         if i==0 or i==r-1 or j==0 or j==c-1:
             l1.append(arr[i][j])
             print(arr[i][j],end=" ")

         else:
             print(end="  ")
    print()
print("Max element of boundary elements:",max(l1))
print("Min element of boundary elements:",min(l1))



