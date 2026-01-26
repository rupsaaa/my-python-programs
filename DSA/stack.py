#easier version
class stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
            self.stack.append(val)
    def peek(self):
         return self.stack[-1]
    def popval(self):
        if len(self.stack)<=0:
            return ("No element in the stack")
        else:
            return self.stack.pop()
    def display(self):
        if len(self.stack)<=0:
            print("No element in the stack")
        else:
             for i in range(len(self.stack)-1,-1,-1):
                 print(self.stack[i])
            #print(*self.stack[::-1],sep=",")
obj=stack()
print("Stack operations")
print("1:Push\n2:Pop\n3:Peek\n4:Display")
while True:
     ch=int(input("Enter choice:"))
     if ch==1:
          n=int(input("Enter value:"))
          obj.push(n)
     elif ch==2:
          print(obj.popval())
     elif ch==3:
          print(obj.peek())
     elif ch==4:
          obj.display()
     else:
          print("WRONG CHOICE")
     