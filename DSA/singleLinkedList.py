class linkedList:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class singleLL:
    def __init__(self):
        self.head=None

    def printList(self):
        num=self.head
        while num is not None:
            print(num.value)
            num=num.next
    def addbeg(self,newval):
        temp=linkedList(newval)
        temp.next=self.head
        self.head=temp
    def addend(self,newval):
        temp=linkedList(newval)
        if self.head is None: #if the list is empty the new node becomes the head node
            self.head=temp
            return
        ptr=self.head
        while (ptr.next):
            ptr=ptr.next
        ptr.next=temp 
    def delBeg(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
    def delEnd(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        ptr=self.head
        while (ptr.next.next):
            ptr=ptr.next
        ptr.next=None    
    def reverse(self):
        if self.head is None:
            return 0
        elif self.head.next is None:
            return 1
        else:
          ptr=self.head
          ptr1=ptr2=None
          while ptr is not None:
            ptr2=ptr.next
            ptr.next=ptr1
            ptr1=ptr
            ptr=ptr2
          self.head=ptr1
          return 2
    def ispalindrome(self):
        ptr=self.head
        list1=singleLL()
        while ptr is not None:
            list1.addend(ptr.value)
            ptr=ptr.next
        ptr=self.head
        list1.reverse()
        ptr2=list1.head
        while ptr is not None:
            if ptr.value!=ptr2.value:
                print("Not Palindrome")
                return
            ptr=ptr.next
            ptr2=ptr2.next
        print("Palindrome")
        
    def printEvenPosition(self):
        ptr=self.head
        c=0
        while ptr is not None:
            c=c+1
            if c%2==0:
                print(ptr.value)
            ptr=ptr.next
    
    
       

slist=singleLL()
slist.head=linkedList("MON")
node2=linkedList("TUES")
node3=linkedList("WED")
node4=linkedList("THURS")
slist.head.next=node2
node2.next=node3
node3.next=node4
slist.addbeg("SUN")
slist.addend("FRI")
slist.printList()
print()
slist.printEvenPosition()
slist.reverse()
slist.printList()


    