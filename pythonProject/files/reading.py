from pathlib import Path

import os

print(os.getcwd())

#os.chdir(r'C:\Users\mohbc\Projects\pythonProject\files')
print(Path.home())

#myFile = open(r"..\..\New folder\file_one.txt","r")
#myFile = open(r"C:\Users\mohbc\OneDrive\Escritorio\New folder\file_one.txt","r")
myFile = open(Path.home() / Path("OneDrive", "Escritorio", "New folder", "file_one.txt"), "r")
print(str(Path.home() / Path("OneDrive", "Escritorio", "New folder", "file_one.txt")))
print(myFile)
print(myFile.name)
print(myFile.mode)

#print(myFile.read())  # .read() can only be used ones in the code
#print(myFile.read(9))  # this only reads 9 characters of the file
#print(myFile.readline())  # readline() and readlines() notice the second one has plural 's'
#print(myFile.readlines())  # this reads all the lines in the folder

# imagine we want to print the first five lines only
# this is a way using readlines()
lines = myFile.readlines()
print(lines[0:5])  # now you can choose which line to read

# another way is using a for loop
print("-" * 50)
i = 0
for line in lines:
    print(line)
    i += 1
    if i == 5:
        break
myFile.close()  # it's good practice to always close the files
