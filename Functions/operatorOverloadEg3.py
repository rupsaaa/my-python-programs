class Student:
     def __init__(self,name,marks):
          self.name=name
          self.marks=marks
     def display(self):
          print(self.name,self.marks)
     def __add__(self,S):
          Temp=Student(S.name,[])
          for i in range(len(self.marks)):
               Temp.marks.append(self.marks[i]+S.marks[i])
          return Temp
S1=Student("Nikhil",[87,90,85])
S2=Student("Nikhil",[83,86,88])
S1.display()
S2.display()
S3=Student("",[])
S3=S1+S2
S3.display()