from pathlib import Path

# 'w' write does two things 1. it creates a file if it does not find one and
# 2. it erases what the content of the file and writes over (careful)
myFile = open('file_one.txt', 'w')
myFile = open(Path.home() / Path("OneDrive", "Escritorio", "New folder", "file_one.txt"), "a")
# notice you can change the 'w' with 'a' which is the same as 'w' but it does not erase the content of the file
myFile.write("\n16. Hello how are you doing today\n")
myFile.write("17. I hope you have a nice day\n")
myFile.write("18. Take care and see you soon\n")

# writelines()
# myList= ['\n14. Today is a good day\n', '15. Life is short, have fun\n']
# myFile.writelines(myList)
