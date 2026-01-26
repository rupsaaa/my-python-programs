#traditional version
class Stack:
     def __init__(self):
          self.stack=[]
          self.SIZE=int(input("Enter size of the stack: "))
          self.TOP=-1

     # use list append method to add elements
     def push(self,val):
          if self.TOP == self.SIZE-1: # Overflow
               print("Stack Overflow...")
          else:
               self.TOP=self.TOP+1
               self.stack.append(val)
               print("Value pushed successfully")
          
     # use list pop method to remove elements
     def pop(self):
          if self.TOP==-1: # Underflow
               print("Stack Underflow...")
          else:
               n=self.stack.pop()
               self.TOP=self.TOP-1
               return n
          
     # Display existing stack
     def display(self):
          if self.TOP==-1: # Empty stack
               print("Stack is empty...")
          else:
               print("Existing stack: ")
               for i in range(self.TOP,-1,-1):
                    print(self.stack[i],end=" , ")
               print()
     
     # Display the topmost element from the stack
     def peek(self):
          if self.TOP==-1: # Empty stack
               print("Stack is empty...")
          else:
               return self.stack[self.TOP]

s=Stack()
print("**********MAIN MENU**********")
print("Choice 1: Push")
print("Choice 2: Pop")
print("Choice 3: Display")
print("Choice 4: Peek")
print("Enter any other choice to exit...")
print("************************")
while(True):
     ch=int(input("\nEnter your choice: "))
     match ch:
          case 1:
               data=input("Enter a value: ")
               s.push(data)
          case 2:
               n=s.pop()
               if n is not None:
                    print("Value popped successfully: ",n)
          case 3:
               s.display()
          case 4:
               n=s.peek()
               if n is not None:
                    print("The TOP value is: ",n)
          case _:
               exit("\nProgram ended succesfully....")