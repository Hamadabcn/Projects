import openpyxl
from pathlib import Path

excelFile = openpyxl.load_workbook(Path.home() / Path("OneDrive", "Escritorio", "example.xlsx"))
sheet = excelFile['Sheet1']

#sheet['B7'] = '=SUM(B1:B6)'  # in english Excel it's SUM but in spanish it's SUMA
#sheet['B7'] = '=average(B1:B6)'  # average will print the average of the salaries in the Excel sheet
# exercise could you find all the employees that have a salary more than 750€
sheet['B7'] = '=COUNTIF(B1:B6, ">750")'  # this will get all the employees that gain more than 750€

excelFile.save(filename=Path.home() / Path("OneDrive", "Escritorio") / 'example.xlsx')
