import zipfile
from pathlib import Path
import os
import shutil

compressZip = zipfile.ZipFile(Path.home() / Path("OneDrive", "Escritorio", "New folder.zip"))

print(compressZip.namelist())

fileInfo = compressZip.getinfo('New folder/New folder01/99%.png')

print(fileInfo.file_size)   # real size
print(fileInfo.compress_size)  # compressed size using zip


# extract
os.chdir(Path.home() / Path("OneDrive", "Escritorio"))
compressZip.extractall()

compressZip.extract('New folder/New folder01/99%.png', Path.home() / Path("OneDrive", "Escritorio", "extractFile"))

# compress files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('New folder/New folder01/99%.png')


# compress folder
folderZip = zipfile.ZipFile('newFolder.zip', 'w')  # this will be the name of the folder
folderZip.write(Path.home() / Path("OneDrive", "Escritorio", "New folder"))

shutil.make_archive("compressedFolder", 'zip', Path.home() / Path("OneDrive", "Escritorio", "New folder"))
