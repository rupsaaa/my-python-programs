lt=[2,4,7,2,7,3,9,3]
dt={}
for i in lt:
    if i not in dt:
        dt[i]=1
    else:
        dt[i]+=1
for k,v in dt.items():
    print(k,"=",v)