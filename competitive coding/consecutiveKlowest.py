'''A city has installed smart water meters in every house.
Each meter records daily water usage (in liters) for N days.
The government wants to find a period of K continuous days where:
The total water usage is minimum,
so they can analyze low-consumption behavior.'''

arr=[120,80,100,90,60,110,70]
k=3
s=0
minsum=sum(arr[0:k])
for i in range(1,len(arr)-k+1):
    s=sum(arr[i:i+k])
    if s<minsum:
        minsum=s
print(minsum)

