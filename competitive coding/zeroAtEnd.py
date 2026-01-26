lt=list(map(int,input().split()))
c=[i for i in lt if i!=0]
print(c+[0]*lt.count(0))


