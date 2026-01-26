'''The Treasure Hunt
In an old castle, you found a chest with N locks, each lock has a number.
You also have a bunch of keys (array of integers).
A lock opens if there exists a pair of keys whose sum equals the lock’s number.
Count how many locks can be opened.
Example:
Locks = [10, 15, 7]
Keys  = [2, 3, 5, 7, 8, 10]
Output = 3   # (10 opened by 2+8, 15 opened by 7+8, 7 can be opened by 5+2)'''
def sumpair(arr, n):
    pair = set()
    for i in arr:
        if n - i in arr and (i, n - i) not in pair and (n - i, i) not in pair:
            print(i, ",", n - i)
            pair.add((i, n - i))


l=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in l:
    sumpair(k,i)