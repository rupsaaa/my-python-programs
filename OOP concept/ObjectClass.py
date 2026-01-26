# All classes are subclasses of 'object' class internally
class A(object):
     def __init__(self):
          self.a='a'
          print(self.a)
          super().__init__()
class B(object):
     def __init__(self):
          self.b='b'
          print(self.b)
          super().__init__()
class C(A,B):
     def __init__(self):
          self.c='c'
          print(self.c)
          super().__init__()
obj=C()
'''In this program,the search will start from C.As the object of C is created,the constructor of C is 
called an 'c' is displayed.Then super()._init_() will call the constuctor of left side class of C,i.e.,of
A. So,the constructo of A is called and 'a' is displayed.But inside the constructor of A,we again called 
its super class constructor using super()._init_().Since 'object' is the super class for A,an attempt to 
execute object class constructor will be done but object class does not have any constructor.So, the search
will continue down to right hand side class of object class.That is class B.Hence B's constructor is 
executed and 'b' is displayed.After that the statement super()._init_() wil attempt to execute
constructor of B's super class.That is nothing but 'object' class.Since object class is already visited,the
search stops here.As a result, the output will be 'c','a','b'.Searching in this manner for constructors or
methods is called Method Resolution Order(MRO).
In the above program if we did not write super()._init_() inside A's sonstructor then the output would
have been 'c','a'.
'''