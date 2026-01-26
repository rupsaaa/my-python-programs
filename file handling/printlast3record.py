import csv
with open('E:/python programs/file handling/employees.csv','r') as file:
    reader=list(csv.reader(file))
    header=reader[0]
    print("Header:",header)
    print("Last three records:")
    for row in reader[-3:]:
        print(row)