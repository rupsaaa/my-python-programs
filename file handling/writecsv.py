import csv
head=["name","area","countrycode"]
dt=['India',91,'IN']
with open('E:/python programs/file handling/country.csv','w') as f:
    wr=csv.writer(f)
    wr.writerow(head)
    wr.writerow(dt)
print("written into csv file successful")