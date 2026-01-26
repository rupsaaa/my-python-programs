r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
arr=[]
for i in range (r):
   arr2=[]
   for j in range(c):
       x=int(input())  
       arr2.append(x)
   arr.append(arr2)

   trans=[]
   
for j in range (c):
    ar=[]
    for i in range (r):
        ar.append(arr[i][j])
    trans.append(ar)
for i in range (c):
    for j in range (r):
         print(trans[i][j],end=" ")
         
    print()
         
        


    