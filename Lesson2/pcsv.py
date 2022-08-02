import csv

# data_file = input('Enter file to process: ')
data_file = 'file-samples/sample_products.csv'
clean_data = 'file-samples/clean_products.csv'


# Open the product csv file and create a list of products with
# categories
count = 0
w_cat = 0
with open(data_file, newline='\n') as f:
    reader = csv.reader(f)
    clean_lines = []

    for row in reader:  # Loops through the rest of the lines
        if row[25]:  # Index for category
            w_cat += 1
            clean_lines.append(row)
            #print(row)
            #print(row[25])
        count += 1


# Create a new csv file with the products with categories including
# the csv header.
with open(clean_data, 'w', newline='\n') as f:
    wrt = csv.DictWriter(f, 'Categories')
    wrt.writeheader()
    wrt.writerow('Categories')  # writes the header row
    wrt.writerows(clean_lines)  # writes the products


print('Total lines: ', count)
print('Lines with category: ', w_cat)
