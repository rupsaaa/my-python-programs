lt=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element "))
    lt.append(num)
k=int(input("Enter the position k:"))
print(lt[k+1:]+(lt[0:k+1]))