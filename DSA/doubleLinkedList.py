class CreateNode:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def countNode(self):
        ptr=self.head
        c=0
        while ptr is not None:
            ptr=ptr.next
            c=c+1
        return c
    def AddEnd(self, data):
        temp = CreateNode(data)
        if self.head is None:
            self.head = self.tail = temp
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
            self.tail.next = None
    def AddBeg(self,data):
        temp = CreateNode(data)
        if self.head is None:
            self.head = self.tail = temp
            self.head.prev = None
            self.tail.next = None
        else:
            temp.prev=None
            temp.next=self.head
            self.head.prev = temp 
            self.head=temp
    def addAnyPosition(self,data):
        temp=CreateNode(data)
        n=int(input("Enter the position of the new node:"))
        c=1
        if self.head is None and n!=0:
            print("List is Empty..Insertion at ",n," position not possible")
            return
        if n < 1 or n >self.countNode()+ 1:
            print(f"Insertion at position {n} is not possible. Valid range: 1 to {self.countNode() + 1}")
            return
        if n==1:
            self.AddBeg(data)
            return
        if n==self.countNode()+1:
            self.AddEnd(data)
            return
        ptr=self.head
        while c<n:
            ptr=ptr.next
            c=c+1
        ptr.prev.next=temp
        temp.prev=ptr.prev
        temp.next=ptr
        ptr.prev=temp
    def delBeg(self):
        if self.head is None:
            print("Deletion not possible list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head.next.prev=None
        self.head=self.head.next
    def delEnd(self):
        if self.head is None:
            print("Deletion not possible list is empty")
            return
        if self.head.next is None:
            self.head=None
            return 
        self.tail.prev.next=None
        self.tail=self.tail.prev
    def delAnyPosition(self):
        n=int(input("Enter the position of the node to delete:"))
        c=1
        if self.head is None and n!=0:
            print("List is Empty..Deletion at ",n," position not possible")
            return
        if n < 1 or n >self.countNode()+ 1:
            print(f"Deletion at position {n} is not possible. Valid range: 1 to {self.countNode() + 1}")
            return
        if n==1:
            self.delBeg()
            return
        if n==self.countNode():
            self.delEnd()
            return
        ptr=self.head
        while c<n:
            ptr=ptr.next
            c=c+1
        ptr.prev.next=ptr.next
        ptr.next.prev=ptr.prev
    def reverse(self):
        ptr=self.tail
        while ptr is not None:
             print(ptr.num, end=" <-> ")
             ptr = ptr.prev
        print("None")
    def traverse(self):
        ptr = self.head
        if self.head is None:
            print("Empty list")
            return
        
        while ptr is not None:
            print(ptr.num, end=" <-> ")
            ptr = ptr.next
        print("None")

# Example Usage
dll = DoublyLinkedList()
print("*******DOUBLE LINKED LIST MENU********")
print("1.Add Node at the Beginning")
print("2.Add Node at the End")
print("3.Add at any position")
print("4.Delete Node at the Beginning")
print("5.Delete Node at the End")
print("6.Delete from any position")
print("7.Reverse List")
print("8.Display the List")
print("Any other number:EXIT")
while True:
   ch=int(input("Enter your choice:"))
   if ch==1:
       data=int(input("Enter the value to insert in the new node:"))
       dll.AddBeg(data)
   elif ch==2:
       data=int(input("Enter the value to insert in the new node:"))
       dll.AddEnd(data)
   elif ch==3:
       data=int(input("Enter the value to insert in the new node:"))
       dll.addAnyPosition(data)   
   elif ch==4:
       dll.delBeg()
   elif ch==5:
       dll.delEnd()
   elif ch==6:
       dll.delAnyPosition()
   elif ch==7:
       dll.reverse()
   elif ch==8:
       dll.traverse()
   else:
       print("Exiting...")
       break

