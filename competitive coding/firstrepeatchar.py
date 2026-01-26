str=input("Enter a string:")
for i in range(len(str)):
    if str[i] in str[i+1:len(str)+1]:
        print("The first repeated character:",str[i])
        exit()
print("No repeated character found.")
      
    
    
