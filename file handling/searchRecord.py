import csv
ser_field='designation'
ser_val="Manager"
with open('E:/python programs/file handling/employees.csv','r') as file:
    reader=csv.DictReader(file)
    found=False
    for row in reader:
        if row[ser_field]==ser_val:
            print("Record Found:",row)
            found=True
            break
    if not found:
        print(f"No Record found with {ser_field}={ser_val}")

