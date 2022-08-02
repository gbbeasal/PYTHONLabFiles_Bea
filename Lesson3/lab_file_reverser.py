#=================================================
# Ma. Beatriz Salazar 
# This script is for part Lesson 3, Lab 3.1.2
#=================================================

import argparse
import sys # add import for sys module

# create an instance of ArgumentParser without any arguments:
# to parse = somewhat is how we breakdown a sentence into separate
# components 
parser = argparse.ArgumentParser(description='Read a file in reverse')

# use the add_argument method to specify a positional 
# argument called filename and provide some help text using 
# the help argument:
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# tell the parser to parse the arguments from stdin using
# the parse_args method and store the parsed arguments as 
# to the variable args:
args = parser.parse_args()

'''
OLD
# add the actual business logic for reversing the contents of the file
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()
if args.limit:
    lines = lines[:args.limit]
for line in lines:
    print(line.strip()[::-1])
'''

# We utilize the try statement to denote that it’s quite possible for an
#error to happen within the try block.
#If you didn't specify a file name, magkakaron ng FileNotFoundError. The code
#must be able to work around this scenario so we'll use the try-except

try:
    f = open(args.filename)
    limit = args.limit
# We can handle specific types of errors using the except keyword (we can have more than one).
except FileNotFoundError as err:
    print(f"Error: {err}")
    # set exit status to 1 to indicate error
    #sys.exit("An error has occured") <-- if instead na echo $? tas output 1 gusto mo, you can set a message instead
    sys.exit(1)
# If there isn’t an error, we want to carry out the code that is in the else block
else:
    with f:
        lines = f.readlines() #readlines() method returns a list 
                              #containing each line in the file as a list item
        #print(lines)
        lines.reverse() #reverses order of objects of the List
        if args.limit:
            lines = lines[:args.limit]
            
        for line in lines:
            print(line.strip()[::-1])
# If we want to execute some code regardless of there being an error or not,
# we can put that in a finally block at the very end of our try/except code