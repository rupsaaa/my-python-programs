import array as ar
a=ar.array('i',[2,4,1,3,6])#i is for integers
v=ar.array('d',[2.9,4.1,1.6,3.0,6.5])#d is for double
c=ar.array('u',['a','b','c'])#u is for characters
print(a)
print ("The array of integer elements:")
for b in a:
    print(b)
print ("The array of double elements:")
for b in v:
      print(b)
print ("The array of char elements:")
for b in range(len(c)):
       print(c[b])