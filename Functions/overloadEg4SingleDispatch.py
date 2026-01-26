from functools import singledispatch #module
import math
@singledispatch
def myfun(arg):#main function
    print(f"Default:{arg}")
@myfun.register(int)
def _(arg):#underscore represents function name you can give other names too
    print(f"Integer:{arg}")
@myfun.register(str)
def _(arg):
    print(f"String:{arg}")
myfun(23.16)
myfun([10,20,30,40])
myfun("Codehub")