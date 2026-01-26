x=input("Enter a String:")
vowels="aeiou"
vowel=[word for  word in x.split() if set(vowels).issubset(set(word.lower()))]
if len(vowel)==0:
    print("No words have all five vowels present")
else:
    print("The words that have all the five vowels present are:",vowel)