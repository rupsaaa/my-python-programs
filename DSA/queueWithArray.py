class queue:
    def __init__(self):
        self.queue=[]
    def insert(self,val):
        self.queue.append(val)
    def delete(self):
        if len(self.queue)<1:
            return ("Empty")
        return self.queue.pop(0)
    def display(self):
        print(*self.queue,sep=",")
obj=queue()
print("Queue operations")
print("1:Insert\n2:Delete\n3:Display")
while True:
     ch=int(input("Enter choice:"))
     if ch==1:
          n=int(input("Enter value:"))
          obj.insert(n)
     elif ch==2:
          print(obj.delete())
     elif ch==3:
          obj.display()
     else:
          print("WRONG CHOICE")  