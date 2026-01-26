import math
class Perfect:
    start=0
    end=0
    @classmethod
    def isPerfectSq(cls,num):
         n=int(math.sqrt(num))
         if(n*n==num):
              return 1
    @classmethod
    def display(cls):
         for i in range(cls.start,cls.end+1):
            if(cls.isPerfectSq(i)==1):
                print(i)
Perfect.start=int(input("Enter the start of the range:"))
Perfect.end=int(input("Enter the end of the range:"))
Perfect.display()
