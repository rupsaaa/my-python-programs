#Second largest element from a list
data=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    data.append(num)
lt=set(data)
largest=max(lt)
lt.remove(largest)
print("The Second largest element in the list is ",max(lt))

