def shift_zero(num):
    c1=num.count(0)
    c2=num.count(1)
    print(','.join("0"*c1+"1"*c2))
dt=[]
s=int(input("Enter total number of input:"))
for i in range(s):
    num=int(input("enter element"))
    dt.append(num)

print(shift_zero(dt))
      

            