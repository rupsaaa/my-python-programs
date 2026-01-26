def sumpair(arr, n):
    pair = set()
    for i in arr:
        if n - i in arr and (i, n - i) not in pair and (n - i, i) not in pair:
            print(i, ",", n - i)
            pair.add((i, n - i))

arr = [8, 7, 2, 5, 3, 1, 5]
sumpair(arr, 10)
