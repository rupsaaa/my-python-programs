fo=open("palin.txt","w")
fo.write("madam hello wow dad mom bye R ")
fo.write("\n come go txt ama yay ")
fo.write("\n hh l o")
fo.close()
fo=open("palin.txt","r")
words=fo.read().split()
palindrome=[i for i in words if i==i[len(i)-1::-1]]
print("Palindrome words are:")
for i in palindrome:
   print(i)

