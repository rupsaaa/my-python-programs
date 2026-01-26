import csv
from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['student']
col=db['Student_Details']
data=list(col.find())
if data:
    all_keys=set() #collect all unique keys across all documents
    for doc in data:
        all_keys.update(doc.keys())
    keys=list(all_keys)
    with open('stud_details.csv','w',newline='') as newcsv:
        writer=csv.DictWriter(newcsv,fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print("data exported to csv file successfully...")
else:
    print("no data found in collection")