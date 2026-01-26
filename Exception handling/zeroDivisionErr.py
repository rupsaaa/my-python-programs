a=int(input("Enter first number"))
b=int(input("Enter second number"))
try:
  result=a/b
  print("Result=",result)
except ZeroDivisionError:
  print("Division by zero")
else:
  print("Successful Division")
  
