import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json')
file = gspread.authorize(credentials)

#sheet = file.open("example")  # here opens the file by it's name
sheet = file.open_by_url('https://docs.google.com/spreadsheets/d/1BZrvS7B81RoAVTL9Xnz2EXHA0HGKMPHRmHPX1aAuH2Q/edit?usp=sharing')
# here opens from the url directly (example above)

#workSheet = sheet.get_worksheet(0)  # this will look for sheet 1
workSheet = sheet.worksheet('Hoja 1')

workSheet_list = sheet.worksheets()
print(workSheet_list)

# read from sheet
val = workSheet.acell('A1').value
print(val)
val = workSheet.acell('B1').value
print(val)

val = workSheet.cell(4, 1).value
print(val)

# what if you want to read the whole line 2
value_list = workSheet.row_values(2)  # this will all line 2
print(value_list)

# what if you want to print all the names of the employees
value_list = workSheet.col_values(1)  # this will print column 1 which contains all the names
print(value_list)

# what if you want to read all the information in the sheet
# get all values
list_of_lists = workSheet.get_all_values()  # print values and keys in a separate list
print(list_of_lists)

# what if you want the information in a dictionary
list_of_dict = workSheet.get_all_records()  # this will print all the information in a dictionary
print(list_of_dict)
