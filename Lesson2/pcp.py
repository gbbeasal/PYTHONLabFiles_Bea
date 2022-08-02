import csv
import pdb

data_file = input('Enter file to process: ') #file-samples/sample_products.csv
clean_data = 'file-samples/clean_products.csv'

# Open the product csv file and create a list of products with
# categories
count = 0
w_cat = 0
with open(data_file, newline='\n') as f:
    DReader = csv.DictReader(f)
    clean_lines = []

    for row in DReader:  # Loops through the rest of the lines
        #print(row['Categories'])
        if row['Categories']:
            w_cat += 1 #for line counter of rows with categories
            clean_lines.append(row) #adds the row to the last part per iteration
            #print(row)
            #print(row["Categories"])
        count += 1 #for updating count value, used in iteration
#print(clean_lines)

# Create a new csv file with the products with categories including
# the csv header.
#fields = ['Categories'] 
fieldnames = DReader.fieldnames
with open(clean_data, 'w', newline='\n') as f:
    wrt = csv.DictWriter(f, fieldnames = fieldnames)
    wrt.writeheader()# writes the header row
    wrt.writerows(clean_lines)  # writes the products

#print(clean_lines)
print('Total lines: ', count)
print('Lines with category: ', w_cat)