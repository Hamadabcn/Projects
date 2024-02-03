import csv
from pathlib import Path

file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"))
dictReader = csv.DictReader(file)

for row in dictReader:
    print(row['Name'], row['Salary'], row['Date'])
