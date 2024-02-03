import shutil
from pathlib import Path

# copy and copytree to copy the whole folder
shutil.copy(Path.home() / Path("OneDrive", "Escritorio", "New folder", "file_one.txt"), Path.home() / Path("OneDrive", "Escritorio", "files", "file_one.copied.txt"))
shutil.copytree(Path.home() / Path("OneDrive", "Escritorio", "New folder"), Path.home() / Path("OneDrive", "Escritorio", "folder backup"))
