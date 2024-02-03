import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json')
file = gspread.authorize(credentials)

new_file = file.open('example')
worksheet = new_file.worksheet('Hoja 1')
# spreadsheet formulas: "=MAX(B2:B7)", "=MIN(B2:B7)", "=PROMEDIO(B2:B7)", "=SUMA(B2:B7)"
worksheet.update_cell(8, 2, "=SUMA(B2:B7)")  # formula to get the total amount from those indexes in the spreadsheet
# know what if you want to know the formula used to get that answer
cell = worksheet.acell('B8', value_render_option='FORMULA').value
print(cell)
