#count words and lines of the file abc.txt
fo=open("abc.txt","r")
lt=fo.readlines()
print("No.of lines in the text file is:",len(lt))
c=0
for w in lt:
    c+=len(w.split())
print("No.of words in the text file is:",c)
#fo.seek(0,0)
#lt2=fo.read().split(' ')
#print("No.of words in the text file is:",len(lt2))
