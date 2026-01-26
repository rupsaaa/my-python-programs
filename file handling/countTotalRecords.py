import csv
with open('E:/python programs/file handling/employees.csv','r') as file:
    reader=list(csv.reader(file))
    count=sum(1 for row in reader)-1
    print(f"Total Records:{count}")