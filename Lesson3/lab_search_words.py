#=================================================
# Ma. Beatriz Salazar 
# This script is for part Lesson 3, Lab 3.5
#=================================================

'''
Filter out items in that list
Modify every item in the list
'''

import argparse
parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args() #turns elem to list
snippet = args.snippet.lower()

'''
OLD
with open('words.txt') as f:
    words = f.readlines()
matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)
print(matches)
'''

words = open('words.txt').readlines()
print([word for word in words if snippet in word.lower()])