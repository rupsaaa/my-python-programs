from collections import Counter
lt=[2,4,7,5,8,9,8,7,4,2,2]
freq=Counter(lt)

max_keys={key:value for key,value in freq.items() if  value>1}
if len(max_keys)==0:
    print("No repetation of numbers")
else:
    print(max_keys)