#given two list of sorted order merge them in sorted order 
#eg: 1 4 6 7 and 3 8 9 11 output:1 3 4 6 7 8 9 11
class linkedList:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class singleLL:
    def __init__(self):
        self.head=None
    def addend(self,newval):
        temp=linkedList(newval)
        if self.head is None:
            self.head=temp
            return
        ptr=self.head
        while (ptr.next):
            ptr=ptr.next
        ptr.next=temp 
    def printList(self):
        num=self.head
        while num is not None:
            print(num.data)
            num=num.next
    
    def mergeList(self, list2):
     ptr1 = self.head
     ptr2 = list2.head
     lt = []

     while ptr1 is not None or ptr2 is not None:
        if ptr1 is None:
            lt.append(ptr2.data)
            ptr2 = ptr2.next
        elif ptr2 is None:
            lt.append(ptr1.data)
            ptr1 = ptr1.next
        elif ptr1.data <= ptr2.data:
            lt.append(ptr1.data)
            ptr1 = ptr1.next
        else:
            lt.append(ptr2.data)
            ptr2 = ptr2.next

     return lt

list1=singleLL()
list1.addend(1)
list1.addend(3)
list1.addend(4)
list1.addend(9)
list1.addend(19)
list1.addend(25)
list2=singleLL()
list2.addend(3)
list2.addend(5)
list2.addend(6)
list2.addend(17)
list2.addend(20)
print(list1.mergeList(list2))