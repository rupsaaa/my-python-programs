dt=[]
sum=0
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    dt.append(num)
    sum=sum+dt[i]
avg=sum/s
print("Sum of the numbers in the array: ",sum)
print("Average of the numbers in the array: ",avg)