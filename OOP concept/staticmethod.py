class MyClass:
    n=0 #n is class or static variable
    def __init__(self):
        MyClass.n=MyClass.n+1 #increments class variable n when an instance is created
    @classmethod #class/static variables is same but for method, class and static needs to be declared separately.
    def noObjects(cls):
        print("No.of instances created:",cls.n)
obj1=MyClass()
obj2=MyClass()
obj3=MyClass()
MyClass.noObjects()
obj2.noObjects()
'''Static method:
1)No need to create objects to be called
2)does not need cls or self variables
3)clearly indicates that is independent of instance or class variables
4)class method can modify the class attributes using cls but static method cannot
'''

    