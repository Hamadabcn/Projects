import shutil, os, re
from pathlib import Path


datePattern = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"


for filename in os.listdir(Path.home() / Path("OneDrive", "Escritorio", "files")):
    search = re.search(datePattern, filename)

    if search == None:

        continue

    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)


    newFileName = beforePart + dayPart + '-', + monthPart + '-' + yearPart + afterPart
    print(f'Renaming "{filename}" to "{newFileName}"')

    oldName = Path.home() / Path("OneDrive", "Escritorio", "files") / filename
    newName = Path.home() / Path("OneDrive", "Escritorio", "files") / newFileName
    shutil.move(oldName, newName)
