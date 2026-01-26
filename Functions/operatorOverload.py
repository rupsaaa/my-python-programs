'''operator overloading gives new meaning to the operator.
Calculations can easily be done in primitive data types but for objects the meaning and calculations are different'''
class Complex:
    def __init__(self):
        self.real=0
        self.img=0
    def setValue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,C):
        Temp=Complex()
        Temp.real=self.real+C.real
        Temp.img=self.img+C.img
        return Temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
C1=Complex()
C1.setValue(1,2)
C2=Complex()
C2.setValue(3,4)
C3=Complex()
C3=C1+C2
print("Result=")
C3.display()

