x=input("Enter a string:")
words=x.split()
y=sorted(words,key=len)
print(str(y).replace("[","").replace("]","").replace(",","").replace("'",''))