import csv
with open('E:/python programs/file handling/employees.csv','r') as file:
    reader=csv.reader(file)
    header=next(reader)
    print("Header:",header)
    for i,row in enumerate(reader):
        if i<2:
            print(row)
        else:
            break
    '''for i in range(2):
          print(next(reader))'''





































































