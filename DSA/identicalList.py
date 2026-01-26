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
    def countNode(self):
        ptr=self.head
        c=0
        while ptr is not None:
            ptr=ptr.next
            c=c+1
        return c
    def getData(self):
        data_list = []
        ptr = self.head
        while ptr:
            data_list.append(ptr.data)
            ptr = ptr.next
        return data_list
def isIdentical(list1,list2):
        if list1.countNode() != list2.countNode():
           return False
        if list1.getData()==list2.getData():
            return True
list1=singleLL()
list1.addend(5)
list1.addend(3)
list1.addend(6)
list1.addend(7)
list2=singleLL()
list2.addend(3)
list2.addend(5)
list2.addend(6)
list2.addend(7)
print(list1.getData())
if isIdentical(list1,list2):
    print("identical")
else:
    print("Non identical")

