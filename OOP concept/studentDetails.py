class Student:
    def __init__(self): #init is a constructor and self is a default keyword that refers to instances
        self.name="Vishnu"
        self.age=20
        self.marks=900
    def talk(self):
        print("Hi I am ",self.name)
        print("My age is ",self.age)
        print("My marks are ",self.marks)
s1=Student() #create an instance to Student class
s1.talk()
