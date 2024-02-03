import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json')
file = gspread.authorize(credentials)

sheet = file.open("test").sheet1

sheet.update_cell(1, 1, 'Name')
sheet.update_cell(1, 2, 'Birth date')
sheet.update_cell(1, 4, 'Address')
sheet.update_cell(1, 3, 'Phone Number')
sheet.update_cell(1, 6, 'Place of birth')

sheet.update_cell(2, 3, '420')
sheet.update_cell(2, 4, 'The World')
sheet.update_cell(2, 5, 'Python')
sheet.update_cell(2, 6, 'USA')

sheet.update_cell(2, 1, 'Hello, world!')
sheet.update_cell(2, 2, 'here I come')
sheet.update_cell(1, 5, 'Code')

sheet.update_cell(3, 1, 'Amira')
sheet.update_cell(3, 2, '01/01/1983')
sheet.update_cell(3, 3, '680 965 667')
sheet.update_cell(3, 4, 'Paris 167')
sheet.update_cell(3, 5, 'Niche')
sheet.update_cell(3, 6, 'Egypt, Alexandria')

sheet.update_cell(4, 1, 'Yassin')
sheet.update_cell(4, 2, '05/07/2010')
sheet.update_cell(4, 3, '678 795 530')
sheet.update_cell(4, 4, 'Muntaner 183')
sheet.update_cell(4, 5, 'Fortnite')
sheet.update_cell(4, 6, 'España, Barcelona')

sheet.update_cell(5, 1, 'Frida')
sheet.update_cell(5, 2, '31/07/2011')
sheet.update_cell(5, 3, '673 216 552')
sheet.update_cell(5, 4, 'Muntaner 183')
sheet.update_cell(5, 5, 'Elite')
sheet.update_cell(5, 6, 'España, Barcelona')

sheet.update_cell(6, 1, 'Hamada')
sheet.update_cell(6, 2, '23/09/1981')
sheet.update_cell(6, 3, '630 379 484')
sheet.update_cell(6, 4, 'Paris 179')
sheet.update_cell(6, 5, 'Power')
sheet.update_cell(6, 6, 'Egypt, Alexandria')

sheet.update_cell(7, 1, 'Mamina')
sheet.update_cell(7, 2, '31/07/1959')
sheet.update_cell(7, 3, '626 652 128')
sheet.update_cell(7, 4, 'Casanova 173')
sheet.update_cell(7, 5, 'Persist')
sheet.update_cell(7, 6, 'Egypt, Alexandria')

sheet.update_cell(8, 1, 'Mami')
sheet.update_cell(8, 2, '31/07/1971')
sheet.update_cell(8, 3, '649 497 731')
sheet.update_cell(8, 4, 'Paris 179 bajos')
sheet.update_cell(8, 5, 'Stay Put')
sheet.update_cell(8, 6, 'Egypt, Alexandria')

