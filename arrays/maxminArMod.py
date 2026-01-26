from array import *
l=[int(i) for i in input("Enter numbers:").split(',')]
arr=array('i',l)
print("Maximum numbers from the list",max(arr))
print("Minimum numbers from the list",min(arr))
