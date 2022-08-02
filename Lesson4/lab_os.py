'''
#at repl:
python3
import os

#os.environ = needs a variable to be set before running
#os.getenv = doesnt need input to run

###os.environ = just this, ang lalabas is a dictionary of the system environment

os.environ
print(os.environ["GEM_PATH"]) #GEM_PATH is a key we saw when we ran line 11
print(os.environ["STAGE"]) #since this key doesnt exist, an error message will appear

#need to set the key first para no error pag os.environ gamit:
export STAGE="value" <-- outside of repl


###os.getenv

os.getenv("GEM_PATH")
os.getenv("STAGE") #returns no error, and returns None
'''
import os

os.getcwd() #gets current path/directory
print(os.getcwd()) 

#gets files in the current directory
print(f"The dir files are: {os.listdir(os.getcwd())}") 

#os.remove("example2.txt") <-- to remove file
