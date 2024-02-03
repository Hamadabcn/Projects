import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json')
file = gspread.authorize(credentials)

# create a new file
# this is commented because every time you start the program it will create a new file
# new_file = file.create('A new spreadsheet')
# this is to share the Google account with my account
# new_file.share('triumphbcn@gmail.com', perm_type='user', role='writer')

new_file = file.open("A new spreadsheet")

# create a new sheet
# this is commented because every time you start the program it will create a new sheet called sheet2 it will crash
# worksheet = new_file.add_worksheet(title='sheet2', rows=100, cols=20)

# now how can you write on a sheet (first choose which sheet you want to write on)
# write to sheet
worksheet = new_file.worksheet('Sheet1')
# worksheet.update('B1', 'hello, world!')
# worksheet.update_cell(2, 4, 'hello, family!')

worksheet.update('A1:C2', [['Hasan', 1000, '14/05/2021'], ['Yara', 500, '01/09/2021']])
