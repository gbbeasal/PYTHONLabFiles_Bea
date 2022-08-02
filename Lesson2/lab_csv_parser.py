import csv

with open('testing.csv', 'r') as f:
    Reader = csv.reader(f)
    for row in Reader:
        print(row)
        #print(type(row)) #prints rows as list
    
with open('csv_testing.csv', 'w') as fw:
    Writer = csv.writer(fw)
    Writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])