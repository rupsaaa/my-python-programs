a=16
def my_fun():
    global a
    print(a)
    a=28
my_fun()
print (a)