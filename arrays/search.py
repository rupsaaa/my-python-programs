dt=[]
#data=[12,68,34,56,25,40]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    dt.append(num)
key=int(input("Enter the number you want to search:"))
if key in dt:
    print("number found")
else:
    print("number not found")    
