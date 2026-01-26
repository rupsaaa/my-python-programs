fo=open("abc.txt","r+")
print(fo.read(23))
pos=fo.tell()
print("current file position",pos)
print(fo.read(23))
pos=fo.seek(0,0)
print(fo.readline())#read only one line and read() reads entire file

fo.close()