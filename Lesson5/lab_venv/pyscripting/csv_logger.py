#=================================================
# Ma. Beatriz Salazar 
# This script edited to add logging functionality
#=================================================

import csv, pdb, requests, os

import logging
#logging.basicConfig(filename='example.log', level=logging.DEBUG) <-- normie, no format
logging.basicConfig(
    filename = 'file-samples/csv_logs.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
)

logger = logging.getLogger(__name__) 


#url_todl = input('Enter URL of data file: ')
url_todl = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'
clean_data = 'file-samples/clean_products.csv'

data_file = requests.get(url_todl) #output is in response object
logger.info('Data File download completed')

with open('dfile.csv', 'w') as f:
    f.write(data_file.text) #write data_file na puro string, into csv
logger.info('Data File conversion to csv completed')

# Open the product csv file and create a list of products with
# categories
count = 0
w_cat = 0
with open(os.getcwd()+'/''dfile.csv', newline='\n') as f:
    DReader = csv.DictReader(f)
    clean_lines = []

    for row in DReader:  # Loops through the rest of the lines
        #print(row['Categories'])
        if row['Categories']:
            logger.info('Row with Category found')
            w_cat += 1 #for line counter of rows with categories
            clean_lines.append(row) #adds the row to the last part per iteration
            #print(row)
            #print(row["Categories"])
        count += 1 #for updating count value, used in iteration
#print(clean_lines)
logger.info('Data File processing completed')

# Create a new csv file with the products with categories including
# the csv header.
fieldnames = DReader.fieldnames
with open(clean_data, 'w', newline='\n') as f:
    wrt = csv.DictWriter(f, fieldnames = fieldnames)
    wrt.writeheader()# writes the header row
    wrt.writerows(clean_lines)  # writes the products

#print(clean_lines)
logger.info('csv file of cleaned Data File has been created')
print('Total lines: ', count)
print('Lines with category: ', w_cat)

import json
import requests

url = 'https://m6z1649x88.execute-api.ap-southeast-1.amazonaws.com/test1/bea_email_notif_service'

data = json.dumps({
    'log_level': 'critical',
    'email': 'ma.salazar@globe.com.ph',
    'message': 'hello world try message',
    })
    
res = requests.post(url,data)

print(res)