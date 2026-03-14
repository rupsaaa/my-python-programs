#intersection data of two linked list
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
    def printnode(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def intersection(self,head1,head2):
        s=set()
        temp=head1
        while temp:
            s.add(temp.data)
            temp=temp.next
        temp=head2
        while temp:
            if temp.data in s:
                print(temp.data,end=" ")
            temp=temp.next

l1=linkedlist()
l1.add(1)
l1.add(2)
l1.add(3)       
l1.add(4)
l1.add(5) 
print("First linked list is:")
l1.printnode()
l2=linkedlist()
l2.add(3)
l2.add(4)
l2.add(5)
l2.add(6)
l2.add(7)
print("\nSecond linked list is:")
l2.printnode()
print("Intersection of two linked list is:")
l1.intersection(l1.head,l2.head)