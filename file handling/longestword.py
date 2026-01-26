fo=open("abc.txt","r")
lt=fo.readlines()
max=0
for w in lt:
    for c in w.split():
        if len(c)>max:
            max=len(c)
            longest=c
print("Longest word in the text file:",longest," of length:",max)

            
