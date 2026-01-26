try:
    x=int(input("Enter a number: "))
    result=10/x
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Invalid input!")