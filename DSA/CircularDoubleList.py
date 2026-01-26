class cdlist:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class circulardlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def createlist(self,val):
        temp=cdlist(val)
        temp.next=None
        temp.prev=None
        self.head=temp
        self.tail=temp
    def Addbeg(self,val):
        if self.head is not None:
            ptr=cdlist(val)
            self.head.prev=ptr
            ptr.next=self.head
            self.head=ptr
            self.tail.next=self.head
            self.head.prev=self.tail
    def Addend(self,val):
        ptr=cdlist(val)
        if self.head is None:
           self.head=ptr
           self.tail=ptr
           return
        temp=self.head
        while(temp.next!=self.head):
            temp=temp.next
        temp.next=ptr
        ptr.prev=temp
        self.tail=ptr
        self.tail.next=self.head
        self.head.prev=self.tail
    def display(self):
        if self.tail==None:
            print("The list is empty")
            return
        ptr=self.tail.next
        while ptr:
            print(ptr.value,end="->")
            ptr=ptr.next
            if ptr==self.tail.next:
                print(ptr.value)
                break
    def deleteBeg(self):
        if(self.head==None):
            return
        elif(self.head.next==self.tail.next):
            self.head=self.tail=None
            return
        elif(self.head is not None):
            temp=self.head.next
            temp.prev=None
            self.head=temp
            self.tail.next=self.head
            self.head.prev=self.tail
            return
    def deleteEnd(self):
        if(self.head==None):
            return
        elif(self.head.next==self.tail.next):
            self.head=self.tail=None
            return
        else:  
            self.tail=self.tail.prev.next
            self.tail.prev.next=self.head
            self.head.prev=self.tail   
            return
    def searchAndDelete(self, val):
       if self.head is None:
          print("List is empty")
          return
       ptr = self.head
       while True:
          if ptr.value == val:
             if ptr == self.head:
                self.deleteBeg()
             elif ptr == self.tail:
                self.deleteEnd()
             else:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
                return  
          ptr = ptr.next
          if ptr == self.head:
            break
       

        
cl=circulardlist()
cl.createlist(7)
cl.Addbeg(4)
cl.Addbeg(10)
cl.Addend(12)
#cl.deleteBeg()
#cl.deleteEnd()
cl.searchAndDelete(10)
cl.display()