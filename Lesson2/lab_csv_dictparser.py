import csv

with open('testing.csv', 'r') as f:
    DReader = csv.DictReader(f)
    for row in DReader:
        #print(row) returns ordereddict obj
        print(row['header1'], row['header2']) #returns no 1st row bc it sees it as the header
