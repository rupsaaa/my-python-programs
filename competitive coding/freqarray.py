import array as ar
lt=ar.array('i',[2,2,1,3,6,3])
dt={}
for i in lt:
    if i not in dt:
        dt[i]=1
    else:
        dt[i]+=1
for k,v in dt.items():
       print(k,"=",v," times")
   
        