nums= list(range(1, 11)) 
evens = []   
for n in nums:
    if n % 2 == 0:
        evens.append(n)
evens_comp = [n for n in nums if n % 2 == 0] 
print(f"Max: {max(nums)}, Min: {min(nums)}") 