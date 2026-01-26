#Example of Required Parameter
def value_change(a):
    a=10
    print("value inside function=",a)
    return
a=input("enter a number:")
#value_change() error: parameter missing
value_change(a)
print("value outside function=",a)