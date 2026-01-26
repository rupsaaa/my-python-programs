import csv
with open("E:/python programs/file handling/Book1.csv","r") as fp:
    rd=csv.DictReader(fp)
    for row in rd:
        if int (row['marks'])>70 and int(row['marks'])<95:
            print(row)

