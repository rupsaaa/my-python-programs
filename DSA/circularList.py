class clist:
    def __init__(self,val):
        self.val=val
        self.next=None
class circularlist:
    def __init__(self):
        self.last=None #using last because we get head by last.next
    def createlist(self,val):
        if self.last!=None: #if list is non empty return last node
            return self.last
        temp=clist(val)
        self.last=temp
        self.last.next=self.last
        return self.last
    def addBeg(self,val):
        if self.last==None:
           return self.createlist(val)
        temp=clist(val)
        temp.next=self.last.next
        self.last.next=temp
        return self.last
    def addEnd(self,val):
        if self.last==None:
           return self.createlist(val)
        temp=clist(val)
        temp.next=self.last.next
        self.last.next=temp
        self.last=temp
        return self.last
    def display(self):
        if self.last==None:
            print("The list is empty")
            return
        ptr=self.last.next
        while ptr:
            print(ptr.val,end="->")
            ptr=ptr.next
            if ptr==self.last.next:
                print(ptr.val)
                break
    


cl=circularlist()
cl.createlist(7)
cl.addBeg(4)
cl.addEnd(9)
cl.addEnd(10)
cl.display()

