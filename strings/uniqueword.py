x=input("Enter a word:")
unique=''.join(sorted(set(x),key=x.index))
print(unique)
