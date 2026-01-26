import csv
fileread=open("E:/python programs/file handling/Book1.csv","r")
csvreader=csv.reader(fileread)
filewrite= open('E:/python programs/file handling/Book3.csv','w',newline="") 
csvwriter=csv.writer(filewrite)
for row in csvreader:   
    csvwriter.writerow(row)
print("copying successful")