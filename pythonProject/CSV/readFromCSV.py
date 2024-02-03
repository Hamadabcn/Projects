import csv
from pathlib import Path
file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"))
reader = csv.reader(file)

# data = list(reader)
# print(data)  # prints the whole data
# print(data[1][0])  # prints only the first index
# print(data[1][1])  # prints the first salary
# print(data[1][2])  # prints the first date

for row in reader:
    print('Row # ' + str(reader.line_num) + ' ' + str(row))
