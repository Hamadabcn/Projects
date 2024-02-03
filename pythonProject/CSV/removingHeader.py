import csv, os
from pathlib import Path

# exercise to remove the header from several csv files
os.makedirs(Path.home() / Path("OneDrive", "Escritorio", "CSV files"), exist_ok=True)

for csvFilename in os.listdir(Path.home() / Path("OneDrive", "Escritorio", "CSV files")):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    csvRows = []  # this will contain all the lines but the first line of each file (the header)
    csvFileObj = open(Path.home() / Path("OneDrive", "Escritorio", "CSV files", csvFilename))
    readObj = csv.reader(csvFileObj)

    for row in readObj:
        if readObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(Path.home() / Path("OneDrive", "Escritorio", "CSV files", csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)

    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
