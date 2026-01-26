def myfun(val):
    if isinstance(val,int):
        print(f"you pass integer:{val}")
    elif isinstance(val,str):
        print(f"you pass string:{val}")
    elif isinstance(val,float):
       print(f"you pass float:{val}")
    else:
        print(f"invalid type:{type(val)}")
myfun(15)
myfun(17.76)
myfun("Rupsa")
myfun([1,2,3,4])