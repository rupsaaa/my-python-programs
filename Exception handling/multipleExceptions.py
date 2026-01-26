try:
  a=int(input("Enter first number"))
  b=int(input("Enter second number"))
  result=a/b
  print("Result=",result)
except (ZeroDivisionError,TypeError):
  print("Error occured")
else:
  print("Successful Division")