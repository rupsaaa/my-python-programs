#check whether there is a cycle in the linked list or not
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
    def checkcycle(self):
        ptr1=self.head
        s=set()
        while ptr1 and ptr1.next:
                ptr1=ptr1.next   
                if ptr1 in s:
                    return True
                s.add(ptr1)
        return False