import csv
file=open("E:/python programs/file handling/Book1.csv","r")
csvreader=csv.reader(file)
arr=[]
arr=next(csvreader)
print(arr)
rows=[]
for row in csvreader:
    rows.append(row)#or directly write print(row)
print(rows)
file.close()