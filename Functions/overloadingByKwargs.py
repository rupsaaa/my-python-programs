def Dis_Info(**kwargs):#used for multiple arguments passed in the form of a dictionary **is compulsory name can be anything
    for key,val in kwargs.items():
        print(f"{key}:{val}")
Dis_Info(name="Arpan",age=23,marks=87)
Dis_Info(name="Ram",desig="manager")
