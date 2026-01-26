def check(lt):
   s1=[]
   s2=[]
   s3=[]
   for word in lt:
      if (word==word[::-1]):
        s1.append(word)
      elif (word[0]==word[-1]):
         s2.append(word)
      else:
         s3.append(word)
   return s1,s2,s3
s=['rupsa','madam','mom','hello','aisha']
a,b,c=check(s)
print("Words that are Palindrome as well as Special are:",a)
print("Words that are only Special but not palindrome are:",b)
print("Words that are neither Special nor palindrome are:",c)
