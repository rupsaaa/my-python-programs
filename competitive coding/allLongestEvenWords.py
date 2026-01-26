def maximum(i,max):
    return i==max
s=input("Enter a sentence:")
max=0
lon_word=[]
for word in s.split():
      if len(word)%2==0:
           if len(word)>max:
                max=len(word)
                lon_word=[word]
           elif len(word)==max:
                lon_word.append(word)
print(lon_word)



