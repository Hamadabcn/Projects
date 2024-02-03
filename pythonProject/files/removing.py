import os
from pathlib import Path
import shutil  # this will remove full files
import send2trash

# unlink
#os.unlink(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFile01.txt"))
#os.unlink(Path.home() / Path("OneDrive", "Escritorio", "New folder"))  # this will return error
# rmdir remove directory only removes empty files
#os.rmdir(Path.home() / Path("OneDrive", "Escritorio", "New folder", "empty"))

#shutil.rmtree(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFolder"))

send2trash.send2trash(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFolder"))
send2trash.send2trash(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFile.txt"))
