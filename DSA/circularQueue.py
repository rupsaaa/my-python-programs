class circularQ:
    def __init__(self,size):
         self.size=size
         self.arr=[None]*size
         self.front=self.rear=-1
    def insert(self,num):
          if((self.rear+1)%self.size==self.front):
               print("Circular Queue is full")
          elif(self.front==-1):
               self.front=self.rear=0
               self.arr[self.rear]=num
          else:
               self.rear=(self.rear+1)%self.size
               self.arr[self.rear]=num
    def delete(self):
          if(self.front==-1):
               print("The circuar queue is empty")
          elif(self.front==self.rear):
               n=self.arr[self.front]
               self.front=self.rear=-1
               return n
          else:
               n=self.arr[self.front]
               self.front=(self.front+1)%self.size
               return n
    def printqueue(self):
          if(self.front==-1):
               print("No elements")
          elif(self.rear>=self.front):
               for j in range(self.front,self.rear+1):
                    print(self.arr[j],end=" ")
                    print()
          else:
               for j in range(self.front,self.size):
                    print(self.arr[j],end=" ")
               for j in range(0,self.rear+1):
                    print(self.arr[j],end=" ")
               print()
ob=circularQ(4)
ob.insert(14)
ob.insert(16)
ob.insert(19)
ob.insert(21)
print("Display queue")
ob.printqueue()
ob.delete()
ob.delete()
print("Queue after deletion")
ob.printqueue()