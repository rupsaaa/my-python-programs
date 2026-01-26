x=input("Enter a word:")
d={}
#for char in set(x):
    #print(char,"=",x.count(char))
d={char:x.count(char) for char in sorted(set(x))}
print("Frequency of each character: ")
print(str(d).replace("{","").replace("}","").replace(",","\n"))

max_val=max(d.values())
max_keys=[key for key,value in d.items() if value==max_val]
print(max_keys,"=",max_val)

