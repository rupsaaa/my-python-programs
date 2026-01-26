try:
    x=int(input("Enter a number: "))
    result=10/x
except (ZeroDivisionError,ValueError) as e:
    print("An error occured",e)
else:
    print("Result is:",result)