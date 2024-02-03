import re  # regular expressions

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json')
file = gspread.authorize(credentials)

sheet = file.open('example').sheet1

# now imagine you want to find an employee with the name 'hadi'
# the problem is find() only gets the first value then breaks if two employees have the same name it will not look
# for the second one so instead of find() you need findall()
# cell = sheet.find("hadi")
# print(cell)
# print("Found something at Row: %s and column: %s" % (cell.row, cell.col))

# findall()
cell = sheet.findall("hadi")
print(cell)
# print("Found something at Row: %s and column: %s" % (cell.row, cell.col))  # in findall() this has to commented

# you can also search for a name using regular expressions
employees = re.compile(r'(anas|sara)')  # | pipe operator means 'and' in python
cell = sheet.findall(employees)
print(cell)


# clear information form a Google spreadsheet
# batch clear
sheet.batch_clear(["A8:C8"])  # we can clear a single cell or a range of index to clear

# clear the whole sheet
sheet.clear()
