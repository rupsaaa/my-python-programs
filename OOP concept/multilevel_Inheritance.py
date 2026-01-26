class Super:
    def square(self,a):
        return a*a
class Child(Super):
    def cube(self,a):
        return a**3
class MiniChild(Child):
    def power(self,a,b):
        return a**b
ob=MiniChild()
print(ob.square(5))
print(ob.cube(3))
print(ob.power(4,3))