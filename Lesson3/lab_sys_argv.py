#=================================================
# Ma. Beatriz Salazar 
# This script is for part Lesson 3, Lab 3.1.1
# For accepting simple positional arguments
#=================================================

import sys
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
print(f"Positional arguments: {sys.argv[1:]}")
print(f"First argument: {sys.argv[1]}")
print(sys.argv) #is a list
print("sys.argv is a type: ", type(sys.argv))
#in sys.argv, index 0 is for the filename