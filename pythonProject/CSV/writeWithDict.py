import csv
from pathlib import Path

# file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"), 'a', newline='')
# DictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=';')  # adds a semicolon
# DictWriter.writerow({'Name':'Ali', 'Salary': '1500', 'Date': '23/09/2016'})  # notice {} means a dictionary

# file.close()

file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.test.csv"), 'w', newline='')
DictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'])
DictWriter.writeheader()
# notice how the order of the keys does not affect the output because it's a dictionary
DictWriter.writerow({'Name':'Ali', 'Salary': '1500', 'Date': '23/09/2016'})
DictWriter.writerow({'Salary':'2000', 'Name': 'Hamada', 'Date': '31/07/2011'})
DictWriter.writerow({'Date':'01/01/2020', 'Salary': '1400', 'Name': 'Amira'})
file.close()
