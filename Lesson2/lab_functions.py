#functions in the Python Lesson 2 Handouts:

#function without an argument:
def say_hello():
    print("Hello World!!")
    #return #whether this exists or not, output is None data type

say_hello() #you need to define this para magamit si say_hello
            #if you dont, di sya macacall and no output lalabas
            #when you run lab_functions.py


#function without an argument:
def say_hello2(name):
    print(f'Hello, {name}')
    
say_hello2('Bea')

def add_numbers(a, b):
    return a + b
#add_numbers(3,2) <-- pag ganito no printed output
print(add_numbers(3,2), '\n')

#==============================
#2.4 Using Standard Library Packages:

import time
now = time.localtime()
print(now)
print(now.tm_hour) #to print only the hour section

from time import localtime, mktime, strftime #for importing specific modules

#==============================
#2.5 Working with Environment Variables:

import os
''' VIA OS.ENVIRON[]
#os.environ = It returns a dictionary having user’s environmental variable 
# as key and their values as value:
stage = os.environ["STAGE"].upper() #creates the $STAGE variable
output = f"We're running in {stage}"
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output)
#need to export STAGE later when running:
#export STAGE="staging" or export STAGE="PROD" before python3 lab_check_stage.py
'''

#VIA OS.GETENV()
#os.getenv = doesnt need you to set/export a variable first BECAUSE
# you can set a default variable like "dev".
#returns the value of the environment variable key if it exists,
#otherwise returns the default value.

#if you export STAGE='staging' or 'PROD'
#check via: echo $STAGE, kahit no output (meaning none set), it will run!

stage = os.getenv("STAGE", "dev").upper()
output = f"We're running in {stage}"
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output, '\n')
