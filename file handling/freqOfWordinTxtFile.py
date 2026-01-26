#frequency of each word in the text file xyz.txt
fo=open("abc.txt","r")
words=fo.read().split()
freq={num:words.count(num) for num in set(words)}
print (freq)