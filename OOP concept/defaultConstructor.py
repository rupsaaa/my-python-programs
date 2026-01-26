class Student:
    def __init__(self,n='',m=0): #parameterized constructor with default values
        self.name=n
        self.marks=m
    def talk(self):
        print("Hi I am ",self.name)
        print("My marks are ",self.marks)
s1=Student() #no parameters so it will take default values
s1.talk()
s2=Student("Ram",546)
s2.talk()
