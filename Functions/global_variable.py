count=0
def increment():
    global count
    count+=1
def print_count():
    global count
    count+=1
    print(count)
increment()
print_count()
