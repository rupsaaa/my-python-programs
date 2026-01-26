
l1=[2,3,1,4]
l2=[5,10,20,30]
sq=map(lambda n1:n1*n1,l1)
res=map(lambda n1,n2:n1+n2,l1,l2)
print(list(sq))
print(list(res))
