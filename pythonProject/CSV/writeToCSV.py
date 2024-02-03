import csv
from pathlib import Path

# add multiple lines
# header = ('Name', 'Salary', 'Date')
# data = [
#     ['Hadi', 1000, '04/08/2021'],
#     ['Sara', 800, '06/04/2021'],
#     ['Eman', 400, '07/04/2020'],
#     ['Yara', 750, '08/04/2020'],
#     ['Anas', 1200, '09/04/2019']
# ]
#
# the path to the file on my desktop
# file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"), 'a', newline='')
# 'w' write but erases old data, 'a' appends to the data
# writer = csv.writer(file)
#
# writer.writerow(header)  # new data to add to the file
# writer.writerows(data)
#
# file.close()  # remember to close the file

# delimiter and line terminator keyword
file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"), 'a', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n-----------------------------------\n')   # '\t' adds a tab
writer.writerow(['Amira', 1000, '04/08/2021'])
writer.writerow(['Hamada', 1000, '08/08/2020'])
writer.writerow(['Anas', 1200, '09/04/2019'])
writer.writerow(['Hadi', 1000, '04/08/2021'])
writer.writerow(['Sara', 800, '06/04/2021'])
writer.writerow(['Yara', 750, '08/04/2020'])
file.close()
