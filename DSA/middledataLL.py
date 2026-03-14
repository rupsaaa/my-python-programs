#find middle element of a linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def add(self,data):
        ptr=node(data)
        if self.head is None:
            self.head=ptr
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=ptr
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    def middle(self):
        ptr1=self.head
        ptr2=self.head
        while ptr2 and ptr2.next:
                ptr1=ptr1.next
                ptr2=ptr2.next.next
        return ptr1.data
        
l=linkedlist()
l.add(1)    
l.add(2)
l.add(3)        
l.add(4)
l.add(5)
l.add(6)
l.add(7)
l.add(8)
l.add(9)

print(l.middle())
