#swap keys and values
dt={'Name':'Rupsa','Roll':41,'Dept':'CSBS','Age':20}
print(dt)
dt2={value:key for key,value in dt.items()}
print (dt2)