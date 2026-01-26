data=[23,45,31,53,61]
data.append(39) #adds at the end
data.extend([76,90,81])
data.insert(3,61) #inserts 61 at 3rd index
data.remove(45) #removes 45
print(data)
print(data.index(81)) #returns index of 81
print(data.count(61)) #frequency of 61
data.pop(5)
print(data) #removes and prints item at ith index
data.sort()
print(data) #sorts the list in ascending order
data.sort(reverse=True)
print(data) #sorts the list in descending order
data.reverse() #reverses the list
print(data)
print(data.clear()) #returns None
