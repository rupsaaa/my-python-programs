#copying contents of abc.txt to xyz.txt file
f1=open("abc.txt","r")
f2=open("xyz.txt","w")
for line in f1.readlines():
    f2.write(line)
f1.close()
f2.close()
print("Copies successfully...")
