data=[12,68,34,56,25,40]
key=int(input("Enter the number you want to search:"))
k=0
for i in range (len(data)):
    if key==data[i]:
     k=1
if k==1:
    print("search successful")
else:  
    print("Search unsuccessful")
