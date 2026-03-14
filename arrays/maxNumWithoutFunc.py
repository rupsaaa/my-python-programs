#dont use max() function to find the maximum number in a list
def find_maximum(lst):
    m=lst[0]
    for i in lst:
        if i>m:
            m=i
    return m
numbers = [3, 5, 2, 8, 1]
max_number = find_maximum(numbers)
print(max_number)