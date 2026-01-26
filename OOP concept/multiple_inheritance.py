class Addition:
    def add(Self,a,b):
        return a+b
class Subtract:
    def difference(Self,a,b):
        return a-b
class Calculation(Addition,Subtract):
    def division(self,a,b):
        return a/b
calc=Calculation()
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print(calc.add(x,y))
print(calc.difference(x,y))
print(calc.division(x,y))

