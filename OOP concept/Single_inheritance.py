class Addition:
    def add(self,a,b):
        return a+b
class Calculation(Addition):
    def multiply(self,a,b):
        return a*b
calc=Calculation()
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print(calc.add(x,y))
print(calc.multiply(x,y))