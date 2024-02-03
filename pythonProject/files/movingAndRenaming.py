import shutil
from pathlib import Path

# move() as it means moves the file not copy it
#shutil.move(Path.home() / Path("OneDrive", "Escritorio", "New folder", "test.txt"), Path.home() / Path("OneDrive", "Escritorio", "files"))
#shutil.move(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFile.txt"), Path.home() / Path("OneDrive", "Escritorio", "files", "file.txt"))
#shutil.move(Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFile.txt"), Path.home() / Path("OneDrive", "Escritorio", "tests"))
#shutil.move(Path.home() / Path("OneDrive", "Escritorio", "New folder", "test.txt"), Path.home() / Path("OneDrive", "Escritorio", "files"))
shutil.move(Path.home() / Path("OneDrive", "Escritorio", "New folder", "test.txt"), Path.home() / Path("OneDrive", "Escritorio", "New folder", "myFile01.txt"))
