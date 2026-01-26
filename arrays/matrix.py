r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
arr=[]
for i in range (r):
   arr2=[]
   for j in range(c):
       x=int(input())  
       arr2.append(x)
   arr.append(arr2)
   sum=0
   bsum=0 
   nbsum=0
for i in range (r):
    for j in range (c):
         sum=sum+arr[i][j]
         if i==0 or i==r-1 or j==0 or j==c-1:
            bsum=bsum+arr[i][j]
         else:
            nbsum+=arr[i][j]
         print(arr[i][j],end=" ")
    print()
print("Average of all elements in the array",(sum/(r*c)))
print("Sum of boundary elements",bsum)
print("Sum of non-boundary elements",nbsum)
ld=0
rd=0
  
for i in range (r):
    ld=ld+arr[i][i]
    rd=rd+arr[i][r-i-1] 
print ("Sum of left diagonals=",ld)
print ("Sum of right diagonals=",rd)


   