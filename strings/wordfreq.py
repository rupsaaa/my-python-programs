from collections import Counter
x=input("Enter a sentence:")
'''d={y:x.count(y) for y in set(x.split())}
print("Frequency of each word: ")
'''
freq=Counter(x.split())
print(str(freq).replace("Counter({","").replace("})","").replace(",","\n"))