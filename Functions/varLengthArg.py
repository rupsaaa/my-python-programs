def variableLengthArg(*argument):#multiple arguments can be passed
    for i in argument: 
        print (i)
variableLengthArg(10.8,7,"hello",'i')