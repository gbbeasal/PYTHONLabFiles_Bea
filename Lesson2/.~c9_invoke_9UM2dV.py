#For parts in Lesson 2.6 Interacting with Files

print('opening the file:')
dogs_file = open('dogs_base.txt', 'r') #mode r = read
print(dogs_file, '\n\n') #will print current parameters configured for dog_file

print('reading the file:')
print(dogs_file.read(), "\n\n")

''' @REPL:
dogs_file.read() <---at first lalabas yung contents ng file bc the cursor is at 0
dogs_file.read() <---for the next runs, empty string na lang bc the cursor is moved
                     already at the end of the file's contents.
                     
dogs_file.seek(0) <--- need so we can move cursor back to the start
dogs_file.seek(2) <--- cursor starts after character 2, print out is 2 and beyond

for line in dogs_file:
    print(line, end="")

'''
dogs_file.close() #need to close to save resources



#########creating a new file and writing to it:
dogs_base = open('dogs_base.txt')
print(dogs_base) #will print current parameters configured

new_dogs = open('new_dogs.txt', 'w') #file doesnt exist yet so it will be created
new_dogs.write(dogs_base.read()) #reads the contents of dog_base and writes it

#w = write = The specified file will be emptied before the text will be inserted 
#at the current file stream position, default 0.

#a = append = new contents will be added to the last part of the initial contents

new_dogs.close()
new_dogs = open('new_dogs.txt', 'r+')
new_dogs.read()
print(new_dogs.close())