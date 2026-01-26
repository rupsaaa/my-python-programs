x=input("Enter a sentence:")
d={}
x=x.split()
d={i:len(i) for i in x}
maxlen=max(d.values())
print(maxlen)
long_word=[key for key,value in d.items() if value==maxlen]
print(long_word)